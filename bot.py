import re
import os
from SafoneAPI import SafoneAPI
from pyrogram import Client, filters

Safone = Client(
    os.getenv("SESSION_STRING", "BQAik9QEBA2ce8pmyLSQUmU5xp3IVSOL_rEGNo3zNYap7j54ebLJPeEsGxON4EyTbpiTerm9irFfpLIQtBbYySFEKxMBzo0wtdeCbzizTqhuO1QwVbxL4PSanDINIaAoR-V7NlopZHsMXOhICEcshzc_M2boFRah4DRlFDKZZnkhr0jH48YZzM82b8Z9KwyOD99sTfMiEWu-lJ5d1rhlTxxb7VKwmru-IazuyAZyA-n16YoQRFvE0APA2QNw-ye1m6AY8gVfuwgTDmUdt651uL3VwX2Jb0cG925HTTL9APgMtFIPnCeiShTI_2cWd4XVRCqI1lRCZnICrAkZQjkf9cwXAAAAAWej9QcA"),
    api_id=os.getenv("API_ID", "13429768"),
    api_hash=os.getenv("API_HASH", "63b6d07b85e038eae4183c2902c4347b"),
)
api = SafoneAPI()


@Safone.on_message(filters.regex("sk_live_"))
async def sk_check_(c, m):
    k = await m.reply("`Checking... Please wait!`")
    check = await api.skcheck(m.text)
    result = "✅ **LIVE KEY** ✅\n\n" if check.status == 200 else "❌ **DEAD KEY** ❌\n\n"
    result += f"**KEY:** `{m.text}`\n**RESPONSE:** `{check.message}`\n\n🥷🏻 **Checked By** -» {m.from_user.mention}\n❤️ **Developed By** -» @mobius_die👑"
    await k.edit(result)


@Safone.on_message(filters.command("ccscrape", "."))
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
    file = f"x{count} CC Scrapped By @scrape.txt"
    caption = f"✅ **CC Scrapped Successfully!**\n\n**Source** -» `{chat}`\n**Amount** -» `{total}`\n**CC Found** -» `{count}`\n\n🥷🏻 **Scrapped By** -» {m.from_user.mention}\n❤️ **Developed By** -» @mobius_die👑"
    with open(file, "w+") as outfile:
        outfile.write(out)
    try:
        await m.reply_document(file, caption=caption)
        await k.delete()
        os.remove(file)
    except BaseException:
        await k.edit(f"❌ **No CC Found!**")

Safone.run()
