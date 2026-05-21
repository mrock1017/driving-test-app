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

        "premium": "⭐ Premium User"
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

        "premium": "⭐ Premium User"
    },

    "ne": {

        "study_mode": "🧠 अध्ययन मोड",
        "reviewer_karimen": "🧠 Reviewer Karimen",
        "reviewer_honmen": "🧠 Reviewer Honmen",

        "karimen_mock": "📝 Karimen Mock Test",
        "karimen_test_1": "📝 Karimen Test 1",
        "karimen_test_2": "📝 Karimen Test 2",

        "honmen_mock": "🏁 Honmen Mock Test",
        "honmen_test_1": "🏁 Honmen Test 1",
        "honmen_test_2": "🏁 Honmen Test 2",
        "honmen_test_3": "🏁 Honmen Test 3",

        "app_info": "⚙️ एप जानकारी",
        "score_history": "📊 स्कोर इतिहास",
        "privacy": "🔒 गोपनीयता नीति",
        "terms": "📄 प्रयोगका सर्तहरू",
        "contact": "✉️ सम्पर्क गर्नुहोस्",

        "dark_mode": "🌙 Dark Mode",

        "login": "👤 Login",
        "register": "📝 Register",
        "logout": "🚪 Logout",
        "welcome": "Welcome",

        "ai_title": "🧠 AI Tutor",

        "premium": "⭐ Premium User"
    },

        "vi": {

        "study_mode": "Chế Độ Học",

        "reviewer_karimen": "Ôn Tập Karimen",

        "reviewer_honmen": "Ôn Tập Honmen",

        "karimen_mock": "Bài Thi Karimen",

        "honmen_mock": "Honmen Master",

        "app_info": "Thông Tin Ứng Dụng",

        "dark_mode": "🌙 Chế Độ Tối",

        "login": "Đăng Nhập",

        "register": "Đăng Ký",

        "logout": "Đăng Xuất",

        "welcome": "Xin chào",

        "premium": "⭐ Premium",

        "privacy": "Chính Sách Riêng Tư",

        "terms": "Điều Khoản",

        "contact": "Liên Hệ",

        "score_history": "Lịch Sử Điểm"

    },

        "pt": {

        "study_mode": "Modo de Estudo",

        "reviewer_karimen": "Revisão Karimen",

        "reviewer_honmen": "Revisão Honmen",

        "karimen_mock": "Teste Karimen",

        "honmen_mock": "Honmen Master",

        "app_info": "Informações do App",

        "dark_mode": "🌙 Modo Escuro",

        "login": "Entrar",

        "register": "Registrar",

        "logout": "Sair",

        "welcome": "Bem-vindo",

        "premium": "⭐ Premium",

        "privacy": "Política de Privacidade",

        "terms": "Termos",

        "contact": "Contato",

        "score_history": "Histórico de Pontuação"

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