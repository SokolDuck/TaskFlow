import asyncio
from flow import AsyncFlow, Flow
from task import AsyncTask, Task
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


async def atask(number):
    print(f"task {number}: start ")
    await asyncio.sleep(0.4)
    print(f"task {number}: end")

async def along_task(number):
    print(f"long task {number}: start ")
    for i in range(5):
        print(f"long task {number}: ping ")
        await asyncio.sleep(0.4)
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


async def async_test1():
    flow = AsyncFlow()
    start_time = time()

    flow.add_sync(
        AsyncTask(atask, 1),
        AsyncTask(atask, 2),
        AsyncTask(atask, 3),
    )

    flow.print_exec_plan()
    await flow.exec()

    print(f"AsyncTest 1 - Time : {time() - start_time} sec")

async def async_test2():
    flow = AsyncFlow()
    start_time = time()

    flow.add_async(
        AsyncTask(atask, 2.1),
        AsyncTask(atask, 2.2),
        AsyncTask(atask, 2.3),
    )

    flow.print_exec_plan()
    await flow.exec()

    print(f"AsyncTest 2 - Time : {time() - start_time} sec")
    
async def async_test3():
    flow = AsyncFlow()
    start_time = time()

    flow.add_sync(
        AsyncTask(atask, 1),
    )
    flow.add_infinit(
        AsyncTask(along_task, 2)
    )
    flow.add_sync(
        AsyncTask(atask, 3)
    )

    flow.print_exec_plan()
    await flow.exec()

    print(f"AsyncTest 3 - Time : {time() - start_time} sec")
    

if __name__ == '__main__':
    
    print("Test 0 \n")
    test0()
    print("\nTest 1 \n")
    test1()
    print("\nTest 2 \n")
    test2()
    print("\nTest 3 \n")
    test3()

    print("\nAsyncTest 1 \n")
    asyncio.run(async_test1())
    print("\nAsyncTest 2 \n")
    asyncio.run(async_test2())
    print("\nAsyncTest 3 \n")
    asyncio.run(async_test3())
    
    