from pyexectime.inspector import PyExecTime

with PyExecTime():
    for i in range(10000):
        print(i, end = ' ')

# as of above example we can make the execution time calculation for any of your code by using "with PyExecTime():"