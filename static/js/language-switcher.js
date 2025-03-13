// SGEIB - Language Switcher JavaScript File

document.addEventListener('DOMContentLoaded', function() {
    // Dictionary of translations
    const translations = {
        'en': {
            // Navigation
            'nav_home': 'Home',
            'nav_dashboard': 'Dashboard',
            'nav_knowledge_base': 'Knowledge Base',
            'nav_strategic_advisor': 'Strategic Advisor',
            'nav_guidance_system': 'Guidance System',
            'nav_trend_forecaster': 'Trend Forecaster',
            'nav_report_generator': 'Report Generator',
            'nav_profile': 'Profile',
            'nav_login': 'Login',
            'nav_register': 'Register',
            'nav_logout': 'Logout',
            
            // Buttons
            'btn_search': 'Search',
            'btn_submit': 'Submit',
            'btn_generate': 'Generate',
            'btn_view': 'View',
            'btn_edit': 'Edit',
            'btn_delete': 'Delete',
            'btn_save': 'Save',
            'btn_cancel': 'Cancel',
            
            // Forms
            'form_username': 'Username',
            'form_email': 'Email',
            'form_password': 'Password',
            'form_confirm_password': 'Confirm Password',
            'form_first_name': 'First Name',
            'form_last_name': 'Last Name',
            'form_organization': 'Organization',
            'form_role': 'Role',
            'form_query': 'Enter your question or request',
            'form_report_title': 'Report Title',
            'form_report_category': 'Report Category',
            'form_report_description': 'Report Description',
            
            // Dashboard
            'dashboard_title': 'Dashboard',
            'dashboard_welcome': 'Welcome to the Saudi Gaming & Esports Industry Brain',
            'dashboard_summary': 'Industry Summary',
            'dashboard_market_data': 'Market Data',
            'dashboard_upcoming_events': 'Upcoming Events',
            'dashboard_recent_queries': 'Your Recent Queries',
            'dashboard_reports': 'Your Reports',
            
            // Knowledge Base
            'kb_title': 'Knowledge Base',
            'kb_intro': 'Explore our comprehensive database of information about the Saudi gaming and esports industry.',
            'kb_categories': 'Categories',
            'kb_search': 'Search Knowledge Base',
            'kb_market_data': 'Market Data',
            'kb_regulatory': 'Regulatory Frameworks',
            'kb_companies': 'Company Profiles',
            'kb_talent': 'Talent Database',
            'kb_events': 'Events',
            'kb_research': 'Research',
            
            // Strategic Advisor
            'advisor_title': 'Strategic Advisor',
            'advisor_intro': 'Get strategic recommendations and insights tailored to your needs.',
            'advisor_query_placeholder': 'E.g., What sponsorship opportunities exist in Saudi esports?',
            'advisor_suggestions': 'Suggested Topics',
            'advisor_sponsorship': 'Sponsorship Strategy',
            'advisor_investment': 'Investment Opportunities',
            'advisor_team_development': 'Esports Team Development',
            'advisor_localization': 'Game Localization',
            'advisor_infrastructure': 'Esports Infrastructure',
            
            // Guidance System
            'guidance_title': 'Guidance System',
            'guidance_intro': 'Get step-by-step guidance on various processes in the Saudi gaming and esports ecosystem.',
            'guidance_query_placeholder': 'E.g., How do I start an esports team in Saudi Arabia?',
            'guidance_suggestions': 'Suggested Topics',
            'guidance_starting_team': 'Starting an Esports Team',
            'guidance_developing_game': 'Developing a Game for Saudi Market',
            'guidance_securing_sponsorship': 'Securing Sponsorships',
            'guidance_running_event': 'Running Gaming Events',
            'guidance_regulatory': 'Navigating Regulations',
            
            // Trend Forecaster
            'trend_title': 'Trend Forecaster',
            'trend_intro': 'Explore emerging trends and opportunities in the Saudi gaming and esports market.',
            'trend_confidence': 'Confidence Score',
            'trend_categories': 'Trend Categories',
            'trend_game_genres': 'Game Genres',
            'trend_technologies': 'Technologies',
            'trend_consumer_preferences': 'Consumer Preferences',
            
            // Report Generator
            'report_title': 'Report Generator',
            'report_intro': 'Generate customized reports for various stakeholders.',
            'report_description_placeholder': 'Describe what you want included in the report...',
            'report_market_analysis': 'Market Analysis',
            'report_investment_proposal': 'Investment Proposal',
            'report_sponsorship_package': 'Sponsorship Package',
            'report_performance_dashboard': 'Performance Dashboard'
        },
        'ar': {
            // Navigation
            'nav_home': 'الرئيسية',
            'nav_dashboard': 'لوحة التحكم',
            'nav_knowledge_base': 'قاعدة المعرفة',
            'nav_strategic_advisor': 'المستشار الاستراتيجي',
            'nav_guidance_system': 'نظام التوجيه',
            'nav_trend_forecaster': 'توقعات الاتجاهات',
            'nav_report_generator': 'مولد التقارير',
            'nav_profile': 'الملف الشخصي',
            'nav_login': 'تسجيل الدخول',
            'nav_register': 'التسجيل',
            'nav_logout': 'تسجيل الخروج',
            
            // Buttons
            'btn_search': 'بحث',
            'btn_submit': 'إرسال',
            'btn_generate': 'إنشاء',
            'btn_view': 'عرض',
            'btn_edit': 'تعديل',
            'btn_delete': 'حذف',
            'btn_save': 'حفظ',
            'btn_cancel': 'إلغاء',
            
            // Forms
            'form_username': 'اسم المستخدم',
            'form_email': 'البريد الإلكتروني',
            'form_password': 'كلمة المرور',
            'form_confirm_password': 'تأكيد كلمة المرور',
            'form_first_name': 'الاسم الأول',
            'form_last_name': 'اسم العائلة',
            'form_organization': 'المنظمة',
            'form_role': 'الدور',
            'form_query': 'أدخل سؤالك أو طلبك',
            'form_report_title': 'عنوان التقرير',
            'form_report_category': 'فئة التقرير',
            'form_report_description': 'وصف التقرير',
            
            // Dashboard
            'dashboard_title': 'لوحة التحكم',
            'dashboard_welcome': 'مرحبًا بك في عقل صناعة الألعاب والرياضات الإلكترونية السعودية',
            'dashboard_summary': 'ملخص الصناعة',
            'dashboard_market_data': 'بيانات السوق',
            'dashboard_upcoming_events': 'الفعاليات القادمة',
            'dashboard_recent_queries': 'استفساراتك الأخيرة',
            'dashboard_reports': 'تقاريرك',
            
            // Knowledge Base
            'kb_title': 'قاعدة المعرفة',
            'kb_intro': 'استكشف قاعدة بياناتنا الشاملة للمعلومات حول صناعة الألعاب والرياضات الإلكترونية السعودية.',
            'kb_categories': 'الفئات',
            'kb_search': 'البحث في قاعدة المعرفة',
            'kb_market_data': 'بيانات السوق',
            'kb_regulatory': 'الأطر التنظيمية',
            'kb_companies': 'ملفات الشركات',
            'kb_talent': 'قاعدة بيانات المواهب',
            'kb_events': 'الفعاليات',
            'kb_research': 'البحوث',
            
            // Strategic Advisor
            'advisor_title': 'المستشار الاستراتيجي',
            'advisor_intro': 'احصل على توصيات وأفكار استراتيجية مخصصة لاحتياجاتك.',
            'advisor_query_placeholder': 'مثال: ما هي فرص الرعاية الموجودة في الرياضات الإلكترونية السعودية؟',
            'advisor_suggestions': 'المواضيع المقترحة',
            'advisor_sponsorship': 'استراتيجية الرعاية',
            'advisor_investment': 'فرص الاستثمار',
            'advisor_team_development': 'تطوير فريق الرياضات الإلكترونية',
            'advisor_localization': 'تعريب الألعاب',
            'advisor_infrastructure': 'البنية التحتية للرياضات الإلكترونية',
            
            // Guidance System
            'guidance_title': 'نظام التوجيه',
            'guidance_intro': 'احصل على إرشادات خطوة بخطوة حول مختلف العمليات في نظام الألعاب والرياضات الإلكترونية السعودية.',
            'guidance_query_placeholder': 'مثال: كيف أبدأ فريق رياضات إلكترونية في المملكة العربية السعودية؟',
            'guidance_suggestions': 'المواضيع المقترحة',
            'guidance_starting_team': 'بدء فريق رياضات إلكترونية',
            'guidance_developing_game': 'تطوير لعبة للسوق السعودي',
            'guidance_securing_sponsorship': 'تأمين الرعاية',
            'guidance_running_event': 'إدارة فعاليات الألعاب',
            'guidance_regulatory': 'التنقل في اللوائح التنظيمية',
            
            // Trend Forecaster
            'trend_title': 'توقعات الاتجاهات',
            'trend_intro': 'استكشف الاتجاهات والفرص الناشئة في سوق الألعاب والرياضات الإلكترونية السعودية.',
            'trend_confidence': 'درجة الثقة',
            'trend_categories': 'فئات الاتجاهات',
            'trend_game_genres': 'أنواع الألعاب',
            'trend_technologies': 'التقنيات',
            'trend_consumer_preferences': 'تفضيلات المستهلك',
            
            // Report Generator
            'report_title': 'مولد التقارير',
            'report_intro': 'إنشاء تقارير مخصصة لمختلف أصحاب المصلحة.',
            'report_description_placeholder': 'صف ما تريد تضمينه في التقرير...',
            'report_market_analysis': 'تحليل السوق',
            'report_investment_proposal': 'مقترح استثماري',
            'report_sponsorship_package': 'حزمة الرعاية',
            'report_performance_dashboard': 'لوحة تحكم الأداء'
        }
    };

    // Function to set the language
    function setLanguage(lang) {
        // Store the selected language in localStorage
        localStorage.setItem('sgeib_language', lang);
        
        // Get all elements with the data-i18n attribute
        const elements = document.querySelectorAll('[data-i18n]');
        
        // Update the text content of each element based on the selected language
        elements.forEach(element => {
            const key = element.getAttribute('data-i18n');
            if (translations[lang] && translations[lang][key]) {
                element.textContent = translations[lang][key];
            }
        });
        
        // Update form placeholders
        const placeholders = document.querySelectorAll('[data-i18n-placeholder]');
        placeholders.forEach(element => {
            const key = element.getAttribute('data-i18n-placeholder');
            if (translations[lang] && translations[lang][key]) {
                element.setAttribute('placeholder', translations[lang][key]);
            }
        });
        
        // Update document direction for Arabic
        document.dir = lang === 'ar' ? 'rtl' : 'ltr';
        
        // Update Bootstrap RTL/LTR
        const html = document.querySelector('html');
        if (lang === 'ar') {
            html.setAttribute('dir', 'rtl');
            html.setAttribute('lang', 'ar');
            
            // Add RTL CSS if needed
            if (!document.getElementById('bootstrap-rtl')) {
                const rtlStyle = document.createElement('link');
                rtlStyle.id = 'bootstrap-rtl';
                rtlStyle.rel = 'stylesheet';
                rtlStyle.href = 'https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.rtl.min.css';
                document.head.appendChild(rtlStyle);
            }
        } else {
            html.setAttribute('dir', 'ltr');
            html.setAttribute('lang', 'en');
            
            // Remove RTL CSS if exists
            const rtlStyle = document.getElementById('bootstrap-rtl');
            if (rtlStyle) {
                rtlStyle.remove();
            }
        }
    }

    // Function to switch language
    function switchLanguage() {
        const currentLang = localStorage.getItem('sgeib_language') || 'en';
        const newLang = currentLang === 'en' ? 'ar' : 'en';
        setLanguage(newLang);
        
        // Update language switcher button text
        const langSwitcher = document.getElementById('languageSwitcher');
        if (langSwitcher) {
            langSwitcher.textContent = newLang === 'en' ? 'العربية' : 'English';
        }
    }

    // Initialize language based on stored preference or user's browser language
    function initializeLanguage() {
        let lang = localStorage.getItem('sgeib_language');
        
        if (!lang) {
            // Check browser language
            const browserLang = navigator.language || navigator.userLanguage;
            lang = browserLang.startsWith('ar') ? 'ar' : 'en';
        }
        
        setLanguage(lang);
        
        // Update language switcher button text
        const langSwitcher = document.getElementById('languageSwitcher');
        if (langSwitcher) {
            langSwitcher.textContent = lang === 'en' ? 'العربية' : 'English';
        }
    }

    // Attach event listener to language switcher
    const langSwitcher = document.getElementById('languageSwitcher');
    if (langSwitcher) {
        langSwitcher.addEventListener('click', function(e) {
            e.preventDefault();
            switchLanguage();
        });
    }

    // Initialize language on page load
    initializeLanguage();
});
