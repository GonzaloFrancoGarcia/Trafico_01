import asyncio
import aio_pika
 
async def enviar_evento(mensaje, queue_name):
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    async with connection:
        channel = await connection.channel()
        await channel.default_exchange.publish(
            aio_pika.Message(body=mensaje.encode()),
            routing_key=queue_name,
        )