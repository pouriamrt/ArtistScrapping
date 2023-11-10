from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

def clean(text):
    text = text.replace(",", "")
    if 'K' in text:
        text = text.replace('K', '*1000')
    elif 'M' in text:
        text = text.replace('M', '*1000000')
    return eval(text)

def soundcloud(url):
    url = url + "/tracks"
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager" 
    
    driver = webdriver.Chrome('chromedriver', options=chrome_options, desired_capabilities=caps)
    driver.get(url)
    
    sleep(0.5)
    
    try:
        cookie = driver.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler")
        cookie.click()
    except:
        pass
    
    sleep(0.5)
    
    last_scroll_height = driver.execute_script('return document.body.scrollHeight')
    
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        sleep(1)
        
        new_scroll_height = driver.execute_script('return document.body.scrollHeight')
        
        if new_scroll_height == last_scroll_height:
            break
            
        last_scroll_height = new_scroll_height
        
    
    html = driver.page_source
    
    driver.close()
    
    soup = BeautifulSoup(html, 'html.parser')

    songs = soup.select("#content > div > div.l-fluid-fixed > div.l-main.l-user-main.sc-border-light-right > div > div.userMain__content > div > ul > li")
    
    song_list = {}
    sum_count = 0
    
    for song in songs:
        count = song.select("div > div > div.sound__content > div.sound__footer.g-all-transitions-300 > div.sound__footerRight.sc-mt-1x > div > ul > li:nth-child(1) > span > span:nth-child(2)")
        if len(count) == 0:
            continue
        count = clean(count[0].text)
        name = song.select("div > div > div.sound__content > div.sound__header.sc-mb-1\.5x.sc-px-2x > div > div > div.soundTitle__usernameTitleContainer.sc-mb-0\.5x > a > span")[0].text
        sum_count += count
        song_list[count] = name
        
    followers = soup.select("#content > div > div.l-fluid-fixed > div.l-sidebar-right.l-user-sidebar-right > div > article.infoStats > table > tbody > tr > td:nth-child(1) > a > div")[0].text
    return followers, song_list, sum_count

if __name__ == "__main__":
    user_name = "ilove12am" # "404vincent"
    url = f'https://soundcloud.com/{user_name}'
    url = "https://soundcloud.com/leith-ross"
    url = "https://soundcloud.com/user-908495214"
    followers, song_list, sum_count = soundcloud(url)
    print("Followers: ", followers)
    print("Most popular song: ", song_list[max(song_list.keys())], " -> Count: ", max(song_list.keys()))
    print("Total stream count: ", int(sum_count))


