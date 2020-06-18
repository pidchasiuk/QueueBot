import telebot
import dbqueue as dbq

bot = telebot.TeleBot('1058265955:AAEhi2xia18dZCRuDPnZYB7NE5ZzAFxehtQ')


def send_queue():
    res = dbq.get_id_name()
    res_message = ''
    for i in res:
            temp = '{0} - {1}'.format(i[0], i[1])
            res_message += temp + '\n'
    return res_message


@bot.message_handler(commands=['start'])
def start_message(message):
    dbq.del_table_queue()
    dbq.create_table_queue()
    bot.send_message(message.chat.id, 'Давай створимо чергу. \n'
                                      'Щоб зайняти місце натисни /reg \n'
                                      'Коли чергу буде сформовано натисни /end')


@bot.message_handler(commands=['reg'])
def reg_message(message):
    """Додавання користувача в базу даних і в чергу"""
    dbq.add_user(message.from_user.username)
    bot.send_message(message.chat.id, 'Ти в черзі')


@bot.message_handler(commands=['end'])
def end_message(message):
    """Завершення створення черги, без можливості внести зміни."""
    bot.send_message(message.chat.id, 'Чергу створено.\n'
                                      'Щоб переглянути чергу натисни /check\n')


@bot.message_handler(commands=['check'])
def check_message(message):
    """Перевірка черги. Вивід списку учасників"""
    bot.send_message(message.chat.id, send_queue())


@bot.message_handler(commands=['del'])
def del_message(message):
    """Видалення користувача з черги і бази даних"""
    dbq.del_user(message.from_user.username)
    bot.send_message(message.chat.id, 'Тебе видалено з черги')


@bot.message_handler(commands=['inform'])
def inform_message(message):
    """Вивід інформації про можливості бота."""
    bot.send_message(message.chat.id, 'Щоб розпочати створення черги натисни /start\n'
                                      'Щоб зайняти місце натисни /reg\n'
                                      'Щоб зупинити процес створення черги натисни /end\n'
                                      'Щоб видалити себе із черги натисни /del\n'
                                      'Щоб переглянути список натисни /check')

bot.polling()
