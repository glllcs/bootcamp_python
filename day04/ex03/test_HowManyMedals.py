from FileLoader import FileLoader
from HowManyMedals import howManyMedals


def test_howManyMedals__one():
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')
    expected_dict = {
        1992: {
            'G': 1,
            'S': 0,
            'B': 1
        },
        1994: {
            'G': 0,
            'S': 2,
            'B': 1
        },
        1998: {
            'G': 0,
            'S': 0,
            'B': 0
        },
        2002: {
            'G': 2,
            'S': 0,
            'B': 0
        },
        2006: {
            'G': 1,
            'S': 0,
            'B': 0
        },
    }
    assert howManyMedals(data, 'Kjetil Andr Aamodt') == expected_dict


def test_howManyMedals__two():
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')
    expected_dict = {2004: {'G': 0, 'S': 1, 'B': 0}}
    assert howManyMedals(data, 'Tamila Rashidovna Abasova') == expected_dict
