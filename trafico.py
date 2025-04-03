import asyncio
 
async def mover_vehiculo(vehiculo):
    while True:
        vehiculo.mover()
        await asyncio.sleep(0.1)  # Ajusta el intervalo según la simulación
 
async def cambiar_estado_semáforo(semáforo):
    while True:
        semáforo.cambiar_estado()
        await asyncio.sleep(5)  # Ejemplo: cambiar cada 5 segundos
 
async def main_simulacion(vehiculos, semaforos):
    tareas = [mover_vehiculo(v) for v in vehiculos] + [cambiar_estado_semáforo(s) for s in semaforos]
    await asyncio.gather(*tareas)
 
# Luego, en el bloque principal:
# asyncio.run(main_simulacion(lista_de_vehiculos, lista_de_semaforos))
 