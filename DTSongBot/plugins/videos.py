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

@app.on_message(filters.command("video") & ~filters.edited & filters.group)
async def song(client, message):
    cap = "@JEBotZ"
    url = message.text.split(None, 1)[1]
    rkp = await message.reply("Processing...")
    if not url:
        await rkp.edit("**What's the song you want?**\nUsage`/song <song name>`")
    search = Searchvideos(url, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except BaseException:
        return await rkp.edit("Failed to find that song.")
    type = "video"
    if type == "video":
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp4",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": "%(id)s.mp4",
            "quiet": True,
            "logtostderr": False,
        }
        song = True
    try:
        await rkp.edit("Downloading...")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await rkp.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await rkp.edit("`The download content was too short.`")
        return
    except GeoRestrictedError:
        await rkp.edit(
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`"
        )
        return
    except MaxDownloadsReached:
        await rkp.edit("`Max-downloads limit has been reached.`")
        return
    except PostProcessingError:
        await rkp.edit("`There was an error during post processing.`")
        return
    except UnavailableVideoError:
        await rkp.edit("`Media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        await rkp.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await rkp.edit("`There was an error during info extraction.`")
        return
    except Exception as e:
        await rkp.edit(f"{str(type(e)): {str(e)}}")
        return
    time.time()
    if song:
        await rkp.edit("Uploading...") #ImJanindu
        lol = "./thumb.jpg"
        lel = await message.reply_audio(
                 f"{rip_data['id']}.mp4",
                 duration=int(rip_data["duration"]),
                 title=str(rip_data["title"]),
                 performer=str(rip_data["uploader"]),
                 thumb=lol,
                 caption=cap)  #JEBotZ
        await rkp.delete()
