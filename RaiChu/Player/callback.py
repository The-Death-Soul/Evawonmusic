# Umm Null Coder

from Process.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from RaiChu.config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**I á´á´ ð­ðð¥ð ð ððð¶ð°   
Êá´á´ ðð²ðð²ð¹ð¼ð½ð²ð± ÊÊ [â¢â¢â¥â§âð¿âðð®Í¦Ì¥ââð¥ ÍÍâ¤âº](https://t.me/zara_THE_addiction)
Thanks to add me ð**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ðï¸ðªð¡ðð¥", url="https://t.me/zara_THE_addiction"
                    ),
                    InlineKeyboardButton(
                        "ðð¨ð¦ð¦ðð§ð ðð¢ð¬ð­", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "How to add með¤·", callback_data="cbhowtouse"
                    ),
                  ],[
                    InlineKeyboardButton(
                       " ðð®ð©ð©ð¨ð«ð­", url="https://t.me/+R7D0nHLk8s9jODA1"
                    ),
                    InlineKeyboardButton(
                        "ðð©ððð­ðð¬", url="https://t.me/ZaraSupport"
                    )
                ],[
                    InlineKeyboardButton(
                        "â ððð ðð ðð¨ ðð¨ð®ð« ðð«ð¨ð®ð©â",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""â **Basic Guide for using this bot:**
        
â https://te.legra.ph/file/d3185c725b9ba69b3f339.jpg

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

ð **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

ð¡ **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

**â¨ á´á´á´ á´Êá´á´á´á´ ÊÊ á´¢á´ÉªÉ´ Êá´ssá´ÉªÉ´** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Ê á´ á´ á´", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""â¨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

Â» **press the button below to read the explanation and see the list of available commands !**

**â á´á´á´ á´Êá´á´á´á´ BÊ: á´¢á´ÉªÉ´ Êá´ssá´ÉªÉ´!** """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ð·ð» á´á´á´ÉªÉ´ á´á´á´", callback_data="cbadmin"),
                    InlineKeyboardButton("ð§ð» ê±á´á´á´ á´á´á´", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("ð Êá´ê±Éªá´ á´á´á´", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("Ê á´ á´ á´", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""â¹ï¸ ðð¨ð¦ð¦ðð§ð ðð¢ð¬ð­ !

ð©ð»âð¼ Â» /play - Type this with give the song title or youtube link or audio file to play Music. (Remember to don't play YouTube live stream by using this command!, because it will cause unforeseen problems.)

ð©ð»âð¼ Â» /vplay - Type this with give the song title or youtube link or video file to play Video. (Remember to don't play YouTube live video by using this command!, because it will cause unforeseen problems.)

ð©ð»âð¼ Â» /vstream - Type this with give the YouTube live stream video link or m3u8 link to play live Video. (Remember to don't play local audio/video files or non-live YouTube video by using this command!, because it will cause unforeseen problems.)

ð¤· Â» /skip - to Skip current song

ð Â» /end - to end play song in vc

 **â á´á´á´ á´Êá´á´á´á´ BÊ:á´¢á´ÉªÉ´ Êá´ssá´ÉªÉ´!** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ð Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ð® here is the admin commands:

â¯ /pause - pause the stream
â¯ /resume - resume the stream
â¯ /skip - switch to next stream
â¯ /stop - stop the streaming
â¯ /vmute - mute the userbot on voice chat
â¯ /vunmute - unmute the userbot on voice chat
â¯ /volume `1-200` - adjust the volume of music (userbot must be admin)
â¯ /reload - reload bot and refresh the admin data
â¯ /userbotjoin - invite the userbot to join group
â¯ /userbotleave - order userbot to leave from group

**â á´á´á´ á´Êá´á´á´á´ BÊ: á´¢á´ÉªÉ´ Êá´ssá´ÉªÉ´!** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ð Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ð® here is the sudo commands:

â¯ /rmw - clean all raw files
â¯ /rmd - clean all downloaded files
â¯ /sysinfo - show the system information
â¯ /update - update your bot to latest version
â¯ /restart - restart your bot
â¯ /leaveall - order userbot to leave from all group

**â á´á´á´ á´Êá´á´á´á´ BÊ: á´¢á´ÉªÉ´ Êá´ssá´ÉªÉ´!** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ð Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\nÂ» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð¡ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"âï¸ **settings of** {query.message.chat.title}\n\nâ¸ : pause stream\nâ¶ï¸ : resume stream\nð : mute userbot\nð : unmute userbot\nâ¹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("â¹", callback_data="cbstop"),
                      InlineKeyboardButton("â¸", callback_data="cbpause"),
                      InlineKeyboardButton("â¶ï¸", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("ð", callback_data="cbmute"),
                      InlineKeyboardButton("ð", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("ð Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("â nothing is currently streaming", show_alert=True)

# SETUP BUTTON OPEN......................................................................................................................................................................................

@Client.on_callback_query(filters.regex("cbsetup"))
async def cbsetup(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Hello !**
Â» **press the button below to read the explanation and see the help commands !**
**â á´á´á´ á´Êá´á´á´á´ BÊ: á´¢á´ÉªÉ´ Êá´ssá´ÉªÉ´!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("welcome", callback_data="noiwel"),
                    InlineKeyboardButton("Lyric", callback_data="noilyric"),
                    InlineKeyboardButton("voice", callback_data="noivoice"),
                ],
                [
                    InlineKeyboardButton("How To Add Me â", callback_data="cbhowtouse"),
                ],
                [InlineKeyboardButton("ð Go Back", callback_data="cbstart")],
            ]
        ),
    )
@Client.on_callback_query(filters.regex("noiwel"))
async def noiwel(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ð® **HEAR THE WELCOME PLUGIN ( soon )**

â¯ /setwelcome for set welcome message.

â¯ /resetwelcome for reset welcome message.

**â á´á´á´ á´Êá´á´á´á´ BÊ: á´¢á´ÉªÉ´ Êá´ssá´ÉªÉ´!** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ð Go Back", callback_data="cbsetup")]]
        ),
    )
@Client.on_callback_query(filters.regex("noilyric"))
async def noilyric(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ð® **HEAR THE LYRIC PLUGIN**

â¯ /lyric ( song name ) for the get lyric of song

**â á´á´á´ á´Êá´á´á´á´ BÊ: á´¢á´ÉªÉ´ Êá´ssá´ÉªÉ´!** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ð Go Back", callback_data="cbsetup")]]
        ),
    )
    
@Client.on_callback_query(filters.regex("noivoice"))
async def noivoice(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ð® **HEAR THE VOICE PLUGIN**

â¯ /tts fot get voice from text message

**â á´á´á´ á´Êá´á´á´á´ BÊ: á´¢á´ÉªÉ´ Êá´ssá´ÉªÉ´!** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ð Go Back", callback_data="cbsetup")]]
        ),
    )    

    
@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð¡ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
