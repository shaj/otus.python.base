import asyncio
from loguru import logger
from models import DB_DSN, db, User


async def create_record(Row: db.Model, username: str):
    logger.info('Start for name "{}"', username)
    row: Row = await Row.query.where(Row.username == username).gino.first()
    logger.info('Retreive "{}"', username)
    print(type(row), row)
    if row is None:
        row = Row(username=username, is_staff=True)
        await row.create()
    else:
        try:
            counter = row.user_class
            counter = str(int(counter) + 1)
        except Exception:
            counter = '0'
        finally:
            await row.update(user_class=counter).apply()
    print(row)
    logger.info('End "{}"', username)


async def main():
    await asyncio.wait({asyncio.create_task(db.set_bind(DB_DSN))})
    coro = asyncio.wait({asyncio.create_task(create_record(User, n)) for n in ['john', 'admin', 'guest', 'bob']})
    await coro
    await asyncio.wait({asyncio.create_task(db.pop_bind().close())})


if __name__ == '__main__':
    asyncio.run(main())
