import json

from app.storage.database import db_client


async def fill_database(file: str):
    with open(file, "r") as f:
        user_data = json.load(f)

    res = await db_client.insert_many_user_data(user_data)
    return res


async def main():
    res = await fill_database("example.json")
    print(res)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())