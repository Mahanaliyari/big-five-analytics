import requests  
from dotenv import load_dotenv
import os 


def configure(): 
    load_dotenv()

configure()    
headers = { "X-Auth-Token" : os.getenv('API_TOKEN')}

leagues={
        "premier league": "PL",
        "la liga": "PD",
        "bundesliga": "BL1",
        "serie a": "SA",
        "ligue 1": "FL1"
}
    
def get_league_code(league_name,leagues):
    return leagues[league_name]


def fetch_league(league_code):
    response = requests.get(f"http://api.football-data.org/v4/competitions/{league_code}/standings?season=2024",headers = headers )
    if response.status_code != 200: 
        return None
    return response.json()



    

    
         
        

    
