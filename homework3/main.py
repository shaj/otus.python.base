import asyncio
from dataclasses import dataclass
from aiohttp import ClientSession

from urllib.parse import urljoin
from loguru import logger
from models import (
    DB_DSN,
    db,
    User,
    Todo,
    Post,
    Comment,
    Album,
    Photo,
)


BASE_URL = "https://jsonplaceholder.typicode.com/"


@dataclass
class Table:
    Row: db.Model
    url: str


REQUESTS1 = [
    Table(User, "users"),
]

REQUESTS2 = [
    Table(Todo, "todos"),
    Table(Post, "posts"),
    Table(Album, "albums"),
]

REQUESTS3 = [
    Table(Comment, "comments"),
    Table(Photo, "photos"),
]


async def create_record(Row: db.Model, data: dict):
    row: Row = None
    try:
        row = await Row.get(int(data["id"]))
    except Exception:
        pass
    if row is None:
        row = Row()
        row.update_jsonplaceholder(data)
        await row.create()
    # else:
    #     row.update_jsonplaceholder(data)
    #     await row.update().apply()


async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_data(table: Table):
    counter = 1
    logger.info("Start {}", table.url)
    while True:
        data = {}
        async with ClientSession() as session:
            u = urljoin(BASE_URL, str(table.url + "/" + str(counter)))
            data = await fetch_json(session, u)
        if len(data) == 0:
            break
        logger.info("Fetched {}/{}", table.url, counter)
        await create_record(table.Row, data)

        counter += 1
        logger.info("Stored {}/{}", table.url, counter)
    logger.info("End {}. Fetched {} items", table.url, counter)


async def main():
    await asyncio.wait({asyncio.create_task(db.set_bind(DB_DSN))})
    coro1 = asyncio.wait({asyncio.create_task(fetch_data(t)) for t in REQUESTS1})
    await coro1
    coro2 = asyncio.wait({asyncio.create_task(fetch_data(t)) for t in REQUESTS2})
    await coro2
    coro3 = asyncio.wait({asyncio.create_task(fetch_data(t)) for t in REQUESTS3})
    await coro3
    await asyncio.wait({asyncio.create_task(db.pop_bind().close())})


if __name__ == '__main__':
    asyncio.run(main())
