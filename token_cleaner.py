from keyauth import api
import os
import sys
import os.path
import platform
import hashlib
from time import sleep
from datetime import datetime

# watch setup video if you need help https://www.youtube.com/watch?v=L2eAQOmuUiA
os.system("cls")
os.system("title Token Cleaner")
print("Initializing")
def getchecksum():
	path = os.path.basename(__file__)
	if not os.path.exists(path):
		path = path[:-2] + "exe"
	md5_hash = hashlib.md5()
	a_file = open(path,"rb")
	content = a_file.read()
	md5_hash.update(content)
	digest = md5_hash.hexdigest()
	return digest

keyauthapp = api(
	name = "Token Cleaner",
	ownerid = "FGXpwCiiYY",
	secret = "350322420f523b43b87c6adc8d3644184522f5f3d62c7881426a0f7d2358fca2",
	version = "1.0",
	hash_to_check = getchecksum()
)
print ("""

██╗███╗   ███╗██████╗ ███████╗██████╗ ██╗ █████╗ ██╗     
██║████╗ ████║██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██║     
██║██╔████╔██║██████╔╝█████╗  ██████╔╝██║███████║██║     
██║██║╚██╔╝██║██╔═══╝ ██╔══╝  ██╔══██╗██║██╔══██║██║     
██║██║ ╚═╝ ██║██║     ███████╗██║  ██║██║██║  ██║███████╗
╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝
                                                         
 █████╗ ██╗   ██╗████████╗██╗  ██╗                       
██╔══██╗██║   ██║╚══██╔══╝██║  ██║                       
███████║██║   ██║   ██║   ███████║                       
██╔══██║██║   ██║   ██║   ██╔══██║                       
██║  ██║╚██████╔╝   ██║   ██║  ██║                       
╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝                       
                                                         

1.Login
2.Register
""")
ans=input("Select Option: ") 
if ans=="1": 
	user = input('Provide username: ')
	password = input('Provide password: ')
	keyauthapp.login(user,password)
elif ans=="2":
	user = input('Provide username: ')
	password = input('Provide password: ')
	license = input('Provide License: ')
	keyauthapp.register(user,password,license) 
elif ans=="3":
	user = input('Provide username: ')
	license = input('Provide License: ')
	keyauthapp.upgrade(user,license)
    
elif ans=="4":
	key = input('Enter your license: ')
	keyauthapp.license(key)
else:
	print("\nNot Valid Option") 
	sys.exit()


#region Extra Functions

#* Download Files form the server to your computer using the download function in the api class
#bytes = keyauthapp.download("FILEID")
#f = open("example.exe", "wb")
#f.write(bytes)
#f.close()


#* Set up user variable
#keyauthapp.setvar("varName", "varValue")

#* Get user variable and print it
#data = keyauthapp.getvar("varName")
#print(data)

#* Get normal variable and print it
#data = keyauthapp.var("varName")
#print(data)

#* Log message to the server and then to your webhook what is set on app settings
#keyauthapp.log("Message")

#* Get if the user pc have been blacklisted
#print(f"Blacklisted? : {keyauthapp.checkblacklist()}")

#* See if the current session is validated
#print(f"Session Validated?: {keyauthapp.check()}")


#* example to send normal request with no POST data
#data = keyauthapp.webhook("WebhookID", "?type=resetuser&user=username")

#endregion




import requests,os,threading
from time import sleep
from colorama import Fore

if os.name == 'nt':
	os.system("cls")
else:
	os.system("clear")

print(f"""{Fore.MAGENTA}
░▀█▀░█▀█░█░█░█▀▀░█▀█░░░█▀▀░█░░░█▀▀░█▀█░█▀█░█▀▀░█▀▄
░░█░░█░█░█▀▄░█▀▀░█░█░░░█░░░█░░░█▀▀░█▀█░█░█░█▀▀░█▀▄
░░▀░░▀▀▀░▀░▀░▀▀▀░▀░▀░░░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀{Fore.RESET} v1 \n""")

tokens_type = input(f"{Fore.LIGHTMAGENTA_EX}Token Type (combo/token): {Fore.RESET}")
proxy = input(f"{Fore.LIGHTMAGENTA_EX}Proxy (username:password@ip:port): {Fore.RESET}")

if proxy != "":
	proxies = {
	"https": f"http://{proxy}"
	}
else:
	proxies = None

if tokens_type.lower() != "combo":
    tokens = open("tokens.txt", 'r').read().splitlines()
    total_token = len(tokens)
else:
    tokens = open("tokens.txt", "r").read()
    total_token = len(tokens.splitlines())

print(f"{Fore.YELLOW}\n[!] Loaded {total_token} tokens.\n{Fore.RESET}")

def clear(token):

    headers = {
    	"x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjkzLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTMuMCIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAwODA0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
    	"sec-fetch-dest": "empty",
    	"x-debug-options": "bugReporterEnabled",
    	"sec-fetch-mode": "cors",
    	"sec-fetch-site": "same-origin",
    	"accept": "*/*",
    	"accept-language": "en-GB",
    	"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.16 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
    	"TE": "trailers"
    }

    headers_reg = {
        "accept": "*/*",
        "authority": "discord.com",
        "method": "POST",
        "path": "/api/v9/auth/register",
        "scheme": "https",
        "origin": "discord.com",
        "referer": "discord.com/register",
        "x-debug-options": "bugReporterEnabled",
        "accept-language": "en-US,en;q=0.9",
        "connection": "keep-alive",
        "content-Type": "application/json",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0OTY3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin"
    }

    def request_cookie():
        response1 = requests.get("https://discord.com")
        cookie = response1.cookies.get_dict()
        return cookie

    def request_fingerprint():
        response2 = requests.get("https://discordapp.com/api/v9/experiments", headers=headers_reg).json()
        fingerprint = response2["fingerprint"]
        return fingerprint

    while True:
        try:
            headers["authorization"] = token
            headers["x-fingerprint"] = request_fingerprint()
            cookie = request_cookie()
            response = requests.get(f"https://discord.com/api/v9/users/@me/guilds", headers=headers, cookies=cookie, proxies=proxies, timeout=15)
            if response.status_code == 200 or response.status_code == 204:
                for server in response.json():
                    response2 = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{server['id']}", headers=headers, cookies=cookie, json={'lurking': 'false'}, proxies=proxies, timeout=15)
                    if response2.status_code == 204:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {token[:36]}******* left! {Fore.LIGHTBLACK_EX}({server['name']}){Fore.RESET}")
                    else:
                        print(f"{Fore.LIGHTRED_EX}[!] Token {token[:36]}******* can't left! {Fore.LIGHTBLACK_EX}({response2.text}){Fore.RESET}")
    
                chat_response = requests.get(f"https://discord.com/api/v9/users/@me/channels", headers=headers, cookies=cookie, proxies=proxies, timeout=15)
                if chat_response.status_code == 200:
                    for chat in chat_response.json():
                        close_response = requests.delete(f"https://discord.com/api/v9/channels/{chat['id']}", headers=headers, cookies=cookie, proxies=proxies, timeout=15)
                        if close_response.status_code == 200:
                            print(f"{Fore.LIGHTGREEN_EX}[+] {token[:36]}******* deleted chat! {Fore.LIGHTBLACK_EX}({chat['id']}){Fore.RESET}")
                        else:
                            print(f"{Fore.LIGHTRED_EX}[!] {token[:36]}******* can't deleted chat! {Fore.LIGHTBLACK_EX}({close_response.text}){Fore.RESET}")
            break
        except Exception as err:
            print(f"{Fore.YELLOW}[!] {token[:36]}******* retrying.. {Fore.RESET}({Fore.LIGHTBLACK_EX}{err}{Fore.RESET})")
            pass

threads = []

for x in range(total_token):

    if tokens_type.lower() != "combo":
        token = tokens[x]
    else:
        token = tokens.split()[x].split(':')[2]

    t = threading.Thread(target=clear, args=(token,))
    t.daemon = True
    threads.append(t)

for x in range(total_token):
    threads[x].start()
    sleep(.5)

for x in range(total_token):
    threads[x].join()