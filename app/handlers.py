from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import app.keyboards as kb
# from config import cnt
from app.keyboards import changer, onlychanger, menue, catalog

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply_video(video="BAACAgIAAxkBAAICpmYEaXhl3qsHcBEppWFMUkO0V4qTAAJKSwACc9wpSGcoGxIEiJWHNAQ",
                              caption=f'Привет!\n\n\n Я Бот ВАЛОДКЛИКЕР.\n\n\n Жми Тап!',
                              reply_markup=kb.tapik)


# получить айди
@router.message(F.video)
async def vid(message: Message):
    await message.answer((f'{message.video.file_id}'))


@router.message(F.photo)
async def ph(message: Message):
    await message.answer((f'{message.photo[-1].file_id}'))


user_taps = {}
user_coins = {}
user_mnoj = {}
price = {}


# tap
@router.message(F.text == 'Тап!')
async def tapok(message: Message):
    user_id = message.from_user.id
    if user_id not in user_taps:
        user_taps[user_id] = 0
    if user_id not in user_mnoj:
        user_mnoj[user_id] = 1
    user_taps[user_id] += user_mnoj[user_id]
    user_taps[user_id] = round(user_taps[user_id], 1)
    await message.reply(str(user_taps[user_id]))
    if user_taps[user_id] == 10:
        await message.reply_video(video="BAACAgIAAxkBAAIIVWYEhQE2kbMeBhoF4K76-Ualb1TgAAIhTAACc9wpSJfpb92A9ZwINAQ",
                                  caption=f'Ты достиг 10! Получай мем\n\nКликай дальше и увидишь больше мемов')
    if user_taps[user_id] == 100:
        await message.reply_video(video="BAACAgIAAxkBAAIIV2YEhQSG8J6xiLwrPtKyDAH1jWl8AAIiTAACc9wpSLoNnmQKYD4yNAQ",
                                  caption=f'Ты достиг 100! Получай мем\n\nКликай дальше и увидишь больше мемов')
    if user_taps[user_id] == 300:
        await message.reply_video(video="BAACAgIAAxkBAAIIW2YEhxAvd2UECC3CO3NVJxDGBM8YAAInTAACc9wpSPhQ3sXjycLrNAQ",
                                  caption=f'Ты достиг 300! Получай мем\n\nКликай дальше и увидишь больше мемов')
    if user_taps[user_id] == 500:
        await message.reply_video(video="BAACAgIAAxkBAAIIXWYEhxMKNVPE1eZ4-OaZh4gQCHegAAIoTAACc9wpSCUlt-4FPT6nNAQ",
                                  caption=f'Ты достиг 500! Получай мем\n\nКликай дальше и увидишь больше мемов')
    if user_taps[user_id] == 800:
        await message.reply_video(video="BAACAgIAAxkBAAIIWWYEhQaDD89De-JK8ZqqoSUzvOEgAAIjTAACc9wpSLpEsMM8BAbSNAQ",
                                  caption=f'Ты достиг 800! Получай мем\n\nКликай дальше и увидишь больше мемов')
    if user_taps[user_id] == 1000:
        await message.reply_video(video="BAACAgIAAxkBAAIIX2YEhxa1gG5yA1585gr9mKqLfvWjAAIpTAACc9wpSMTZrqpHQDnsNAQ",
                                  caption=f'Ты достиг 1000! Получай мем\n\nКликай дальше и увидишь больше мемов')
    if user_taps[user_id] == 1500:
        await message.reply_video(video="BAACAgIAAxkBAAIIYWYEhx3ZtCQfVAEEBurzl-svC8_MAAIqTAACc9wpSMCyAAE55botfzQE",
                                  caption=f'Ты достиг 1500! Получай мем\n\nдальше делать мемы мне было лень пиздец')


@router.message(F.text == 'Меню обменника')
async def nol(message: Message):
    user_id = message.from_user.id
    if user_id not in user_coins:
        user_coins[user_id] = 0
    await message.reply_photo(
        photo="AgACAgIAAxkBAAITSGYFUX1OQfKc4DyiQaL2T14YKPHcAAIx1TEb8N4pSMBwzE7QaqA_AQADAgADeQADNAQ",
        caption=f'Ты попал в *меню обменника* (к Мартину)\n\n\n'
                f'Сейчас ты можешь совершить обмен по курсу:\n\n'
                f'*10 Тапов --> 1 Коин*', reply_markup=changer
        , parse_mode='Markdown')


@router.callback_query(F.data == 'men')
async def mee(callback: CallbackQuery):
    user_id = callback.from_user.id
    if user_id not in user_coins:
        user_coins[user_id] = 0
    await callback.message.answer_photo(
        photo="AgACAgIAAxkBAAITSGYFUX1OQfKc4DyiQaL2T14YKPHcAAIx1TEb8N4pSMBwzE7QaqA_AQADAgADeQADNAQ",
        caption=f'Ты попал в *меню обменника* (к Мартину)\n\n\n'
                f'Сейчас ты можешь совершить обмен по курсу:\n\n'
                f'*10 Тапов --> 1 Коин*', reply_markup=changer
        , parse_mode='Markdown')


@router.callback_query(F.data == 'ch')
async def ch(callback: CallbackQuery):
    user_id = callback.from_user.id
    if user_id not in user_coins:
        user_coins[user_id] = 0
    if user_id not in user_taps:
        user_taps[user_id] = 0
    if user_id not in user_mnoj:
        user_mnoj[user_id] = 1
    user_coins[user_id] = user_coins[user_id] + (user_taps[user_id] / 10)
    user_coins[user_id] = round(user_coins[user_id], 1)
    user_taps[user_id] = 0
    await callback.message.answer(text=f'Твой баланс:\n\n'
                                       f'Количество твоих *Тапов*: {str(user_taps[user_id])}\n'
                                       f'Количество твоих *Коинов*: {str(user_coins[user_id])}\n'
                                       f'Количество твоих *Множителей*: {str(user_mnoj[user_id])}'
                                  , parse_mode='Markdown')


@router.callback_query(F.data == 'bal')
async def ch(callback: CallbackQuery):
    user_id = callback.from_user.id
    if user_id not in user_coins:
        user_coins[user_id] = 0
    if user_id not in user_taps:
        user_taps[user_id] = 0
    await callback.message.answer(text=f'Твой баланс:\n\n'
                                       f'Количество твоих *Тапов*: {str(user_taps[user_id])}\n'
                                       f'Количество твоих *Коинов*: {str(user_coins[user_id])}\n'
                                       f'Количество твоих *Множителей*: {str(user_mnoj[user_id])}',
                                  reply_markup=onlychanger, parse_mode='Markdown')


@router.message(F.text == 'Меню')
async def men(message: Message):
    await message.reply_photo(
        photo='AgACAgIAAxkBAAIWE2YFaFNYsk4LFYRJo3dsSl8BQD4eAALd2TEbztExSGR08wrGZ6jLAQADAgADeAADNAQ',
        caption='Здесь ты можешь обменять *валюту*, пойти в *магазин*, или проверить *баланс*',
        reply_markup=menue, parse_mode='Markdown')


@router.callback_query(F.data == 'mag')
async def ch(callback: CallbackQuery):
    user_id = callback.from_user.id
    if user_id not in user_coins:
        user_coins[user_id] = 0
    if user_id not in user_taps:
        user_taps[user_id] = 0
    await callback.message.answer_photo(
        photo='AgACAgIAAxkBAAIWImYFbC7fko7aXJBkuHv0c7Kc7PyAAALS1TEb8N4pSDffaQk_1Lt_AQADAgADeQADNAQ',
        caption=f'Ты попал в *магазин*. Выбери улучшение\n\n'
                f'Количество твоих Коинов: {str(user_coins[user_id])}',
        reply_markup=catalog, parse_mode='Markdown')


@router.callback_query(F.data == 'tapmn')
async def tapmn(callback: CallbackQuery):
    user_id = callback.from_user.id
    if user_id not in user_coins:
        user_coins[user_id] = 0
    if user_id not in user_taps:
        user_taps[user_id] = 0
    if user_id not in user_mnoj:
        user_mnoj[user_id] = 1
    if user_coins[user_id] >= 10:
        user_mnoj[user_id] += 0.1
        user_coins[user_id] -= 10
        await callback.message.answer(text=f'Покупка удалась! За один клик ты делаешь *{str(user_mnoj[user_id])}* тапа'
                                      , parse_mode='Markdown')
    if user_coins[user_id] < 10:
        await callback.message.answer(text='Недостаточно средств')
    await callback.message.answer(text=f'Твой баланс:\n\n'
                                       f'Количество твоих *Тапов*: *{str(user_taps[user_id])}*\n'
                                       f'Количество твоих *Коинов*: *{str(user_coins[user_id])}*\n'
                                       f'Количество твоих *Множителей*: *{str(user_mnoj[user_id])}*',
                                  reply_markup=onlychanger, parse_mode='Markdown')
