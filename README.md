# 🛡 Cyber Threat Auto Blog Bot

This bot fetches cyber threat news from trusted sources, summarizes it using GPT, and publishes it to your Medium blog.

## ⚙️ Setup

1. Clone or download the repo
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file from `.env.example` and add your keys:
   - `OPENAI_API_KEY`
   - `MEDIUM_INTEGRATION_TOKEN`
4. Run the bot:
   ```
   python main.py
   ```

## 🔁 Optional: Automate with cron
Use `cron` (Linux/macOS) or Task Scheduler (Windows) to run `main.py` daily.
