import telebot

TOKEN = '7084189698:AAE-hObXQoML4mrfv8iqbCiEHUM7sVZuKMs'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: message.new_chat_members is not None)
def new_chat_member(message):
    for member in message.new_chat_members:
        bot.send_message(member.id, "Приветствую вас в нашем сообществе!")

bot.polling()
