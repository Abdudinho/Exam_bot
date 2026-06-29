from aiogram.types import KeyboardButton, KeyboardButtonPollType, ReplyKeyboardMarkup, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.i18n import gettext as _

def menu_btn():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text=_("Change language"))
    ])
    rkb.adjust(1)
    return rkb.as_markup(resize_keyboard=True)

def lang_btn():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text="Uzbek"),
        KeyboardButton(text="English"),
        KeyboardButton(text="Russian")
    ])
    rkb.adjust(3)
    return rkb.as_markup(resize_keyboard=True)

def auth_buttons():
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text=_("Change language"))
    )
    rkb.adjust(2)
    return rkb.as_markup(resize_keyboard=True)
def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛍 Mahsulotlar bo'limi", callback_data="products")],
        [InlineKeyboardButton(text="📞 Biz bilan bog'lanish", callback_data="contact")],
    ])

def products_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👕 Kiyimlar", callback_data="cat_kiyim")],
        [InlineKeyboardButton(text="📱 Elektronika", callback_data="cat_elektro")],
        [InlineKeyboardButton(text="🥦 Oziq-ovqat", callback_data="cat_oziq")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_main")],
    ])

def kiyim_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👕 Futbolkalar", callback_data="sub_futbolka")],
        [InlineKeyboardButton(text="👖 Shimlar", callback_data="sub_shim")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_products")],
    ])

def elektro_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📱 Smartfonlar", callback_data="sub_smartfon")],
        [InlineKeyboardButton(text="💻 Noutbuklar", callback_data="sub_noutbuk")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_products")],
    ])

def oziq_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🍞 Non mahsulotlari", callback_data="sub_non")],
        [InlineKeyboardButton(text="🍬 Shirinliklar", callback_data="sub_shirin")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_products")],
    ])
