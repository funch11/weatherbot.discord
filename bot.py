import discord 
from discord.ext import commands
from pyowm import OWM
from pyowm.utils.config import get_default_config
import asyncio
import keep_alive

client = commands.Bot(command_prefix='*')

config_dict = get_default_config()
config_dict['language'] = 'ru'
 
owm = OWM("98de26f79803d03f20d5d1f769e26af8", config_dict)
mgr = owm.weather_manager()

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name='*погода <город>'))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name=f"Пинг {round(client.latency * 1000)} мс"))
        await asyncio.sleep(10)

@client.event
async def on_ready():
    client.loop.create_task(status_task())
    print("Бот запущен!")

@client.command()
async def погода(ctx,*,city):
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

    emb = discord.Embed(title="Погода  :white_sun_rain_cloud:", description = f"**Запрошенный {ctx.author.mention}**",color=0x00FFFF)
    emb.add_field(name="Город:", value=f"_{c}_",inline=False)
    emb.add_field(name="Регион:", value=f"_{s}_",inline=False)
    emb.add_field(name="Температура:", value=f"_{t}°C_",inline=False)
    emb.add_field(name="Минимальная:", value=f"_{h}°C_",inline=False)
    emb.add_field(name="Максимальная:", value=f"_{k}°C_",inline=False)
    emb.add_field(name="Ощущается как:", value=f"_{f}°C_",inline=False)
    emb.add_field(name="Статус:", value=f"_{st}_",inline=False)
    emb.add_field(name="Скорость ветра:", value=f"_{wi} м/с_",inline=False)
    emb.add_field(name="Влажность:", value=f"_{humi}%_",inline=False)
    emb.add_field(name="Облачность:", value=f"_{cl}%_",inline=False)
    emb.add_field(name="Давление:", value=f"_{pr} мм.рт.ст_",inline=False)
    emb.add_field(name="Видимость:", value=f"_{vd} м_",inline=False)
    emb.set_footer(text="Разработчик getxay#3896  •  Источник OWM")
    await ctx.send(embed = emb)


@погода.error
async def w_error(ctx: commands.Context, error:commands.CommandInvokeError):
    if isinstance(error,commands.CommandInvokeError):
        emd = discord.Embed(title="Город не найден  :mag:", description = f"**Запрошенный {ctx.author.mention}**")
        await ctx.send(embed = emd)

keep_alive.keep_alive()
client.run("ODIwNTc5MjMwMTIzMDMyNTc2.YE3N9g.HChUBr4u2KeVlT32bqea4yutRBY")
                       






