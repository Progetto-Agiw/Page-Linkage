from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from Filereader import Filereader

GECKO_PATH = "./geckodriver"
ADBLOCK_PATH = "./adblock_plus-3.10-an fx.xpi"

ffprofile = webdriver.FirefoxProfile()
ffprofile.add_extension(ADBLOCK_PATH)
ffprofile.set_preference("extensions.adblockplus.currentVersion", "3.10")
binary = FirefoxBinary('/usr/bin/firefox')
firefox = webdriver.Firefox(firefox_profile=ffprofile, firefox_binary=binary, executable_path=GECKO_PATH)

filereader = Filereader()
urls = filereader.get_page("url_s24h.txt") 
   

for page in urls:
    if(page == ''):
        break
    print('Caricando pagina' + page + '\n')
    firefox.get(page)
    html = firefox.page_source
    filename = page[page.rfind('/')+1:] + '.html'
    print(filename)
    my_file = open(('./S24H_pages/' + filename), "w")
    print('Scrivendo pagina' + page + '\n')
    my_file.write(str(html))
    my_file.close
