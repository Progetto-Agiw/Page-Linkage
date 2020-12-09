from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from Filereader import Filereader
from collections import deque

GECKO_PATH = "./geckodriver"
ADBLOCK_PATH = "./adblock_plus-3.10-an fx.xpi"

ffprofile = webdriver.FirefoxProfile()
ffprofile.add_extension(ADBLOCK_PATH)
ffprofile.set_preference("extensions.adblockplus.currentVersion", "3.10")
binary = FirefoxBinary('/usr/bin/firefox')
firefox = webdriver.Firefox(firefox_profile=ffprofile, firefox_binary=binary, executable_path=GECKO_PATH)

filereader = Filereader()
urls = filereader.get_page("url_nba.txt") 

names = deque([])   

new_urls = []
for url in urls:
    
    temp = (url[url.rfind('https://www.nba.com/player/'):(url.rfind('/'))])
    names.append(temp[(temp.rfind('/')+1):])
    
    url_temp = url[:url.rfind('/')-1]
    url_id = url_temp[27 :url_temp.rfind('/')]
    url_finale = 'https://www.nba.com/' + '/stats/player/' + url_id + '/career'
    new_urls.append(url_finale)

for page in new_urls:
    if(page == ''):
        break
    print('Caricando pagina' + page + '\n')
    firefox.get(page)
    html = firefox.page_source
    filename = names.popleft() + '.html'
    my_file = open(filename, "w")
    print('Scrivendo pagina' + page + '\n')
    my_file.write(str(html))
    my_file.close

