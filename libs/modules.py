# -*- coding: UTF8 -*-

import os
import time
from sys import stdout
import sys, webbrowser

from colors import *

def VersionLocal():
    return '1.8'


def DetectPyVersion():
    import platform
    if platform.python_version()[0] == '2':
        pass
    else:
        print("You need the version 2.7.X of Python")
        exit(1)

def Command_exe(msg, cmd):
  i = "STATUS" + White + "::[Processing]"
  stdout.write( msg + " %s" % i)
  stdout.flush()
  os.system(cmd)
  j = White + "[" + Green + "OK" + White + "]"
  stdout.write(Yellow + "\n" + msg + " STATUS" + White + "::%s" % j)

def CheckM(Module):

  global chk_1
  ModuleI = Module.upper()
  line = White + "--------------------------------------------------------------------------------------------------------------------" + Yellow

  if os.name == "nt":
    chk_1 = "N"
  elif os.name == "posix":
    chk_1 = "✘"

  print " [" + Red + chk_1 + Yellow + "]" + "::[" + ModuleI + "]: " + Red + "Not installed! " + Yellow


  if os.name == "nt":
    print "\n"
    print line
    os.system("python -m pip install " + Module)
    print line
    chk_2 = "Y"
  else:
    print "\n"
    print line
    os.system("pip install " + Module)
    print line
    chk_2 = "✓"

  print "\n [" + Green + chk_2 + Yellow + "]" + "::[" + ModuleI + "]: " + Green + "Installed! " + Yellow

def pprint(Module_E):
  global simbol
  Module_L = Module_E.upper()

  if os.name == "nt":
    simbol = "Y"
  elif os.name == "posix":
    simbol = "✓"

  print " [" + Green + simbol + Yellow + "]" + "::[" + Module_L + "]: " + Green + "Installed! " + Yellow

def DeleteCache():
  print "\n"
  if os.name == "posix":
    print Command_exe(White + "[" + time.strftime('%H:%M:%S') + "]" + Yellow + "  Deleting Cache.                 ", 'rm libs/__init__.pyc && rm libs/modules.pyc && rm libs/view.pyc && rm libs/colors.pyc')
    print Command_exe(White + "[" + time.strftime('%H:%M:%S') + "]" + Yellow + "  Deleting Cache.                 ", 'cd && rm usr/share/DoxingFramework/libs/__init__.pyc && rm usr/share/DoxingFramework/libs/modules.pyc && rm libs/view.pyc && rm usr/share/DoxingFramework/libs/colors.pyc')

  elif os.name == "nt":
    print Command_exe(White + "[" + time.strftime('%H:%M:%S') + "]" + Yellow + "  Deleting Cache.                 ", 'cd libs && del /F /Q __init__.pyc && del /F /Q modules.pyc && del /F /Q view.pyc && del /F /Q colors.pyc')
  else:
    pass

  time.sleep(1.0)
  print Yellow + '\n[/] Thanks for use' + Green + ' |DoxingFramework|' + White
  time.sleep(1.5)

  if os.name == "nt":  
    os.system("cls")
  elif os.name == "posix":
    os.system("clear")
  else:
    pass

  exit(1)

def ctrl_c(signal, frame):
  print Yellow + '\n\n[Canceled by user: Ctrl+C Detected.] Exiting of' + Green + ' |DoxingFramework| ...' + Yellow
  time.sleep(2)
  DeleteCache()


def Update():
    from urllib2 import urlopen
    openurl_version = urlopen('http://pastebin.com/raw/vbbNwSYJ')  # Online version
    version_online = openurl_version.read()

    if os.name == "posix":
        if VersionLocal() == version_online:
            print Red + "[!]" + Yellow + " DoxingFramework is updated to the latest version."
        else:
            print Command_exe(White + "[" + time.strftime('%H:%M:%S') + "]" + Yellow + "  Updating...                                ", 'git clone https://github.com/Sempatte/DoxingFramework.git /tmp')
            print Command_exe(White + "[" + time.strftime('%H:%M:%S') + "]" + Yellow + "  Coping and deleting files.                 ", 'cp -R /tmp/* /usr/share/DoxingFramework/ && rm -rf /tmp')
            print Command_exe(White + "[" + time.strftime('%H:%M:%S') + "]" + Yellow + "  Installed.                                 ", 'echo DoxingFramework was updated.')
            exit(1)
    else:
        print Red + "[!]" + Yellow + " Doxing framework cannot be updated in Windows."
        time.sleep(1.5)
        webbrowser.open_new("https://github.com/Sempatte/DoxingFramework")

