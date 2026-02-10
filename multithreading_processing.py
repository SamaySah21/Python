import threading
import time

###################### multithreading example#########################
def square_num(n):
    for i in range(n):
        print(f"Square of {n} is {n*n}")
        if i % 2 == 0:
            print(f"Even: {i}")
        time.sleep(2)

# def count_num():
#     for i in range(5):
#         print(i)
#         time.sleep(1)

# def count_letter():
#     for letter in ['a', 'b', 'c', 'd', 'e']:
#         print(letter)
#         time.sleep(1.5)

# if __name__ == "__main__":
#     #normal execution (only one function runs at a time)
#     # count_num()
#     # count_letter()

#     #threading execution (both functions run concurrently)
#     t1 = threading.Thread(target=count_num) 
#     t2 = threading.Thread(target=count_letter)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

#     print("We can check in Task Manager -> Processes -> only on python.exe(interpretor) is running ")
    
###################### multiprocessing example#########################
import multiprocessing
def square_num_mp(n):
    for i in range(n):
        print(f"Square of {n} is {n*n}")
        time.sleep(2)

def cube_num(n):
    for i in range(n):
        print(f"Cube of {n} is {n*n*n}")
        time.sleep(3)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=square_num_mp, args=(15,))
    p2 = multiprocessing.Process(target=cube_num, args=(15,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("We can check in Task Manager -> Background Processes -> 3 processes are running (1 is main.py i.e \
          primary process and 2 are child processes for square_num and cube_num functions) ")
    
    
from multiprocessing import Pool
import os

def burn_cpu(n):
    total = 0
    for i in range(50000000):
        total += i
    return total

if __name__ == "__main__":
    with Pool(processes=6) as p:
        p.map(burn_cpu, range(6))
    


