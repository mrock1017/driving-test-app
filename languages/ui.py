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

        "master_start": "🚀 Start Master Exam",
        "back_to_menu": "🏠 Back To Menu",
        "how_it_works": "How It Works",
        "exam_details": "📋 Exam Details",
        "questions_label": "Questions",
        "passing_score_label": "Passing Score",
        "time_limit_label": "Time Limit",
        "question_source_label": "Question Source",
        "generation_type_label": "Generation Type",
        "randomized_master_exam": "Randomized Master Exam",
        "karimen_question_bank": "Karimen Question Bank",
        "honmen_question_bank": "Honmen Question Bank",

        "gaimen_master": "🌏 Gaimen Kirikae Master",
        "gentsuki_master": "🛵 Gentsuki Master",
        "gaimen_question_bank": "Gaimen Kirikae Question Bank",
        "gentsuki_question_bank": "Gentsuki Question Bank",
        "total_score_label": "Total Score",
        "time_minutes": "Minutes",

        "master_exams": "📚 Master Exams",
        "generate_new_test": "🔄 Generate New Test",
        "return_to_menu": "🏠 Return To Menu",
        "reviewer_gaimen": "🌏 Reviewer Gaimen Kirikae",
        "reviewer_gentsuki": "🛵 Reviewer Gentsuki",

                "master_exam_description":
        "This exam is generated from a large question bank and may differ every time you attempt it.",

        "master_random_notice":
        "Every attempt generates a new randomized exam from the question bank. Questions may differ each time you start a new test.",

        "master_random_question_1":
        "Each attempt contains randomly selected questions.",

        "master_random_question_2":
        "Questions are generated from the question bank.",

        "master_random_question_3":
        "Every attempt may contain a different question combination.",

        "master_random_question_4":
        "This helps improve familiarity with actual Japanese driving examinations.",

        "master_random_question_5":
        "Reviewers remain available for study at any time.",

        "karimen_notice":
        "Karimen questions focus on basic traffic rules, road signs, and safe driving practices.",

        "honmen_notice":
        "Honmen questions include advanced traffic situations, hazard prediction, and practical driving judgment.",

        "gaimen_notice":
        "Many Gaimen Kirikae questions focus on Japanese-specific traffic rules and safe driving judgment.",

        "gentsuki_notice":
        "Gentsuki questions often focus on moped rules, speed restrictions, road signs, and safe riding behavior.",

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
        "backup_progress": "☁️ Backup Progress",
        "account_optional_note": "Optional: create an account to back up progress and restore Premium on another device.",
    },

    "tl": {
        "premium_reviewers": "🔒 Premium Reviewers",
        "premium_features": "⭐ Mga Premium Feature",
        "unlock_premium": "🔒 I-unlock ang Premium",
        "premium_active": "✅ Aktibo ang Premium",
        "manage_subscription": "💳 Pamahalaan ang Subscription",
        "upgrade": "⭐ Mag Upgrade",

        "karimen_master": "📝 Karimen Master",
        "honmen_master": "🛣 Honmen Master",

        "master_start": "🚀 Simulan ang Master Exam",
        "back_to_menu": "🏠 Bumalik sa Menu",
        "how_it_works": "Paano Ito Gumagana",
        "exam_details": "📋 Detalye ng Exam",
        "questions_label": "Mga Tanong",
        "passing_score_label": "Passing Score",
        "time_limit_label": "Limitasyon sa Oras",
        "question_source_label": "Pinagmulan ng Tanong",
        "generation_type_label": "Uri ng Pagbuo",
        "randomized_master_exam": "Randomized Master Exam",
        "karimen_question_bank": "Karimen Question Bank",
        "honmen_question_bank": "Honmen Question Bank",

        "gaimen_master": "🌏 Gaimen Kirikae Master",
        "gentsuki_master": "🛵 Gentsuki Master",
        "gaimen_question_bank": "Question Bank ng Gaimen Kirikae",
        "gentsuki_question_bank": "Question Bank ng Gentsuki",
        "total_score_label": "Kabuuang Iskor",
        "time_minutes": "Minuto",

        "master_exams": "📚 Mga Master Exam",
        "generate_new_test": "🔄 Gumawa ng Bagong Test",
        "return_to_menu": "🏠 Bumalik sa Menu",
        "reviewer_gaimen": "🌏 Reviewer ng Gaimen Kirikae",
        "reviewer_gentsuki": "🛵 Reviewer ng Gentsuki",

                "master_exam_description":
        "Ang exam na ito ay ginagawa mula sa malaking question bank at maaaring mag-iba sa bawat attempt.",

        "master_random_notice":
        "Bawat attempt ay gumagawa ng bagong randomized exam mula sa question bank. Maaaring mag-iba ang mga tanong sa bawat pagsisimula ng bagong test.",

        "master_random_question_1":
        "Bawat attempt ay may mga tanong na pinipili nang random.",

        "master_random_question_2":
        "Ang mga tanong ay kinukuha mula sa question bank.",

        "master_random_question_3":
        "Maaaring iba ang kombinasyon ng mga tanong sa bawat attempt.",

        "master_random_question_4":
        "Nakakatulong ito upang mas maging pamilyar ka sa tunay na Japanese driving examinations.",

        "master_random_question_5":
        "Ang reviewers ay maaari pa ring gamitin para sa pag-aaral anumang oras.",

        "karimen_notice":
        "Ang Karimen questions ay nakatuon sa basic traffic rules, road signs, at safe driving practices.",

        "honmen_notice":
        "Ang Honmen questions ay may advanced traffic situations, hazard prediction, at practical driving judgment.",

        "gaimen_notice":
        "Maraming Gaimen Kirikae questions ang nakatuon sa Japanese-specific traffic rules at safe driving judgment.",

        "gentsuki_notice":
        "Ang Gentsuki questions ay madalas nakatuon sa moped rules, speed restrictions, road signs, at safe riding behavior.",

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
        "select_language": "Pumili ng Wika",
        "unlimited_mock_exams": "⭐ Walang Limit na Mock Exams",
        "advanced_analytics": "⭐ Advanced Analytics",
        "ai_tutor_unlimited": "⭐ Walang Limit na AI Tutor",
        "reviewers": "📚 Reviewers",
        "settings": "⚙️ Settings",
        "account": "👤 Account",
        "language": "🌐 Wika",
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

        "master_start": "🚀 मास्टर परीक्षा सुरु गर्नुहोस्",
        "back_to_menu": "🏠 मेनुमा फर्कनुहोस्",
        "how_it_works": "यसले कसरी काम गर्छ",
        "exam_details": "📋 परीक्षा विवरण",
        "questions_label": "प्रश्नहरू",
        "passing_score_label": "उत्तीर्ण अंक",
        "time_limit_label": "समय सीमा",
        "question_source_label": "प्रश्न स्रोत",
        "generation_type_label": "बनाउने प्रकार",
        "randomized_master_exam": "अनियमित मास्टर परीक्षा",
        "karimen_question_bank": "करिमेन प्रश्न बैंक",
        "honmen_question_bank": "होनमेन प्रश्न बैंक",

        "gaimen_master": "🌏 गाइमें किरिकाए मास्टर",
        "gentsuki_master": "🛵 गेन्त्सुकी मास्टर",
        "gaimen_question_bank": "गाइमें किरिकाए प्रश्न बैंक",
        "gentsuki_question_bank": "गेन्त्सुकी प्रश्न बैंक",
        "total_score_label": "कुल अंक",
        "time_minutes": "मिनेट",

        "master_exams": "📚 मास्टर परीक्षाहरू",
        "generate_new_test": "🔄 नयाँ परीक्षा बनाउनुहोस्",
        "return_to_menu": "🏠 मेनुमा फर्कनुहोस्",
        "reviewer_gaimen": "🌏 गाइमें किरिकाए रिभ्युअर",
        "reviewer_gentsuki": "🛵 गेन्त्सुकी रिभ्युअर",

                "master_exam_description":
        "यो परीक्षा ठूलो प्रश्न बैंकबाट बनाइन्छ र प्रत्येक प्रयासमा फरक हुन सक्छ।",

        "master_random_notice":
        "हरेक प्रयासमा प्रश्न बैंकबाट नयाँ अनियमित परीक्षा बनाइन्छ। नयाँ टेस्ट सुरु गर्दा प्रश्नहरू फरक हुन सक्छन्।",

        "master_random_question_1":
        "हरेक प्रयासमा अनियमित रूपमा छानिएका प्रश्नहरू समावेश हुन्छन्।",

        "master_random_question_2":
        "प्रश्नहरू प्रश्न बैंकबाट उत्पन्न गरिन्छन्।",

        "master_random_question_3":
        "हरेक प्रयासमा प्रश्नहरूको संयोजन फरक हुन सक्छ।",

        "master_random_question_4":
        "यसले वास्तविक जापानी सवारी चालक परीक्षा प्रति परिचित हुन मद्दत गर्छ।",

        "master_random_question_5":
        "रिभ्युअरहरू कुनै पनि समयमा अध्ययनका लागि उपलब्ध रहनेछन्।",

        "karimen_notice":
        "करिमेन प्रश्नहरू आधारभूत ट्राफिक नियमहरू, सडक संकेतहरू, र सुरक्षित सवारी अभ्यासमा केन्द्रित हुन्छन्।",

        "honmen_notice":
        "होनमेन प्रश्नहरू उन्नत ट्राफिक अवस्था, जोखिम पूर्वानुमान, र व्यावहारिक सवारी निर्णय समावेश गर्छन्।",

        "gaimen_notice":
        "धेरै गाइमेन किरिकाए प्रश्नहरू जापान-विशेष ट्राफिक नियमहरू र सुरक्षित सवारी निर्णयमा केन्द्रित हुन्छन्।",

        "gentsuki_notice":
        "गेन्त्सुकी प्रश्नहरू प्रायः मोपेड नियमहरू, गति सीमाहरू, सडक संकेतहरू, र सुरक्षित सवारी व्यवहारमा केन्द्रित हुन्छन्।",

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

        "master_start": "🚀 Bắt Đầu Bài Thi Master",
        "back_to_menu": "🏠 Quay Lại Menu",
        "how_it_works": "Cách Hoạt Động",
        "exam_details": "📋 Chi Tiết Bài Thi",
        "questions_label": "Câu Hỏi",
        "passing_score_label": "Điểm Đạt",
        "time_limit_label": "Thời Gian Giới Hạn",
        "question_source_label": "Nguồn Câu Hỏi",
        "generation_type_label": "Kiểu Tạo Đề",
        "randomized_master_exam": "Bài Thi Master Ngẫu Nhiên",
        "karimen_question_bank": "Ngân Hàng Câu Hỏi Karimen",
        "honmen_question_bank": "Ngân Hàng Câu Hỏi Honmen",

        "gaimen_master": "🌏 Gaimen Kirikae Master",
        "gentsuki_master": "🛵 Gentsuki Master",
        "gaimen_question_bank": "Ngân Hàng Câu Hỏi Gaimen Kirikae",
        "gentsuki_question_bank": "Ngân Hàng Câu Hỏi Gentsuki",
        "total_score_label": "Tổng Điểm",
        "time_minutes": "Phút",

        "master_exams": "📚 Bài Thi Master",
        "generate_new_test": "🔄 Tạo Bài Thi Mới",
        "return_to_menu": "🏠 Quay Lại Menu",
        "reviewer_gaimen": "🌏 Ôn Tập Gaimen Kirikae",
        "reviewer_gentsuki": "🛵 Ôn Tập Gentsuki",

                "master_exam_description":
        "Bài thi này được tạo từ một ngân hàng câu hỏi lớn và có thể khác nhau trong mỗi lần làm bài.",

        "master_random_notice":
        "Mỗi lần làm bài sẽ tạo ra một bài thi ngẫu nhiên mới từ ngân hàng câu hỏi. Các câu hỏi có thể thay đổi mỗi khi bạn bắt đầu bài thi mới.",

        "master_random_question_1":
        "Mỗi lần làm bài đều chứa các câu hỏi được chọn ngẫu nhiên.",

        "master_random_question_2":
        "Các câu hỏi được lấy từ ngân hàng câu hỏi.",

        "master_random_question_3":
        "Mỗi lần làm bài có thể có tổ hợp câu hỏi khác nhau.",

        "master_random_question_4":
        "Điều này giúp bạn làm quen tốt hơn với các kỳ thi lái xe thực tế tại Nhật Bản.",

        "master_random_question_5":
        "Các mục ôn tập vẫn luôn có sẵn để học bất cứ lúc nào.",

        "karimen_notice":
        "Các câu hỏi Karimen tập trung vào luật giao thông cơ bản, biển báo giao thông và các nguyên tắc lái xe an toàn.",

        "honmen_notice":
        "Các câu hỏi Honmen bao gồm các tình huống giao thông nâng cao, dự đoán nguy hiểm và đánh giá kỹ năng lái xe thực tế.",

        "gaimen_notice":
        "Nhiều câu hỏi Gaimen Kirikae tập trung vào các quy tắc giao thông đặc thù của Nhật Bản và khả năng phán đoán lái xe an toàn.",

        "gentsuki_notice":
        "Các câu hỏi Gentsuki thường tập trung vào quy định dành cho xe gắn máy nhỏ, giới hạn tốc độ, biển báo giao thông và hành vi lái xe an toàn.",

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

        "master_start": "🚀 Iniciar Exame Master",
        "back_to_menu": "🏠 Voltar ao Menu",
        "how_it_works": "Como Funciona",
        "exam_details": "📋 Detalhes do Exame",
        "questions_label": "Perguntas",
        "passing_score_label": "Pontuação para Aprovação",
        "time_limit_label": "Limite de Tempo",
        "question_source_label": "Fonte das Perguntas",
        "generation_type_label": "Tipo de Geração",
        "randomized_master_exam": "Exame Master Aleatório",
        "karimen_question_bank": "Banco de Perguntas Karimen",
        "honmen_question_bank": "Banco de Perguntas Honmen",

        "gaimen_master": "🌏 Mestre Gaimen Kirikae",
        "gentsuki_master": "🛵 Mestre Gentsuki",
        "gaimen_question_bank": "Banco de Perguntas Gaimen Kirikae",
        "gentsuki_question_bank": "Banco de Perguntas Gentsuki",
        "total_score_label": "Pontuação Total",
        "time_minutes": "Minutos",

        "master_exams": "📚 Exames Master",
        "generate_new_test": "🔄 Gerar Novo Teste",
        "return_to_menu": "🏠 Voltar ao Menu",
        "reviewer_gaimen": "🌏 Revisão Gaimen Kirikae",
        "reviewer_gentsuki": "🛵 Revisão Gentsuki",

                "master_exam_description":
        "Este exame é gerado a partir de um grande banco de perguntas e pode ser diferente a cada tentativa.",

        "master_random_notice":
        "Cada tentativa gera um novo exame aleatório a partir do banco de perguntas. As perguntas podem mudar toda vez que você iniciar um novo teste.",

        "master_random_question_1":
        "Cada tentativa contém perguntas selecionadas aleatoriamente.",

        "master_random_question_2":
        "As perguntas são geradas a partir do banco de perguntas.",

        "master_random_question_3":
        "Cada tentativa pode apresentar uma combinação diferente de perguntas.",

        "master_random_question_4":
        "Isso ajuda você a se familiarizar melhor com os exames reais de direção do Japão.",

        "master_random_question_5":
        "Os revisores continuam disponíveis para estudo a qualquer momento.",

        "karimen_notice":
        "As perguntas do Karimen focam em regras básicas de trânsito, placas de sinalização e práticas de direção segura.",

        "honmen_notice":
        "As perguntas do Honmen incluem situações avançadas de trânsito, previsão de riscos e julgamento prático na condução.",

        "gaimen_notice":
        "Muitas perguntas do Gaimen Kirikae focam em regras de trânsito específicas do Japão e em decisões seguras ao dirigir.",

        "gentsuki_notice":
        "As perguntas do Gentsuki geralmente focam em regras para ciclomotores, limites de velocidade, placas de trânsito e comportamento seguro ao pilotar.",

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
        "premium_reviewers": "🔒 Reviewer Premium",
        "premium_features": "⭐ Fitur Premium",
        "unlock_premium": "🔒 Buka Premium",
        "premium_active": "✅ Premium Aktif",
        "manage_subscription": "💳 Kelola Langganan",
        "upgrade": "⭐ Upgrade",

        "karimen_master": "📝 Karimen Master",
        "honmen_master": "🛣 Honmen Master",

        "master_start": "🚀 Mulai Ujian Master",
        "back_to_menu": "🏠 Kembali ke Menu",
        "how_it_works": "Cara Kerjanya",
        "exam_details": "📋 Detail Ujian",
        "questions_label": "Pertanyaan",
        "passing_score_label": "Nilai Kelulusan",
        "time_limit_label": "Batas Waktu",
        "question_source_label": "Sumber Pertanyaan",
        "generation_type_label": "Jenis Pembuatan",
        "randomized_master_exam": "Ujian Master Acak",
        "karimen_question_bank": "Bank Soal Karimen",
        "honmen_question_bank": "Bank Soal Honmen",

        "gaimen_master": "🌏 Master Gaimen Kirikae",
        "gentsuki_master": "🛵 Master Gentsuki",
        "gaimen_question_bank": "Bank Soal Gaimen Kirikae",
        "gentsuki_question_bank": "Bank Soal Gentsuki",
        "total_score_label": "Total Nilai",
        "time_minutes": "Menit",

        "master_exams": "📚 Ujian Master",
        "generate_new_test": "🔄 Buat Tes Baru",
        "return_to_menu": "🏠 Kembali ke Menu",
        "reviewer_gaimen": "🌏 Reviewer Gaimen Kirikae",
        "reviewer_gentsuki": "🛵 Reviewer Gentsuki",

                "master_exam_description":
        "Ujian ini dibuat dari bank soal yang besar dan dapat berbeda setiap kali Anda mencobanya.",

        "master_random_notice":
        "Setiap percobaan akan menghasilkan ujian acak baru dari bank soal. Pertanyaan dapat berbeda setiap kali Anda memulai tes baru.",

        "master_random_question_1":
        "Setiap percobaan berisi pertanyaan yang dipilih secara acak.",

        "master_random_question_2":
        "Pertanyaan diambil dari bank soal.",

        "master_random_question_3":
        "Setiap percobaan dapat memiliki kombinasi pertanyaan yang berbeda.",

        "master_random_question_4":
        "Hal ini membantu Anda lebih terbiasa dengan ujian mengemudi Jepang yang sebenarnya.",

        "master_random_question_5":
        "Reviewer tetap tersedia untuk belajar kapan saja.",

        "karimen_notice":
        "Soal Karimen berfokus pada peraturan lalu lintas dasar, rambu jalan, dan praktik berkendara yang aman.",

        "honmen_notice":
        "Soal Honmen mencakup situasi lalu lintas tingkat lanjut, prediksi bahaya, dan penilaian berkendara secara praktis.",

        "gaimen_notice":
        "Banyak soal Gaimen Kirikae berfokus pada peraturan lalu lintas khusus Jepang dan penilaian berkendara yang aman.",

        "gentsuki_notice":
        "Soal Gentsuki sering berfokus pada aturan moped, batas kecepatan, rambu lalu lintas, dan perilaku berkendara yang aman.",

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
        "select_language": "Pilih Bahasa"
    },

    "ar": {
        "premium_reviewers": "🔒 مراجعات بريميوم",
        "premium_features": "⭐ ميزات بريميوم",
        "unlock_premium": "🔒 فتح بريميوم",
        "premium_active": "✅ البريميوم مفعل",
        "manage_subscription": "💳 إدارة الاشتراك",
        "upgrade": "⭐ ترقية",

        "karimen_master": "📝 كاريمين ماستر",
        "honmen_master": "🛣 هونمن ماستر",

        "master_start": "🚀 ابدأ اختبار الماستر",
        "back_to_menu": "🏠 العودة إلى القائمة",
        "how_it_works": "كيف يعمل",
        "exam_details": "📋 تفاصيل الاختبار",
        "questions_label": "الأسئلة",
        "passing_score_label": "درجة النجاح",
        "time_limit_label": "الوقت المحدد",
        "question_source_label": "مصدر الأسئلة",
        "generation_type_label": "نوع التوليد",
        "randomized_master_exam": "اختبار ماستر عشوائي",
        "karimen_question_bank": "بنك أسئلة كاريمين",
        "honmen_question_bank": "بنك أسئلة هونمن",

        "gaimen_master": "🌏 ماستر غايمن كيريكاي",
        "gentsuki_master": "🛵 ماستر جينتسوكي",
        "gaimen_question_bank": "بنك أسئلة غايمن كيريكاي",
        "gentsuki_question_bank": "بنك أسئلة جينتسوكي",
        "total_score_label": "إجمالي الدرجات",
        "time_minutes": "دقائق",

        "master_exams": "📚 اختبارات الماستر",
        "generate_new_test": "🔄 إنشاء اختبار جديد",
        "return_to_menu": "🏠 العودة إلى القائمة",
        "reviewer_gaimen": "🌏 مراجعة غايمن كيريكاي",
        "reviewer_gentsuki": "🛵 مراجعة جينتسوكي",

                "master_exam_description":
        "يتم إنشاء هذا الاختبار من بنك أسئلة كبير وقد يختلف في كل مرة تقوم بمحاولته.",

        "master_random_notice":
        "في كل محاولة يتم إنشاء اختبار عشوائي جديد من بنك الأسئلة. قد تختلف الأسئلة في كل مرة تبدأ فيها اختبارًا جديدًا.",

        "master_random_question_1":
        "تحتوي كل محاولة على أسئلة يتم اختيارها بشكل عشوائي.",

        "master_random_question_2":
        "يتم إنشاء الأسئلة من بنك الأسئلة.",

        "master_random_question_3":
        "قد تحتوي كل محاولة على مجموعة مختلفة من الأسئلة.",

        "master_random_question_4":
        "يساعدك ذلك على التعود بشكل أفضل على اختبارات القيادة اليابانية الفعلية.",

        "master_random_question_5":
        "تبقى المراجعات متاحة للدراسة في أي وقت.",

        "karimen_notice":
        "تركز أسئلة كاريمين على قواعد المرور الأساسية، وإشارات الطرق، وممارسات القيادة الآمنة.",

        "honmen_notice":
        "تتضمن أسئلة هونمن مواقف مرورية متقدمة، والتنبؤ بالمخاطر، واتخاذ القرارات العملية أثناء القيادة.",

        "gaimen_notice":
        "تركز العديد من أسئلة غايمن كيريكاي على قواعد المرور الخاصة باليابان واتخاذ القرارات الآمنة أثناء القيادة.",

        "gentsuki_notice":
        "تركز أسئلة جينتسوكي غالبًا على قواعد الدراجات الصغيرة (الموبيد)، وحدود السرعة، وإشارات المرور، وسلوك القيادة الآمن.",

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
        "select_language": "اختر اللغة"
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

        "master_start": "🚀 ماسٹر امتحان شروع کریں",
        "back_to_menu": "🏠 مینو پر واپس جائیں",
        "how_it_works": "یہ کیسے کام کرتا ہے",
        "exam_details": "📋 امتحان کی تفصیلات",
        "questions_label": "سوالات",
        "passing_score_label": "پاسنگ اسکور",
        "time_limit_label": "وقت کی حد",
        "question_source_label": "سوالات کا ماخذ",
        "generation_type_label": "جنریشن کی قسم",
        "randomized_master_exam": "رینڈم ماسٹر امتحان",
        "karimen_question_bank": "کاریمن سوالات کا بینک",
        "honmen_question_bank": "ہونمین سوالات کا بینک",

        "gaimen_master": "🌏 گائیمین کیریکائے ماسٹر",
        "gentsuki_master": "🛵 گینتسوکی ماسٹر",
        "gaimen_question_bank": "گائیمین کیریکائے سوالات کا بینک",
        "gentsuki_question_bank": "گینتسوکی سوالات کا بینک",
        "total_score_label": "کل اسکور",
        "time_minutes": "منٹ",

        "master_exams": "📚 ماسٹر امتحانات",
        "generate_new_test": "🔄 نیا امتحان بنائیں",
        "return_to_menu": "🏠 مینو پر واپس جائیں",
        "reviewer_gaimen": "🌏 گائیمین کیریکائے ریویور",
        "reviewer_gentsuki": "🛵 گینتسوکی ریویور",

                "master_exam_description":
        "یہ امتحان ایک بڑے سوالات کے بینک سے تیار کیا جاتا ہے اور ہر کوشش میں مختلف ہو سکتا ہے۔",

        "master_random_notice":
        "ہر کوشش میں سوالات کے بینک سے ایک نیا رینڈم امتحان تیار کیا جاتا ہے۔ ہر بار نیا ٹیسٹ شروع کرنے پر سوالات مختلف ہو سکتے ہیں۔",

        "master_random_question_1":
        "ہر کوشش میں رینڈم طور پر منتخب کیے گئے سوالات شامل ہوتے ہیں۔",

        "master_random_question_2":
        "سوالات سوالات کے بینک سے تیار کیے جاتے ہیں۔",

        "master_random_question_3":
        "ہر کوشش میں سوالات کا مجموعہ مختلف ہو سکتا ہے۔",

        "master_random_question_4":
        "یہ آپ کو جاپان کے اصل ڈرائیونگ امتحانات سے بہتر طور پر واقف ہونے میں مدد دیتا ہے۔",

        "master_random_question_5":
        "ریویورز کسی بھی وقت مطالعے کے لیے دستیاب رہتے ہیں۔",

        "karimen_notice":
        "کاریمن سوالات بنیادی ٹریفک قوانین، سڑک کے اشاروں اور محفوظ ڈرائیونگ کے طریقوں پر مرکوز ہوتے ہیں۔",

        "honmen_notice":
        "ہونمین سوالات میں جدید ٹریفک صورتحال، خطرات کی پیش گوئی اور عملی ڈرائیونگ فیصلے شامل ہوتے ہیں۔",

        "gaimen_notice":
        "بہت سے گائیمین کیریکائے سوالات جاپان کے مخصوص ٹریفک قوانین اور محفوظ ڈرائیونگ فیصلوں پر مرکوز ہوتے ہیں۔",

        "gentsuki_notice":
        "گینتسوکی سوالات عموماً موپیڈ قوانین، رفتار کی حد، سڑک کے اشاروں اور محفوظ سواری کے رویوں پر مرکوز ہوتے ہیں۔",

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

        "master_start": "🚀 Master စာမေးပွဲ စတင်ရန်",
        "back_to_menu": "🏠 မီနူးသို့ ပြန်သွားရန်",
        "how_it_works": "ဘယ်လို အလုပ်လုပ်သလဲ",
        "exam_details": "📋 စာမေးပွဲ အချက်အလက်",
        "questions_label": "မေးခွန်းများ",
        "passing_score_label": "အောင်မှတ်",
        "time_limit_label": "အချိန်ကန့်သတ်ချက်",
        "question_source_label": "မေးခွန်းရင်းမြစ်",
        "generation_type_label": "ထုတ်လုပ်မှုအမျိုးအစား",
        "randomized_master_exam": "ကျပန်း Master စာမေးပွဲ",
        "karimen_question_bank": "Karimen မေးခွန်းဘဏ်",
        "honmen_question_bank": "Honmen မေးခွန်းဘဏ်",

        "gaimen_master": "🌏 Gaimen Kirikae မာစတာ",
        "gentsuki_master": "🛵 Gentsuki မာစတာ",
        "gaimen_question_bank": "Gaimen Kirikae မေးခွန်းဘဏ်",
        "gentsuki_question_bank": "Gentsuki မေးခွန်းဘဏ်",
        "total_score_label": "စုစုပေါင်း ရမှတ်",
        "time_minutes": "မိနစ်",

        "master_exams": "📚 မာစတာ စာမေးပွဲများ",
        "generate_new_test": "🔄 စာမေးပွဲအသစ် ဖန်တီးရန်",
        "return_to_menu": "🏠 မီနူးသို့ ပြန်သွားရန်",
        "reviewer_gaimen": "🌏 Gaimen Kirikae ပြန်လည်လေ့ကျင့်ခန်း",
        "reviewer_gentsuki": "🛵 Gentsuki ပြန်လည်လေ့ကျင့်ခန်း",

                "master_exam_description":
        "ဤစာမေးပွဲသည် မေးခွန်းဘဏ်ကြီးမှ ဖန်တီးထားပြီး ကြိုးစားမှုတိုင်းတွင် ကွဲပြားနိုင်ပါသည်။",

        "master_random_notice":
        "ကြိုးစားမှုတိုင်းတွင် မေးခွန်းဘဏ်မှ ကျပန်းစာမေးပွဲအသစ်ကို ဖန်တီးပေးပါသည်။ စာမေးပွဲအသစ် စတင်တိုင်း မေးခွန်းများ ကွဲပြားနိုင်ပါသည်။",

        "master_random_question_1":
        "ကြိုးစားမှုတိုင်းတွင် ကျပန်းရွေးချယ်ထားသော မေးခွန်းများ ပါဝင်ပါသည်။",

        "master_random_question_2":
        "မေးခွန်းများကို မေးခွန်းဘဏ်မှ ထုတ်လုပ်ပေးပါသည်။",

        "master_random_question_3":
        "ကြိုးစားမှုတိုင်းတွင် မေးခွန်းပေါင်းစပ်မှု ကွဲပြားနိုင်ပါသည်။",

        "master_random_question_4":
        "၎င်းသည် ဂျပန်ယာဉ်မောင်းစာမေးပွဲအစစ်များနှင့် ပိုမိုရင်းနှီးလာစေရန် ကူညီပေးပါသည်။",

        "master_random_question_5":
        "ပြန်လည်လေ့ကျင့်ခန်းများကို မည်သည့်အချိန်တွင်မဆို လေ့လာနိုင်ပါသည်။",

        "karimen_notice":
        "Karimen မေးခွန်းများသည် အခြေခံယာဉ်စည်းကမ်းများ၊ လမ်းညွှန်ဆိုင်းဘုတ်များနှင့် လုံခြုံသောမောင်းနှင်မှုအလေ့အကျင့်များကို အဓိကထားပါသည်။",

        "honmen_notice":
        "Honmen မေးခွန်းများတွင် အဆင့်မြင့်ယာဉ်အသွားအလာအခြေအနေများ၊ အန္တရာယ်ကြိုတင်ခန့်မှန်းခြင်းနှင့် လက်တွေ့မောင်းနှင်မှု ဆုံးဖြတ်ချက်များ ပါဝင်ပါသည်။",

        "gaimen_notice":
        "Gaimen Kirikae မေးခွန်းအများစုသည် ဂျပန်နိုင်ငံအတွက် သီးသန့်ယာဉ်စည်းကမ်းများနှင့် လုံခြုံသောမောင်းနှင်မှု ဆုံးဖြတ်ချက်များကို အဓိကထားပါသည်။",

        "gentsuki_notice":
        "Gentsuki မေးခွန်းများသည် မော်ပက်စည်းကမ်းများ၊ အမြန်နှုန်းကန့်သတ်ချက်များ၊ လမ်းညွှန်ဆိုင်းဘုတ်များနှင့် လုံခြုံသောစီးနင်းမှုအပြုအမူများကို အဓိကထားလေ့ရှိပါသည်。",

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