from main import bot, dp
from keyboards import keyboard
from aiogram import types
from aiogram.dispatcher.filters import Command

@dp.message_handler(Command('start'))
async def start(message: types.Message):
    await bot.send_message(message.chat.id, 'Test Capsulle.md!',
                           reply_markup=keyboard)

PRICE = {
    '1': [types.LabeledPrice(label='Item1', amount=160)],
    '2': [types.LabeledPrice(label='Item2', amount=160)],
    '3': [types.LabeledPrice(label='Item3', amount=160)],
    '4': [types.LabeledPrice(label='Item4', amount=160)],
    '5': [types.LabeledPrice(label='Item5', amount=160)],
    '6': [types.LabeledPrice(label='Item6', amount=160)],
    '7': [types.LabeledPrice(label='Item7', amount=160)],
    '8': [types.LabeledPrice(label='Item8', amount=160)],
    '9': [types.LabeledPrice(label='Item9', amount=160)],
    '10': [types.LabeledPrice(label='Item10', amount=160)],
    '11': [types.LabeledPrice(label='Item11', amount=160)],
    '12': [types.LabeledPrice(label='Item12', amount=160)],
}

@dp.message_handler(content_types='web_app_data')
async def buy_process(web_app_message):
    await bot.send_invoice(web_app_message.chat.id,
                           title='Laptop',
                           description='Description',
                           provider_token='pay_token',
                           currency='mdl',
                           need_email=True,
                           prices=PRICE[f'{web_app_message.web_app_data.data}'],
                           start_parameter='example',
                           payload='some_invoice')

@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_process(pre_checkout: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    await bot.send_message(message.chat.id, 'Plata executata cu succes')
