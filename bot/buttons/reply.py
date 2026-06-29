from aiogram.types import KeyboardButton, KeyboardButtonPollType, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.i18n import gettext as _

# def menu_btn():
#     rkb = ReplyKeyboardBuilder()
#     rkb.add(*[
#         KeyboardButton(text=_("Change language"))
#     ])
#     rkb.adjust(1)
#     return rkb.as_markup(resize_keyboard=True)
#
# def lang_btn():
#     rkb = ReplyKeyboardBuilder()
#     rkb.add(*[
#         KeyboardButton(text="Uzbek"),
#         KeyboardButton(text="English"),
#         KeyboardButton(text="Russian")
#     ])
#     rkb.adjust(3)
#     return rkb.as_markup(resize_keyboard=True)
#
# def auth_buttons():
#     rkb = ReplyKeyboardBuilder()
#     rkb.add(
#         KeyboardButton(text=_("Change language"))
#     )
#     rkb.adjust(2)
#     return rkb.as_markup(resize_keyboard=True)

def clothes_buttons():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text=_("Kiyimlar"))
    ])
    rkb.adjust(1)
    return rkb.as_markup(resize_keyboard=True)

def type_buttons():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text="Shim"),
        KeyboardButton(text="Futbolka"),
    ])
    rkb.adjust(3)
    return rkb.as_markup(resize_keyboard=True)

def technology_buttons():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text=_("Elektronika tanlang"))
    ])
    rkb.adjust(1)
    return rkb.as_markup(resize_keyboard=True)

def gadget_buttons():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text="Smatfonlar"),
        KeyboardButton(text="Noutbuklar"),
    ])
    rkb.adjust(3)
    return rkb.as_markup(resize_keyboard=True)

def food_buttons():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text=_("Oziq-ovqat tanlang"))
    ])
    rkb.adjust(1)
    return rkb.as_markup(resize_keyboard=True)

def healthy_food_buttons():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text="Non mahsulotlari"),
        KeyboardButton(text="Shirinliklar"),
    ])
    rkb.adjust(3)
    return rkb.as_markup(resize_keyboard=True)
