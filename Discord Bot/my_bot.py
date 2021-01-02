import discord
from discord.ext import commands
import keyboard

client = commands.Bot(command_prefix='!')


@client.event
async def on_disconnect():
  bot_status = client.get_channel(789589480486600704)
  await bot_status.send('Offline')



@client.event 
async def on_connect():
  bot_status = client.get_channel(789589480486600704)
  await bot_status.send('Online')










@client.event
async def on_ready():
    print("The Bot Is Online")


@client.event
async def on_message(message):

    if message.content == '!help':
        bot_cmd = client.get_channel(789589480486600704)

        help = discord.Embed(title="Help", description="Shows list of commands", color=0x00ff00)
        help.add_field(name="Hello", value="Hi!", inline=False)
        help.set_footer(text="List of commands")

        await bot_cmd.send(embed=help)



@client.command()
async def verify(ctx, amount = 0):
    await ctx.channel.purge(limit = amount)
    role = get(message.server.roles, name='alt')
    await client.add_roles(message.author, role)



client.run('NzAyMjY0MjQ4ODQzMjM5NDM1.Xp9gjA.jUsDEmv66E4HbimzgKPVq6HTamA')
