import flask
import discord
from discord import app_commands
from discord.ext import commands

from bot_ping import bot_ping


# ==[ DISCORD CODE ]===========================================================

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



# ==[ FLASK CODE ]===========================================================

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def keep_running():
    if flask.request.method == "GET":
        return flask.jsonify({ "status": "success", "data": "successfully called this API." }), 200
    else:
        return flask.jsonify({ "status": "failure", "data": "only GET requests supported" }), 405

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
