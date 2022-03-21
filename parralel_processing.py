import multiprocessing
import os

print(multiprocessing.cpu_count())   #8 i.e i have 8 cores CPU

def cube(num):
    print(os.getpid())
    print(f"cube of {num} is {num * num *num}")

def sqr(num):
    print(os.getpid())
    print(f"Square of {num} is {num * num}")

cube(2)
sqr(2)

# till here process id will be same for above os.getpid()

# now creating 2 process which will run on 2 cores simultaneously

p1 = multiprocessing.Process(target=cube, args = (3, ))
p2 = multiprocessing.Process(target=sqr, args = (5, ))

# to start processes
p1.start()
p2.start()

# to check whether processes are running
print(print(p1.is_alive()))
print(print(p2.is_alive()))

# join command will completed only when p1 and p2 is completed
p1.join()
p2.join()

print("Process Completed")