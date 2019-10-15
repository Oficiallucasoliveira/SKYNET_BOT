#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project Creators
# GNU/Dan && Mr Bonnano && Kmiokande
# Bot created to assist in telegram group begins the hackers


import telebot
import os
import subprocess

#Banner Personalizado BOT SKYNET 
print ("""
	

	 ____  _                     _   
	/ ___|| | ___   _ _ __   ___| |_ 
	\___ \| |/ / | | | '_ \ / _ \ __|
	 ___) |   <| |_| | | | |  __/ |_ 
	|____/|_|\_\\__, |_| |_|\___|\__|
	            |___/                
	  @coder: Mr<B0nN4n0


	""")
print ("\t \t \t B E G I N S T H E H A C K E R S ")

#Fim do Banner 
ids = [898925771]

text_messages = {
    'welcome':
        u'Welcome {name}!\n\n'
        u'Este grupo serve para discutir sobre desenvolvimento de Hackers.\n'
        u'Sinta-se livre para tirar dúvidas bem como discutir sobre áreas de TI.\n\n'
        u'Se você quer ser um ciber criminoso, estude por conta própria,\n'
        u'Pois nesse grupo ninguém vai te ajudar com seu Grande Plano \n'
        u'Dan Morris, criador do grupo de estudos @hackbr\n'
        u'Veja as regras /regras /ajuda para ver comandos!\n'
        u'Espero que goste, enjoy!'
}

BOT_API_TOKEN = "930304890:AAGVOCp_g9rH-YiVf_2OH-kZBSA8-xuUHYk"  # Aqui voce coloca sua Chave de acesso! do BotFather

bot = telebot.TeleBot(BOT_API_TOKEN)

# adiciona os comandos help e ajuda
@bot.message_handler(commands=['start', 'ajuda', ])
def foo(message):
    bot.reply_to(message, """
		🤖Ola meu nome e C0der🤖
              Vou auxiliar 
                   Voce
		 Para ver os comandos basta 
		 

		 -> /regras - Regras Gerais GP

		 -> /canal  - Mr Bonnano

		 -> /github - Repositorio GITHUB

		 -> /shell  - Comando ADM

		 -> /reboot - Reinicia RP3

		 -> /foto     - Tirar foto

		 -> /tsorte  - Resul TSORTE

		 -> /id 	- Mostra ID
												""")

# adiciona o comando chama o canal do youtube
@bot.message_handler(commands=['canal'])
def foo(message):
    bot.reply_to(message, """ https://www.youtube.com/mrbonnano """)


@bot.message_handler(func=lambda m: True, content_types=['new_chat_members'])
def on_user_joins(message):
    bot.reply_to(message, text_messages['welcome'].format(name='Novo Usuario'))

# chamar as regras
@bot.message_handler(commands=['regras'])
def foo(message):
    bot.reply_to(message, """ Regras do grupo
	
	-> Não poste conteudos Infectados
	-> Não poste conteudos como CURSOS ou PDFS
	-> Não poste conteudos Cards ou Bankers 
	-> Não poste conteudos Pornograficos
	-> Respeite a todos os membros do Grupo
	-> Qualquer Descumprimentos dessas Regras Resultara em Ban
""")
@bot.message_handler(commands=['github'])
def foo(message):
    bot.reply_to(message, "https://github.com/mrbonnano/")


@bot.message_handler(commands=['link'])
def foo(message):
    bot.reply_to(message, "https://t.me/beginsthehackers")

# Frases do Dia
@bot.message_handler(commands=['frase'])
def foo(message):
    bot.reply_to(message, """Frase do Dia\n
	 Se você conhece o inimigo e conhece a si mesmo, não precisa temer o resultado de cem batalhas.\n
	 Se você se conhece mas não conhece o inimigo, para cada vitória ganha sofrerá também uma derrota.\n
	 Se você não conhece nem o inimigo nem a si mesmo, perderá todas as batalhas...\n""")

#Para ter acesso a shell or cmd
@bot.message_handler(commands=['shell'])
def shell(message):

    if message.from_user.id in ids:
        comando = message.text.replace('/shell', '')
        bot.reply_to(message, subprocess.getoutput(comando))

    else:
        bot.reply_to(message, 'Voce nao tem permissão de comando!')
        print(message.chat.first_name)

#Envia o Id do User
@bot.message_handler(commands=['id'])
def foo(message):
    if message:
        bot.reply_to(message, message.chat.id)


bot.polling()
