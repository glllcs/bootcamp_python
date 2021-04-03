import pandas as pd
from typing import Dict


def howManyMedals(df: pd.DataFrame, name: 'str') -> Dict[int, Dict[str, int]]:
    """
    Returns a dictionary of dictionaries giving the number and type of medals
    for each year during which the participant won medals.
    """
    player_df = df[df['Name'] == name]
    year_medal = {}
    for __, year in player_df['Year'].drop_duplicates().items():
        year_df = player_df[player_df['Year'] == year]
        year_medal[year] = {}
        medals = ('Gold', 'Silver', 'Bronze')
        for medal in medals:
            year_medal[year][medal[0]] = len(year_df[year_df['Medal'] == medal])
    
    return year_medal
