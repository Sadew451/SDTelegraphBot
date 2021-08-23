#    This file is part of the ChannelAutoForwarder distribution (https://github.com/Sadew451/TelegraphUploader).
#    Copyright (c) 2021 Sadew451
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/Sadew451/TelegraphUploader/blob/main/License> 

import os
from telegraph import upload_file
import pyrogram
from pyrogram import filters, Client
from sample_config import Config
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton,
    CallbackQuery, InlineQuery)

Tgraph = Client(
   "Telegra.ph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@SDBOTS.on_message(filters.photo)
async def uploadphoto(client, message):
  msg = await message.reply_text("`𝙏ʀʏɪɴɢ 𝙏ᴏ 𝘿ᴏᴡɴʟᴏᴀᴅ ⚡️`")
  userid = str(message.chat.id)
  img_path = (f"./DOWNLOADS/{userid}.jpg")
  img_path = await client.download_media(message=message, file_name=img_path)
  await msg.edit_text("`𝙏ʀʏɪɴɢ 𝙏ᴏ 𝙐ᴘʟᴏᴀᴅ.....🧨`")
  try:
    tlink = upload_file(img_path)
  except:
    await msg.edit_text("`Something went wrong`") 
  else:
    await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
    os.remove(img_path) 

@SDBOTs.on_message(filters.animation)
async def uploadgif(client, message):
  if(message.animation.file_size < 5242880):
    msg = await message.reply_text("`𝙏ʀʏɪɴɢ 𝙏ᴏ 𝘿ᴏᴡɴʟᴏᴀᴅ ⚡️`")
    userid = str(message.chat.id)
    gif_path = (f"./DOWNLOADS/{userid}.mp4")
    gif_path = await client.download_media(message=message, file_name=gif_path)
    await msg.edit_text("`𝙏ʀʏɪɴɢ 𝙏ᴏ 𝙐ᴘʟᴏᴀᴅ.....🧨`")
    try:
      tlink = upload_file(gif_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")   
      os.remove(gif_path)   
    except:
      await msg.edit_text("Something really Happend Wrong...") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb")

@SDBOTS.on_message(filters.video)
async def uploadvid(client, message):
  if(message.video.file_size < 5242880):
    msg = await message.reply_text("`𝙏ʀʏɪɴɢ 𝙏ᴏ 𝘿ᴏᴡɴʟᴏᴀᴅ ⚡️`")
    userid = str(message.chat.id)
    vid_path = (f"./DOWNLOADS/{userid}.mp4")
    vid_path = await client.download_media(message=message, file_name=vid_path)
    await msg.edit_text("`𝙏ʀʏɪɴɢ 𝙏ᴏ 𝙐ᴘʟᴏᴀᴅ.....🧨`")
    try:
      tlink = upload_file(vid_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
      os.remove(vid_path)   
    except:
      await msg.edit_text("Something really Happend Wrong...") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb")

@SDBOTS.on_message(filters.command(["start"]))
async def home(client, message):
  buttons = [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('⚡️ Our Channel 📣', url='http://telegram.me/SDBOTs_Inifinity'),
        InlineKeyboardButton('📋 Source Code 📋', url='https://github.com/Sadew451/TelegraphUploader')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await Tgraph.send_message(
        chat_id=message.chat.id,
        text="""<b>Hey there,
        
👋 𝙞𝙢 𝙖 𝙩𝙚𝙡𝙚𝙜𝙧𝙖𝙥𝙝 𝙐𝙥𝙡𝙤𝙖𝙙𝙚𝙧 𝙏𝙝𝙖𝙩 𝘾𝙖𝙣 𝙐𝙥𝙡𝙤𝙖𝙙 𝙋𝙝𝙤𝙩𝙤, 𝙑𝙞𝙙𝙚𝙤 𝘼𝙣𝙙 𝙂𝙞𝙛
        
𝚂𝚒𝚖𝚙𝚕𝚢 𝚜𝚎𝚗𝚍 𝚖𝚎 𝚙𝚑𝚘𝚝𝚘, 𝚟𝚒𝚍𝚎𝚘 𝚘𝚛 𝚐𝚒𝚏 𝚝𝚘 𝚞𝚙𝚕𝚘𝚊𝚍 𝚝𝚘 𝚃𝚎𝚕𝚎𝚐𝚛𝚊.𝚙𝚑
        
𝙈𝙖𝙙𝙚 𝙒𝙞𝙩𝙝 𝙇𝙤𝙫𝙚 𝘽𝙮 ❤️ @SDBotsz</b>""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )

@SDBOTS.on_message(filters.command(["help"]))
async def help(client, message):
  buttons = [[
        InlineKeyboardButton('Home ⚡️', callback_data='home'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ],
    [
        InlineKeyboardButton('⚡️ Our Channel 📣', url='http://telegram.me/SDBOTs_Inifinity')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await Tgraph.send_message(
        chat_id=message.chat.id,
        text="""There Is Nothung To KnowMore,
        
𝙅𝙪𝙨𝙩 𝙎𝙚𝙣𝙙 𝙈𝙚 𝘼 𝙑𝙞𝙙𝙚𝙤/𝙜𝙞𝙛/𝙥𝙝𝙤𝙩𝙤 𝙐𝙥𝙩𝙤 5𝙢𝙗.
𝙞'𝙡𝙡 𝙪𝙥𝙡𝙤𝙖𝙙 𝙪𝙩 𝙩𝙤 𝙩𝙚𝙡𝙚𝙜𝙧𝙖.𝙥𝙝 𝙖𝙣𝙙 𝙜𝙞𝙫𝙚 𝙮𝙤𝙪 𝙩𝙝𝙚 𝙙𝙞𝙧𝙚𝙘𝙩 𝙡𝙞𝙣𝙠""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )                           
@SDBOTS.on_callback_query()
async def button(Tgraph, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(Tgraph, update.message)
      elif "close" in cb_data:
        await update.message.delete() 
      elif "home" in cb_data:
        await update.message.delete()
        await home(Tgraph, update.message)

SDBOTS.run()
