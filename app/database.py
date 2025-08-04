import asyncpg

DB_NAME = "bookstore_db"
DB_USER = "store_user"
DB_PASSWORD = "store_pass"
DB_HOST = "db"
DB_PORT = 5432

async def get_db_pool():
    return await asyncpg.create_pool(
        user=DB_USER, password=DB_PASSWORD, database=DB_NAME, host=DB_HOST, port=DB_PORT
    )

# Pool is created on app startup
db_pool = None

async def get_connection():
    global db_pool
    if db_pool is None:
        db_pool = await get_db_pool()
    return db_pool
