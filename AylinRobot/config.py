

import os

class Config:

   API_ID = int(os.getenv("API_ID", "12345789"))
   API_HASH = os.getenv("API_HASH", "12345789")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "7882850656:AAG9DWcXoAkgSdts4qtguYZRTPZwREG_LXA")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "xOyunRobot")
   BOT_NAME = os.environ.get("BOT_NAME", "Söz Oyunu")   
   OWNER_ID = int(os.environ.get("OWNER_ID","7218327869"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "LerroAndMee") 
   GONDERME_TURU = bool(os.environ.get("GONDERME_TURU", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "123457890")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002209683682"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "X_Botlar")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1002209683682"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1002209683682"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "123456789")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "LERRO")
   CHANNEL = os.environ.get("CHANNEL", "X_Botlar")
   SUPPORT = os.environ.get("SUPPORT", "X_Destek")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "") 
   START_IMG = os.environ.get("START_IMG", "")
   COMMAND_PREFIXES = list(os.environ.get("COMMAND_PREFIXES", "/ ! .").split())
