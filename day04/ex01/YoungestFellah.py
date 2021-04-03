import pandas as pd
from typing import Dict


def youngestFellah(df: pd.DataFrame, year: int) -> Dict[str, float]:
    """
	The function returns a dictionary containing the age of the youngest woman
	and man who took part in the Olympics on that year.
	"""
    men_in_year = df[(df['Year'] == year) & (df['Sex'] == 'M')]
    youngest_man = men_in_year['Age'].min()

    women_in_year = df[(df['Year'] == year) & (df['Sex'] == 'F')]
    youngest_woman = women_in_year['Age'].min()

    youngest_fellah = {
        'yougest_woman': youngest_woman,
        'youngest_man': youngest_man,
    }

    return youngest_fellah
