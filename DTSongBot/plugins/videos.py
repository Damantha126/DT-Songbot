# Plugin by @Mr_Dark_Prince
# Anki Vector Updates <https://t.me/ankivectorUpdates>

import os
import requests
import aiohttp
import youtube_dl
from pytube import YouTube
from DTSongBot import DTbot as app
from pyrogram import filters, Client
from youtube_search import YoutubeSearch
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputTextMessageContent

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))

@app.on_message(filters.command('video'))
def ytmusic(client, message):
    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('𝙋𝙧𝙤𝙘𝙚𝙨𝙨𝙞𝙣𝙜 ••• 🚀')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com/watch?v={results[0]['url_suffix']}"
        #print(results)
        thum = mio[0]["title"]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)

        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]
        yt = YouTube(link)
    except Exception as e:
        m.edit(
            "❌ Found Nothing.\n\nTry another keywork or maybe spell it properly."
        )
        print(str(e))
        return
    m.edit("𝘿𝙤𝙬𝙣𝙡𝙤𝒹𝙞𝙣𝙜 𝙨𝙤𝙣𝙜•••😉")
    try:
        is_downloading = True
        with youtube_dl.YoutubeDL(opts) as ytdl:
            infoo = ytdl.extract_info(url, False)
            duration = round(infoo["duration"] / 60)

            if duration > DURATION_LIMIT:
                m.edit(
                    f"❌ Videos longer than {DURATION_LIMIT} minute(s) aren't allowed, the provided video is {duration} minute(s)"
                )
                is_downloading = False
                return
            ytdl_data = ytdl.extract_info(url, download=True)

    except Exception:
        # await pablo.edit(event, f"**Failed To Download** \n**Error :** `{str(e)}`")
        is_downloading = False
        return

    c_time = time.time()
    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"**Video Name ➠** `{thum}` \n**Requested For :** `{urlissed}` \n**Channel :** `{thums}` \n**Link :** `{mo}`"
    m.client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        supports_streaming=True,
        progress=progress,
        progress_args=(
            pablo,
            c_time,
            f"`Uploading {urlissed} Song From YouTube Music!`",
            file_stark,
        ),
    )
    m.delete()
    is_downloading = False
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)
