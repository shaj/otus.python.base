#!/bin/env python3

import asyncio
from dataclasses import dataclass
from aiohttp import ClientSession

from urllib.parse import urljoin
from pprint import pprint
from loguru import logger

from models import (
    Session,
    Base,
    User,
    Todo,
    Post,
    Comment,
    Album,
    Photo,
)


BASE_URL = "https://jsonplaceholder.typicode.com"


@dataclass
class ServTemplate:
    name: str
    table: Base


REQUESTS = [
    ServTemplate("users", User),
    ServTemplate("todos", Todo),
    ServTemplate("posts", Post),
    ServTemplate("comments", Comment),
    ServTemplate("albums", Album),
    ServTemplate("photos", Photo),
]


async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_data(service: ServTemplate):
    logger.info("Start {}", service.name)
    url = urljoin(BASE_URL, service.name)
    item_id = 0
    data: dict = None
    while True:
        async with ClientSession() as session:
            data = await fetch_json(session, urljoin(url), str(item_id))
        if len(data) == 0:
            break

        dbSession = Session()
        record = dbSession.query(service.table).filter(service.table.id.ilike(data["id"])).first()
        record.updateFromJson(data)
        dbSession.commit()
        dbSession.close()

    logger.info("End {}", service.name)


async def pull_data():
    coro = asyncio.wait(
        {
            asyncio.create_task(fetch_data(service)) for service in REQUESTS
        },
        # timeout=5,
        # return_when=asyncio.FIRST_COMPLETED,
    )
    await coro


def main():
    print('\n\n\n')
    logger.info("Starting")
    result = asyncio.run(pull_data())
    logger.info("Result: {}", result)
    print('\n\n~\n')


if __name__ == '__main__':
    main()
