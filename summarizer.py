import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_article(title, summary, link):
    prompt = f"Summarize the following cyber threat article for a Medium blog post. Include the title and a short summary. Mention the link at the end.\n\nTitle: {title}\n\nSummary: {summary}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=400
    )
    
    return response.choices[0].message['content']
