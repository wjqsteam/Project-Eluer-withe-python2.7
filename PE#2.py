# python2.7

def Fibonacci():
    numbers = [1,1]
    for i in xrange(1,99):
        if numbers[i] > 100 :
            break
        else:
            a = numbers[i-1] + numbers[i]
            numbers.append(a)
    print numbers
    print "%d" % i


Fibonacci()
