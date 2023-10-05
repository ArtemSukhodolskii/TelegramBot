from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


k_help_button = KeyboardButton('/help')
k_close_button = KeyboardButton('/close')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(k_help_button).add(k_close_button)





