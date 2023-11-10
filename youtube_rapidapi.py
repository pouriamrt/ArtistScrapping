import requests

def youtube(artist_id):
    url = "https://youtube138.p.rapidapi.com/channel/details/"
    
    querystring = {"id":f"{artist_id}","hl":"en","gl":"US"}
    
    headers = {
    	"X-RapidAPI-Key": "f01ec7d61cmshc06ec35bc9681d7p12ab04jsnf73b3c4af348",
    	"X-RapidAPI-Host": "youtube138.p.rapidapi.com"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    data = response.json()
    
    subscribers = data['stats']['subscribers']
    views = data['stats']['views']
    
    
    url1 = "https://youtube138.p.rapidapi.com/channel/videos/"
    
    response = requests.request("GET", url1, headers=headers, params=querystring)
    
    data = response.json()
    
    top_vid = ['', 0]
    for c in data['contents']:
        temp = [c['video']['title'], c['video']['stats']['views']]
        if temp[1] > top_vid[1]:
            top_vid = temp
        
    top_video = top_vid[0]
    top_video_views = top_vid[1]
    
    return subscribers, views, top_video, top_video_views


if __name__ == "__main__":
    artist_id = "UChZV-PINuYsY_nWHM5HbhBA"
    subscribers, views, top_video, top_video_views = youtube(artist_id)
    print(subscribers, views, top_video, top_video_views)
    