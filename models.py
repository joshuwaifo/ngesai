from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    organization = db.Column(db.String(128))
    role = db.Column(db.String(64))  # User's role in the system (admin, investor, team owner, etc.)
    language_preference = db.Column(db.String(10), default='en')  # 'en' for English, 'ar' for Arabic
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, nullable=True)
    
    # Relationships
    reports = db.relationship('Report', backref='author', lazy='dynamic')
    queries = db.relationship('Query', backref='user', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'

class Query(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(64))  # knowledge_base, strategic_advisor, guidance, trend_forecaster
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Query {self.text[:30]}...>'

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(64))  # market_analysis, investment_proposal, sponsorship_package, etc.
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Report {self.title}>'

class KnowledgeBase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(64))  # market_data, regulatory, company_profiles, talent, events, research
    source = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<KnowledgeBase {self.title}>'

class MarketData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    metric_name = db.Column(db.String(64), nullable=False)
    value = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(32))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(64))  # revenue, users, demographics, game_preferences
    source = db.Column(db.String(256))
    
    def __repr__(self):
        return f'<MarketData {self.metric_name}: {self.value} {self.unit}>'

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    event_type = db.Column(db.String(64))  # tournament, conference, exhibition
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(256))
    organizer = db.Column(db.String(120))
    website = db.Column(db.String(256))
    
    def __repr__(self):
        return f'<Event {self.name}>'

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    company_type = db.Column(db.String(64))  # developer, esports_team, event_organizer
    founded_year = db.Column(db.Integer)
    headquarters = db.Column(db.String(256))
    website = db.Column(db.String(256))
    
    def __repr__(self):
        return f'<Company {self.name}>'

class TrendData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trend_name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(64))  # game_genres, technologies, consumer_preferences
    confidence_score = db.Column(db.Float)  # 0-1 score indicating confidence in the trend
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<TrendData {self.trend_name}>'
