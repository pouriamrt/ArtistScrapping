import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from openpyxl import load_workbook

df = pd.read_excel('Social Media Accounts.xlsx', index_col=0)
excel_file = load_workbook('Social Media Accounts.xlsx')
sheet = excel_file.active
# sheet.insert_cols(idx=7)
i = 1
for artist in df.index:
    try:
        youtube_url = df.loc[artist]['YouTube1']
        if youtube_url not in ['', '-']:
            y_lst = youtube_url.split('/')
            if y_lst[-2] == 'channel':
                y_id = y_lst[-1]
                sheet['G'][i].value = "https://www.youtube.com/channel/" + y_id
                i += 1
            else:
                response = requests.get(f"https://www.googleapis.com/youtube/v3/channels?key=AIzaSyAvv2-sjklJbH_Z3I4hraTNnMUfu7BTzek&forUsername={y_lst[-1].replace('@', '')}&part=id")
                if 'items' in response.json():
                    y_id = response.json()['items'][0]['id']
                    sheet['G'][i].value = "https://www.youtube.com/channel/" + y_id
                    i += 1
                else:
                    chrome_options = Options()
                    chrome_options.add_argument('--headless')
    
                    caps = DesiredCapabilities().CHROME
                    caps["pageLoadStrategy"] = "eager"
    
                    driver = webdriver.Chrome('chromedriver', desired_capabilities=caps, options=chrome_options) 
                    driver.get(youtube_url)
                    
                    y_id = driver.execute_script("return ytInitialData.metadata.channelMetadataRenderer.externalId;")
                    
                    driver.close()
                    
                    sheet['G'][i].value = "https://www.youtube.com/channel/" + y_id
                    i += 1
        else:
            sheet['G'][i].value = ''
            i += 1
    except:
        sheet['G'][i].value = ''
        i += 1
        pass

excel_file.save('Social Media Accounts.xlsx')


