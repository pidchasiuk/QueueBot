import telebot
import dbqueue as dbq

bot = telebot.TeleBot('1058265955:AAEhi2xia18dZCRuDPnZYB7NE5ZzAFxehtQ')


def add_id(id: int):
    id += 1
    return id


def add_number(number: int):
    number += 1
    return number


def format_queue(number, name):
    return '{0} - {1}'.format(number, name)


def send_queue():
    # subject = 'Предмет:' + '\n'
    # date = 'Дата:' + '\n'
    queue = 'Актуальна черга:' + '\n'
    res = dbq.get_name_number()
    res_message = ''
    for i in res:
        res_message += (i + '\n')
    print(res_message)


if __name__ == '__main__':
    dbq.get_name_number()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Давай створимо чергу. \n'
                                      'Щоб зайняти місце натисни /reg \n'
                                      'Коли чергу буде сформовано натисни /end')


@bot.message_handler(commands=['reg'])
def reg_message(message):
    """Додавання користувача в базу даних і в чергу"""
    i = 0
    dbq.add_user(add_id(i), add_number(i), message.from_user.username)
    bot.send_message(message.chat.id, 'Ти в черзі')
    i += 1


@bot.message_handler(commands=['end'])
def end_message(message):
    """Завершення створення черги, без можливості внести зміни."""
    bot.send_message(message.chat.id, 'Чергу створено.\n'
                                      'Щоб переглянути чергу натисни /check\n')


@bot.message_handler(commands=['inform'])
def inform_message(message):
    """Вивід інформації про можливості бота."""
    bot.send_message(message.chat.id, 'Щоб розпочати створення черги натисни /start\n'
                                      'Щоб зайняти місце натисни /reg\n'
                                      'Щоб зупинити процес створення черги натисни /end\n'
                                      'Щоб переглянути список натисни /check')
bot.polling()
