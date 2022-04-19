from aiogram import types
from misc import dp, bot
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import random

Price1 = 420
Price2 = 360
Price3 = 310
Price4 = 285
Price5 = 745

content_chat = -1001780671252

url = 'https://oplata.qiwi.com/create?'
key = 'publicKey=48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iPsZPmVFjj6M3Tgts8VLcUi2mAp14a2BbyqbQAsx5oYX7KmzANtyXsc853KAFhgtGmMcvGJkGaEA5YFtDMfKm1fnvE7jDavw7FYw93xXJhM'


@dp.callback_query_handler(lambda call: True, state = '*')
async def answer_push_inline_button(call, state: FSMContext):
    markup = types.InlineKeyboardMarkup()
    bat_exit = types.InlineKeyboardButton(text='👈 НАЗАД', callback_data='bat_exit')




    if call.data == 'bat_1': #🍼Р0DDOM (D0 4)🍼
        price = f'&amount={Price1}'
        finish_url = url+key+price
        bat_pay = types.InlineKeyboardButton(text='🎫ОПЛАТИТЬ', url = finish_url)
        markup.add(bat_pay)
        markup.add(bat_exit)
        await bot.copy_message(chat_id=call.message.chat.id,message_id=11,from_chat_id=content_chat,reply_markup=markup)


    if call.data == 'bat_2': #👶Л@П0ЧkИ (I0+-)👶
        price = f'&amount={Price2}'
        finish_url = url + key + price

        bat_pay = types.InlineKeyboardButton(text='🎫ОПЛАТИТЬ', url=finish_url)
        markup.add(bat_pay)
        markup.add(bat_exit)
        await bot.copy_message(chat_id=call.message.chat.id,message_id=8,from_chat_id=content_chat,reply_markup=markup)


    if call.data == 'bat_3':#🎒|||k0льNицы🎒(I4+-)
        price = f'&amount={Price3}'
        finish_url = url + key + price

        bat_pay = types.InlineKeyboardButton(text='🎫ОПЛАТИТЬ', url=finish_url)
        markup.add(bat_pay)
        markup.add(bat_exit)
        await bot.copy_message(chat_id=call.message.chat.id,message_id=7,from_chat_id=content_chat,reply_markup=markup)


    if call.data == 'bat_4':#📚STУDENТКИ (I7+-)📚
        price = f'&amount={Price4}'
        finish_url = url + key + price

        bat_pay = types.InlineKeyboardButton(text='🎫ОПЛАТИТЬ', url=finish_url)
        markup.add(bat_pay)
        markup.add(bat_exit)
        await bot.copy_message(chat_id=call.message.chat.id,message_id=12,from_chat_id=content_chat,reply_markup=markup)


    if call.data == 'bat_5':#🏆🤑Всё тарифы вместе🤑🏆
        price = f'&amount={Price5}'
        finish_url = url + key + price

        bat_pay = types.InlineKeyboardButton(text='🎫ОПЛАТИТЬ', url=finish_url)
        markup.add(bat_pay)
        markup.add(bat_exit)
        await bot.copy_message(chat_id=call.message.chat.id,message_id=6,from_chat_id=content_chat,reply_markup=markup)

    if call.data == 'bat_exit':  # 🏆🤑Всё тарифы вместе🤑🏆
        await bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)


    await bot.answer_callback_query(callback_query_id=call.id)