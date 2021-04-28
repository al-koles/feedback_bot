import secret

beta_mess = "Now bot is running in beta mode. So if you find bugs etc., please write us: olexii.kolesnyk@gmail.com"
admin_hello_mess = "Hello, buddy! I'm 'Anon questions bot' and I bet you are a new admin. Welcome to the club! Now you start receiving messages from clients in this chat. To reply them you only need to reply on their messages in this chat and I promise to deliver the message for a small fee ;)"
user_hello_mess = "Hello, buddy! I'm 'Anon questions bot' and I see here is a new user. So now I'm ready for work. Write me a message and I will send it to my administrators. Don't worry, they won't see any information about you. After sending the message you will get the answer like a reply, but it may take some time."
your_message = "Your message:"
reply = "\n\nReply:\n"
sending_error = "Sorry error sending the reply.\nError: "
successful_reply = "The reply was sent successfully."
sending_error_2 = "Sorry... Something went wrong.\n Error: "
successful_sent = "Thank you! I sent your message to our feedback team. They will reply you soon."

def isAdmin(message):
	if secret.adminchat_id == str(message.chat.id):
		return True
	else:
		return False