import os
import json

def load_questions(folder, language, filename):

    filepath = os.path.join(
        "data",
        folder,
        language,
        filename
    )

    print("TRYING FILE:", filepath)

    if not os.path.exists(filepath):

        print("NOT FOUND, TRYING EN FALLBACK")

        filepath = os.path.join(
            "data",
            folder,
            "en",
            filename
        )

        print("FALLBACK FILE:", filepath)

    if not os.path.exists(filepath):

        print("FINAL FILE NOT FOUND:", filepath)

        return []

    try:

        with open(
            filepath,
            encoding="utf-8-sig"
        ) as f:

            data = json.load(f)

            print("LOADED QUESTIONS:", len(data))

            return data

    except Exception as e:

        print("JSON LOAD ERROR:", e)
        print("FAILED FILE:", filepath)

        return []