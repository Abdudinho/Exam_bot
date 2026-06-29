from aiogram import F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand, ReplyKeyboardMarkup, KeyboardButton, CallbackQuery, InlineKeyboardButton, \
    InlineKeyboardMarkup
from aiogram.utils.i18n import I18n
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __
from bot.buttons.reply import menu_btn, auth_buttons, products_menu, main_menu, kiyim_menu, elektro_menu, oziq_menu
from bot.dispetcher import dp


@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.bot.set_my_commands([
        BotCommand(command="/start", description="Qayta boshlash"),
        BotCommand(command="/help", description="yordam olish uchun")
    ])
    await message.answer(
        "Assalomu alaykum! Kerakli bo'limni tanlang:",
        reply_markup=main_menu()
    )


@dp.message(F.text == __("Change language"))
async def lang_btn_handler(message: Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Uzbek")],
            [KeyboardButton(text="English")],
            [KeyboardButton(text="Russian")],
        ],
        resize_keyboard=True
    )
    await message.answer("Tilni tanlang / Choose language:", reply_markup=keyboard)


@dp.message(F.text.in_({"Uzbek", "English", "Russian"}))
async def choose_lang_handler(message: Message, state: FSMContext, i18n: I18n):
    map_ = {
        "Uzbek": "uz",
        "English": "en",
        "Russian": "ru",
    }
    code = map_.get(message.text)
    await state.update_data({"locale": code})
    i18n.current_locale = code
    await message.answer(_("Success lang changed!"), reply_markup=menu_btn())


@dp.callback_query(F.data == "products")
async def show_products(call: CallbackQuery):
    await call.message.edit_text("Mahsulotlar bo'limini tanlang:", reply_markup=products_menu())


@dp.callback_query(F.data == "contact")
async def show_contact(call: CallbackQuery):
    await call.message.edit_text(
        "📞 Biz bilan bog'lanish:\n@admin_username",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_main")]
        ])
    )


@dp.callback_query(F.data == "back_main")
async def back_to_main(call: CallbackQuery):
    await call.message.edit_text("Assalomu alaykum! Kerakli bo'limni tanlang:", reply_markup=main_menu())


@dp.callback_query(F.data == "cat_kiyim")
async def show_kiyim(call: CallbackQuery):
    await call.message.edit_text("👕 Kiyimlar — subkategoriya tanlang:", reply_markup=kiyim_menu())


@dp.callback_query(F.data == "cat_elektro")
async def show_elektro(call: CallbackQuery):
    await call.message.edit_text("📱 Elektronika — subkategoriya tanlang:", reply_markup=elektro_menu())


@dp.callback_query(F.data == "cat_oziq")
async def show_oziq(call: CallbackQuery):
    await call.message.edit_text("🥦 Oziq-ovqat — subkategoriya tanlang:", reply_markup=oziq_menu())


@dp.callback_query(F.data == "back_products")
async def back_to_products(call: CallbackQuery):
    await call.message.edit_text("Mahsulotlar bo'limini tanlang:", reply_markup=products_menu())


SUBCATS = {
    "sub_futbolka": "👕 Futbolkalar bo'limi tanlandi!",
    "sub_shim": "👖 Shimlar bo'limi tanlandi!",
    "sub_smartfon": "📱 Smartfonlar bo'limi tanlandi!",
    "sub_noutbuk": "💻 Noutbuklar bo'limi tanlandi!",
    "sub_non": "🍞 Non mahsulotlari bo'limi tanlandi!",
    "sub_shirin": "🍬 Shirinliklar bo'limi tanlandi!",
}


@dp.callback_query(F.data.startswith("sub_"))
async def show_subcat(call: CallbackQuery):
    text = SUBCATS.get(call.data, "Noma'lum bo'lim")
    await call.message.edit_text(
        text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_products")]
        ])
    )
