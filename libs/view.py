# -*- coding: UTF8 -*-

import urllib, os

from colors import *

def connected(host='http://google.com'):
    # noinspection PyBroadException
    try:
        urllib.urlopen(host)
        return True
    except:
        return False


from urllib2 import urlopen
# noinspection PyUnresolvedReferences
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
    openurl_version_2 = urlopen('http://pastebin.com/raw/vbbNwSYJ') #Online Version
    _version_2 = openurl_version_2.read()

    print Yellow +"               ______  "+ Green +" _______  __   __  ___   __    _  _______                    "+ Red +"               ____             "
    print Yellow +"              |      | "+ Green +"|       ||  |_|  ||___| |  |  | ||       |                   "+ Red +"        _,-ddd888888bbb-._      "
    print Yellow +"              |  _    |"+ Green +"|   _   ||       | ___  |   |_| ||    ___|                   "+ Red +"      d88888888888888888888b    "
    print Yellow +"              | | |   |"+ Green +"|  | |  ||       ||   | |       ||   | __                    "+ Red +"    d888888888888888888888888b  "
    print Yellow +"              | |_|   |"+ Green +"|  |_|  | |     | |   | |  _    ||   ||  |                   "+ Red +"   6888888888888888888888888889 "
    print Yellow +"              |       |"+ Green +"|       ||   _   ||   | | | |   ||   |_| |                   "+ Red +"   68888b8##8q8888888p8##8d88889"
    print Yellow +"              |______| "+ Green +"|_______||__| |__||___| |_|  |__||_______|                   "+ Red +"   `d8887     p88888q     4888b'"
    print Yellow +"   _______ "+ Green +" ______    _______ "+ Yellow +" __   __ "+ Green +" _______  _     _  _______  ______    ___   _   "+ Red +" `d8887    p88888q    4888b' "
    print Yellow +"  |       |"+ Green +"|    _ |  |   _   |"+ Yellow +"|  |_|  |"+ Green +"|       || | _ | ||       ||    _ |  |   | | |  "+ Red +"   `d887   p88888q   488b'   "
    print Yellow +"  |    ___|"+ Green +"|   | ||  |  |_|  |"+ Yellow +"|       |"+ Green +"|    ___|| || || ||   _   ||   | ||  |   |_| |  "+ Red +"      `d88888888888888d'     "
    print Yellow +"  |   |___ "+ Green +"|   |_||_ |       |"+ Yellow +"|       |"+ Green +"|   |___ |       ||  | |  ||   |_||_ |      _|  "+ Red +"         `d88888888b'        "
    print Yellow +"  |    ___|"+ Green +"|    __  ||       |"+ Yellow +"|       |"+ Green +"|    ___||       ||  |_|  ||    __  ||     |_   "+ Red +"           `d8888b'          "
    print Yellow +"  |   |    "+ Green +"|   |  | ||   _   |"+ Yellow +"| ||_|| |"+ Green +"|   |___ |   _   ||       ||   |  | ||    _  |  "+ Red +"             `bd'            "
    print Yellow +"  |___|    "+ Green +"|___|  |_||__| |__|"+ Yellow +"|_|   |_|"+ Green +"|_______||__| |__||_______||___|  |_||___| |_|  "+ Red +"                             "
    if os.name == "posix":
        print Cyan + '\n                ╔════════════════════════════════╗'+ Red + '      DEPELOVER:      SEMPATTE'
        print Cyan + '                   https://www.fuck-society.com   '+ Red + '      DATE:           18/06/18'
        print Cyan + '                ╚════════════════════════════════╝'+ Red + '      VERSION:        '+_v + Yellow + D
        print Red  + '                                                        ONLINE VERSION: ' + _version_2
        print White
    elif os.name == "nt":
        print Cyan + '\n                                                '+ Red + '        DEPELOVER:      SEMPATTE'
        print Cyan + '                  https://www.fuck-society.com    '+ Red + '      DATE:           18/06/18'
        print Cyan + '                                                  '+ Red + '      VERSION:        '+_v + Yellow + D
        print Red  + '                                                        ONLINE VERSION: ' + _version_2
        print White



def Help():
    print Purple
    print '[~] Use' + White + ' use' + Red + ' [Module]' + Purple + ' to select option' + White + ' Ex: use dox/find_dni' + Purple
    print '[~] Use'+ Red + ' showm ' + Purple + 'to open the menu of modules. '
    print '[~] Use' + Red +  ' exit ' + Purple + 'to close the framework.'
    print '[~] Use'+ Red + ' clear ' + Purple + 'to clear the console. '
    print '[~] Use'+ Red + ' help ' + Purple + 'to open the menu of help. '



def Menu():
    print Green +'\n--------------------------------------------------------------------------------------------------------------------'
    print Blue + '\n         Module                                        Description\n'
    print Yellow + ' |::| dox/find_dni                 Search for the DNI number or name. Working only in Peru'
    print               ' |::| pys/email_bomb               Send emails in bigs quantities '
    print               ' |::| dox/whois                    Whois web for IP o HOST. '
    print               ' |::| dox/found_op                 Found the carrier.'
    print               ' |::| dox/ve_email                 Check if the email exists. '
    print               ' |::| pys/send_sms                 Send free SMS. '
    print               ' |::| pys/fake_email               Send fake emails. '
    print Green +'--------------------------------------------------------------------------------------------------------------------'

