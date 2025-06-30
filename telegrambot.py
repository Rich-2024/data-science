import asyncio
import datetime
import openai
from telegram import Bot

# Config
TELEGRAM_BOT_TOKEN = '7474758626:AAFZ3BrJnP0aZ28f7usiMilsOGGPj-6RWo8'
CHAT_ID = '@RichieForexComunity'
OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY
bot = Bot(token=TELEGRAM_BOT_TOKEN)

async def test_telegram_send():
    try:
        await bot.send_message(chat_id=CHAT_ID, text="Test message from bot")
        print("Test message sent successfully")
    except Exception as e:
        print("Failed to send test message:", e)

def generate_content():
    print("[INFO] Generating AI content...")
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Share a short Forex trading tip or motivation."}]
        )
        content = response.choices[0].message.content.strip()
        print(f"[INFO] AI content generated: {content}")
        return content
    except Exception as e:
        print("[ERROR] AI generation failed:", e)
        fallback = "Tip: Plan your trade and trade your plan."
        print("[INFO] Using fallback tip:", fallback)
        return fallback

async def post_to_telegram():
    content = generate_content()  # synchronous call
    try:
        await bot.send_message(chat_id=CHAT_ID, text=content)
        print(f"[{datetime.datetime.now()}] Posted to Telegram: {content}")
    except Exception as e:
        print("[ERROR] Telegram posting failed:", e)

async def main():
    await test_telegram_send()  # Test on start

    print(f"Bot is running... Posting every 1 minute to {CHAT_ID}")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            await post_to_telegram()
            await asyncio.sleep(60)
    except KeyboardInterrupt:
        print("Bot stopped by user.")

if __name__ == "__main__":
    asyncio.run(main())