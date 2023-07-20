'''

v1 Shuffle Command: Shuffles the teams randomly, requires 6, 8, 10 names

Developers:

'Holy Morals'
'Digitalpain'

'''


import random
import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

# Set the "/" prefix

bot = commands.Bot(command_prefix="/", intents=intents)

# Bring the bot online

@bot.event
async def on_ready():
    print(f"{bot.user.name} online")

@bot.slash_command()
async def shuffle(ctx, *, names: str):
    team_names = names.split(",")
    team_size = len(team_names)
    if team_size not in [4, 6, 8, 10]:
        await ctx.send("Please enter 4, 6, 8, or 10 names separated by commas.")
        return

    random.shuffle(team_names)

    if team_size == 4:
        await ctx.send(f"**Organized 2v2**\n \n**Team 1**: {', '.join(team_names[:2])} | **Team 2**: {', '.join(team_names[2:])}")
    elif team_size == 6:
        await ctx.send(f"**Organized 3v3**\n \n**Team 1**: {', '.join(team_names[:3])} | **Team 2**: {', '.join(team_names[3:])}")
    elif team_size == 8:
        await ctx.send(f"**Organized 4v4**\n \n**Team 1**: {', '.join(team_names[:4])} | **Team 2**: {', '.join(team_names[4:])}")
    elif team_size == 10:
        await ctx.send(f"**Organized 5v5**\n \n**Team 1**: {', '.join(team_names[:5])} | **Team 2**: {', '.join(team_names[5:])}")

bot.run('INSERT_YOUR_BOT_TOKEN')
