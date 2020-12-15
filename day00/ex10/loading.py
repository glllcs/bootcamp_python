from time import sleep
import time


def ft_progress(listy, length=20, printEnd="\r"):
    total = len(listy)
    start = time.time()
    wid = len(str(abs(total)))

    def printProgressBar(i, time):
        percent = ("{0:3.0f}").format(100 * (i / float(total)))
        filledLength = int(length * i // total)
        bar = ''
        if filledLength > 0:
            bar = '=' * (filledLength - 1) + '>'
        bar += ' ' * (length - filledLength)
        try:
            eta = round(time + (total - i) * (time / i), 2)
        except ZeroDivisionError:
            eta = '????'
        time = round(time, 2)
        print(f'\rETA: {eta:5.4}s [{percent}%] [{bar}] {i:{wid}}/{total}'
              f' | elapsed time {time}s', end=printEnd)
    # Initial Call
    printProgressBar(0, time=0.0)
    # Update Progress Bar
    for i, item in enumerate(listy):
        yield item
        end = time.time()
        printProgressBar(i + 1, time=end-start)
    # Print New Line on Complete
    print()


listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += (elem)
    sleep(.005)
print()
print(ret)
