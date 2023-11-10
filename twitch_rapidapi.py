import requests

def twitch(artist_id):
    url = f"https://gwyo-twitch.p.rapidapi.com/followerscount/{artist_id}"
    
    headers = {
     	"X-RapidAPI-Key": "5dd1ab6fb4msh32b4053fbb17cfdp1017b6jsn30daf1e3d96e",
     	"X-RapidAPI-Host": "gwyo-twitch.p.rapidapi.com"
    }
    
    response = requests.request("GET", url, headers=headers)
    
    data = response.json()
    
    followers = data['followers_count']
    
    return followers

if __name__ == "__main__":
    artist_id = 'shesjade'
    followers = twitch(artist_id)
    print(followers)