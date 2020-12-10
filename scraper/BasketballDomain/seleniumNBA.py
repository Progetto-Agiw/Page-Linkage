from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from Filereader import Filereader
from collections import deque
import platform, time

if platform.system() == 'Windows':
    GECKO_PATH = "./geckodriver.exe"
    binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
else:
    GECKO_PATH = "./geckodriver"
    binary = FirefoxBinary('/usr/bin/firefox')
#Needs absolute path (maybe, didn't work on Windows)
#ADBLOCK_PATH = "./adblock_plus-3.10-an fx.xpi"
#IMAGEBLOCK_PATH = "./image_block-5.0-fx.xpi"

ffprofile = webdriver.FirefoxProfile()
#https://intoli.com/blog/firefox-extensions-with-selenium/
#ffprofile.add_extension(extension=ADBLOCK_PATH)
#ffprofile.add_extension(extension=IMAGEBLOCK_PATH)
ffprofile.set_preference("extensions.adblockplus.currentVersion", "3.10")
ffoptions = webdriver.FirefoxOptions()
ffoptions.headless = True
firefox = webdriver.Firefox(firefox_profile=ffprofile, firefox_binary=binary, executable_path=GECKO_PATH, options=ffoptions)

filereader = Filereader()
urls = filereader.get_page("url_nba.txt") 

names = deque([])   

new_urls = []
for url in urls:
    temp = (url[url.rfind('https://www.nba.com/player/'):(url.rfind('/'))])
    names.append(temp[(temp.rfind('/')+1):])
    
    url_temp = url[:url.rfind('/')-1]
    url_id = url_temp[27 :url_temp.rfind('/')]
    url_finale = 'https://www.nba.com/' + 'stats/player/' + url_id + '/career'
    new_urls.append(url_finale)

page_count = 1

for page in new_urls:
    if page == '':
        break
    print('Caricando pagina ('+ str(page_count) +'/609):' + page)
    firefox.get(page)
    try:
        WebDriverWait(firefox, 60).until(
            #Cerca le tabelle delle stats o il giocatore rookie (no stats)
            EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "nba-stat-table__overflow")] | //div[text()="No statistics are currently available for the selected filters."][1]'))
        )
    except NoSuchElementException:
        print('Stats non trovate')
        raise NoSuchElementException

    html = firefox.page_source
    filename = './NBA_pages_stats/' + names.popleft() + '.html'
    my_file = open(filename, "w", encoding='utf8')
    print('Scrivendo pagina: ' + page + '\n')
    my_file.write(str(html))
    my_file.close
    page_count += 1
    time.sleep(15)

