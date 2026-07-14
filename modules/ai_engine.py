import requests


class AIEngine:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = (
            "https://generativelanguage.googleapis.com/"
            "v1beta/models/gemini-2.5-flash:generateContent"
        )

    def review_code(self, code, static_analysis):
        if not self.api_key:
            return "AI review skipped: API key is missing."

        prompt = f"""
You are a senior software engineer reviewing a Git pull request.

Review only the changed code.

Static analysis:
{static_analysis}

Changed code:
{code}

Check:
1. Code quality
2. Possible bugs
3. Security risks
4. Database/query issues
5. Duplicate or reusable logic
6. Performance issues

Give short, practical suggestions.
"""

        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }

        try:
            response = requests.post(
                self.api_url,
                params={"key": self.api_key},
                json=payload,
                timeout=30
            )

            response.raise_for_status()
            data = response.json()

            return data["candidates"][0]["content"]["parts"][0]["text"]

        except Exception as error:
            return f"AI review failed: {str(error)}"  