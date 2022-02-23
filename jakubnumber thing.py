#number = int(input ("starting number:"))

# import threading
import time
import multiprocessing
def cpu_destroyer(start, end):
    for i in range(start, end):
        number = i
        # print (number, end = " ")
        while number > 1:
            if number % 2 > 0:
                number = number * 3 + 1
            else:
                number = number / 2
        else:
            if number != 1:
                print("###",number)
    print("Tryed Range", start, " to ", end)


def calc_func_(start):
    for i in range(start, start + 10000):
        number = i

        # print (number, end = " ")
        while number > 1:
            if number % 2 > 0:
                number = number * 3 + 1
            else:
                number = number / 2
        else:
            if number != 1:
                print("###",number)
    print("Tryed Range", start, " to ", start + 10000)

def multiprocessing_func(x):
    #time.sleep(2)
    calc_func_(x)

if __name__ == '__main__':
    exponent = 19
    mode = input("Do you want it go go forever? (y)es, (n)o? Press c to compare Speed\n-")
    if mode == "y":
        for exponent in range (0,64):
            max_numb = 2** exponent
            print("\n\n\nTying from 0 to 2 ^", exponent)

            starttime = time.time()
            pool = multiprocessing.Pool()
            pool.map(multiprocessing_func, range(0, max_numb, 10000))
            pool.close()
            print('That took {} seconds'.format(time.time() - starttime))
    elif mode =="c":
        print("Ttrying single threaded solution...")
        starttime = time.time()
        cpu_destroyer(0, 2**exponent)
        print('That took {} seconds'.format(time.time() - starttime))
        print()
        print("Trying Multythreaded / multicore process ...")
        max_numb = 2 ** exponent
        print("\n\n\nTying from 0 to 2 ^", exponent)

        starttime = time.time()
        pool = multiprocessing.Pool()
        pool.map(multiprocessing_func, range(0, max_numb, 10000))
        pool.close()
        print('That took {} seconds'.format(time.time() - starttime))

    else:

        max_numb = 2 ** exponent
        print("\n\n\nTying from 0 to 2 ^", exponent)
        
        starttime = time.time()
        pool = multiprocessing.Pool()
        pool.map(multiprocessing_func, range(0, max_numb, 10000))
        pool.close()
        print('That took {} seconds'.format(time.time() - starttime))