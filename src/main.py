import flask
import discord
import os
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

from bot_ping import bot_ping
from server import run_server


# ==[ DISCORD CODE ]===========================================================

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_BOT_TOKEN')


class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('.'),intents=discord.Intents.all())
    
    async def on_ready(self):
        print(f'Logged in as {self.user.name}') # ----------------------- add timestamp later 
        synced = await self.tree.sync()
        custom_status = discord.Game(name="with herself")
        await client.change_presence(activity=custom_status,status=discord.Status.idle)
        print(f'Slash commands synced: {len(synced)}')

client = Client()



                #PING
@client.tree.command(name='ping',description='Check the bot\'s present latency')
async def ping_check(interaction:discord.Interaction):
    await bot_ping(interaction,client)
    return



run_server()
client.run(DISCORD_TOKEN)
