# Testing Timer class by timing differetn ways of calculating 
# the fibonacci sequence


from timer import Timer

def recursive_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fib(n - 1) + recursive_fib(n - 2)

def memoization_fib(n, mem = {0: 0, 1: 1}):
    if n in mem:
        return mem[n]
    else:
        mem[n] = memoization_fib(n - 1) + memoization_fib(n - 2)
        return mem[n]

def iterative_fib(n):
    last_two = [0, 1]
     
    while n > 1:
        temp = sum(last_two)
        last_two[0] = last_two[1]
        last_two[1] = temp
        n -= 1
    return last_two[n]




def main():
    t = Timer()

    print '\n'

    t.start()
    print recursive_fib(25)
    t.end()

    print '\n'

    t.start()
    print memoization_fib(25)
    t.end()

    print '\n'

    t.start()
    print iterative_fib(25)
    t.end()
    t.configure('minutes')
    t.lastTime()
    t.configure('hours')
    t.lastTime()



if __name__ == "__main__":
    main()



