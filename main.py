
import discord 
from discord.ext import commands 
import os
import random
import requests

intents = discord.Intents.default()  
intents.message_content = True  

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event 
async def on_ready(): 
    print(f'{bot.user} olarak giriş yaptık') 

@bot.command() 
async def merhaba(ctx): 
    await ctx.send(f'Merhaba! Ben {bot.user}! Ben bir botum!')

@bot.command() 
async def yardim(ctx): 
    await ctx.send(f'Üzgünüm :sob: böyle bir konuda sana yardımcı olamam. https://discordapp.com/channels/1426830868634144790/1426831600511094804 ama burdan yardım desteği alabilirsin!')
    

@bot.command()
async def joined(ctx, member: discord.Member):  
    """Bir kişinin sunucuya ne zaman katıldığını söyler."""

    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
  

@bot.command()
async def meme(ctx):
    files = os.listdir('images')
    selected_file = random.choice(files)
    with open(f'images/{selected_file}', 'rb' )as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('ordek')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


def get_wolf_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('kopek')
async def anime(ctx):
    '''anime komutunu çağırdığımızda, program wolf_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_wolf_image_url()
    await ctx.send(image_url)

@bot.command() 
async def cevre(ctx): 
    await ctx.send('''Al sana çevre kirliliği ile ilgili şeyler
                   1. Hava kirliliği
                   2. Su kirliliği
                   3. Toprak kirliliği
                   4. Gürültü kirliliği
                   5. Işık kirliliği
                   istersen fotorafta gönderebilirim !fotoraf yaz''')

@bot.command() 
async def hava(ctx): 
    await ctx.send(f'Hava kirliliği: Fabrika ve araç egzozlarından çıkan dumanlar.')

@bot.command() 
async def su(ctx): 
    await ctx.send(f'Su kirliliği: Denize ya da nehirlere atılan çöpler ve kimyasallar.')

@bot.command() 
async def toprak(ctx): 
    await ctx.send(f'Toprak kirliliği: Tarımda aşırı gübre ve ilaç kullanımı.')

@bot.command() 
async def gurultu(ctx): 
    await ctx.send(f'Gürültü kirliliği: Trafik, inşaat ve yüksek sesli müzikler.')

@bot.command() 
async def isik(ctx): 
    await ctx.send(f'Işık kirliliği: Şehirlerde gece fazla yapay ışık kullanımı.')

@bot.command() 
async def fotoraf(ctx): 
    await ctx.send('''Tabiiki! hangisi ile ilgili fotoraf istersin?
                   1. Hava kirliliği
                   2. Su kirliliği
                   3. Toprak kirliliği
                   4. Gürültü kirliliği
                   5. Işık kirliliği
                   ama sonuna f eklemeyi unutma!''')

@bot.command()
async def havaf(ctx):
    with open('cevre/hava.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def suf(ctx):
    with open('cevre/su.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def toprakf(ctx):
    with open('cevre/toprak.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def gurultuf(ctx):
    with open('cevre/ses.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def isikf(ctx):
    with open('cevre/isik.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command() 
async def cmd(ctx): 
    await ctx.send('''Tabiiki al sana komutlar!
    !yardim
    !meme
    !ordek
    !kopek
    !cevre
    !fotoraf
    !cmd
    !merhaba''')


bot.run("token")
