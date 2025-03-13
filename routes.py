from flask import render_template, redirect, url_for, flash, request, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from models import User, Query, Report, KnowledgeBase, MarketData, Event, Company, TrendData
from forms import LoginForm, RegistrationForm, QueryForm, ReportForm, SearchForm
from ai_engine import process_query, generate_report, get_trend_forecast
from data_processor import search_knowledge_base
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def register_routes(app):
    
    @app.route('/')
    def index():
        return render_template('index.html', title='Home')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password', 'danger')
                return redirect(url_for('login'))
            
            login_user(user, remember=form.remember_me.data)
            user.last_login = datetime.utcnow()
            db.session.commit()
            
            next_page = request.args.get('next')
            if not next_page or not next_page.startswith('/'):
                next_page = url_for('dashboard')
            
            return redirect(next_page)
        
        return render_template('login.html', title='Login', form=form)
    
    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))
    
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(
                username=form.username.data,
                email=form.email.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                organization=form.organization.data,
                role=form.role.data,
                language_preference=form.language_preference.data
            )
            user.set_password(form.password.data)
            
            db.session.add(user)
            db.session.commit()
            
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
        
        return render_template('register.html', title='Register', form=form)
    
    @app.route('/dashboard')
    @login_required
    def dashboard():
        # Get recent market data
        market_data = MarketData.query.order_by(MarketData.date.desc()).limit(5).all()
        
        # Get upcoming events
        upcoming_events = Event.query.filter(Event.start_date >= datetime.utcnow()).order_by(Event.start_date).limit(3).all()
        
        # Get recent queries by the user
        recent_queries = Query.query.filter_by(user_id=current_user.id).order_by(Query.timestamp.desc()).limit(5).all()
        
        # Get recent reports by the user
        user_reports = Report.query.filter_by(author_id=current_user.id).order_by(Report.created_at.desc()).limit(3).all()
        
        return render_template(
            'dashboard.html',
            title='Dashboard',
            market_data=market_data,
            upcoming_events=upcoming_events,
            recent_queries=recent_queries,
            user_reports=user_reports
        )
    
    @app.route('/knowledge-base')
    @login_required
    def knowledge_base():
        # Get knowledge base categories
        categories = db.session.query(KnowledgeBase.category).distinct().all()
        categories = [category[0] for category in categories]
        
        # Get the selected category from query parameters
        selected_category = request.args.get('category', 'all')
        
        # Get knowledge base entries based on the selected category
        if selected_category != 'all':
            kb_entries = KnowledgeBase.query.filter_by(category=selected_category).order_by(KnowledgeBase.title).all()
        else:
            kb_entries = KnowledgeBase.query.order_by(KnowledgeBase.title).all()
        
        return render_template(
            'knowledge_base.html',
            title='Knowledge Base',
            categories=categories,
            selected_category=selected_category,
            kb_entries=kb_entries
        )
    
    @app.route('/strategic-advisor', methods=['GET', 'POST'])
    @login_required
    def strategic_advisor():
        form = QueryForm()
        
        if form.validate_on_submit():
            query_text = form.query_text.data
            
            # Save the query
            query = Query(
                text=query_text,
                category='strategic_advisor',
                user_id=current_user.id
            )
            db.session.add(query)
            db.session.commit()
            
            # Process the query using the AI engine
            response = process_query(query_text, 'strategic_advisor')
            
            return render_template(
                'strategic_advisor.html',
                title='Strategic Advisor',
                form=form,
                query=query_text,
                response=response
            )
        
        return render_template(
            'strategic_advisor.html',
            title='Strategic Advisor',
            form=form
        )
    
    @app.route('/guidance-system', methods=['GET', 'POST'])
    @login_required
    def guidance_system():
        form = QueryForm()
        
        if form.validate_on_submit():
            query_text = form.query_text.data
            
            # Save the query
            query = Query(
                text=query_text,
                category='guidance_system',
                user_id=current_user.id
            )
            db.session.add(query)
            db.session.commit()
            
            # Process the query using the AI engine
            response = process_query(query_text, 'guidance_system')
            
            return render_template(
                'guidance_system.html',
                title='Guidance System',
                form=form,
                query=query_text,
                response=response
            )
        
        return render_template(
            'guidance_system.html',
            title='Guidance System',
            form=form
        )
    
    @app.route('/trend-forecaster')
    @login_required
    def trend_forecaster():
        # Get trend categories
        categories = db.session.query(TrendData.category).distinct().all()
        categories = [category[0] for category in categories]
        
        # Get the selected category from query parameters
        selected_category = request.args.get('category', 'all')
        
        # Get trend data based on the selected category
        if selected_category != 'all':
            trends = TrendData.query.filter_by(category=selected_category).order_by(TrendData.confidence_score.desc()).all()
        else:
            trends = TrendData.query.order_by(TrendData.confidence_score.desc()).all()
        
        # Get trend forecast from AI engine
        forecast = get_trend_forecast()
        
        return render_template(
            'trend_forecaster.html',
            title='Trend Forecaster',
            categories=categories,
            selected_category=selected_category,
            trends=trends,
            forecast=forecast
        )
    
    @app.route('/report-generator', methods=['GET', 'POST'])
    @login_required
    def report_generator():
        form = ReportForm()
        
        if form.validate_on_submit():
            # Generate report using the AI engine
            report_content = generate_report(
                form.title.data,
                form.category.data,
                form.description.data
            )
            
            # Save the report
            report = Report(
                title=form.title.data,
                content=report_content,
                category=form.category.data,
                author_id=current_user.id
            )
            db.session.add(report)
            db.session.commit()
            
            flash('Report generated successfully!', 'success')
            return redirect(url_for('view_report', report_id=report.id))
        
        return render_template(
            'report_generator.html',
            title='Report Generator',
            form=form
        )
    
    @app.route('/report/<int:report_id>')
    @login_required
    def view_report(report_id):
        report = Report.query.get_or_404(report_id)
        
        # Check if the current user is the author of the report
        if report.author_id != current_user.id:
            flash('You do not have permission to view this report.', 'danger')
            return redirect(url_for('dashboard'))
        
        return render_template(
            'view_report.html',
            title=report.title,
            report=report
        )
    
    @app.route('/profile', methods=['GET', 'POST'])
    @login_required
    def profile():
        # Get user's recent activity
        recent_queries = Query.query.filter_by(user_id=current_user.id).order_by(Query.timestamp.desc()).limit(10).all()
        recent_reports = Report.query.filter_by(author_id=current_user.id).order_by(Report.created_at.desc()).limit(5).all()
        
        return render_template(
            'profile.html',
            title='Profile',
            recent_queries=recent_queries,
            recent_reports=recent_reports
        )
    
    @app.route('/search', methods=['GET', 'POST'])
    @login_required
    def search():
        form = SearchForm()
        
        if form.validate_on_submit() or request.args.get('q'):
            # Get search query from form or URL parameters
            query = form.search_query.data or request.args.get('q')
            
            # Search the knowledge base
            results = search_knowledge_base(query)
            
            return render_template(
                'search_results.html',
                title='Search Results',
                form=form,
                query=query,
                results=results
            )
        
        return render_template(
            'search.html',
            title='Search',
            form=form
        )
    
    @app.route('/set-language/<language>')
    def set_language(language):
        if language not in ['en', 'ar']:
            language = 'en'
        
        # Store the language preference in the session
        session['language'] = language
        
        # Update the user's language preference if logged in
        if current_user.is_authenticated:
            current_user.language_preference = language
            db.session.commit()
        
        # Redirect back to the previous page
        return redirect(request.referrer or url_for('index'))
    
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('error.html', error_code=404, error_message='Page not found'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('error.html', error_code=500, error_message='Internal server error'), 500
    
    # API routes for AJAX requests
    @app.route('/api/market-data/<category>')
    @login_required
    def api_market_data(category):
        data = MarketData.query.filter_by(category=category).order_by(MarketData.date).all()
        result = [
            {
                'metric_name': item.metric_name,
                'value': item.value,
                'unit': item.unit,
                'date': item.date.strftime('%Y-%m-%d'),
                'category': item.category,
                'source': item.source
            }
            for item in data
        ]
        return jsonify(result)
    
    logger.info("Routes registered successfully!")
