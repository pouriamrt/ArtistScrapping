# import requests

# user_name = "404vincent"

# url = f"https://tokapi-mobile-version.p.rapidapi.com/v1/user/@{user_name}"

# headers = {
# 	"content-type": "application/octet-stream",
# 	"X-RapidAPI-Key": "5dd1ab6fb4msh32b4053fbb17cfdp1017b6jsn30daf1e3d96e",
# 	"X-RapidAPI-Host": "tokapi-mobile-version.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)
# data = response.json()

# print("Followers: ", data['user']['follower_count'])
# print("Likes: ", data['user']['total_favorited'])

import requests
from bs4 import BeautifulSoup
from time import sleep

def clean(text):
    text = text.replace(",", "")
    if 'K' in text:
        text = text.replace('K', '*1000')
    elif 'M' in text:
        text = text.replace('M', '*1000000')
    return int(eval(text))

def tiktok(url):
    site = requests.get(url)
    
    soup = BeautifulSoup(site.text, 'html.parser')
    sleep(0.5)
    
    views = soup.select("#main-content-others_homepage > div > div.tiktok-833rgq-DivShareLayoutMain.ee7zj8d4 > div.tiktok-1qb12g8-DivThreeColumnContainer.eegew6e2 > div > div")
    
    followers = soup.find_all('strong', {'title':'Followers'})
    
    likes = soup.find_all('strong', {'title':'Likes'})
    
    s = 0
    for i in views:
        item = i.select("div.tiktok-x6f6za-DivContainer-StyledDivContainerV2.eq741c50 > div > div > a > div > div.tiktok-11u47i-DivCardFooter.e148ts220 > strong")[0].text
        if 'K' in item:
            s += eval(item[:-1])*1000
        else:
            s += eval(item)
        # print(item)
    return clean(followers[0].text), clean(likes[0].text), int(s)


if __name__ == "__main__":
    user_name = "rip12am" #404vincent
    url = f'https://www.tiktok.com/@{user_name}?lang=en'
    followers, likes, s = tiktok(url)
    print("Followers: ", followers)
    print("Likes: ", likes)
    print("Views: ", s)

