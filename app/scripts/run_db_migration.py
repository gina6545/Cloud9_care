import asyncio

from tortoise import Tortoise

from app.core.config import config


async def main():
    await Tortoise.init(
        db_url=f"mysql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}",
        modules={"models": []},
    )
    conn = Tortoise.get_connection("default")

    try:
        await conn.execute_query("ALTER TABLE llm_life_guides DROP COLUMN generated_content;")
        print("Dropped generated_content")
    except Exception as e:
        print(f"generated_content: {e}")

    await Tortoise.close_connections()


if __name__ == "__main__":
    asyncio.run(main())
