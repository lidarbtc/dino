
# 개발 중
# config = 디스코드 안에서 서버 아이피, 포트, 스팀아이디, 플레이어토큰 설정 할 수 있게 하기
# 인게임 명령어 분할( 터렛1 = *sw1 터렛2 = *sw2 )

import asyncio
from cProfile import label
from distutils import errors
from email import message
from http import client
from multiprocessing.dummy import Pool
from pickle import FALSE, TRUE
from socket import socket
import threading
from tkinter import ON
from tkinter.tix import Tree
from tkinter.ttk import Style
from rustplus import RustSocket, CommandOptions, Command, RustMarker
import discord
from discord.ext import commands
from discord.ui import Button, View
from discord.utils import get
import os
import rustplus
from discord import Embed
from rustplus.commands import command
from rustplus.exceptions.exceptions import RequestError
import time
import multiprocessing

intents = discord.Intents.all()

# bot, in-game command prefix
client = commands.Bot(command_prefix='/', intents = intents)
options = CommandOptions(prefix="*")

#rust_socket("ip", "port", player_id, player_token)
socket = RustSocket()

Token = 'token'

switch_list = []
name = []
@client.command()
async def switch(ctx, switch_id):

    # channel id
    channel = client.get_channel(1011889444472758302) 

    # switch_id save
    switch_list.extend([switch_id])
    print(switch_list)

    # command delete 
    await ctx.message.delete()

    # embed switch message on/off
    switch_on_embed = Embed(title='스마트 스위치',description="이 스위치는 스마트 스위치를 제어합니다. \n ```Entity ID: " + switch_id + "``` ```현재 상태 : ON```", colour=discord.Colour.blue()).set_thumbnail(url = "https://cdn.discordapp.com/attachments/1007167310458519602/1007548619299229766/unknown.png")
    switch_off_embed = Embed(title='스마트 스위치',description="이 스위치는 스마트 스위치를 제어합니다. \n ```Entity ID: " + switch_id + "``` ```현재 상태 : OFF```", colour=discord.Colour.blue()).set_thumbnail(url = "https://cdn.discordapp.com/attachments/1007167310458519602/1007548619299229766/unknown.png")
    switch_on_error_embed = Embed(title='스마트 스위치',description="이 스위치는 스마트 스위치를 제어합니다. \n ```Entity ID: " + switch_id + "``` ```현재 켜져있는 상태입니다.```", colour=discord.Colour.blue()).set_thumbnail(url = "https://cdn.discordapp.com/attachments/1007167310458519602/1007548619299229766/unknown.png")
    switch_off_error_embed = Embed(title='스마트 스위치',description="이 스위치는 스마트 스위치를 제어합니다. \n ```Entity ID: " + switch_id + "``` ```현재 꺼져있는 상태입니다.```", colour=discord.Colour.blue()).set_thumbnail(url = "https://cdn.discordapp.com/attachments/1007167310458519602/1007548619299229766/unknown.png")
    
    # button style
    smart_switch_on = Button(label = "ON", style = discord.ButtonStyle.green)
    smart_switch_off = Button(label = "OFF", style = discord.ButtonStyle.red)
    smart_switch_delete = Button(label = "❌")

    # in-game switch command
    @socket.command
    async def sw(Command: command):
        for lists in switch_list:
            status = (await socket.get_entity_info(int(lists))).value
            if status == False:
                await socket.turn_on_smart_switch(int(lists))
                await msg.edit(embed=switch_on_embed)
            elif status == True:
                await socket.turn_off_smart_switch(int(lists))
                await msg.edit(embed=switch_off_embed)

    # discord channel switch on button
    async def smart_switch_on_callback(interaction):
        status = (await socket.get_entity_info(int(switch_id))).value
        if status == False: # if status:
            await interaction.response.defer()
            await socket.turn_on_smart_switch(int(switch_id))
            await msg.edit(embed=switch_on_embed)
        else:
            await msg.edit(embed=switch_on_error_embed)

    # discord channel switch off button
    async def smart_switch_off_callback(interaction):
        status = (await socket.get_entity_info(int(switch_id))).value
        if status == True: # if status:
            await interaction.response.defer()
            await socket.turn_off_smart_switch(int(switch_id))
            await msg.edit(embed=switch_off_embed)
        else:
            await msg.edit(embed=switch_off_error_embed)

    # discord channel switch delete
    async def smart_switch_delete_callback(interaction):
        await msg.delete()

    # button callback
    smart_switch_on.callback = smart_switch_on_callback
    smart_switch_off.callback = smart_switch_off_callback
    smart_switch_delete.callback = smart_switch_delete_callback

    view = View(timeout=None)

    view.add_item(smart_switch_on)
    view.add_item(smart_switch_off)
    view.add_item(smart_switch_delete)

    msg = await channel.send(embed = discord.Embed(title='스마트 스위치',description="이 스위치는 스마트 스위치를 제어합니다. \n ```Entity ID: " + switch_id + "```", colour=discord.Colour.blue()).set_thumbnail(url = "https://cdn.discordapp.com/attachments/1007167310458519602/1007548619299229766/unknown.png"), view=view)


# bradley or heli spawn
async def bradley_spawn(): # 스위치 실행 안됨 
    for e in range(1,10):
        await asyncio.sleep(10)
        if e == 3:
            print("3 = done")
        print(e)
    #events = await socket.get_current_events()
    #for e in events:
    #    if e.type == 3:
    #        await socket.send_team_message("헬기 또는 브래들리가 폭발 했습니다.")
    #        time.sleep(3600)
    #        await socket.send_team_message("브래들리가 스폰하였습니다.")
            
@client.event
async def on_ready():
    print(client.user.name)
    await bradley_spawn()

@client.event
async def test():
    time.sleep(10)
    print("cc")

async def main():
    await socket.connect()

asyncio.run(main()) # 1
client.run(Token) # 3 stop 무한루프