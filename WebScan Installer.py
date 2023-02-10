import os, wget

if not os.path.exists("./WebScan"):
  os.makedirs("./WebScan")

try:
  import wget
except ImportError as err:
  os.system("pip install wget")

if not os.path.isfile("./WebScan/WebScan.exe"):
  wget.download("https://github.com/SansXpl/WebScan/raw/main/WebScan.exe", "./WebScan/")
  
os.chdir("./WebScan/")
os.system("WebScan.exe")