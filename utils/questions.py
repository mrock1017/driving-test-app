import os
import json

# =========================================================
# ✅ LOAD QUESTIONS
# =========================================================

def load_questions(folder, language, filename):

    filepath = os.path.join(
        "data",
        folder,
        language,
        filename
    )

    if not os.path.exists(filepath):

        filepath = os.path.join(
            "data",
            folder,
            "en",
            filename
        )

    if not os.path.exists(filepath):

        return []

    try:

        with open(
            filepath,
            encoding='utf-8-sig'
        ) as f:

            return json.load(f)

    except Exception as e:

        print("JSON ERROR:", e)
        print("FILE:", filepath)

        return []