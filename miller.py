from os import path
import os,base64,zlib,pip,urllib

import os,sys,tempfile,string,random,subprocess,platform,uuid,os,shutil,zlib,smtplib,base64,uuid,time,json,re


#_______[ BASIC COLORS ]_____>>
white = '\033[1;37m'
red = '\033[1;31m'
green = '\x1b[38;5;46m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
orange = '\033[1;35m'
extra ='\x1b[38;5;208m'
black="\033[1;30m"
#_________[ LOGO ]______>>>
def logo():
    os.system("clear")
    print(f"""
{blue}██╗ ███████╗██╗   ██╗██╗
{red}██╔══██╗██╔════╝██║   ██║██║
{green}██║  ██║█████╗  ██║   ██║██║
{yellow}██║  ██║██╔══╝  ╚██╗ ██╔╝██║
{red}██████╔╝███████╗ ╚████╔╝ ██║
{blue}╚═════╝ ╚══════╝  ╚═══╝  ╚═╝
                            
{blue}██████╗  ██████╗ ███╗   ███╗██╗                                                       
{green}██╔══██╗██╔═══██╗████╗ ████║██║                                                       
{yellow}██████╔╝██║   ██║██╔████╔██║██║                                                       
{red}██╔══██╗██║   ██║██║╚██╔╝██║██║                                                       
{green}██║  ██║╚██████╔╝██║ ╚═╝ ██║██║                                                       
{blue}╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝                                                       
                                                                                      
{blue}██████╗ ██╗      █████╗  ██████╗██╗  ██╗███╗   ███╗██╗██╗     ██╗     ███████╗██████╗ 
{green}██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝████╗ ████║██║██║     ██║     ██╔════╝██╔══██╗
{yellow}██████╔╝██║     ███████║██║     █████╔╝ ██╔████╔██║██║██║     ██║     █████╗  ██████╔╝
{green}██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██║╚██╔╝██║██║██║     ██║     ██╔══╝  ██╔══██╗
{blue}██████╔╝███████╗██║  ██║╚██████╗██║  ██╗██║ ╚═╝ ██║██║███████╗███████╗███████╗██║  ██║
{red}╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝

 FACEBOOK LINKS TO HACKED CONTACT AND GALLERY PIC AND FB ID HACKED100%                                                                                                                                                                                                            
     
-------------------------------------------------
Owner            :           ROM1 BADMASH X D3VI
Github           :       ROMI D9D        
version          :           0.69.091
Status           :           KING""")
    print(54*'-')



def devi():
    logo()
    print("[1] Gallery pic")
    print("[2] Contact list")
    print("[3] Link to Fb Extra Data")
    print("[4] Uid to Hack Facebook")
    print(54*"-")
    okh =input("[?] Choose option : ")
    if okh in ["01","1"]:
        main()
    if okh in ["02","2"]:
        login()
    if okh in ["E","e"]:
        exit()
    else:
        exit("[×] Re-Run Cammands")

def main():
    logo()
    cookies = input(' [?] input cookies : ')
    logo()
    limit = int(input('[?] Limit of comments : '))
    logo()
    print('[*] Use a comma to separate text comments')
    print('[*] for example: hell bro, Great Job')
    print(54*"-")
    text_comment = input('[?] Text comment : ')
    print(54*"-")
    print("[?] Put Post Link 🔗 like that : 2551707761661610")
    print(54*"-")
    userid = input('[?] Post id : ') 
    with requests.Session() as x:
         x.headers.update({
            "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com",
            "origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8",
         })
         try:
               link = x.get("https://business.facebook.com/business_locations", cookies = {'cookie':cookies})
               search = re.search("(EAAG\w+)", link.text).group(1)
               if 'EAAG' in search:
                   comment(cookies,search,limit,text_comment,userid)
         except AttributeError:exit('\n [×] failed comment, invalid cookie')

def comment(coki,token,limit,text_comment,userid):
    a = 0
    for _ in range(limit):
        a +=1
        for z in text_comment.split(','):
            b = requests.post(f'https://graph.facebook.com/{userid}/comments/?message={z}&access_token={token}', cookies={'cookie':coki})
            if 'We limit how often you can post, comment, or do other things in a certain amount of time to help protect the community from spam. You can try again later. Learn More' in b.text:
                exit('\n [×] account restricted dude ')
            if 'id' in b.text:
                print(f'\r[*] Total Comments : {a}',end=' ')
            else:
                continue

uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""

bumper = f'{id}{xp}'


import os, re, requests, json, bs4
from bs4 import BeautifulSoup as parser
ses=requests.Session()

def login():
    logo()
    cookie = input("[?] Put cookie : ")
    try:
        data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
        find_token = re.search("(EAAG\w+)", data.text)
        open("token.txt", "w").write(find_token.group(1))
        open("cookie.txt", "w").write(cookie)
        menu()
    except:
        os.system("rm token.txt cookie.txt")
        exit("[×] May Be cookies Expired or Incorrect Link")
        
    
def menu():
    try:
        token = open("token.txt","r").read()
        cok = open("cookie.txt","r").read()
        cookie = {"cookie":cok}
        nama = ses.get(f"https://graph.facebook.com/me?fields=name&access_token={token}",cookies=cookie).json()["name"]
    except:
        login()
    logo()
    print(f"[❤] Welcome  {nama} To Shareing Tool")
    print(54*"-")
    idt = input("[>] Put Post Full link : ")
    print(54*"-")
    limit = int(input("[?] Put Shareing limit : "))
    logo()
    try:
        n = 0
        header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
        for x in range(limit):
            n+=1
            post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={idt}&published=0&access_token={token}",headers=header, cookies=cookie).text
            data = json.loads(post)
            if "id" in post:
                print(f"[{n}] SUCCESSFULLY SHARED {data['id']}")
            else:
                exit("[×] may Be Cookies Expired or Incorrect link 🔗")
    except:
        exit("[×] may Be Cookies Expired or Incorrect link 🔗 ")
    


        

if __name__ == '__main__':
    devi()
