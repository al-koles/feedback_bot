import telebot
import config
import secret
import re

bot = telebot.TeleBot(secret.TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def start(message):
	bot.send_message(message.chat.id, config.beta_mess)
	if config.isAdmin(message):
		bot.send_message(message.chat.id, config.admin_hello_mess)
	else:
		bot.send_message(message.chat.id, config.user_hello_mess)


@bot.message_handler(content_types=['text'])
def text_mess(message):
	if config.isAdmin(message):
		client_message = message.reply_to_message;
		if(client_message):
			client_chat_id = re.match(r"\d{9}", client_message.text)
			if(client_chat_id):
				try:
					client_message = re.sub(client_chat_id.group(0), config.your_message, client_message.text, 1)
					bot.send_message(client_chat_id.group(0), client_message + config.reply + message.text)
				except Exception as e:
					bot.reply_to(message, config.sending_error + str(e))
				else:
					bot.reply_to(message, config.successful_reply)
				finally:
					pass
	else:
		try:
			bot.send_message(secret.adminchat_id, str(message.chat.id) + "\n" + message.text)
		except Exception as e:
			bot.reply_to(message, config.sending_error_2 + str(e))
		else:
			bot.reply_to(message, config.successful_sent)
		finally:
			pass

bot.polling(none_stop = True)