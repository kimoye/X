import os, asyncio, time                    #function modules in build-in libary
import logging                              #debuging modules in build-in libary
from aiohttp import web                     #function modules in unoffical libary


async def l_init(loop):                     #l_init means lispha(my sever's name) init
    lispha = web.Application()              #server's name
    await loop.create_server(lispha.make_handler(), '127.0.0.1', 9000)       #他妈的创建服务器也用异步？
    print('listening on port: 9000')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    #一直轮询协程,除非主动终止
    loop.run_forever(l_init(loop))



    