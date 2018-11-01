import orm 
import asyncio
from models import User

async def test(loop):
	await orm.create_pool(loop,user="root",password="root",database='webpy')
	
	u = User(name="admin1",email="408043727@qq.com",password='1234567890',image='about:blank')
	
	await u.save()
	
if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(test(loop))
	print('Test finished.')
	loop.close()