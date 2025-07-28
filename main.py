# نویسنده سورس : سید محمد حسین موسوی رجا
# روبیکا : @O_and_ONE_01
# تلگرام : @Hacker123457890
from fast_rub import Client,Update,filters
import httpx
bot=Client("bot_speaker")
@bot.on_message_updates(filters=filters.is_user())
async def main(message:Update):
    try:
        async with httpx.AsyncClient() as cl:
            result=await cl.get(f"https://api.parssource.ir/spokesperson/?text={message.text}")
            result=(result.json())['result']
            if result:
                await message.reply(result+"""

کانال کتابخانه fast rub : @fast_rub""")
    except Exception as e:
        print(e)
bot.run()
# نویسنده سورس : سید محمد حسین موسوی رجا
# روبیکا : @O_and_ONE_01
# تلگرام : @Hacker123457890
