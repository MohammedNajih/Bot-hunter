import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from uuid import uuid4 
from faker import Faker
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
import json
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def boten(message):
	
    
    
    mas = types.InlineKeyboardMarkup(row_width=2)
    
    A = types.InlineKeyboardButton(text ="CHECK HUNTER INSTAGRAM", callback_data="F1")
    
    E = types.InlineKeyboardButton(text ="SOON... ", callback_data="F1") 
    
    M = types.InlineKeyboardButton('المطور', url='https://t.me/GDO00')
    
    mas.add(A,E,M)
    
    bot.send_message(message.chat.id, f"CHECKER BOT HUNTER EMAILS AND ACCOUNT INSTAGRAM OLD USERS AND 4TH USERS ️",reply_markup=mas)
    
    
@bot.callback_query_handler(func=lambda call: True)
def masg(call):
	
	
	global nam
	
	if call.data =="GDO00":
		
		mas = types.InlineKeyboardMarkup(row_width=2)
		
		A = types.InlineKeyboardButton(text ="CHECK HUNTER INSTAGRAM", callback_data="F1")

		E = types.InlineKeyboardButton(text ="SOON... ", callback_data="F2") 

		M = types.InlineKeyboardButton('المطور', url='https://t.me/GDO00')
		
		M = types.InlineKeyboardButton('المطور', url='https://t.me/GDO00')
		
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="CHECKER BOT HUNTER EMAILS AND ACCOUNT INSTAGRAM OLD USERS AND 4TH USERS ️",reply_markup=mas)

	elif call.data =="F1":
		ok = 0
		sk = 0
		gm = 0
		ins = 0
		while True:
			uid = uuid4()
			user = Faker().email().split("@")[0]
			email = user+"@gmail.com"
			url = 'https://android.clients.google.com/setup/checkavail'
			h = {'Content-Length':'98','Content-Type':'text/plain; charset=UTF-8','Host':'android.clients.google.com','Connection':'Keep-Alive','user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
			d = json.dumps({'username':user,'version':'3','firstName':'AbaLahb','lastName':'AbuJahl'})
			res = requests.post(url,data=d,headers=h)
			url1='https://i.instagram.com/api/v1/accounts/login/'
			headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*','Cookie':'missing','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US','X-IG-Capabilities':'3brTvw==','X-IG-Connection-Type':'WIFI','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Host':'i.instagram.com'}
			data = {'uuid':uid,  'password':'@gdo00bot','username':email,'device_id':uid,'from_reg':'false','_csrftoken':'missing','login_attempt_countn':'0'}
			req= requests.post(url1, headers=headers, data=data).text
			if ('"error_type":"bad_password"') in req:
					ins+=1
					ok+=1
					info=f"https://soud.me/api/Instagram?username={user}"
					req= requests.get(info).json()
					bio=req["info"]["bio"]
					name=req["info"]["name"]
					followers=req["info"]["followers"]
					following=req["info"]["following"]
					isv = req["info"]["verified"]
					isp = req["info"]["private"]
					id=req["info"]["id"]
					link = req["info"]["url"]
					user=req["info"]["username"]
					resp = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")  
					reep = resp.json()
					date = reep['data']
					GDO =(f"""𝙷𝙸 𝙸𝙽f𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 𝙰𝙲𝙲𝙾𝚄𝙽𝚃 ⎙\n• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •\n⌯ ɴᴀᴍᴇ » {name}\n⌯ ᴜsᴇʀɴᴀᴍᴇ » {user}\n⌯ ғᴏʟʟᴏᴡᴇʀs » {followers}\n⌯ ғᴏʟʟᴏᴡɪɴɢ » {following}\n⌯ ᴅᴀᴛᴇ » {date}\n⌯ ɪᴅ » {id}\n⌯ ᴘᴏsᴛs »\n⌯ ᴠᴇʀɪғɪᴇᴅ » {isv}\n⌯ ᴘʀɪvᴀᴛᴇ » {isp}\n⌯ ʙɪᴏ » {bio}\n⌯ 𝙻𝙸𝙽𝚔 » https://www.instagram.com/{user}\n⌯ 𝙻𝙸𝙽𝚔 » {link}\n• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •""")
					bot.send_message(call.message.chat.id,GDO)
					#bot.send_message(call.message.chat.id,f'𝙷𝙸 𝙸𝙽f𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 𝙰𝙲𝙲𝙾𝚄𝙽𝚃 ⎙\n• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •\n⌯ 𝐄𝐌𝐀𝐈𝐋 » {email}\n• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •')
			if res.json()['status'] == 'SUCCESS':
				gm+=1
			else:
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GMAIL : {gm}',callback_data="1x")
				E = types.InlineKeyboardButton(f' INSTA : {ins}', callback_data="1x")
				B = types.InlineKeyboardButton(f'GOOD : {ok}', callback_data="1x")
				R = types.InlineKeyboardButton(f'BAD : {sk}', callback_data="1x")
				M = types.InlineKeyboardButton('المطور', url='https://t.me/GDO00')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="START CHECKER",reply_markup=mas)
				
	elif call.data =="F2":
		bot.send_message(message.chat.id, f" FUCTION SOON ️",reply_markup=mas)
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://bothunterinsta.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
