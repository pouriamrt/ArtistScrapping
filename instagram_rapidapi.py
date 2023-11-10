import requests
    
def instagram(user_id):
    url = "https://instagram130.p.rapidapi.com/account-info"
    
    querystring = {"username":f"{user_id}"}
    
    headers = {
    	"X-RapidAPI-Key": "f01ec7d61cmshc06ec35bc9681d7p12ab04jsnf73b3c4af348",
    	"X-RapidAPI-Host": "instagram130.p.rapidapi.com"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    data = response.json()
    
    followers = data['edge_followed_by']['count']
    
    return followers
    
    
if __name__ == "__main__":
    user_id = "12am"
    followers = instagram(user_id)
    print(followers)
