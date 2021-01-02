#import Discord Package
import discord
from discord.ext import commands

#the bot
client = commands.Bot(command_prefix="#")

playerNumber = 0

#when #play
@client.command(name="play")
async def play(context, *game):


    myEmbed = discord.Embed(title=" ".join(game), description="React to join the Game Party", color=0xFF69B4)
    myEmbed.add_field(name="Lobby:", value="TBD", inline=False)
    myEmbed.add_field(name="Players:", value=playerNumber, inline=False)
    myEmbed.set_footer(text="This is a sample footer")
    myEmbed.set_author(name="Hosted by: {}".format(context.author))

    await context.message.channel.send(embed=myEmbed)

@client.event
async def on_reaction_add(reaction, user):
    global playerNumber
    if reaction == str(":rocket:"):
        users = await reaction.users().flatten()
        playerNumber = len(users)
        print(len(users))
        print(reaction)
    #print(reaction)

#on startup
@client.event
async def on_ready():
    print("Bot is online")
    general_channel = client.get_channel(794685678453391383)
    await general_channel.send("Bonjour! :partying_face:")


#run the client on the server
client.run("Nzk0NjgyMTQ3NjQxNzUzNjAw.X--XbA.DG7MTdVTRpei8HhCar4RGhWnmk4")