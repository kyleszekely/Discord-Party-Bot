import json
import discord
from discord.ext import commands

with open('token.json', "r") as f:
    data = json.load(f) 
print(data.get('TOKEN'))

TOKEN = data.get('TOKEN')

client = commands.Bot(command_prefix="#")

playerNumber = 0

@client.command(name="play")
async def play(context, *game):

    myEmbed = discord.Embed(title=" ".join(game), description="React to join the Game Party", color=0xFF69B4)
    myEmbed.add_field(name="Lobby:", value="TBD", inline=True)
    myEmbed.add_field(name="Players:", value=playerNumber, inline=True)
    myEmbed.set_footer(text=" ")
    myEmbed.set_author(name="Hosted by: {}".format(context.author))

    message = await context.message.channel.send(embed=myEmbed)
    await context.message.delete()
    await message.add_reaction("🚀")

@client.event
async def on_reaction_add(reaction, user):
    global playerNumber
    if reaction.emoji == "🚀":
        users = await reaction.users().flatten()
        playerNumber = len(users)
        print(reaction.message)
        #reaction.message.edit(embed = newEmbed)
        print("List of Users that reacted: {}".format(len(users)))
        print(users)

@client.event
async def on_ready():
    print("Bot is online.")


client.run(TOKEN)

