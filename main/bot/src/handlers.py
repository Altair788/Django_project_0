import telebot
from telebot import types
from keyboa import Keyboa

from src.buttons import button_author_inline, button_reader_inline, button_edit_work_inline, \
    button_change_personal_data_inline, button_send_feedback_inline, button_other_inline, \
    button_get_back_to_support_inline, button_support_1_inline, button_support_2_inline, button_support_3_inline, \
    button_get_back_to_send_support_inline, button_send_support_inline
from src.settings import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    print("start")
    # bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    # if is_user_authorized(PERSONAL_GROUP_ID, call.message.from_user.id):
    markup = types.InlineKeyboardMarkup()
    # markup.add(types.InlineKeyboardButton("Разовый    🪪‍", callback_data="one_time_pass"))
    markup.add(button_author_inline, button_reader_inline)

    bot.send_message(chat_id=message.chat.id, text="Кто вы?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "author")
def author(call: types.CallbackQuery) -> None:
    bot.clear_step_handler_by_chat_id(call.message.chat.id)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    bot.send_message(chat_id=call.message.chat.id, text='Ваш ник на ***')
    bot.register_next_step_handler(call.message, get_user_status)


@bot.callback_query_handler(func=lambda call: call.data == "reader")
def author(call: types.CallbackQuery) -> None:
    bot.clear_step_handler_by_chat_id(call.message.chat.id)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    bot.send_message(chat_id=call.message.chat.id, text='Ваш ник на ***')
    bot.register_next_step_handler(call.message, get_user_status)


def get_user_status(message: types.Message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    # bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    bot.send_message(chat_id=message.chat.id, text='Как к вам обращаться?')
    bot.register_next_step_handler(message, support)


def support(message: types.Message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    # bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    markup = types.InlineKeyboardMarkup()
    markup.add(button_edit_work_inline)
    markup.add(button_change_personal_data_inline)
    markup.add(button_send_feedback_inline)
    markup.add(button_send_support_inline)
    markup.add(button_other_inline)
    bot.send_message(chat_id=message.chat.id, text='Чем вам помочь?', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "edit_work")
def edit_work(call: types.CallbackQuery) -> None:
    bot.clear_step_handler_by_chat_id(call.message.chat.id)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    markup = types.InlineKeyboardMarkup()
    markup.add(button_get_back_to_support_inline)
    bot.send_message(chat_id=call.message.chat.id, text='Тут будет функционал "Редактирование работы"',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "change_personal_data")
def change_personal_data(call: types.CallbackQuery) -> None:
    bot.clear_step_handler_by_chat_id(call.message.chat.id)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    markup = types.InlineKeyboardMarkup()
    markup.add(button_get_back_to_support_inline)
    bot.send_message(chat_id=call.message.chat.id, text='Тут будет функционал "Изменение персональных данных"',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "send_feedback")
def send_feedback(call: types.CallbackQuery) -> None:
    bot.clear_step_handler_by_chat_id(call.message.chat.id)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    markup = types.InlineKeyboardMarkup()
    markup.add(button_get_back_to_support_inline)
    bot.send_message(chat_id=call.message.chat.id, text='Тут будет функционал "Предложение/обратная связь"',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "send_support")
def send_support(call: types.CallbackQuery) -> None:
    bot.clear_step_handler_by_chat_id(call.message.chat.id)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    markup = types.InlineKeyboardMarkup()
    markup.add(button_support_1_inline)
    markup.add(button_support_2_inline)
    markup.add(button_support_3_inline)
    markup.add(button_get_back_to_support_inline)

    bot.send_message(chat_id=call.message.chat.id, text='На что хотели бы пожаловаться?', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "support_1")
def support_1(call: types.CallbackQuery) -> None:
    bot.clear_step_handler_by_chat_id(call.message.chat.id)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    markup = types.InlineKeyboardMarkup()
    # markup.add(button_get_back_to_send_support_inline)
    markup.add(button_get_back_to_support_inline)
    bot.send_message(chat_id=call.message.chat.id, text='Тут будет функционал "Жалоба1"', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "support_2")
def support_2(call: types.CallbackQuery) -> None:
    bot.clear_step_handler_by_chat_id(call.message.chat.id)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    markup = types.InlineKeyboardMarkup()
    # markup.add(button_get_back_to_send_support_inline)
    markup.add(button_get_back_to_support_inline)
    bot.send_message(chat_id=call.message.chat.id, text='Тут будет функционал "Жалоба2"', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "support_3")
def support_3(call: types.CallbackQuery) -> None:
    bot.clear_step_handler_by_chat_id(call.message.chat.id)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    markup = types.InlineKeyboardMarkup()
    # markup.add(button_get_back_to_send_support_inline)
    markup.add(button_get_back_to_support_inline)
    bot.send_message(chat_id=call.message.chat.id, text='Тут будет функционал "Жалоба3"', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "get_back_to_support")
def get_back_to_support(call: types.CallbackQuery) -> None:
    bot.clear_step_handler_by_chat_id(call.message.chat.id)
    support(call.message)

#
# @bot.callback_query_handler(func=lambda call: call.data == "get_back_to_send_support")
# def get_back_to_send_support(call: types.CallbackQuery) -> None:
#     bot.clear_step_handler_by_chat_id(call.message.chat.id)
#     send_support(call.message)


@bot.message_handler()
def delete_input(message) -> None:
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
