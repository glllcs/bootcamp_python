import pandas as pd


def proportionBySport(
    df: pd.DataFrame,
    year: int,
    sport: str,
    gender: str,
) -> float:
    """
    The function returns a float corresponding to the proportion (percentage)
    of participants who played the given sport among the participants of the
    given gender.
    """
    df.drop_duplicates(subset=['ID', 'Year', 'Sport'], inplace=True)
    gender_in_year = df[(df['Sex'] == gender) & (df['Year'] == year)]
    if len(gender_in_year) == 0:
        return 0
    gender_in_sport_in_year = gender_in_year[gender_in_year['Sport'] == sport]
    return len(gender_in_sport_in_year) / len(gender_in_year)
