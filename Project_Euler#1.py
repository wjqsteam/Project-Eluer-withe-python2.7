#python2.7
def f():
     s=0
     for i in xrange(0,1000):
         if i % 3 ==0 or i % 5 ==0:
             print "%d\n" % i
             s += i
     print "%d" % s

f()
