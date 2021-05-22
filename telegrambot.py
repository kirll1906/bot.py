# -*- coding: utf-8 -*-
"""
Created on Sat May 22 16:17:02 2021

@author: user
"""
import telebot
import random
import urllib.request
from urllib.parse import quote
from lxml.html import fromstring 
bot = telebot.TeleBot('1610192837:AAHNulo4TyPr7OY6p2UU8IC9tDDD2SnbGt8')
greeting = ['Привет', 'Hi', 'Hello', 'ку', 'хай', 'здарова']
@bot.message_handler(content_types = ['text'])
def send_text(message):
    if 'привет' in message.text.lower():
        bot.send_message(message.chat.id, greeting[random.randint(0, len(greeting) - 1)])
    elif 'рифма' in message.text.lower():
        question = message.text.lower().replace('рифма', '')
        url = urllib.request.Request('https://rifme.net/r/' + quote(question), headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(url).read()
        page = fromstring(response)
        answer = ''
        for i in range(1, 11):
            if page.xpath('//*[@id="tochnye"]/li[' + str(i) + ']'):
                result = page.xpath('//*[@id="tochnye"]/li[' + str(i) + ']')
                answer += result[0].attrib['data-w'] + '\n'
        if answer:
            bot.send_message(message.chat.id, answer)
bot.polling()