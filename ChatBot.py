from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import yaml


bot = ChatBot('Bot')
trainer = ListTrainer(bot)

for files in os.listdir('C:/Users/swati/Desktop/Deep-Learning-Workshop-master/ChatBot/data/'):
	data = open('C:/Users/swati/Desktop/Deep-Learning-Workshop-master/ChatBot/data/' + files, 'r', encoding="utf8").readlines()
	trainer.train(data)
	

while True:
	message = input('You : ')
	if message.strip() != 'Bye':
		reply = bot.get_response(message)
		print('ChatBot : ',reply)
	
	if message.strip() == 'Bye':
		print("ChatBot : Bye")
		break

	
