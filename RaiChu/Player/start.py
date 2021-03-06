
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from RaiChu.config import BOT_NAME as bn
from Process.filters import other_filters2
from time import time
from datetime import datetime
from Process.decorators import authorized_users_only
from RaiChu.config import BOT_USERNAME, ASSISTANT_USERNAME

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""**I á´á´ ðððð ð ððð¶ð° ð  
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
