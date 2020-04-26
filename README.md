# Price Monitoring Bot
A bot that will help you monitor price of products on a website and notify you using a telegram bot. 

## Instructions to run

* Pre-requisites:
	-  Python3

* Directions to install
	- Setting up a virtual env 
	```bash
	virtualenv env
	env\Scripts\activate
	```
	- Installing Packages
	```bash
	pip install -r requirements.txt
	```

## Instructions to setup own Telegram bot

* Go to Telegram bot_father
* Create new Bot using /newbot
* Give your bot name and copy the apikey
* Go to your bot on telegram, click on start and send a message to it
* In browser go to https://api.telegram.org/bot{apikey}/getUpdates and copy the chat id
* Use https://api.telegram.org/bot{apikey}/sendMessage?text={message}&chat_id={chat_id} to send messages to your telegram bot
