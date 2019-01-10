# -*- coding: UTF8 -*-

import os, time, sys
from colors import *

def CheckM(Module):


  global chk_1
  ModuleI = Module.upper()
  line = "--------------------------------------------------------------------------------------------------------------------"

  if os.name == "nt":
    chk_1 = "N"
  elif os.name == "posix":
    chk_1 = "✘"

  print " [ " + chk_1 + "]" + "::[" + ModuleI + "]: " + "Not installed! "


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

  print "\n [" + chk_2 + "]" + "::[" + ModuleI + "]: " + "Installed! "

def pprint(Module_E):
  global simbol
  Module_L = Module_E.upper()

  if os.name == "nt":
    simbol = "Y"
  elif os.name == "posix":
    simbol = "✓"

  print " [" + simbol + "]" + "::[" + Module_L + "]: " + "Installed! "

def DeleteCache():
  print Yellow + '\n[/] Deleting cache... '

  if os.name == "posix":
    os.system("rm libs/__init__.pyc && rm libs/modules.pyc && rm libs/view.pyc && rm libs/colors.pyc")
    os.system("cd && rm usr/share/DoxingFramework/libs/__init__.pyc && rm usr/share/DoxingFramework/libs/modules.pyc && rm libs/view.pyc && rm usr/share/DoxingFramework/libs/colors.pyc")
  elif os.name == "nt":
    os.system("cd libs && del /F /Q __init__.pyc && del /F /Q modules.pyc && del /F /Q view.pyc && del /F /Q colors.pyc")
  else:
    pass

  time.sleep(1.0)
  print Yellow + '[/] Thanks for use' + Green + ' |DoxingFramework|' + White
  time.sleep(1.5)

  if os.name == "nt":  
    os.system("cls")
  elif os.name == "posix":
    os.system("clear")
  else:
    pass
  sys.exit()

def ctrl_c(signal, frame):
  print Yellow + '\n\n[Canceled by user: Ctrl+C Detected.] Exiting of' + Green + ' |DoxingFramework| ...'
  time.sleep(2)
  DeleteCache()
