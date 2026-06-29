from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

week_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Kiyimlar", callback_data="clothes")],
        [InlineKeyboardButton(text="Elektronika", callback_data="Gadgets")],
        [InlineKeyboardButton(text="Oziq-ovqat", callback_data="Food")],
    ]
)

def pagination(page, max_page):
    ikb = InlineKeyboardBuilder()
    buttons = []
    if page > 0:
        buttons.append(InlineKeyboardButton(text='Prev', callback_data=f"page_{page-1}"))
    if page < max_page - 1:
        buttons.append(InlineKeyboardButton(text='Next', callback_data=f"page_{page+1}"))
    ikb.add(*buttons)
    ikb.adjust(2)
    return ikb.as_markup()