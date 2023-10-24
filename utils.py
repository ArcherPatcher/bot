import aiofiles
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from states import user_input
import logging
import json
import requests


async def check_user(user_input):
    try:
        async with aiofiles.open('users.json', mode='r') as f:
            contents = await f.read()
            data = json.loads(contents)
            
            # Поиск пользователя по имени
            user = next((user for user in data if user('name') == user_input), None)
            
            if user:
                return user
            else:
                return None
    except Exception as e:
        logging.error(e)
        return None                  
                            
             
                           