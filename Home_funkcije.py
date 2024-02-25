
import db_funkcije
import os
import websockets
import asyncio
def Home_screen(user):
    db_funkcije.Zaglavlje(user)
    Ispis_funkcija_aplikacije()


def Ispis_funkcija_aplikacije():
    print(60*"=")
    print(5*"-"+"> "+"Send message to: <msg>")
    print(5*"-"+"> " + "Create directory: <mkdir>")
    print(5 * "-" + "> " + "Remove directory: <rmdir>")
    print(5 * "-" + "> " + "Create group: <mkgrp>")
    print(5 * "-" + "> " + "Remove group: <rmgrp>")
    print(5 * "-" + "> " + "Share : <shr>")
    print(5 * "-" + "> " + "Account status: <stat>")
    print(5 * "-"+"Upload File: <upload>")
    print(5 * "-" + "> " + "Inbox: <ibox>")
    print(5 * "-" + "> " + "for help time <option> --help ")


#Ovaj dio definitivno treba nauciti sto znaci i sto je
    async def echo(websocket, path):
        async for message in websocket:
            await websocket.send(message)

    start_server = websockets.serve(echo, "localhost", 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

    async def send_message():
        async with websockets.connect("ws://localhost:8765") as websocket:
            await websocket.send("Ovo je testna poruka")
            response = await websocket.recv()
            print("Primljen odgovor od servera:", response)

    asyncio.get_event_loop().run_until_complete(send_message())