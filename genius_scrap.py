from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def genius(user_name):
    url = f'https://genius.com/artists/{user_name}'
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager" 
    
    driver = webdriver.Chrome('chromedriver', desired_capabilities=caps, options=chrome_options) 
    driver.get(url)
    
    sleep(1)
    
    html = driver.page_source
    
    driver.close()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    followers = soup.select("body > routable-page > ng-outlet > routable-profile-page > ng-outlet > routed-page > profile-page > div.profile_header > div.column_layout > div.column_layout-column_span.column_layout-column_span--primary > div > h3:nth-child(2) > span")
    songs = soup.select("body > routable-page > ng-outlet > routable-profile-page > ng-outlet > routed-page > profile-page > div.column_layout > div.column_layout-column_span.column_layout-column_span--primary > artist-songs-and-albums > div.mini_card_grid > div")
    
    song_list = []
    sum_view = 0
    for song in songs:
        try:
            view = song.find('span', {'ng-if': ':: $ctrl.song.stats.pageviews'}).text.split()[0]
            if 'K' in view:
                view = view.replace('K', '*1000')
            elif 'M' in view:
                view = view.replace('M', '*1000000')
            view = eval(view)
            song_list.append(view)
            sum_view += view
        except:
            pass
        
    return followers, sum_view

if __name__ == "__main__":
    user_name = "404vincent" #"12am"
    followers, sum_view = genius(user_name)
    print("Followers: ", followers[0].text)
    print("Views: ", int(sum_view))
