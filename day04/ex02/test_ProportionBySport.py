from FileLoader import FileLoader
from ProportionBySport import proportionBySport

def test_proportionBySport():
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')

    assert proportionBySport(data, 2004, 'Tennis', 'F') == 0.019302325581395347

    assert proportionBySport(data, 1992, 'Cycling', 'M') == 0.04710008768633346

    assert proportionBySport(data, 1920, 'Judo', 'M') == 0
