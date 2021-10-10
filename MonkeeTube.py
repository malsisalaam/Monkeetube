import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('God loves all monkeys')

@client.event
async def on_member_join(member):
    print(f"{member} has joined a server.")

@client.event
async def on_member_remove(member):
    print(f"{member} has left a server.")

@client.command(pass_context=True)
async def clear(ctx, number = 1):
    number = int(number)
    await ctx.channel.purge(limit=number+1)


@client.command()
async def ping(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"Pong! {ctx.author}::: Ping is {round(client.latency * 1000)} ms")


@client.command()
async def load(ctx, extension):
    client.load_extensions(f"cogs.{extension}")

for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")



client.run("ODg2MjI2NDk5NjAxMDM5Mzgw.YTygvg.kZyl2_R0gKdwLzen9Z6JumBiqug")
