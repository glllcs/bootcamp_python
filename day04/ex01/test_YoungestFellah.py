from FileLoader import FileLoader
from YoungestFellah import youngestFellah


def test_youngestFellah():
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')
    assert youngestFellah(data, 2004) == {
        'yougest_woman': 13.0,
        'youngest_man': 14.0,
    }
