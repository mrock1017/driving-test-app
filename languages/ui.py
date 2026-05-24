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

        "study_mode": "🧠 Study Mode",
        "reviewer_karimen": "🧠 Reviewer Karimen",
        "reviewer_honmen": "🧠 Reviewer Honmen",

        "karimen_mock": "📝 Karimen Mock Test",
        "karimen_test_1": "📝 Karimen Test 1",
        "karimen_test_2": "📝 Karimen Test 2",

        "honmen_mock": "🏁 Honmen Mock Test",
        "honmen_test_1": "🏁 Honmen Test 1",
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
        "honmen_test_1": "🏁 Honmen Test 1",
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

        "study_mode": "🧠 अध्ययन मोड",

        "reviewer_karimen": "🧠 करिमेन रिभ्युअर",

        "reviewer_honmen": "🧠 होनमेन रिभ्युअर",

        "karimen_mock": "📝 करिमेन मोक टेस्ट",

        "karimen_test_1": "📝 करिमेन परीक्षा १",

        "karimen_test_2": "📝 करिमेन परीक्षा २",

        "honmen_mock": "🏁 होनमेन मोक टेस्ट",

        "honmen_test_1": "🏁 होनमेन परीक्षा १",

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

        "study_mode": "🧠 Chế Độ Học",

        "reviewer_karimen": "🧠 Ôn Tập Karimen",

        "reviewer_honmen": "🧠 Ôn Tập Honmen",

        "karimen_mock": "📝 Bài Thi Karimen",

        "karimen_test_1": "📝 Bài Thi Karimen 1",

        "karimen_test_2": "📝 Bài Thi Karimen 2",

        "honmen_mock": "🏁 Bài Thi Honmen",

        "honmen_test_1": "🏁 Bài Thi Honmen 1",

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

        "study_mode": "🧠 Modo de Estudo",

        "reviewer_karimen": "🧠 Revisão Karimen",

        "reviewer_honmen": "🧠 Revisão Honmen",

        "karimen_mock": "📝 Teste Karimen",

        "karimen_test_1": "📝 Teste Karimen 1",

        "karimen_test_2": "📝 Teste Karimen 2",

        "honmen_mock": "🏁 Teste Honmen",

        "honmen_test_1": "🏁 Teste Honmen 1",

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