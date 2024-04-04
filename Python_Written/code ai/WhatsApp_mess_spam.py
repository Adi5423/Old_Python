import pywhatkit
def spam_message(message, chat_name, number_of_times):
  """Sends a spam message to a WhatsApp chat.

  Args:
    message: The message to spam.
    chat_name: The name of the WhatsApp chat.
    number_of_times: The number of times to send the message.
  """

  for i in range(number_of_times):
    pywhatkit.sendwhatmsg(chat_name, message)
spam_message("Your message here", "Chat name here", 69)