import telebot

# Bot Token
BOT_TOKEN = '8003252655:AAF9d039Y48eSLt36NzFbcKCMYrc-kxPMd8'

# Bot Init
bot = telebot.TeleBot(BOT_TOKEN, parse_mode='Markdown')

@bot.message_handler(commands=['start'])
def start_command(message):
    first_name = message.from_user.first_name or ""
    last_name = message.from_user.last_name or ""
    username = message.from_user.username or "N/A"
    user_id = message.from_user.id
    language_code = message.from_user.language_code or "N/A"

    # Escape underscores in username if needed (Markdown rule)
    safe_username = username.replace('_', '\\_')

    info = f"""
Username: @{safe_username}
User 🆔️: `{user_id}`
First Name: {first_name}
Last Name: {last_name}
Language: {language_code}
"""

    bot.reply_to(message, info)

print("Bot is running...")
bot.polling()
