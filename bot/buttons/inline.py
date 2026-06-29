from aiogram import F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.buttons.reply import products_menu, main_menu
from bot.dispetcher import dp

@dp.callback_query(F.data == "back_main")
async def back_main(call: CallbackQuery):
    await call.message.edit_text("Kerakli bo'limni tanlang:", reply_markup=main_menu())

@dp.callback_query(F.data == "back_products")
async def back_products(call: CallbackQuery):
    await call.message.edit_text("Mahsulotlar bo'limini tanlang:", reply_markup=products_menu())

