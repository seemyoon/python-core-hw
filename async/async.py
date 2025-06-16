import asyncio


async def print_num(time):
    num = 1
    while True:
        text = ''
        if time < 1: text = ' count'

        print(f'{num}={text}')
        num += 1
        await asyncio.sleep(time)


async def main():
    task_1 = asyncio.create_task(print_num(1))
    task_2 = asyncio.create_task(print_num(0.1))

    await asyncio.gather(task_1, task_2)


asyncio.run(main())
