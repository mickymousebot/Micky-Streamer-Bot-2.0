from aiohttp import web
from .stream_routes import routes

#Dont Remove My Credit @Tech_Shreyansh
#This Repo Is By @SmartEdith_Bot 
# For Any Kind Of Error Ask Us In Support Group @Tech_Shreyansh2

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

#Dont Remove My Credit @Tech_Shreyansh
#This Repo Is By @SmartEdith_Bot 
# For Any Kind Of Error Ask Us In Support Group @Tech_Shreyansh2
