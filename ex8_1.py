#Create loop that will print time of execution of work() function a 1000 times
import time

def work():
    for i in xrange(1,100000):
        a = (i**.5 + i**2)/i**.3

if __name__ == '__main__':
    for i in xrange(1000):
        print 'Execution started at', time.clock()
        t1 = time.time()
        work()
        print 'Iteration number: %s\n' %i, 'Execution time equals: %s.sec' %(time.time() - t1)
