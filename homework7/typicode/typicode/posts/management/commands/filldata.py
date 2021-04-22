import asyncio
from dataclasses import dataclass
from aiohttp import ClientSession
from urllib.parse import urljoin

from typing import Any, Optional
from django.core.management.base import BaseCommand
from django.db import models
from posts.models import User, Todo, Post, Comment, Album, Photo


BASE_URL = "https://jsonplaceholder.typicode.com/"

@dataclass
class Table:
    Row: models.Model
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


class Command(BaseCommand):
    help = "Fill database with data from jsonplaceholder.com"
    
    def create_record(self, Row: models.Model, data: dict):
        row: Row = None
        try:
            row = await Row.get(int(data["id"]))
        except Exception:
            pass
        try:
            if row is None:
                row = Row()
                row.update_jsonplaceholder(data)
                await row.create()
        except Exception as e:
            print(e.args[0])
            print("{}  ::  {}", Row.__repr__, repr(data))

    async def fetch_json(self, session: ClientSession, url: str) -> dict:
        async with session.get(url) as response:
            return await response.json()

    async def fetch_data(self, table: Table):
        counter = 1
        print("Start {}", table.url)
        while True:
            data = {}
            async with ClientSession() as session:
                u = urljoin(BASE_URL, str(table.url + "/" + str(counter)))
                data = await self.fetch_json(session, u)
            if len(data) == 0:
                break
            print("Fetched {}/{}", table.url, counter)
            self.create_record(table.Row, data)

            counter += 1
            print("Stored {}/{}", table.url, counter)
        print("End {}. Fetched {} items", table.url, counter)

    async def main(self):
        # await asyncio.wait({asyncio.create_task(db.set_bind(DB_DSN))})
        coro1 = asyncio.wait({asyncio.create_task(self.fetch_data(t)) for t in REQUESTS1})
        await coro1
        coro2 = asyncio.wait({asyncio.create_task(self.fetch_data(t)) for t in REQUESTS2})
        await coro2
        coro3 = asyncio.wait({asyncio.create_task(self.fetch_data(t)) for t in REQUESTS3})
        await coro3
        # await asyncio.wait({asyncio.create_task(db.pop_bind().close())})

    def handle(self, *args: Any, **options: Any) -> Optional[str]:

        Photo.objects.all().delete()
        Album.objects.all().delete()
        Comment.objects.all().delete()
        Post.objects.all().delete()
        Todo.objects.all().delete()
        User.objects.all().delete()
        
        asyncio.run(self.main())

        return 'My first Django command COMPLETE'
    
    
    


