import json
import discord
from discord.ext import commands

with open('token.json', "r") as f:
    data = json.load(f) 
print(data.get('TOKEN'))

TOKEN = data.get('TOKEN')

client = commands.Bot(command_prefix="#")

playerNumber = 0

dictionary = {}

@client.command(name="play")
async def play(context, *game):

    global dictionary

    myEmbed = discord.Embed(title=" ".join(game), description="React to join the Game Party", color=0xFF69B4)
    myEmbed.add_field(name="Lobby:", value="TBD", inline=True)
    myEmbed.add_field(name="Players:", value="TBD", inline=True)
    myEmbed.set_footer(text=" ")
    myEmbed.set_author(name="Hosted by: {}".format(context.author), icon_url=context.author.avatar_url)

    message = await context.message.channel.send(embed=myEmbed)
    dictionary.update({message.id: myEmbed})
    
    await context.message.delete()
    await message.add_reaction("🚀")
       

@client.event
async def on_reaction_add(reaction, user):
    global playerNumber
   
    if dictionary.get(reaction.message.id):
        if reaction.emoji == "🚀":
            
            if not user.bot:
            
                users = await reaction.users().flatten()

                print("React: {}".format(users))
                
                playerNumber = (len(users))-1
           
                updatedEmbed = dictionary.get(reaction.message.id).set_field_at(1 , name="Players:", value='\u200b\n'.join([user.name for user in users if user.name != "PartyBot"]), inline=True)
                await reaction.message.edit(embed=updatedEmbed)
               

@client.event
async def on_reaction_remove(reaction, user):

    print("hello")

    if dictionary.get(reaction.message.id):
        print("Test1")
        if reaction.emoji == "🚀":
            print("test2")
            if not user.bot:
                
                users = await reaction.users().flatten()

                print("Unreact: {}".format(users))
                
                playerNumber -= 1

                print(playerNumber)
           
                updatedEmbed = dictionary.get(reaction.message.id).set_field_at(1 , name="Players:", value='\u200b\n'.join([user.name for user in users if user.name != "PartyBot"]), inline=True)
                await reaction.message.edit(embed=updatedEmbed)

@client.event
async def on_ready():
    print("Bot is online.")


client.run(TOKEN)

