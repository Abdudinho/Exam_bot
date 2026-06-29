# from aiogram import F
# from aiogram.filters import CommandStart
# from aiogram.fsm.context import FSMContext
# from aiogram.types import Message, BotCommand, ReplyKeyboardMarkup, KeyboardButton
# from aiogram.utils.i18n import I18n
# from aiogram.utils.i18n import gettext as _
# from aiogram.utils.i18n import lazy_gettext as __
# from bot.buttons.reply import menu_btn, auth_buttons
# from bot.dispetcher import dp
#
#
#
#
#
# @dp.message(CommandStart())
# async def start_handler(message: Message) -> None:
#     await message.bot.set_my_commands([
#         BotCommand(command="/start", description="Qayta boshlash"),
#         BotCommand(command="/help", description="yordam olish uchun")
#     ])
#     await message.answer(
#         _("Hello, {}!").format(message.from_user.full_name),
#         reply_markup=auth_buttons()
#     )
#
#
# @dp.message(F.text == __("Change language"))
# async def lang_btn_handler(message: Message, state: FSMContext):
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text="Uzbek")],
#             [KeyboardButton(text="English")],
#             [KeyboardButton(text="Russian")],
#         ],
#         resize_keyboard=True
#     )
#     await message.answer("Tilni tanlang / Choose language:", reply_markup=keyboard)
#
#
# @dp.message(F.text.in_({"Uzbek", "English", "Russian"}))
# async def choose_lang_handler(message: Message, state: FSMContext, i18n: I18n):
#     map_ = {
#         "Uzbek": "uz",
#         "English": "en",
#         "Russian": "ru",
#     }
#     code = map_.get(message.text)
#     await state.update_data({"locale": code})
#     i18n.current_locale = code
#     await message.answer(_("Success lang changed!"), reply_markup=menu_btn())
#
