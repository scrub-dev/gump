import asyncio

async def execute(service) -> bool :
    await asyncio.sleep(1)
    return True