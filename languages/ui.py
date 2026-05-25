from flask import session

# =========================================================
# 🌐 UI TRANSLATIONS
# =========================================================

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

        "login": "👤 Login",
        "register": "📝 Register",
        "logout": "🚪 Logout",
        "welcome": "Welcome",

        "ai_title": "🧠 AI Tutor",

        "premium": "⭐ Premium User",

        "select_language": "Pumili ng Wika"
    },

    "ne": {
        "premium_reviewers": "🔒 प्रिमियम रिभ्युअर",

        "premium_features": "⭐ प्रिमियम सुविधाहरू",

        "unlock_premium": "🔒 प्रिमियम अनलक गर्नुहोस्",

        "premium_active": "✅ प्रिमियम सक्रिय",

        "manage_subscription": "💳 सदस्यता व्यवस्थापन",

        "upgrade": "⭐ अपग्रेड गर्नुहोस्",

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