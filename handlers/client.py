from aiogram import types, Dispatcher
from create_bot import bot
from Keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(chat_id=message.from_user.id,
                               text='Welcome to my bot!',
                               reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply(text='Для общение с ботом, нужно написать ему в ЛС по ссылке:\nhttps://t.me/SiteonPython_bot')


# @dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""<em>Список команд</em>""",
                           parse_mode='html')

async def command_delete_keyboard(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='The keyboard was successfully removed',
                           reply_markup=ReplyKeyboardRemove())

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(command_delete_keyboard, commands=['close'])

