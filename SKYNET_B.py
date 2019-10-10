# Project Creators
# GNU/Dan && Mr Bonnano && Kmiokande
# Bot created to assist in telegram group begins the hackers

import telebot
import os
import subprocess
print ("""
	 ____  _                     _   
	/ ___|| | ___   _ _ __   ___| |_ 
	\___ \| |/ / | | | '_ \ / _ \ __|
	 ___) |   <| |_| | | | |  __/ |_ 
	|____/|_|\_\\__, |_| |_|\___|\__|
	            |___/                


	""")

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

BOT_API_TOKEN = "Chave API"  # Aqui voce coloca sua Chave de acesso! do BotFather

bot = telebot.TeleBot(BOT_API_TOKEN)

# adiciona os comandos help e ajuda
@bot.message_handler(commands=['start', 'ajuda', ])
def foo(message):
    bot.reply_to(message, """\
Olá, este são os comandos:
\n/canal - canal no Youtube \n/regras - Regras do grupo \n/github - Nossos Arquivos \n/Link - link do grupo compartilhe \n/frase - Frase da Semana \n /info - Chame o BOT no PV """)


# adiciona o comando chama o canal do youtube
@bot.message_handler(commands=['canal'])
def foo(message):
    bot.reply_to(message, """ https://www.youtube.com/mrbonnano """)


@bot.message_handler(func=lambda m: True, content_types=['new_chat_members'])
def on_user_joins(message):
    bot.reply_to(message, text_messages['welcome'].format(name='Novo Usuario'))

# adiocionado comando para chamar as regras
@bot.message_handler(commands=['regras'])
def foo(message):
    bot.reply_to(message, """ Regras do grupo

    Para participar deste grupo o membro precisa concordar em compartilhar conhecimento, obedecer aos administradores e respeitar os outros membros. Qualquer desrespeito a estas regras ou a qualquer pessoa ou instituição poderá implicar em banimento do membro delitoso.

    Qualquer conteúdo postado fora dos tópicos do grupo deve ser removido, podendo implicar no banimento imediato do membro.

    Postagens que apresentem ou incitem corportamentos ou conteúdos ofensivos à lei serão removidas e o membro será imediatamente excluído.

    Postagens com intenção de doutrinamento político ou religioso serão removidas e o membro poderá ser excluído.

    Postagens que violem direitos autorais ou pessoais ou afetem a boa convivência no grupo serão excluídas e o membro será imediatamente banido.

    Postagens ligando o termo “Hacker” a atitudes criminosas, amorais ou anti-éticas serão eliminadas.

    Postagem com endereço/link suspeito não será aceita e será excluída.

    Postagem com endereço/link para material pirateado ou não autorizado não será aceita e será excluída.

    Postagem com links para outros grupos (e.g grupos do Facebook/Telegram, etc) não será aceita e será excluída.

    Postagem com links para vendas de produtos e/ou cursos (e.g Venda de cursos, etc) não será aceita e será excluída.

    Postagem com links para qualquer tipo de conteúdo visando lucro, negociação, vendas ou envolvendo valores monetários (seja criptomoedas ou dinheiro $$$), seja diretamente intencional ou de forma indireta não será aceita e será excluída.

    Não serão admitidos Lammers, Crackers, pessoas mal intencionadas ou que pretendam se valer do grupo para aprender a cometer crimes. Qualquer membro que seja descoberto em atitude suspeita será imediatamente banido.

    Os casos duvidosos ou excessões pertinentes serão discutidos com os administradores do grupo.
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


@bot.message_handler(commands=['info'])
def foo(message):
    if message:
        bot.reply_to(message, message.chat.id)


bot.polling()
