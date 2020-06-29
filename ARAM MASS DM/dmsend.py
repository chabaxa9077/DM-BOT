


    
    
import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("웨커.")
    game = discord.Game('웨커')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == 703304717828227082:
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="웨커봇테스트")
                        embed.add_field(name="웨커", value=msg, inline=True)
                        embed.set_footer(text=f"https://discord.gg/cfHr3n2")
                        await i.send(embed=embed)
                except:
                    pass


client.run('NzI3MTY1NDc3NTQ5MjQ0NTA4.Xvn30Q.e82PB-6GQ0EEpweYtUGf5aA6BjA')
