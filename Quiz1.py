import asyncio


@asyncio.coroutine
def generate_nums():
    num = 1
    while True:
        yield num
        num = num + 2

nums = generate_nums()

for i in nums:
    print(i)

    if i > 50:
        break




