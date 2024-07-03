from environs import Env
from data.connector import select_admins, select_admins_off
import asyncio

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS =[5944280734]+select_admins_off()
async def get_admins():
    global ADMINS
    ADMINS += await select_admins()

def offline_get_admins():
    ADMINS =[5944280734]+select_admins_off()
    return ADMINS