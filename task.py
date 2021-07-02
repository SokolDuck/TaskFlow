import threading as th
import asyncio


class Task:
    def __init__(self, job, *args, **kwargs) -> None:
        self.job = job
        self.args = args
        self.kwargs = kwargs
        self.th = th.Thread(target=self.job, args=args, kwargs=kwargs)

    def run(self, join: bool = True) -> None:
        self.th.start()

        if join:
            self.join()

    def join(self) -> None:
        self.th.join()

    def __str__(self) -> str:
        return f"{self.job.__name__} with {self.args}, {self.kwargs}"

    def __repr__(self) -> str:
        return str(self)


class AsyncTask:
    def __init__(self, job, *args, **kwargs) -> None:
        self.job = job
        self.args = args
        self.kwargs = kwargs

    async def run(self, join: bool = True) -> None:
        self.th = asyncio.create_task(
            self.job(*self.args, **self.kwargs)
        )

        if join:
            await self.join()

    async def join(self) -> None:
        await self.th

    def __str__(self) -> str:
        return f"{self.job.__name__} with {self.args}, {self.kwargs}"

    def __repr__(self) -> str:
        return str(self)
