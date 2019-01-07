# -*- coding: UTF8 -*-

import urllib, os


def connected(host='http://google.com'):
    try:
        urllib.urlopen(host)
        return True
    except:
        return False


from urllib2 import urlopen
from urllib2 import URLError


openurl_version = urlopen('http://pastebin.com/raw/vbbNwSYJ') # _version =Online Version
_version = openurl_version.read()

_v = '1.5' # Version

if _version == _v:
	D = " (UPDATED)"
else:
	D = " (OUTDADED)"




def Banner():

	from urllib2 import urlopen
	openurl_version = urlopen('http://pastebin.com/raw/vbbNwSYJ') #Online Version
	_version = openurl_version.read()

    	from colorama import Fore
	print Fore.YELLOW +"               ______  "+ Fore.GREEN +" _______  __   __  ___   __    _  _______                    "+ Fore.RED +"               ____             "
	print Fore.YELLOW +"              |      | "+ Fore.GREEN +"|       ||  |_|  ||___| |  |  | ||       |                   "+ Fore.RED +"        _,-ddd888888bbb-._      "
	print Fore.YELLOW +"              |  _    |"+ Fore.GREEN +"|   _   ||       | ___  |   |_| ||    ___|                   "+ Fore.RED +"      d88888888888888888888b    "
	print Fore.YELLOW +"              | | |   |"+ Fore.GREEN +"|  | |  ||       ||   | |       ||   | __                    "+ Fore.RED +"    d888888888888888888888888b  "
	print Fore.YELLOW +"              | |_|   |"+ Fore.GREEN +"|  |_|  | |     | |   | |  _    ||   ||  |                   "+ Fore.RED +"   6888888888888888888888888889 "
	print Fore.YELLOW +"              |       |"+ Fore.GREEN +"|       ||   _   ||   | | | |   ||   |_| |                   "+ Fore.RED +"   68888b8##8q8888888p8##8d88889"
	print Fore.YELLOW +"              |______| "+ Fore.GREEN +"|_______||__| |__||___| |_|  |__||_______|                   "+ Fore.RED +"   `d8887     p88888q     4888b'"
	print Fore.YELLOW +"   _______ "+ Fore.GREEN +" ______    _______ "+ Fore.YELLOW +" __   __ "+ Fore.GREEN +" _______  _     _  _______  ______    ___   _   "+ Fore.RED +" `d8887    p88888q    4888b' "
	print Fore.YELLOW +"  |       |"+ Fore.GREEN +"|    _ |  |   _   |"+ Fore.YELLOW +"|  |_|  |"+ Fore.GREEN +"|       || | _ | ||       ||    _ |  |   | | |  "+ Fore.RED +"   `d887   p88888q   488b'   "
	print Fore.YELLOW +"  |    ___|"+ Fore.GREEN +"|   | ||  |  |_|  |"+ Fore.YELLOW +"|       |"+ Fore.GREEN +"|    ___|| || || ||   _   ||   | ||  |   |_| |  "+ Fore.RED +"      `d88888888888888d'     "
	print Fore.YELLOW +"  |   |___ "+ Fore.GREEN +"|   |_||_ |       |"+ Fore.YELLOW +"|       |"+ Fore.GREEN +"|   |___ |       ||  | |  ||   |_||_ |      _|  "+ Fore.RED +"         `d88888888b'        "
	print Fore.YELLOW +"  |    ___|"+ Fore.GREEN +"|    __  ||       |"+ Fore.YELLOW +"|       |"+ Fore.GREEN +"|    ___||       ||  |_|  ||    __  ||     |_   "+ Fore.RED +"           `d8888b'          "
	print Fore.YELLOW +"  |   |    "+ Fore.GREEN +"|   |  | ||   _   |"+ Fore.YELLOW +"| ||_|| |"+ Fore.GREEN +"|   |___ |   _   ||       ||   |  | ||    _  |  "+ Fore.RED +"             `bd'            "
	print Fore.YELLOW +"  |___|    "+ Fore.GREEN +"|___|  |_||__| |__|"+ Fore.YELLOW +"|_|   |_|"+ Fore.GREEN +"|_______||__| |__||_______||___|  |_||___| |_|  "+ Fore.RED +"                             "
	if os.name == "posix":
		print Fore.CYAN + '\n                ╔════════════════════════════════╗'+ Fore.RED + '        DEPELOVER:      SEMPATTE'
		print Fore.CYAN + '                   https://www.fuck-society.com   '+ Fore.RED + '      DATE:           18/06/18'
		print Fore.CYAN + '                ╚════════════════════════════════╝'+ Fore.RED + '      VERSION:        '+_v + Fore.YELLOW + D
		print Fore.RED  + '                                                        ONLINE VERSION: ' + _version
		print Fore.WHITE
	elif os.name == "nt":
		print Fore.CYAN + '\n                                                '+ Fore.RED + '        DEPELOVER:      SEMPATTE'
		print Fore.CYAN + '                  https://www.fuck-society.com    '+ Fore.RED + '      DATE:           18/06/18'
		print Fore.CYAN + '                                                  '+ Fore.RED + '      VERSION:        '+_v + Fore.YELLOW + D
		print Fore.RED  + '                                                        ONLINE VERSION: ' + _version
		print Fore.WHITE


def Help():
    from colorama import Fore
    print Fore.MAGENTA
    print '[~] Use' + Fore.WHITE + ' use' + Fore.RED + ' [Module]' + Fore.MAGENTA + ' to select option' + Fore.WHITE + ' Ex: use dox/find_dni' + Fore.MAGENTA
    print '[~] Use'+ Fore.RED + ' showm ' + Fore.MAGENTA + 'to open the menu of modules. '
    print '[~] Use' + Fore.RED +  ' exit ' + Fore.MAGENTA + 'to close the framework.'
    print '[~] Use'+ Fore.RED + ' clear ' + Fore.MAGENTA + 'to clear the console. '
    print '[~] Use'+ Fore.RED + ' help ' + Fore.MAGENTA + 'to open the menu of help. '



def Menu():
    from colorama import Fore
    print Fore.YELLOW +'\n-------------------------------------------------------------------------------------------------------------------------------'
    print Fore.BLUE + '\n         Module                                        Description\n'
    print Fore.YELLOW + ' |::| dox/find_dni                 Search for the DNI number or name. Working only in Perú'
    print               ' |::| pys/email_bomb               Send emails in bigs quantities '
    print               ' |::| dox/whois                    Whois web for IP o HOST. '
    print               ' |::| dox/found_op                 Found the carrier.'
    print               ' |::| dox/ve_email                 Check if the email exists. '
    print               ' |::| pys/send_sms                 Send free SMS. '
    print               ' |::| pys/fake_email               Send fake emails. '
    print Fore.YELLOW +'-------------------------------------------------------------------------------------------------------------------------------'

