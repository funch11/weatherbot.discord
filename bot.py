import discord 
from discord.ext import commands
from pyowm import OWM

client = commands.Bot(command_prefix='*')

 
owm = OWM("98de26f79803d03f20d5d1f769e26af8")
mgr = owm.weather_manager()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='*w <city>'))
    print("Bot started!")
    
@client.command()
async def w(ctx,*,city):
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

    emb = discord.Embed(title="Weather  :white_sun_rain_cloud:", description = f"**Requseted by {ctx.author.mention}**",color=0x00FFFF)
    emb.add_field(name="City:", value=f"_{c}_",inline=False)
    emb.add_field(name="Country:", value=f"_{s}_",inline=False)
    emb.add_field(name="Temperature:", value=f"_{t}°C_",inline=False)
    emb.add_field(name="Minimal:", value=f"_{h}°C_",inline=False)
    emb.add_field(name="Maximum:", value=f"_{k}°C_",inline=False)
    emb.add_field(name="Feels like:", value=f"_{f}°C_",inline=False)
    emb.add_field(name="Status:", value=f"_{st}_",inline=False)
    emb.add_field(name="Wind speed:", value=f"_{wi} m/s_",inline=False)
    emb.add_field(name="Humidity:", value=f"_{humi}%_",inline=False)
    emb.add_field(name="Cloudy:", value=f"_{cl}%_",inline=False)
    emb.add_field(name="Pressure:", value=f"_{pr} mmHg_",inline=False)
    emb.add_field(name="Visibility:", value=f"_{vd} m_",inline=False)
    emb.set_footer(text="Created by getxay  •  OWM api")
    await ctx.send(embed = emb)

@client.command()
async def wstats(ctx):
    await ctx.send(f"Connected on {str(len(client.guilds))} servers:")


@w.error
async def w_error(ctx: commands.Context, error:commands.CommandInvokeError):
    if isinstance(error,commands.CommandInvokeError):
        emd = discord.Embed(title="City not found  :mag:", description = f"**Requseted by {ctx.author.mention}**")
        await ctx.send(embed = emd)

client.run("ODIzMDA2Njg2MzY4MzY2NjEy.YFaitA.mmdk66uZa9PyMMupqUvcflZycpU")
                       






