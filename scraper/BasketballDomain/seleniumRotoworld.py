from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


GECKO_PATH = "./geckodriver"
ADBLOCK_PATH = "./adblock_plus-3.10-an fx.xpi"


rotoworld_file = open("url_rotoworld.txt", "r")
content_rotoworld = rotoworld_file.read()
content_list_rotoworld = content_rotoworld.split(",")

s = content_list_rotoworld


ffprofile = webdriver.FirefoxProfile()
ffprofile.add_extension(ADBLOCK_PATH)
ffprofile.set_preference("extensions.adblockplus.currentVersion", "3.10")
binary = FirefoxBinary('/usr/bin/firefox')
firefox = webdriver.Firefox(firefox_profile=ffprofile, firefox_binary=binary, executable_path=GECKO_PATH)

for page in s:
    if(page == ''):
        break
    print('Caricando pagina' + page + '\n')
    firefox.get(page)
    html = firefox.page_source
    filename = page[page.rfind('/')+1: ] + ".html"
    my_file = open('./ROTOWORLD_pages/' + filename, "w")
    print('Scrivendo pagina' + page + '\n')
    my_file.write(str(html))
    my_file.close
