from telebot import types

button_author_inline = types.InlineKeyboardButton("Автор", callback_data="author")
button_reader_inline = types.InlineKeyboardButton("Читатель", callback_data="reader")
button_edit_work_inline = types.InlineKeyboardButton("Редактирование работы", callback_data="edit_work")
button_change_personal_data_inline = types.InlineKeyboardButton("Изменение персональных данных",
                                                                callback_data="change_personal_data")
button_send_feedback_inline = types.InlineKeyboardButton("Предложение/обратная связь", callback_data="send_feedback")
button_send_support_inline = types.InlineKeyboardButton("Пожаловаться", callback_data="send_support")
button_support_1_inline = types.InlineKeyboardButton("Жалоба1", callback_data="support_1")
button_support_2_inline = types.InlineKeyboardButton("Жалоба2", callback_data="support_2")
button_support_3_inline = types.InlineKeyboardButton("Жалоба3", callback_data="support_3")
button_other_inline = types.InlineKeyboardButton("Другое", callback_data="other")
button_get_back_to_support_inline = types.InlineKeyboardButton("Вернуться в предыдущее меню",
                                                               callback_data="get_back_to_support")
button_get_back_to_send_support_inline = types.InlineKeyboardButton("Вернуться к списку жалоб",
                                                               callback_data="get_back_to_send_support")



# button_exit_inline = types.InlineKeyboardButton("Exit", callback_data="exit")
