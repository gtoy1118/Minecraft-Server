import os, sys
from replit import db

class TokenNotFound(Exception):
  pass

def refreshToken():
  try:
    file = open("token.txt")
    token = file.read()
    file.close()
    if token == "":
      raise TokenNotFound("No ngrok token found!")
    db["token"] = token
    os.system("rm token.txt")
    os.system("./ngrok authtoken {token}".format(token=token))
  except:
    try:
      token = db["token"]
      os.system("./ngrok authtoken {token}".format(token=token))
    except:
      file = open("token.txt","a")
      file.write("")
      file.close()
      raise TokenNotFound("No ngrok token found! Put this in token.txt.")
