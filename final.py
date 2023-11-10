import pandas as pd
from genius_scrap import genius
from openpyxl import load_workbook
from soundcloud_scrap import soundcloud
from facebook_scrap import facebook
from tiktok_rapidapi import tiktok
from twitter_rapidapi import twitter
# from time import sleep
from datetime import date
from spotify_rapidapi import spotify, n_plus_thousand, more_than_thousand, less_than_five
from youtube_rapidapi import youtube
from instagram_rapidapi import instagram
from twitch_rapidapi import twitch

df = pd.read_excel('Social Media Accounts.xlsx')
excel_file = load_workbook('Book1.xlsx')
sheet = excel_file.active

def spotify_func(url=None):
    if url == None:
        i = 2
        for user_name in df['Spotify']:
            try:
                user_name = user_name.split('/')[-1].split('?')[0]
                data, total_count, data_album = spotify(user_name)
                sheet['N'][i].value = date.today()
                sheet['O'][i].value = data['stats']['followers']
                sheet['P'][i].value = data['stats']['monthlyListeners']
                sheet['Q'][i].value = data['stats']['worldRank']
                sheet['R'][i].value = data['playlists']['totalCount']
                sheet['S'][i].value = data['relatedContent']['discoveredOn']['totalCount']
                sheet['T'][i].value = data['discography']['topTracks'][0]['name']
                sheet['U'][i].value = data['discography']['topTracks'][0]['playCount']
                sheet['V'][i].value = less_than_five(data['discography']['topTracks'])
                sheet['W'][i].value = more_than_thousand(data['discography']['topTracks'])
                sheet['X'][i].value = n_plus_thousand(data['discography']['topTracks'], 5)
                sheet['Y'][i].value = n_plus_thousand(data['discography']['topTracks'], 10)
                sheet['Z'][i].value = total_count
                sheet['AA'][i].value = data_album['date']
                i += 1
                excel_file.save('Book1.xlsx')
            except Exception as e:
                print("Error: ", e)
                if e == KeyboardInterrupt():
                    break
                else:
                    sheet['N'][i].value = ""
                    sheet['O'][i].value = ""
                    sheet['P'][i].value = ""
                    sheet['Q'][i].value = ""
                    sheet['R'][i].value = ""
                    sheet['S'][i].value = ""
                    sheet['T'][i].value = ""
                    sheet['U'][i].value = ""
                    sheet['V'][i].value = ""
                    sheet['W'][i].value = ""
                    sheet['X'][i].value = ""
                    sheet['Y'][i].value = ""
                    sheet['Z'][i].value = ""
                    sheet['AA'][i].value = ""
                    i += 1
                    pass
    else:
        user_name = url.split('/')[-1].split('?')[0]
        data, total_count, data_album = spotify(user_name)
        print("date: ", date.today())
        print("name: ", data['name'])
        print("followers: ", data['stats']['followers'])
        print("monthlyListeners: ", data['stats']['monthlyListeners'])
        print("worldRank: ", data['stats']['worldRank'])
        print("playlists: ", data['playlists']['totalCount'])
        print("playlists appeared on: ", data['relatedContent']['discoveredOn']['totalCount'])
        print("top song: ", data['discography']['topTracks'][0]['name'], " -> ", data['discography']['topTracks'][0]['playCount'])
        print("< 5 songs on platform: ", less_than_five(data['discography']['topTracks']))
        print("> 1000 streams: ", more_than_thousand(data['discography']['topTracks']))
        print("5+ songs 1000+ streams: ", n_plus_thousand(data['discography']['topTracks'], 5))
        print("10+ songs 1000+ streams: ", n_plus_thousand(data['discography']['topTracks'], 10))
        print("total_count:", total_count)
        print("most recent song: ", data_album['date'])

def genius_func(url=None):
    if url == None:
        i = 2
        for user_name in df['Artist']:
            try:
                followers, sum_view = genius(user_name)
                sheet['B'][i].value = followers[0].text
                sheet['C'][i].value = int(sum_view)
                i += 1
                excel_file.save('Book1.xlsx')
            except Exception as e:
                if e == KeyboardInterrupt():
                    break
                else:
                    sheet['B'][i].value = ""
                    sheet['C'][i].value = ""
                    i += 1
                    pass
    else:
        followers, sum_view = genius(url)
        print("Followers: ", followers[0].text)
        print("Views: ", int(sum_view))
            
def soundcloud_func(url=None):
    if url == None:
        i = 2
        for url in df['Soundcloud']:
            try:
                followers, song_list, sum_count = soundcloud(url)
                sheet['D'][i].value = followers
                try:
                    sheet['E'][i].value = song_list[max(song_list.keys())]
                except:
                    sheet['E'][i].value = ""
                try: 
                    sheet['F'][i].value = max(song_list.keys())
                except:
                    sheet['F'][i].value = ""
                try:
                    sheet['G'][i].value = int(sum_count)
                except:
                    sheet['G'][i].value = ""
                i += 1
                excel_file.save('Book1.xlsx')
            except Exception as e:
                if e == KeyboardInterrupt():
                    break
                else:
                    sheet['D'][i].value = ""
                    sheet['E'][i].value = ""
                    sheet['F'][i].value = ""
                    sheet['G'][i].value = ""
                    i += 1
                    pass
    else:
        followers, song_list, sum_count = soundcloud(url)
        print("Followers: ", followers)
        print("Most popular song: ", song_list[max(song_list.keys())], " -> Count: ", max(song_list.keys()))
        print("Total stream count: ", int(sum_count))
            
def facebook_func(url=None):
    if url == None:
        i = 2
        for url in df['Facebook']:
            try:
                followers, likes = facebook(url)
                sheet['H'][i].value = followers
                sheet['I'][i].value = likes
                i += 1
                excel_file.save('Book1.xlsx')
            except Exception as e:
                if e == KeyboardInterrupt():
                    break
                else:
                    sheet['H'][i].value = ""
                    sheet['I'][i].value = ""
                    i += 1
                    pass
    else:
        followers, likes = facebook(url)
        print("followers: ", followers, "\nlikes: ", likes)
            
def tiktok_func(url=None):
    if url == None:
        i = 2
        for url in df['TikTok']:
            try:
                followers, likes, s = tiktok(url)
                sheet['J'][i].value = followers
                sheet['K'][i].value = likes
                sheet['L'][i].value = s
                i += 1
                excel_file.save('Book1.xlsx')
            except Exception as e:
                if e == KeyboardInterrupt():
                    break
                else:
                    sheet['J'][i].value = ""
                    sheet['K'][i].value = ""
                    sheet['L'][i].value = ""
                    i += 1
                    pass
    else:
        followers, likes, s = tiktok(url)
        print("Followers: ", followers)
        print("Likes: ", likes)
        print("Views: ", s)
            
def twitter_func(url=None):
    if url == None:
        tw = twitter()
        tw.login()
        i = 2
        for url in df['Twitter']:
            try:
                followers = tw.get_data(url)
                sheet['M'][i].value = followers
                excel_file.save('Book1.xlsx')
            except Exception as e:
                if e == KeyboardInterrupt():
                    break
                else:
                    sheet['M'][i].value = ""
                    pass
            i += 1
        tw.closing()
    else:
        tw = twitter()
        tw.login()
        followers = tw.get_data(url)
        tw.closing()
        print("Followers: ", followers)
    
def youtube_func(url=None):
    if url == None:
        i = 2
        for url in df['YouTube']:
            try:
                subscribers, views, top_video, top_video_views = youtube(url.split('/')[-1])
                sheet['AB'][i].value = subscribers
                sheet['AC'][i].value = views
                sheet['AD'][i].value = top_video
                sheet['AE'][i].value = top_video_views
                i += 1
                excel_file.save('Book1.xlsx')
            except Exception as e:
                # print(e)
                if e == KeyboardInterrupt():
                    break
                else:
                    sheet['AB'][i].value = ""
                    sheet['AC'][i].value = ""
                    sheet['AD'][i].value = ""
                    sheet['AE'][i].value = ""
                    i += 1
                    pass
    else:
        subscribers, views, top_video, top_video_views = youtube(url.split('/')[-1])
        print("Subscribers: ", subscribers)
        print("Views: ", views)
        print("Top Video: ", top_video)
        print("Top Video Views: ", top_video_views)
            
def instagram_func(url=None):
    if url == None:
        i = 2
        for url in df['Instagram']:
            try:
                if '?' not in url.split('/')[-1] and ''!=url.split('/')[-1]:
                    url = url.split('/')[-1]
                else:
                    url = url.split('/')[-2]
                    
                followers = instagram(url)
                sheet['AF'][i].value = followers
                i += 1
                excel_file.save('Book1.xlsx')
            except Exception as e:
                if e == KeyboardInterrupt():
                    break
                else:
                    sheet['AF'][i].value = ""
                    i += 1
                    pass
    else:
        if '?' not in url.split('/')[-1] and ''!=url.split('/')[-1]:
            url = url.split('/')[-1]
        else:
            url = url.split('/')[-2]
            
        followers = instagram(url)
        print("Followers: ", followers)
            
def twitch_func(url=None):
    if url == None:
        i = 2
        for url in df['Artist']:
            try:
                followers = twitch(url)
                sheet['AG'][i].value = followers
                i += 1
                excel_file.save('Book1.xlsx')
            except Exception as e:
                if e == KeyboardInterrupt():
                    break
                else:
                    sheet['AG'][i].value = ""
                    i += 1
                    pass
    else:
        followers = twitch(url)
        print(followers)
            
            
if __name__ == "__main__":
    while True:
        try:
            num = eval(input("""Choose a number between 1-9: 
                             1-genius
                             2-soundcloud
                             3-facebook
                             4-tiktok
                             5-twitter
                             6-spotify
                             7-youtube
                             8-instagram \n Your number: """))
            url = input("\nEnter url to get the result for the url or leave it empty to fill the whole list of urls in Social Media excel file: ")
            if url=="":
                url=None
            if num==1:
                genius_func(url)
            elif num==2:
                soundcloud_func(url)
            elif num==3:
                facebook_func(url)
            elif num==4:
                tiktok_func(url)
            elif num==5:
                twitter_func(url)
            elif num==6:
                spotify_func(url)
            elif num==7:
                youtube_func(url)
            elif num==8:
                instagram_func(url)
            # elif num==9:
            #     twitch_func(url)
        
        except Exception as e:
            print("E: ", e)
        
        finally:
            cl = input("\nDo you want to close the program?(Y/n)")
            if cl=='Y' or cl=='y':
                break
