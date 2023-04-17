from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import os

def getimage(n):
    try:
        os.chdir(os.path.join(os.getcwd(),'images'))
    except:
        pass

    scrollnum=2
    sleepTimer=1

    #var='Itachi'
    url=f'https://in.pinterest.com/search/pins/?q={n}'
    options=webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches",['enable-logging'])
    driver=webdriver.Chrome(executable_path='chromedriver.exe',options=options)
    driver.get(url)
    for _ in range(1,scrollnum):
        driver.execute_script("window.scrollTo(1,100000)")
        print('scroll-down')
        time.sleep(sleepTimer)

    soup=BeautifulSoup(driver.page_source,'html.parser')

    for link in soup.findAll('img'):
        #print(link.get('src'))
        namesimage=link.get('src').strip('https://i.pinimg.com/236x/ad/ea/a1/.jpg')
        links=link.get('src')
        #print(namesimage)
        with open(namesimage.replace('/',' ')+'.png','wb' ) as f:
            im=requests.get(links)
            f.write(im.content)
    return

if __name__ == "__main__":
    enter=input('What should I download for you? huh ? ')
    getimage(enter)


