from flask import session

# =========================================================
# 🌐 UI TRANSLATIONS
# =========================================================

UI_TEXT = {
    "en": {
        "premium_reviewers": "🔒 Premium Reviewers",
        "premium_features": "⭐ Premium Features",
        "unlock_premium": "🔒 Unlock Premium",
        "premium_active": "✅ Premium Active",
        "manage_subscription": "💳 Manage Subscription",
        "upgrade": "⭐ Upgrade",

        "karimen_master": "📝 Karimen Master",
        "honmen_master": "🛣 Honmen Master",

        "study_mode": "🧠 Study Mode",
        "reviewer_karimen": "🧠 Reviewer Karimen",
        "reviewer_honmen": "🧠 Reviewer Honmen",

        "karimen_mock": "📝 Karimen Mock Test",
        "karimen_test_1": "📝 Karimen Test 1",
        "karimen_test_2": "📝 Karimen Test 2",

        "honmen_mock": "🏁 Honmen Mock Test",
        "honmen_test_1": "🛣 Honmen Master",
        "honmen_test_2": "🏁 Honmen Test 2",
        "honmen_test_3": "🏁 Honmen Test 3",

        "app_info": "⚙️ App Information",
        "score_history": "📊 Score History",
        "privacy": "🔒 Privacy Policy",
        "terms": "📄 Terms of Use",
        "contact": "✉️ Contact Us",

        "dark_mode": "🌙 Dark Mode",

        "login": "👤 Login",
        "register": "📝 Register",
        "logout": "🚪 Logout",
        "welcome": "Welcome",

        "ai_title": "🧠 AI Tutor",
        "premium": "⭐ Premium User",
        "select_language": "Select Language"
    },

    "tl": {
        "karimen_master": "📝 Karimen Master",
        "honmen_master": "🛣 Honmen Master",

        "study_mode": "🧠 Study Mode",
        "reviewer_karimen": "🧠 Reviewer Karimen",
        "reviewer_honmen": "🧠 Reviewer Honmen",

        "karimen_mock": "📝 Karimen Mock Test",
        "karimen_test_1": "📝 Karimen Test 1",
        "karimen_test_2": "📝 Karimen Test 2",

        "honmen_mock": "🏁 Honmen Mock Test",
        "honmen_test_1": "🛣 Honmen Master",
        "honmen_test_2": "🏁 Honmen Test 2",
        "honmen_test_3": "🏁 Honmen Test 3",

        "app_info": "⚙️ Impormasyon ng App",
        "score_history": "📊 Kasaysayan ng Score",
        "privacy": "🔒 Patakaran sa Privacy",
        "terms": "📄 Mga Tuntunin ng Paggamit",
        "contact": "✉️ Makipag-ugnayan",

        "dark_mode": "🌙 Dark Mode",

        "login": "👤 Mag Login",
        "register": "📝 Mag Register",
        "logout": "🚪 Mag Logout",
        "welcome": "Maligayang Pagdating",

        "ai_title": "🧠 AI Tutor",
        "premium": "⭐ Premium User",

        "premium_reviewers": "🔒 Premium Reviewers",
        "premium_active": "✅ Aktibo ang Premium",
        "manage_subscription": "💳 Pamahalaan ang Subscription",
        "upgrade": "⭐ Mag Upgrade",
        "premium_features": "⭐ Mga Premium Feature",
        "unlock_premium": "🔒 I-unlock ang Premium",

        "unlimited_mock_exams": "⭐ Walang Limit na Mock Exams",
        "advanced_analytics": "⭐ Advanced Analytics",
        "ai_tutor_unlimited": "⭐ Walang Limit na AI Tutor",

        "reviewers": "📚 Reviewers",
        "settings": "⚙️ Settings",
        "account": "👤 Account",
        "language": "🌐 Wika",
        "select_language": "Pumili ng Wika",
        "mock_tests": "📝 Mock Tests",
        "study_reviewer": "📘 Study Reviewer",
        "customer_portal": "💳 Customer Portal"
    },

    "ne": {
        "premium_reviewers": "🔒 प्रिमियम रिभ्युअर",
        "premium_features": "⭐ प्रिमियम सुविधाहरू",
        "unlock_premium": "🔒 प्रिमियम अनलक गर्नुहोस्",
        "premium_active": "✅ प्रिमियम सक्रिय",
        "manage_subscription": "💳 सदस्यता व्यवस्थापन",
        "upgrade": "⭐ अपग्रेड गर्नुहोस्",

        "karimen_master": "📝 करिमेन मास्टर",
        "honmen_master": "🛣 होनमेन मास्टर",

        "study_mode": "🧠 अध्ययन मोड",
        "reviewer_karimen": "🧠 करिमेन रिभ्युअर",
        "reviewer_honmen": "🧠 होनमेन रिभ्युअर",

        "karimen_mock": "📝 करिमेन मोक टेस्ट",
        "karimen_test_1": "📝 करिमेन परीक्षा १",
        "karimen_test_2": "📝 करिमेन परीक्षा २",

        "honmen_mock": "🏁 होनमेन मोक टेस्ट",
        "honmen_test_1": "🛣 होनमेन मास्टर",
        "honmen_test_2": "🏁 होनमेन परीक्षा २",
        "honmen_test_3": "🏁 होनमेन परीक्षा ३",

        "app_info": "⚙️ एप जानकारी",
        "score_history": "📊 स्कोर इतिहास",
        "privacy": "🔒 गोपनीयता नीति",
        "terms": "📄 प्रयोगका सर्तहरू",
        "contact": "✉️ सम्पर्क गर्नुहोस्",

        "dark_mode": "🌙 डार्क मोड",

        "login": "👤 लगइन",
        "register": "📝 दर्ता गर्नुहोस्",
        "logout": "🚪 लगआउट",
        "welcome": "स्वागत छ",

        "ai_title": "🧠 AI ट्यूटर",
        "premium": "⭐ प्रिमियम प्रयोगकर्ता",
        "select_language": "भाषा चयन गर्नुहोस्"
    },

    "vi": {
        "premium_reviewers": "🔒 Ôn Tập Premium",
        "premium_features": "⭐ Tính Năng Premium",
        "unlock_premium": "🔒 Mở Khóa Premium",
        "premium_active": "✅ Premium Đang Hoạt Động",
        "manage_subscription": "💳 Quản Lý Gói Đăng Ký",
        "upgrade": "⭐ Nâng Cấp",

        "karimen_master": "📝 Karimen Master",
        "honmen_master": "🛣 Honmen Master",

        "study_mode": "🧠 Chế Độ Học",
        "reviewer_karimen": "🧠 Ôn Tập Karimen",
        "reviewer_honmen": "🧠 Ôn Tập Honmen",

        "karimen_mock": "📝 Bài Thi Karimen",
        "karimen_test_1": "📝 Bài Thi Karimen 1",
        "karimen_test_2": "📝 Bài Thi Karimen 2",

        "honmen_mock": "🏁 Bài Thi Honmen",
        "honmen_test_1": "🛣 Honmen Master",
        "honmen_test_2": "🏁 Bài Thi Honmen 2",
        "honmen_test_3": "🏁 Bài Thi Honmen 3",

        "app_info": "⚙️ Thông Tin Ứng Dụng",
        "score_history": "📊 Lịch Sử Điểm",
        "privacy": "🔒 Chính Sách Riêng Tư",
        "terms": "📄 Điều Khoản",
        "contact": "✉️ Liên Hệ",

        "dark_mode": "🌙 Chế Độ Tối",

        "login": "👤 Đăng Nhập",
        "register": "📝 Đăng Ký",
        "logout": "🚪 Đăng Xuất",
        "welcome": "Xin chào",

        "ai_title": "🧠 Gia Sư AI",
        "premium": "⭐ Premium",
        "select_language": "Chọn ngôn ngữ"
    },

    "pt": {
        "premium_reviewers": "🔒 Revisões Premium",
        "premium_features": "⭐ Recursos Premium",
        "unlock_premium": "🔒 Desbloquear Premium",
        "premium_active": "✅ Premium Ativo",
        "manage_subscription": "💳 Gerenciar Assinatura",
        "upgrade": "⭐ Atualizar",

        "karimen_master": "📝 Karimen Master",
        "honmen_master": "🛣 Honmen Master",

        "study_mode": "🧠 Modo de Estudo",
        "reviewer_karimen": "🧠 Revisão Karimen",
        "reviewer_honmen": "🧠 Revisão Honmen",

        "karimen_mock": "📝 Teste Karimen",
        "karimen_test_1": "📝 Teste Karimen 1",
        "karimen_test_2": "📝 Teste Karimen 2",

        "honmen_mock": "🏁 Teste Honmen",
        "honmen_test_1": "🛣 Honmen Master",
        "honmen_test_2": "🏁 Teste Honmen 2",
        "honmen_test_3": "🏁 Teste Honmen 3",

        "app_info": "⚙️ Informações do App",
        "score_history": "📊 Histórico de Pontuação",
        "privacy": "🔒 Política de Privacidade",
        "terms": "📄 Termos",
        "contact": "✉️ Contato",

        "dark_mode": "🌙 Modo Escuro",

        "login": "👤 Entrar",
        "register": "📝 Registrar",
        "logout": "🚪 Sair",
        "welcome": "Bem-vindo",

        "ai_title": "🧠 Tutor IA",
        "premium": "⭐ Premium",
        "select_language": "Selecionar idioma"
    },

    "id": {
        "karimen_master": "📝 Karimen Master",
        "honmen_master": "🛣 Honmen Master",

        "study_mode": "🧠 Mode Belajar",
        "reviewer_karimen": "🧠 Reviewer Karimen",
        "reviewer_honmen": "🧠 Reviewer Honmen",

        "karimen_mock": "📝 Tes Karimen",
        "karimen_test_1": "📝 Tes Karimen 1",
        "karimen_test_2": "📝 Tes Karimen 2",

        "honmen_mock": "🏁 Tes Honmen",
        "honmen_test_1": "🛣 Honmen Master",
        "honmen_test_2": "🏁 Tes Honmen 2",
        "honmen_test_3": "🏁 Tes Honmen 3",

        "app_info": "⚙️ Informasi Aplikasi",
        "score_history": "📊 Riwayat Skor",
        "privacy": "🔒 Kebijakan Privasi",
        "terms": "📄 Syarat Penggunaan",
        "contact": "✉️ Hubungi Kami",

        "dark_mode": "🌙 Mode Gelap",

        "login": "👤 Masuk",
        "register": "📝 Daftar",
        "logout": "🚪 Keluar",
        "welcome": "Selamat Datang",

        "ai_title": "🧠 Tutor AI",
        "premium": "⭐ Pengguna Premium",
        "select_language": "Pilih Bahasa",

        "premium_reviewers": "🔒 Reviewer Premium",
        "premium_features": "⭐ Fitur Premium",
        "unlock_premium": "🔒 Buka Premium",
        "premium_active": "✅ Premium Aktif",
        "manage_subscription": "💳 Kelola Langganan",
        "upgrade": "⭐ Upgrade"
    },

    "ar": {
        "karimen_master": "📝 كاريمين ماستر",
        "honmen_master": "🛣 هونمن ماستر",

        "study_mode": "🧠 وضع الدراسة",
        "reviewer_karimen": "🧠 مراجعة كاريمين",
        "reviewer_honmen": "🧠 مراجعة هونمن",

        "karimen_mock": "📝 اختبار كاريمين",
        "karimen_test_1": "📝 اختبار كاريمين 1",
        "karimen_test_2": "📝 اختبار كاريمين 2",

        "honmen_mock": "🏁 اختبار هونمن",
        "honmen_test_1": "🛣 هونمن ماستر",
        "honmen_test_2": "🏁 اختبار هونمن 2",
        "honmen_test_3": "🏁 اختبار هونمن 3",

        "app_info": "⚙️ معلومات التطبيق",
        "score_history": "📊 سجل الدرجات",
        "privacy": "🔒 سياسة الخصوصية",
        "terms": "📄 شروط الاستخدام",
        "contact": "✉️ اتصل بنا",

        "dark_mode": "🌙 الوضع الداكن",

        "login": "👤 تسجيل الدخول",
        "register": "📝 إنشاء حساب",
        "logout": "🚪 تسجيل الخروج",
        "welcome": "مرحبًا",

        "ai_title": "🧠 مدرس الذكاء الاصطناعي",
        "premium": "⭐ مستخدم بريميوم",
        "select_language": "اختر اللغة",

        "premium_reviewers": "🔒 مراجعات بريميوم",
        "premium_features": "⭐ ميزات بريميوم",
        "unlock_premium": "🔒 فتح بريميوم",
        "premium_active": "✅ البريميوم مفعل",
        "manage_subscription": "💳 إدارة الاشتراك",
        "upgrade": "⭐ ترقية"
    },

    "ur": {
        "premium_reviewers": "🔒 پریمیم ریویورز",
        "premium_features": "⭐ پریمیم خصوصیات",
        "unlock_premium": "🔒 پریمیم ان لاک کریں",
        "premium_active": "✅ پریمیم فعال ہے",
        "manage_subscription": "💳 سبسکرپشن کا انتظام کریں",
        "upgrade": "⭐ اپ گریڈ کریں",

        "karimen_master": "📝 کاریمن ماسٹر",
        "honmen_master": "🛣 ہونمین ماسٹر",

        "study_mode": "🧠 مطالعہ موڈ",
        "reviewer_karimen": "🧠 کاریمن ریویور",
        "reviewer_honmen": "🧠 ہونمین ریویور",

        "karimen_mock": "📝 کاریمن موک ٹیسٹ",
        "karimen_test_1": "📝 کاریمن ٹیسٹ 1",
        "karimen_test_2": "📝 کاریمن ٹیسٹ 2",

        "honmen_mock": "🏁 ہونمین موک ٹیسٹ",
        "honmen_test_1": "🛣 ہونمین ماسٹر",
        "honmen_test_2": "🏁 ہونمین ٹیسٹ 2",
        "honmen_test_3": "🏁 ہونمین ٹیسٹ 3",

        "app_info": "⚙️ ایپ کی معلومات",
        "score_history": "📊 اسکور کی تاریخ",
        "privacy": "🔒 رازداری کی پالیسی",
        "terms": "📄 استعمال کی شرائط",
        "contact": "✉️ ہم سے رابطہ کریں",

        "dark_mode": "🌙 ڈارک موڈ",

        "login": "👤 لاگ ان",
        "register": "📝 رجسٹر کریں",
        "logout": "🚪 لاگ آؤٹ",
        "welcome": "خوش آمدید",

        "ai_title": "🧠 اے آئی ٹیوٹر",
        "premium": "⭐ پریمیم صارف",
        "select_language": "زبان منتخب کریں"
    },

    "my": {
        "premium_reviewers": "🔒 ပရီမီယမ် ပြန်လည်လေ့ကျင့်ခန်းများ",
        "premium_features": "⭐ ပရီမီယမ် လုပ်ဆောင်ချက်များ",
        "unlock_premium": "🔒 ပရီမီယမ်ကို ဖွင့်ပါ",
        "premium_active": "✅ ပရီမီယမ် အသုံးပြုနိုင်ပါသည်",
        "manage_subscription": "💳 စာရင်းသွင်းမှုကို စီမံရန်",
        "upgrade": "⭐ အဆင့်မြှင့်ရန်",

        "karimen_master": "📝 Karimen Master",
        "honmen_master": "🛣 Honmen Master",

        "study_mode": "🧠 လေ့လာမှု မုဒ်",
        "reviewer_karimen": "🧠 Karimen ပြန်လည်လေ့ကျင့်ခန်း",
        "reviewer_honmen": "🧠 Honmen ပြန်လည်လေ့ကျင့်ခန်း",

        "karimen_mock": "📝 Karimen စမ်းသပ်စာမေးပွဲ",
        "karimen_test_1": "📝 Karimen Test 1",
        "karimen_test_2": "📝 Karimen Test 2",

        "honmen_mock": "🏁 Honmen စမ်းသပ်စာမေးပွဲ",
        "honmen_test_1": "🛣 Honmen Master",
        "honmen_test_2": "🏁 Honmen Test 2",
        "honmen_test_3": "🏁 Honmen Test 3",

        "app_info": "⚙️ အက်ပ် အချက်အလက်",
        "score_history": "📊 ရမှတ် မှတ်တမ်း",
        "privacy": "🔒 ကိုယ်ရေးလုံခြုံမှု မူဝါဒ",
        "terms": "📄 အသုံးပြုမှု စည်းမျဉ်းများ",
        "contact": "✉️ ဆက်သွယ်ရန်",

        "dark_mode": "🌙 အမှောင် မုဒ်",

        "login": "👤 လော့ဂ်အင်",
        "register": "📝 မှတ်ပုံတင်ရန်",
        "logout": "🚪 လော့ဂ်အောက်",
        "welcome": "ကြိုဆိုပါတယ်",

        "ai_title": "🧠 AI ဆရာ",
        "premium": "⭐ ပရီမီယမ် အသုံးပြုသူ",
        "select_language": "ဘာသာစကား ရွေးချယ်ပါ"
    }
}

# =========================================================
# 🌐 GET UI LANGUAGE
# =========================================================

def get_ui():

    language = session.get('lang', 'en')

    return UI_TEXT.get(
        language,
        UI_TEXT['en']
    )