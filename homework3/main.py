#!/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
from loguru import logger
from random import randint


async def baz(a):
    logger.info('Start baZ')
    await asyncio.sleep(4)
    logger.info('End baZ')


async def eggs(a):
    logger.info('Start eggs')
    await asyncio.sleep(3)
    logger.info('End eggs')


async def foo(a):
    logger.info('Start foo')
    await asyncio.sleep(2)
    logger.info('End foo')


async def bar(a):
    logger.info('Start bar')
    await asyncio.sleep(1)
    logger.info('End bar')


async def spam(t: float):
    logger.info(f'Start spam {t}')
    await asyncio.sleep(t)
    logger.info(f'End spam {t}')


async def run_main():
    logger.info("Starting main")
    # tasks = [foo, bar]
    # wait_tasks = asyncio.wait({asyncio.create_task(t(1)) for t in tasks})
    # more_tasks = asyncio.wait(
    #     {
    #         asyncio.create_task(t) for t in [baz(2), eggs(3)]
    #     }
    # )
    # logger.info("Created tasks")
    # await wait_tasks
    # logger.info("Middle of the room")
    # await asyncio.wait({asyncio.create_task(t(1)) for t in tasks})
    # await more_tasks

    tasklist = [float(randint(10, 50) / 10.0) for _ in range(100)]
    
    coro = asyncio.wait(
        {asyncio.create_task(spam(t)) for t in tasklist},
        return_when=asyncio.FIRST_COMPLETED,
    )
    await coro
    logger.info("End tasks")


def main():
    asyncio.run(run_main())


if __name__ == '__main__':
    main()
