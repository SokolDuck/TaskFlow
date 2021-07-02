from task import AsyncTask, Task


class Flow:
    def __init__(self) -> None:
        self.__flow = {}
        self.__count = 0

    def add_sync(self, *tasks) -> None:
        for t in tasks:
            self.__flow[self.__count] = {
                "tasks": (t,)
            }
            self.__count += 10

    def add_async(self, *tasks) -> None:
        self.__flow[self.__count] = {
            "tasks": tasks
        }
        self.__count += 10

    def add_infinit(self, *tasks) -> None:
        self.__flow[self.__count] = {
            "infin": True,
            "tasks": tasks
        }
        self.__count += 10

    def print_exec_plan(self):
        for k, v in self.__flow.items():
            print(f"{k}: {v.get('tasks')} {'inf' if v.get('infin') else ''}")

    def exec(self):
        running_tasks = []
        
        for _, v in self.__flow.items():
            tasks: tuple[Task] = v.get("tasks")

            for t in tasks:
                t.run(join=False)
                running_tasks.append(t)
            
            if not v.get("infin"):
                for t in tasks:
                    t.join()
            
        for t in running_tasks:
            t.join()


class AsyncFlow:
    def __init__(self) -> None:
        self.__flow = {}
        self.__count = 0

    def add_sync(self, *tasks) -> None:
        for t in tasks:
            self.__flow[self.__count] = {
                "tasks": (t,)
            }
            self.__count += 10

    def add_async(self, *tasks) -> None:
        self.__flow[self.__count] = {
            "tasks": tasks
        }
        self.__count += 10

    def add_infinit(self, *tasks) -> None:
        self.__flow[self.__count] = {
            "infin": True,
            "tasks": tasks
        }
        self.__count += 10

    def print_exec_plan(self):
        for k, v in self.__flow.items():
            print(f"{k}: {v.get('tasks')} {'inf' if v.get('infin') else ''}")

    async def exec(self):
        running_tasks = []
        
        for _, v in self.__flow.items():
            tasks: tuple[AsyncTask] = v.get("tasks")

            for t in tasks:
                await t.run(join=False)
                running_tasks.append(t)
            
            if not v.get("infin"):
                for t in tasks:
                    await t.join()
            
        for t in running_tasks:
            await t.join()