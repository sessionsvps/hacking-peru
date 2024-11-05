from dotenv import load_dotenv
from telethon.sync import TelegramClient, events
import os
import json
import asyncio

# async def getListOfGroups(client):
#     try:
#         dialogs = await client.get_dialogs()
#         groups_info = []
#         for dialog in dialogs:
#             if dialog.is_group or dialog.is_channel:  # Filtra los grupos y canales
#                 group_info = {'group_id': dialog.id, 'group_name': dialog.title}
#                 groups_info.append(group_info)
#                 Imprimir el nombre y el ID del grupo
#                 print(f"Grupo: {dialog.title}, ID: {dialog.id}")
#         return groups_info
#     except Exception as e:
#         print(f"Error: {e}")
#         return []

async def getListOfGroups(client):
    try:
        dialogs = await client.get_dialogs()
        groups_info = []
        for dialog in dialogs:
            if dialog.is_group or dialog.is_channel:
                entity = await client.get_entity(dialog.id)
                can_send_messages = entity.default_banned_rights is None or not entity.default_banned_rights.send_messages
                if can_send_messages:
                    group_info = {'group_id': dialog.id, 'group_name': dialog.title}
                    groups_info.append(group_info)

        return groups_info
    except Exception as e:
        print(e)
        return []
async def getMessagesFromGroup(client, group_id):
    try:
        all_messages = []
        async for message in client.iter_messages(group_id):
            try:
                all_messages.append(message)
            except:
                pass
        return all_messages
    except Exception as e:
        print(e)
        return []

async def logUserBot():
    load_dotenv()
    api_id = 29113526
    api_hash = "7ac7e008d1e4f5c6c88a26a29bdde89e"
    phone_number = "51994578575"
    session_name = "bot_spammer"
    client = TelegramClient(session_name, api_id, api_hash)
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Ingrese el código de verificación: '))
    await client.send_message("@spmhackperu", f'<b>Bot encendido</b>', parse_mode="HTML")
    spammer_group = -4553286692

    while True:
        groups_info = await getListOfGroups(client)
        messages_list = await getMessagesFromGroup(client, spammer_group)

        try:
            await client.send_message("@spmhackperu", f"<b>CANTIDAD DE MENSAJES CONSEGUIDOS PARA PUBLICAR</b> <code>{len(messages_list)-1}</code>",parse_mode="HTML")
        except:
            pass
            
        try:
            for i in groups_info:
                if i['group_name'] not in ["Spam","Spam 2024","RESPALDO🇵🇪BINS PERU","➳𝒀𝑨𝑷𝑬 𝑫𝑬 𝑬𝑺𝑻𝑨𝑭𝑨𝑫𝑶𝑹𝑬𝑺 ✧","QUEMANDO ESTAFADORES","𝐏𝐄𝐑Ú 𝐀𝐘𝐔𝐃𝐀","Referencias Elmer 💸","🎭 CANAL MUNDO STREAMING PERÚ 🇵🇪","TU MARKETPLACE"]:
                    j=0
                    for message_spam in messages_list:
                        j+=1
                        resultado = True
                        try:
                            await client.forward_messages(i["group_id"], message_spam)
                        except Exception as error:
                            await client.send_message("@spmhackperu", f'<b>Error enviando mensajes a {i["group_id"]}</b> - <code>{i["group_name"]}<code>\nCausa:{error}',parse_mode="HTML")
                            resultado = False
                        if resultado:
                            await client.send_message("@spmhackperu", f'<b>Mensaje enviado a {i["group_id"]}</b> - <code>{i["group_name"]}</code>',parse_mode="HTML")  
                        await asyncio.sleep(25)
                        if j==2: break
            await client.send_message("@spmhackperu", f'<b>RONDA ACABADA</b>', parse_mode="HTML")
            await asyncio.sleep(100) 
        except:
            pass


if __name__ == "__main__":
    asyncio.run(logUserBot())
