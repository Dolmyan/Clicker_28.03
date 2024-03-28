from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


tapik = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Тап!')], [KeyboardButton(text='Меню')]
],
    input_field_placeholder='PLAY!',
    resize_keyboard=True)

changer = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Обменять', callback_data='ch')],
    [InlineKeyboardButton(text='Мой баланс', callback_data='bal')]])

onlychanger = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Обменять', callback_data='ch')]])

menue = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='В обменник', callback_data='men'),
     InlineKeyboardButton(text='В магазин', callback_data='mag')],
    [InlineKeyboardButton(text='Посмотреть баланс', callback_data='bal')]])

catalog=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f'МНОЖИТЕЛЬ ТАПОВ',
                          callback_data='tapmn')]
])
