timestamp = (3, 30, 2019, 9, 25)
date = format(timestamp[3], '02') + "/"\
    + format(timestamp[4], '02') + "/"\
    + str(timestamp[2])
time = format(timestamp[0], '02') + ":"\
    + format(timestamp[1], '02')
print(date, time)
