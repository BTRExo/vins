# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# ReCode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import time
from datetime import datetime
from secrets import choice

from speedtest import Speedtest

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, StartTime
from userbot.events import register
from userbot.utils import edit_or_reply, humanbytes, man_cmd

absen = [
    "**Hadir bang** π",
    "**Hadir kak** π",
    "**Hadir dong** π",
    "**Hadir ganteng** π₯΅",
    "**Hadir bro** π",
    "**Hadir kak maap telat** π₯Ί",
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@man_cmd(pattern="ping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(ping, "**β§**")
    await xx.edit("**β§β§**")
    await xx.edit("**β§β§β§**")
    await xx.edit("**β§β§β§β§**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await xx.edit(
        f"**β πΏπΎπ½πΆ!!π**\n"
        f"**ββ’ πΏπΈπ½πΆπ΄π -** `%sms`\n"
        f"**ββ’ ππΏππΈπΌπ΄ -** `{uptime}`\n"
        f"**ββ’ πΎππ½π΄π :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@man_cmd(pattern="xping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xping = await edit_or_reply(ping, "`PΙͺΙ΄Ι’ΙͺΙ΄Ι’....`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xping.edit(
        f"**β α΄α΄Ι΄Ι’!!π€**\n**ββ’ α΄ΙͺΙ΄Ι’α΄Κ :** `%sms`\n**ββ’ Κα΄α΄ α΄α΄α΄Ιͺα΄α΄ :** `{uptime}` π" % (duration)
    )


@man_cmd(pattern="lping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    lping = await edit_or_reply(ping, "**β PING β**")
    await lping.edit("**ββ PING ββ**")
    await lping.edit("**βββ PING βββ**")
    await lping.edit("**ββββ PING ββββ**")
    await lping.edit("**π PONG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await lping.edit(
        f"β **Pinger -** "
        f"`%sms` \n"
        f"β **Uptime -** "
        f"`{uptime}` \n"
        f"**β¦ Owner :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@man_cmd(pattern="keping$")
async def _(pong):
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kopong = await edit_or_reply(pong, "**γβππππππγ**")
    await kopong.edit("**ββπππππππββ**")
    await kopong.edit("**ππππππππ ππππ πππ πππ**")
    await kopong.edit("**ππππ πππππππ ππππππππ πππ**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await kopong.edit(
        f"**β² πΊπΎπ½ππΎπ» πΌπ΄π»π΄π³ππΆ** "
        f"\n β«Έ α΄·α΅βΏα΅α΅Λ‘ - `%sms` \n"
        f"**β² π±πΈπΉπΈ πΏπ΄π»π΄π** "
        f"\n β«Έ α΄·α΅α΅α΅α΅βΏα΅ -γ[{user.first_name}](tg://user?id={user.id})γ \n" % (duration)
    )


# .keping & kping Coded by Koala


@man_cmd(pattern=r"kping$")
async def _(pong):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kping = await edit_or_reply(pong, "8β===D")
    await kping.edit("8=β==D")
    await kping.edit("8==β=D")
    await kping.edit("8===βD")
    await kping.edit("8==β=D")
    await kping.edit("8=β==D")
    await kping.edit("8β===D")
    await kping.edit("8=β==D")
    await kping.edit("8==β=D")
    await kping.edit("8===βD")
    await kping.edit("8==β=D")
    await kping.edit("8=β==D")
    await kping.edit("8β===D")
    await kping.edit("8=β==D")
    await kping.edit("8==β=D")
    await kping.edit("8===βD")
    await kping.edit("8===βDπ¦")
    await kping.edit("8====Dπ¦π¦")
    await kping.edit("**CRO0TTTT PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await kping.edit(
        f"**NGENTOT!! π¨**\n**KAMPANG** : %sms\n**Bot Uptime** : {uptime}π" % (duration)
    )


@man_cmd(pattern="speedtest$")
async def _(speed):
    xxnx = await edit_or_reply(speed, "`Running speed test...`")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    msg = (
        f"**Started at {result['timestamp']}**\n\n"
        "**Client**\n"
        f"**ISP :** `{result['client']['isp']}`\n"
        f"**Country :** `{result['client']['country']}`\n\n"
        "**Server**\n"
        f"**Name :** `{result['server']['name']}`\n"
        f"**Country :** `{result['server']['country']}`\n"
        f"**Sponsor :** `{result['server']['sponsor']}`\n\n"
        f"**Ping :** `{result['ping']}`\n"
        f"**Upload :** `{humanbytes(result['upload'])}/s`\n"
        f"**Download :** `{humanbytes(result['download'])}/s`"
    )
    await xxnx.delete()
    await speed.client.send_file(
        speed.chat_id,
        result["share"],
        caption=msg,
        force_document=False,
    )


@man_cmd(pattern="pong$")
async def _(pong):
    start = datetime.now()
    xx = await edit_or_reply(pong, "`Sepong.....π`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await xx.edit("π **Ping!**\n`%sms`" % (duration))


# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK π‘
@register(pattern=r"^\.absen$", sudo=True)
async def risman(ganteng):
    await ganteng.reply(choice(absen))


# JANGAN DI HAPUS GOBLOK π‘ LU COPY AJA TINGGAL TAMBAHIN
# DI HAPUS GUA GBAN YA π₯΄ GUA TANDAIN LU AKUN TELENYA π‘


CMD_HELP.update(
    {
        "ping": f"**Plugin : **`ping`\
        \n\n  β’  **Syntax :** `{cmd}ping` ; `{cmd}lping` ; `{cmd}xping` ; `{cmd}kping`\
        \n  β’  **Function : **Untuk menunjukkan ping userbot.\
        \n\n  β’  **Syntax :** `{cmd}pong`\
        \n  β’  **Function : **Sama seperti perintah ping\
    "
    }
)


CMD_HELP.update(
    {
        "speedtest": f"**Plugin : **`speedtest`\
        \n\n  β’  **Syntax :** `{cmd}speedtest`\
        \n  β’  **Function : **Untuk Mengetes kecepatan server userbot.\
    "
    }
)
