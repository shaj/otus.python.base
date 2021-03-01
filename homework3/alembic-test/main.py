import asyncio
from asyncpgsa import pg
# from sqlalchemy.orm import joinedload

from models import Session, Base, User


def create_record(session_: Session, Row: Base, username: str):
    session = Session()
    row = session.query(Row).filter_by(username=username).first()
    if row is None:
        row = Row(username=username, is_staff=True)
        session.add(row)
    else:
        try:
            row.user_class = str(int(row.user_class) + 1)
        except Exception:
            row.user_class = '0'
    session.commit()
    print(row)
    session.close()


def main():
    # session = Session()
    session = '1'
    # username = "admin"
    # admin = User(username=username, is_staff=True)
    # print(admin)

    # guest = User(username="guest")
    # print(guest)

    create_record(session, User, 'admin')
    create_record(session, User, 'guest')
    create_record(session, User, 'bob')

    # session.add(admin)
    # session.add(guest)
    # session.commit()
    # print(admin)
    # print(guest)
    # print(bob)

    # session.close()


if __name__ == '__main__':
    main()
