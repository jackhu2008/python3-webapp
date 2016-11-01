from ormdb import create_pool, destory_pool
from models import User, Blog, Comment
import asyncio

loop = asyncio.get_event_loop()

@asyncio.coroutine
def test():
    yield from create_pool(loop, host='', user='root', password='', db='webapp')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    yield from u.save()
    yield from destory_pool()

loop.run_until_complete(test())
loop.close()
