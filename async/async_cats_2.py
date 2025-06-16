import httpx
import requests  # requests - make requests via python
import time
import uuid
import asyncio


def time_decorator(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        func(*args, **kwargs)
        time_end = time.time()
        print(time_end - time_start)

    return wrapper()


def write_file(data):
    file_name = str(uuid.uuid4()) + '.jpg'
    with open(file_name, 'wb') as f:
        f.write(data)


async def get_res(url, client: httpx.AsyncClient):
    # httpx.AsyncClient is an asynchronous HTTP client provided by the httpx library, which is similar to requests but supports asynchrony with async/await.
    res = await client.get(url, follow_redirects=True)
    write_file(res.read())


async def start():  # Asynchronous function that will be launched in the event loop
    url = 'https://loremflickr.com/320/240/dog'  # URL of the image to download
    tasks = []  # List where we will collect tasks (coroutines)

    async with httpx.AsyncClient() as client:  # Create an asynchronous HTTP client that can be used inside the event loop
        for _ in range(50):  # 50 times
            task = asyncio.create_task(get_res(url, client))  # Create an asynchronous task to download the image
            tasks.append(task)  # Add the task to the list
        await asyncio.gather(*tasks)  # Wait for all tasks to complete in parallel


@time_decorator
def main():
    asyncio.run(start())


main()
