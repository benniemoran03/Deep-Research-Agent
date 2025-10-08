import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

class Summarizer:
    def summarize(self, docs, query):
        content = "\n\n".join(d["content"][:3000] for d in docs)
        prompt = f"""You are an academic researcher. 
Summarize the following sources about: "{query}".
Include citations and structured insights.

Sources:
{content[:15000]}"""

        resp = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return resp.choices[0].message.content
