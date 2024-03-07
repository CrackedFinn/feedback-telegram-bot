import os
import asyncio
import aiomysql
from aiomysql import Error
from dotenv import load_dotenv

load_dotenv()
# - - - - - - - - - - #
loop = asyncio.get_event_loop()


async def connect_db():
    try:
        connection = await aiomysql.connect(
            host=os.getenv("HOST"),
            port=24021,
            user=os.getenv("DB_USERNAME"),
            password=os.getenv("PASSWORD"),
            db=os.getenv("DATABASE"),
            loop=loop,
        )

        if connection:
            return connection
        else:
            raise Exception("Database is not connected")

    except Error as e:
        print("Error while connecting to MySQL", e)


async def get_cursor():
    global mydb
    try:
        await mydb.ping(reconnect=True)
    except Error:
        mydb = loop.run_until_complete(connect_db())
    return mydb.cursor()


mydb = loop.run_until_complete(connect_db())


# - - - - - - - - - - #


async def BanUser(UserIDToBan):
    async with await get_cursor() as cur:
        sql = "INSERT INTO SupportBotIDBan (TelegramUserID) VALUES (%s)"
        val = (UserIDToBan,)
        await cur.execute(sql, val)
        await mydb.commit()


async def CheckUser(uid):
    async with await get_cursor() as cur:
        sql = "SELECT * FROM SupportBotIDBan WHERE TelegramUserID = %s"
        val = (uid,)
        await cur.execute(sql, val)
        myresult = await cur.fetchall()
        return myresult
