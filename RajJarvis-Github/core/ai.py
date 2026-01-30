import requests


OLLAMA_URL = "http://localhost:11434/api/generate"


def ask_ai(prompt):

    data = {
        "model": "phi",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=data,
            timeout=60
        )

        if response.status_code == 200:
            result = response.json()
            return result.get("response", "").strip()

        else:
            return "AI server error"

    except Exception as e:
        return "AI is not responding"
