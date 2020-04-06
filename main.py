import discord
from authority import Authority
from discord.ext import commands

client = commands.Bot(command_prefix="/")
client.remove_command("help")


@client.event
async def on_ready():
    print("The bot is ready!")


if __name__ == '__main__':
    client.load_extension("authority")
    client.load_extension("listener")
    client.run('NjkyNTc2MTcxOTAwMTQxNTk4.XoEL6w.z3QOcxuas_iyCcJcM4TsOq7CN3Y')
