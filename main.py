import discord
import os

bot = discord.Client()

@bot.event
async def on_ready():
  print("logged on as {0.user}".format(bot))

@bot.event
async def on_message(message):
  print("received message")
  if message.author == bot.user:
    return
  
  if message.content.startswith("hi"):
    await message.channel.send("hihihihi")
  else:
    await message.channel.send("pls say hi")

bot.run(os.getenv('TOKEN'))