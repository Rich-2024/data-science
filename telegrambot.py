# import asyncio
# from telegram import Bot
# from telegram.error import TelegramError

# BOT_TOKEN = '7474758626:AAFZ3BrJnP0aZ28f7usiMilsOGGPj-6RWo8'
# GROUP_CHAT_ID = '-1002746229552'

# bot = Bot(token=BOT_TOKEN)

# async def get_top_crypto_signals():
#     import aiohttp
#     url = "https://api.coingecko.com/api/v3/coins/markets"
#     params = {
#         'vs_currency': 'usd',
#         'order': 'market_cap_desc',
#         'per_page': 5,
#         'page': 1,
#         'price_change_percentage': '24h'
#     }
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url, params=params) as resp:
#             data = await resp.json()
#     signals = []
#     for coin in data:
#         name = coin['name']
#         price = coin['current_price']
#         change_24h = coin['price_change_percentage_24h']
#         signal = f"{name} - Price: ${price:.2f}, 24h Change: {change_24h:.2f}%"
#         signals.append(signal)
#     return signals

# async def post_signals():
#     while True:
#         signals = await get_top_crypto_signals()
#         message = "🔥 Top Crypto Signals:\n" + "\n".join(signals)
#         try:
#             await bot.send_message(chat_id=GROUP_CHAT_ID, text=message)
#             print("✅ Message posted successfully.")
#         except TelegramError as e:
#             print(f"❌ Failed to post message: {e}")
#         await asyncio.sleep(60)  # wait 60 seconds before posting again

# if __name__ == "__main__":
#     asyncio.run(post_signals())
import asyncio
from telegram import Bot
from telegram.error import TelegramError
import aiohttp

BOT_TOKEN = '7474758626:AAFZ3BrJnP0aZ28f7usiMilsOGGPj-6RWo8'
GROUP_CHAT_ID = '-1002746229552'

bot = Bot(token=BOT_TOKEN)

async def get_top_crypto_signals():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 5,
        "page": 1,
        "price_change_percentage": "24h",
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            data = await resp.json()

    signals = []
    for coin in data:
        name = coin["name"]
        price = coin["current_price"]
        change = coin.get("price_change_percentage_24h")

        if change is None:
            signal = "HOLD"
        elif change > 2:
            signal = "BUY"
        elif change < -2:
            signal = "SELL"
        else:
            signal = "HOLD"

        signals.append(
            f"{name} — 💵 ${price:.2f}, 📉 24h: {change:.2f}%, 📢 Signal: {signal}"
        )

    return signals

async def post_signals():
    while True:
        try:
            signals = await get_top_crypto_signals()
            message = "📊 *Top Crypto Signals*\n\n" + "\n".join(signals)
            await bot.send_message(chat_id=GROUP_CHAT_ID, text=message, parse_mode="Markdown")
            print("✅ Message posted successfully.")
        except TelegramError as e:
            print(f"❌ Failed to post message: {e}")
        except Exception as e:
            print(f"⚠️ Error: {e}")
        await asyncio.sleep(60)  # post every 60 seconds

if __name__ == "__main__":
    asyncio.run(post_signals())
