import discord 
from discord.ext import commands
from pyowm import OWM
import asyncio

client = commands.Bot(command_prefix='*')
 
owm = OWM("owm_api_key")
mgr = owm.weather_manager()

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name='*weather <city>'))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name=f"Ping {round(client.latency * 1000)} ms"))
        await asyncio.sleep(10)

@client.event
async def on_ready():
    client.loop.create_task(status_task())
    print("Ready!")

@client.command()
async def weather(ctx,*,city):
    observation = mgr.weather_at_place(city)
    w = observation.weather
    l = observation.location

    s = l.country
    c = l.name
    t = w.temperature("celsius")["temp"]
    h = w.temperature("celsius")["temp_min"]
    k = w.temperature("celsius")["temp_max"]
    f = w.temperature("celsius")["feels_like"]
    wi = w.wind()['speed'] 
    humi = w.humidity 
    cl = w.clouds 
    st = w.status 
    pr = w.pressure['press'] 
    vd = w.visibility_distance 

    emb = discord.Embed(title="Weather  :white_sun_rain_cloud:", description = f"**Requested by {ctx.author.mention}**",color=0x00FFFF)
    emb.add_field(name="City:", value=f"_{c}_",inline=False)
    emb.add_field(name="Country:", value=f"_{s}_",inline=False)
    emb.add_field(name="Temperature:", value=f"_{t}°C_",inline=False)
    emb.add_field(name="Min:", value=f"_{h}°C_",inline=False)
    emb.add_field(name="Max:", value=f"_{k}°C_",inline=False)
    emb.add_field(name="Feels like:", value=f"_{f}°C_",inline=False)
    emb.add_field(name="Status:", value=f"_{st}_", inline=False)
    emb.add_field(name="Wind speed:", value=f"_{wi} м/с_",inline=False)
    emb.add_field(name="Humidity:", value=f"_{humi}%_",inline=False)
    emb.add_field(name="Cloudy:", value=f"_{cl}%_",inline=False)
    emb.add_field(name="Pressure:", value=f"_{pr} мм.рт.ст_",inline=False)
    emb.add_field(name="Visibility:", value=f"_{vd} м_",inline=False)
    emb.set_footer(text="Created by Little4Win  •  discord.py")
    await ctx.send(embed = emb)


@weather.error
async def w_error(ctx: commands.Context, error:commands.CommandInvokeError):
    if isinstance(error,commands.CommandInvokeError):
        emd = discord.Embed(title="City not found  :mag:", description = f"**Requested by {ctx.author.mention}**")
        await ctx.send(embed = emd)

client.run("discord_api_key")
                       






