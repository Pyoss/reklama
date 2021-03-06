import telebot
import config

types = telebot.types
bot = telebot.TeleBot(config.token)


def send_message(chat_id, text, reply_markup=None):
    return bot.send_message(chat_id, text, reply_markup=reply_markup)


def send_photo(chat_id, photo, caption=None, reply_markup=None):
    return bot.send_photo(chat_id=chat_id, photo=photo, caption=caption, reply_markup=reply_markup)


def edit_message(chat_id, message_id, text, reply_markup=None):
    bot.edit_message_text(message_id=message_id, chat_id=chat_id, text=text, reply_markup=reply_markup)


def send_media_group(chat_id, media_group):
    bot.send_media_group(chat_id, media=media_group)