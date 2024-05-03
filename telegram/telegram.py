import telebot
import time

bot = telebot.TeleBot("7084189698:AAE-hObXQoML4mrfv8iqbCiEHUM7sVZuKMs")
channel_id = "@your_channel_username"

previous_members_count = 0

def send_welcome_message(user_id):
    bot.send_message(user_id, "Добро пожаловать в наш канал!", parse_mode="Markdown")

@bot.channel_post_handler(content_types=["new_chat_members"])
def greet_new_members(message):
    global previous_members_count
    current_members_count = message.chat.members_count
    if current_members_count > previous_members_count:
        for member in message.new_chat_members:
            send_welcome_message(member.id)
        previous_members_count = current_members_count

while True:
    try:
        bot.polling(none_stop=True)
    except ValueError as e:
        print("Error occurred:", e)
        time.sleep(10)
