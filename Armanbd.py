#coding: utf-8
# module
import os,sys,time,getpass

# username
x = "vindra"
# password
y = "vindra"


# mengetik otomatis cepat
def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.002)


# login
def login():
  os.system("clear")
  sp("\033[1;96m       ╔╗   ╔═══╗╔═══╗╔══╗╔═╗ ╔╗")
  sp("       ║║   ║╔═╗║║╔═╗║╚╣─╝║║╚╗║║")
  sp("       ║║   ║║ ║║║║ ╚╝ ║║ ║╔╗╚╝║")
  sp("       ║║ ╔╗║║ ║║║║╔═╗ ║║ ║║╚╗║║")
  sp("       ║╚═╝║║╚═╝║║╚╩═║╔╣─╗║║ ║║║")
  sp("       ╚═══╝╚═══╝╚═══╝╚══╝╚╝ ╚═╝")
  sp("\033[1;96m+\033[1;90m========================================\033[1;96m+")
  sp(" \033[1;97m{\033[1;93m•\033[1;97m} \033[1;93mAuthor   \033[1;91m: \033[1;95mARMAN KING")
  sp(" \033[1;97m{\033[1;94m•\033[1;97m} \033[1;94mFacebook \033[1;91m: \033[1;96mMD ARMAN HOSSAIN ")
  sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;95mYouTube  \033[1;91m: \033[1;97no channel ")
  sp(" \033[1;97m{\033[1;96m•\033[1;97m} \033[1;96mGithub   \033[1;91m: \033[4;98mhttps://github.com/arman3\033[1;0m")
  sp("\033[1;96m+\033[1;90m========================================\033[1;96m+")
  username = raw_input(" \033[1;97m{\033[1;93m+\033[1;97m} \033[1;96mUsername:\033[1;92m ")
  password = getpass.getpass(" \033[1;97m{\033[1;93m+\033[1;97m} \033[1;96mPassword: ")
  if username == x and password == y:
    print(" \033[1;92mAccess Grented")
    time.sleep(1)
  else:
    print(" \033[1;91mAccess Denied")
    time.sleep(1)
    login()

login()
