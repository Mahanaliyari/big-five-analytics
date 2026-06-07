import streamlit as st 
import plotly.express as px 
import plotly.graph_objects as go 
from clean_data import cleaner
from fetch_data import leagues
from fetch_data import get_league_code
from fetch_data import fetch_league


# set the titles 
st.title("Football League Dashboard")
st.subheader("Top 10 teams from Europe's Big Five leagues")

# getting user input as dropdown list 
user_input = st.selectbox("Select a league", options = leagues)
st.divider()

# fetch data
league_code = get_league_code(user_input,leagues)
data_dict = fetch_league(league_code)

# clean data
df = cleaner(data_dict)
df_sorted = df.sort_values("Goals_scored", ascending = False)


#charts
def bar_chart(df):
    fig : go.Figure = px.bar(df,
                x = "short_name",
                y = "Goals_scored",
                color = "Goals_scored",
                text = "Goals_scored",
                labels = {"short_name": "Teams", "Goals_scored": "Goals"},
                color_continuous_scale= "oranges",
                title = f"Goal Score per Team -- {user_input}  ",
                height= 550)

    fig.update_layout(showlegend = False,
                    coloraxis_showscale = False,
                    plot_bgcolor = "white",
                    title_font = dict(size = 20))
    
    st.plotly_chart(fig)
    
    
def group_bar_chart(df):
    fig : go.Figure = px.bar(df,
                            x = "short_name",
                            y = ["won", "draw", "lost"],
                            barmode="group", 
                            labels= {"variable": "Result", "short_name": "Team", "value": "Matches"},
                            title = f"Wins, Draws, Losses -- {user_input}",
                            height = 550)
    
    fig.update_layout(title_font = dict(size = 20))
    st.plotly_chart(fig)
    
    
def bar_chart2(df): 
    fig : go.Figure = px.bar(df,
                            x = "short_name",
                            y = "points",
                            color = "points",
                            text = "points",
                            title= f"Points per team -- {user_input}",
                            labels = {"short_name":"Team", "points": "Points"},
                            height= 550)
    
    fig.update_layout(showlegend = False,
                      coloraxis_showscale = False,
                      title_font = dict(size = 20))
    
    st.plotly_chart(fig)
    

def scatter_chart(df):
    fig : go.Figure = px.scatter(df,
                                x = "Goals_conceded",
                                y = "Goals_scored",
                                text = "short_name", 
                                title = f"Attack vs Defence -- {user_input}",
                                size = "points",
                                size_max= 40,
                                color = "points",
                                color_continuous_scale= "reds",
                                height= 550,
                                hover_name= "team")
    
    fig.update_traces(textposition = "top center")
    fig.update_layout(showlegend = False,
                      coloraxis_showscale = False,
                      title_font = dict(size = 20))
    
    
    st.plotly_chart(fig) 
    
        
# placing charts into two seperate columns
col1, col2 = st.columns(2)

with col1: 
    bar_chart(df_sorted)
    group_bar_chart(df)

with col2: 
    scatter_chart(df)
    bar_chart2(df)
    
