import asyncio
import time
import nsq


writer = nsq.Writer(['127.0.0.1:4150'])


def finish_pub(conn, data):
    print(data)


async def main():
    print('seed')
    writer.pub(
        'nsq_reader',
        bytes(time.strftime('%H:%M:%S'), encoding='utf8'),
        finish_pub
    )
    await asyncio.sleep(2)
    await main()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()