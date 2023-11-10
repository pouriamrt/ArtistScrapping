import requests
from time import sleep, time
from datetime import date

#print(json.dumps(data, indent=3))

# a = json.dumps(data, indent=3)
# with open("test.txt", "w") as file:
#     file.write(a)

# for ->   < 5 songs on platform
def less_than_five(top_tracks):
    top_tracks = list(top_tracks)
    if len(top_tracks) < 5:
        return True
    return False
        
def more_than_thousand(top_tracks):
    top_tracks = list(top_tracks)
    for track in top_tracks:
        if track['playCount'] > 1000:
            return True
    return False

def n_plus_thousand(top_tracks, n):
    top_tracks = list(top_tracks)
    i = 0
    for track in top_tracks:
        if track['playCount'] > 1000:
            i += 1
        if i >= n:
            return True
    return False

def spotify(artist_id):
    # artist_id = url.split("?")[0].split("/")[-1]
    url = "https://spotify-scraper.p.rapidapi.com/v1/artist/overview"
    
    querystring = {"artistId":f"{artist_id}"}

    headers = {
	"X-RapidAPI-Key": "f01ec7d61cmshc06ec35bc9681d7p12ab04jsnf73b3c4af348",
	"X-RapidAPI-Host": "spotify-scraper.p.rapidapi.com"
}

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()
    
    sleep(0.75)
    
    data_album = {"date": ''}
    try:
        url_album = "https://spotify-scraper.p.rapidapi.com/v1/album/metadata"
        response_album = requests.request("GET", url_album, headers=headers, params={"albumId":f"{data['discography']['latest']['id']}"})
        data_album = response_album.json()
    except:
        pass
    
    sleep(0.75)
    
    url = "https://spotify-scraper.p.rapidapi.com/v1/artist/albums"
    querystring = {"artistId":f"{artist_id}","type":"single"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data1 = response.json()
    sleep(0.75)
    total_count = 0
    l = 0
    for i in data1['albums']['items']:
        url = "https://spotify-scraper.p.rapidapi.com/v1/album/tracks"
        sleep(0.75)
        querystring = {"albumId":f"{i['id']}"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        d = response.json()
        try:
            for j in d['tracks']['items']:
                #print(j['playCount'])
                total_count += j['playCount']
                l += 1
            if total_count == 0:
                break
        except:
            pass
        
    return data, total_count, data_album
        
if __name__ == "__main__":
    start_time = time()
    artist_id = "2BzV18PvTZ6ovYT7VjDlo7"
    data, total_count, data_album = spotify(artist_id)
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
    print("running time:", time() - start_time)
