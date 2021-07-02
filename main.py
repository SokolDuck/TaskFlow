from flow import Flow
from task import Task
from time import sleep
from time import time


def task(number):
    print(f"task {number}: start ")
    sleep(0.4)
    print(f"task {number}: end")

def long_task(number):
    print(f"long task {number}: start ")
    for i in range(5):
        print(f"long task {number}: ping ")
        sleep(0.4)
    print(f"long task {number}: end ")


def test0():
    start_time = time()
    tasks = []

    for i in range(5):
        tasks.append(Task(task, i))

    for t in tasks:
        t.run(False)

    for t in tasks:
        t.join()
    
    print(f"Test 0 - Time : {time() - start_time} sec")

def test1():
    flow = Flow()
    start_time = time()

    flow.add_sync(
        Task(task, 1),
        Task(task, 2),
        Task(task, 3),
    )

    flow.print_exec_plan()
    flow.exec()

    print(f"Test 1 - Time : {time() - start_time} sec")

def test2():
    flow = Flow()
    start_time = time()

    flow.add_async(
        Task(task, 2.1),
        Task(task, 2.2),
        Task(task, 2.3),
    )

    flow.print_exec_plan()
    flow.exec()

    print(f"Test 2 - Time : {time() - start_time} sec")
    

def test3():
    flow = Flow()
    start_time = time()

    flow.add_sync(
        Task(task, 1),
    )
    flow.add_infinit(
        Task(long_task, 2)
    )
    flow.add_sync(
        Task(task, 3)
    )

    flow.print_exec_plan()
    flow.exec()

    print(f"Test 3 - Time : {time() - start_time} sec")
    

if __name__ == '__main__':
    
    print("Test 0 \n")
    test0()
    print("\nTest 1 \n")
    test1()
    print("\nTest 2 \n")
    test2()
    print("\nTest 3 \n")
    test3()
    
    