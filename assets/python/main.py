import discord
from discord.ext import commands
from flask import Flask, render_template

app = Flask(__name__)

intents = discord.Intents.default()
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'Bot ID: {bot.user.id}')

@app.route('/')
def home():
    guild_count = len(bot.guilds)
    return render_template('index.html', guild_count=guild_count)

if __name__ == '__main__':
    bot.run('')


