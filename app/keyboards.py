from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardButton, InlineKeyboardMarkup)


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="English 🇬🇧", callback_data="english"),
     InlineKeyboardButton(text="Deutsch 🇩🇪", callback_data="german"),
     ],
    [
    InlineKeyboardButton(text="Čeština 🇨🇿", callback_data="czech"),
    InlineKeyboardButton(text="Українська 🇺🇦", callback_data="ukrainian"),
    ],
    [
    InlineKeyboardButton(text="Français 🇲🇫", callback_data="french"),
    InlineKeyboardButton(text="Español 🇪🇦", callback_data="spanish"),
    ],
    [
    InlineKeyboardButton(text="Русский 🇷🇺", callback_data="russian"),
    InlineKeyboardButton(text="Nederlands 🇳🇱", callback_data="dutch"),
    ]
])

second = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="English 🇬🇧", callback_data="english_1"),
     InlineKeyboardButton(text="Deutsch 🇩🇪", callback_data="german_1"),
     ],
    [
    InlineKeyboardButton(text="Čeština 🇨🇿", callback_data="czech_1"),
    InlineKeyboardButton(text="Українська 🇺🇦", callback_data="ukrainian_1"),
    ],
    [
    InlineKeyboardButton(text="Français 🇲🇫", callback_data="french_1"),
    InlineKeyboardButton(text="Español 🇪🇦", callback_data="spanish_1"),
    ],
    [
    InlineKeyboardButton(text="Русский 🇷🇺", callback_data="russian_1"),
    InlineKeyboardButton(text="Nederlands 🇳🇱", callback_data="dutch_1"),
    ]
])

controls = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔄 Switch languages")],
        [KeyboardButton(text="🔁 Start over")],
    ],
    resize_keyboard=True,
)