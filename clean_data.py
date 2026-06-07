import pandas as pd 
 
def cleaner(data_dict):
    
    # getting the top 10 teams of the league   
    team_stats = data_dict["standings"][0]["table"][0:10] 
    df = pd.DataFrame(team_stats)
    
    # extracting the team's name and short name 
    df["short_name"] = df["team"].apply(lambda x : x["shortName"])
    df["team"] = df["team"].apply(lambda x : x["name"])
    
    df = df.drop(columns=["form"], errors= "ignore")

    # changing column names 
    df = df.rename(columns= {"playedGames": "Games",
    "goalsFor" : "Goals_scored",
    "goalsAgainst": "Goals_conceded",
    "goalDifference": "Goal_difference"})

    return df 

