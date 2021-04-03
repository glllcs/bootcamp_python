from FileLoader import FileLoader

loader = FileLoader()
data = loader.load("../resources/athlete_events.csv")
loader.display(data, 12)
loader.display(data, -12)