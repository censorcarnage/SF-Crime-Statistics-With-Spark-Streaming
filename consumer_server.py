import asyncio

from confluent_kafka import Consumer

async def consumeCallDetails(topic_name):
    conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'details_consumer',
        'auto.offset.reset': 'earliest'
    }
    consumer = Consumer(conf)
    consumer.subscribe([topic_name])
    while 1:
        messages = consumer.consume(1, timeout=1)
        for message in messages:
            if message is None:
                print('No Message Detected...\n')
            elif message.error() is not None:
                print(f'MESSAGE WITH ERROR: {message.error()}\n')
            else:
                print(f'{message.value()}\n')
        await asyncio.sleep(1)
        
try:
    asyncio.run(consumeCallDetails("com.department.police.calls.details"))
except Exception as e:
    print(e)