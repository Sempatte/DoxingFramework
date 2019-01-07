# -*- coding: UTF8 -*-

import os, time, sys


def CheckM(Module):
  ModuleI = Module.upper()
  line = "-------------------------------------------------------------------------------------------------------------------------------------------------------------"
  if os.name == "nt":
    chk_1 = " [N]" + "::[" + ModuleI + "]: " + "Not installed! "
  elif os.name == "posix":
    chk_1 = " [✘]" + "::[" + ModuleI + "]: " + "Not installed! "
  print chk_1
  if os.name == "nt":
    print "\n"
    print line
    os.system("python -m pip install " + Module)
    print line
    print "\n"
    print " [Y]" + "::[" + ModuleI + "]: " + "Installed! "
  elif os.name ==  "posix":
    print "\n"
    print line
    os.system("pip install " + Module)
    print line
    print "\n"
    print " [✓]" + "::[" + ModuleI + "]: " + "Installed! "
  else:
    pass

def pprint(Module_E):
  Module_L = Module_E.upper()
  if os.name == "nt":
    chk = " [Y]" + "::[" + Module_L + "]: " + "Installed! "
  elif os.name == "posix":
    chk = " [✓]" + "::[" + Module_L + "]: " + "Installed! "
  print chk

def DeleteCache():
  from colorama import Fore
  print  Fore.YELLOW + '\n[/] Deleting cache... ' 

  if os.name == "posix":
    os.system("rm libs/__init__.pyc && rm libs/modules.pyc && rm libs/view.pyc")
  elif os.name == "nt":
    os.system("cd libs && del /F /Q __init__.pyc && del /F /Q modules.pyc && del /F /Q view.pyc")
  else:
    pass

  time.sleep(1.0)
  print Fore.YELLOW + '[/] Thanks for use' + Fore.GREEN + ' |DoxingFramework|' + Fore.WHITE
  time.sleep(1.5)

  if os.name == "nt":  
    os.system("cls")
    os.system("color f")
  elif os.name == "posix":
    os.system("clear")
  else:
    pass
  sys.exit()

