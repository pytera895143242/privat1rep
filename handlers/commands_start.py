from aiogram import types
from misc import dp,bot
from .sqlit import reg_user
import asyncio

content_chat = -1001780671252
ids_user = []
import asyncio

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    if message.text[7:] == 'bonus':
        await message.answer(text="""✅БОНУС АКТИВИРОВАН
🔥ПРИ ПОКУПКЕ ЛЮБОГО ТАРИФА ВСЕ ОСТАЛЬНЫЕ ИДУТ В ПОДАРОК""")

        markup = types.InlineKeyboardMarkup()

        bat_1 = types.InlineKeyboardButton(text='🍼Р0DDOM (D0 4)🍼', callback_data='bat_1')
        bat_2 = types.InlineKeyboardButton(text='👶Л@П0ЧkИ (I0+-)👶', callback_data='bat_2')
        bat_3 = types.InlineKeyboardButton(text='🎒|||k0льNицы🎒(I4+-)', callback_data='bat_3')
        bat_4 = types.InlineKeyboardButton(text='📚STУDENТКИ (I7+-)📚', callback_data='bat_4')
        bat_5 = types.InlineKeyboardButton(text='🏆🤑Всё тарифы вместе🤑🏆', callback_data='bat_5')

        markup.add(bat_1)
        markup.add(bat_2)
        markup.add(bat_3)
        markup.add(bat_4)
        markup.add(bat_5)

        await message.answer(text="""<b>Выберите желаемый товар или категорию:</b>""", reply_markup=markup)


    elif message.text[7:] == 'vip':
        url = 'https://oplata.qiwi.com/create?'
        key = 'publicKey=48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iPvxoW7icTDWfQKTrC1vvyquLX2fDP7tkfR256qgd4oJShTzygh94y9FT8XBJhywjVLh1aFVCRVNe5c21S3T6UUKwpjDMqaFWa4jMxfDQuv'
        price = f'&amount={100}'
        finish_url = url + key + price

        markup = types.InlineKeyboardMarkup()
        bat_pay = types.InlineKeyboardButton(text='🎫ОПЛАТИТЬ', url=finish_url)
        markup.add(bat_pay)

        await bot.copy_message(chat_id=message.chat.id, message_id=17, from_chat_id=content_chat,reply_markup=markup)



    else:

        global ids_user
        reg_user(id = message.chat.id)
        await message.answer(text="""<b>✅ Вы успешно активировали промокод.
Вам доступна скидка в 20% </b>""")

        await bot.copy_message(chat_id=message.chat.id,message_id=5,from_chat_id=content_chat) #Отправка приветсвия

        markup = types.InlineKeyboardMarkup()

        bat_1 = types.InlineKeyboardButton(text='🍼Р0DDOM (D0 4)🍼', callback_data='bat_1')
        bat_2 = types.InlineKeyboardButton(text='👶Л@П0ЧkИ (I0+-)👶', callback_data='bat_2')
        bat_3 = types.InlineKeyboardButton(text='🎒|||k0льNицы🎒(I4+-)', callback_data='bat_3')
        bat_4 = types.InlineKeyboardButton(text='📚STУDENТКИ (I7+-)📚', callback_data='bat_4')
        bat_5 = types.InlineKeyboardButton(text='🏆🤑Всё тарифы вместе🤑🏆', callback_data='bat_5')

        markup.add(bat_1)
        markup.add(bat_2)
        markup.add(bat_3)
        markup.add(bat_4)
        markup.add(bat_5)


        await message.answer(text="""<b>Выберите желаемый товар или категорию:</b>""",reply_markup=markup)

        if message.chat.id not in ids_user:
            try:
                ids_user.append(message.chat.id)
                await asyncio.sleep(1200) #20 минут
                await bot.copy_message(chat_id=message.chat.id,from_chat_id=content_chat,message_id=13) #32 места
                await asyncio.sleep(3600) #Час с предыдущего
                await bot.copy_message(chat_id=message.chat.id,from_chat_id=content_chat,message_id=14) #12 мест
                await asyncio.sleep(21600/2) #3 Часа с предыдущего
                await bot.copy_message(chat_id=message.chat.id,from_chat_id=content_chat,message_id=15) #2 места
                await asyncio.sleep(21600) #6 часов с предыдущего
                try:
                    user_n = message.from_user.first_name
                    await bot.send_message(chat_id=message.chat.id,text=f"""{user_n}, ку 👋🏻 Тебе доступен вип тариф 🔝
            

🔥ВСЕ НАШИ ПАКИ ЗА 100₽🔥

🏆🔹-🍼Р0DDOM (D0 4)🍼
🏆🔹-👶Л@П0ЧkИ (I0+-)👶
🏆🔹-🎒|||k0льNицы🎒(I4+-)
🏆🔹-📚STУDENТКИ (I7+-)📚
🎁🔑 - 😋Лесбухи💦
🎁🔑- ✨ТРАНСИКИ✨
🎁🔑 - 👩‍🦳Милфы👩‍🦳
🎁🔑 - 🤰👩‍🍼Беременные👩‍🍼🤰

ВИП ТАРИФ ПО ЭТОЙ ССЫЛКЕ:
https://t.me/lehdjdksobot?start=vip""") #ВИП ТАРИФ
                except:
                    await bot.send_message(chat_id=message.chat.id, text=f"""КУ 👋🏻 Тебе доступен вип тариф 🔝


🔥ВСЕ НАШИ ПАКИ ЗА 100₽🔥

🏆🔹-🍼Р0DDOM (D0 4)🍼
🏆🔹-👶Л@П0ЧkИ (I0+-)👶
🏆🔹-🎒|||k0льNицы🎒(I4+-)
🏆🔹-📚STУDENТКИ (I7+-)📚
🎁🔑 - 😋Лесбухи💦
🎁🔑- ✨ТРАНСИКИ✨
🎁🔑 - 👩‍🦳Милфы👩‍🦳
🎁🔑 - 🤰👩‍🍼Беременные👩‍🍼🤰

ВИП ТАРИФ ПО ЭТОЙ ССЫЛКЕ:
https://t.me/lehdjdksobot?start=vip""")  # ВИП ТАРИФ
                await asyncio.sleep(21600)  # 6 часов с предыдущего
                await message.answer(text = 'ТЫ ГДЕ ???')


            except:
                pass
