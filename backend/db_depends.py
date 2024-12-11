from .db import SessionLokal


async def get_db():
    db = SessionLokal()
    try:
        yield db
    finally:
        db.close()