#!/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
from loguru import logger


async def baz():
    logger.info('Start baZ')
    await asyncio.sleep(3)
    logger.info('End baZ')


async def eggs():
    logger.info('Start eggs')
    await asyncio.sleep(2)
    logger.info('End eggs')


async def foo():
    logger.info('Start foo')
    await asyncio.sleep(2)
    logger.info('End foo')


async def bar():
    logger.info('Start bar')
    await asyncio.sleep(1)
    logger.info('End bar')


async def run_main():
    logger.info("Starting main")
    tasks = [foo(), bar()]
    wait_tasks = asyncio.wait({asyncio.create_task(t) for t in tasks})
    more_tasks = asyncio.wait(
        {
            asyncio.create_task(t) for t in [baz(), eggs()]
        }
    )
    logger.info("Created tasks")
    await wait_tasks
    await more_tasks
    logger.info("End tasks")


def main():
    asyncio.run(run_main())


if __name__ == '__main__':
    main()
