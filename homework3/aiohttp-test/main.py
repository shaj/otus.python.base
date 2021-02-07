#!/bin/env python3

import asyncio
from dataclasses import dataclass
from aiohttp import ClientSession

from urllib.parse import urljoin
from pprint import pprint
from loguru import logger


@dataclass
class ServTemplate:
    name: str
    url: str
    range_: tuple[int, int]


@dataclass
class Service:
    name: str
    url: str
    data: dict


REQUESTS = [
    ServTemplate("Post", "https://jsonplaceholder.typicode.com/posts/", (1, 99)),
]


async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_data(service: Service):
    logger.info("Start {}", service.name)
    async with ClientSession() as session:
        service.data = await fetch_json(session, service.url)
    logger.info("End {}", service.name)


async def pull_data():
    services = []
    for srv in REQUESTS:
        for item_id in range(srv.range_[0], srv.range_[1]):
            services.append(Service(' '.join((srv.name, str(item_id))), urljoin(srv.url, str(item_id)), None))
    logger.info('Prepared {} services'.format(len(services)))
    logger.info('service[0] {}'.format(services[0]))
    coro = asyncio.wait(
        {
            asyncio.create_task(fetch_data(service)) for service in services
        },
        # timeout=5,
        # return_when=asyncio.FIRST_COMPLETED,
    )
    await coro

    pprint(services[0].data)


def main():
    print('\n\n\n')
    logger.info("Starting")
    result = asyncio.run(pull_data())
    logger.info("Result: {}", result)
    print('\n\n~\n')


if __name__ == '__main__':
    main()
