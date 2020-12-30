import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!genshin ', case_insensitive = True)  #switch to GI if genshin starts to become inconvenient

#images of the characters were taken from the genshin wiki site: https://genshin-impact.fandom.com/wiki/Genshin_Impact_Wiki
#Will try to keep the list of commands in the following order except for qiqi because she was the first one I wrote:
#Characters (alphabetical), Daily Talent/Weapons materials, Weapons (by type of weapon)
@bot.command(name='qiqi',help ="Displays ascension materials for Qiqi. Include talent to see talents instead or all to see both")
async def qiqi(ctx,flags:str=None):
    def ascension():
        gem = "Shivada Jade"
        boss = "Hoarfrost Core"
        Local ="Violetgrass"
        Common1 = "Divining Scroll"
        Common2 = "Sealed Scroll"
        Common3 = "Forbidden Curse Scroll"
        
        embed = discord.Embed(title="Qiqi Ascension Materials",colour = discord.Colour.teal())
        embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/b/b9/Character_Qiqi_Card.jpg") 
        embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
        embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
        embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
        embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
        embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
        embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)
        return embed
    def talent():
        book = "Prosperity"
        boss = "Tail of Boreas"
        Common1 = "Divining Scroll"
        Common2 = "Sealed Scroll"
        Common3 = "Forbidden Curse Scroll"
        embed = discord.Embed(title="Qiqi Talent Materials",colour = discord.Colour.teal())
        embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/b/b9/Character_Qiqi_Card.jpg")
        embed.add_field(name = "Talent level 2",value = f'6x {Common1}, 3x Teachings of "{book}", 12,500 Mora',inline = False)
        embed.add_field(name = "Talent level 3",value = f'3x {Common2}, 2x Guide to "{book}", 17,500 Mora',inline = False)
        embed.add_field(name = "Talent level 4",value = f'4x {Common2}, 4x Guide to "{book}", 25,000 Mora',inline = False)
        embed.add_field(name = "Talent level 5",value = f'6x {Common2}, 6x Guide to "{book}", 30,000 Mora',inline = False)
        embed.add_field(name = "Talent level 6",value = f'9x {Common2}, 9x Guide to "{book}", 37,500 Mora',inline = False)
        embed.add_field(name = "Talent level 7",value = f'4x {Common3}, 4x Philosophies of "{book}", 1x {boss}, 120,000 Mora',inline = False)
        embed.add_field(name = "Talent level 8",value = f'6x {Common3}, 6x Philosophies of "{book}", 1x {boss}, 260,000 Mora',inline = False)
        embed.add_field(name = "Talent level 9",value = f'9x {Common3}, 12x Philosophies of "{book}", 2x {boss}, 450,000 Mora',inline = False)
        embed.add_field(name = "Talent level 10",value = f'12x {Common3}, 16x Philosophies of "{book}", 2x {boss}, 700,000 Mora',inline = False)          
        return embed
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent()
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension()
            await ctx.send(embed=embed)
            embed = talent()
            await ctx.send(embed=embed)
    else:
        embed = ascension()
        await ctx.send(embed=embed)

@bot.command(name ='albedo',help ="Displays ascension materials for Albedo")
async def albedo(ctx):
    gem = "Prithiva Topaz"
    boss = "Basalt Pillar"
    Local ="Cecilia"
    Common1 = "Divining Scroll"
    Common2 = "Sealed Scroll"
    Common3 = "Forbidden Curse Scroll"
    
    embed = discord.Embed(title="Albedo",colour = discord.Colour.gold())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/f/f8/Character_Albedo_Card.png") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name ='amber',help = "Displays ascension materials for Amber")
async def amber(ctx):
    gem = "Agnidus Agate"
    boss = "Everflame Seed"
    Local ="Small Lamp Grass"
    Common1 = "Firm Arrowhead"
    Common2 = "Sharp Arrowhead"
    Common3 = "Weathered Arrowhead"
    
    embed = discord.Embed(title="Amber",colour = discord.Colour.red())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/2/26/Character_Amber_Card.jpg") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name ='barbara',help = "Displays ascension materials for Barbara")
async def barbara(ctx):
    gem = "Varunada Lazurite"
    boss = "Cleansing Heart"
    Local ="Philanemo Mushroom"
    Common1 = "Divining Scroll"
    Common2 = "Sealed Scroll"
    Common3 = "Forbidden Curse Scroll"
    
    embed = discord.Embed(title="Barbara",colour = discord.Colour.blue())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/9/93/Character_Barbara_Card.jpg") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name = 'beidou',help ='Displays ascension materials for Beidou')
async def beidou(ctx):
    gem = "Varjada Amethust"
    boss = "Lightning Prism"
    Local ="Noctilucous Jade"
    Common1 = "Treasure Hoarder Insignia"
    Common2 = "Silver Raven Insignia"
    Common3 = "Golden Raven Insignia"
    
    embed = discord.Embed(title="Beidou",colour = discord.Colour.purple())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/8/84/Character_Beidou_Card.jpg") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)

@bot.command(name ='bennett',help = "Displays ascension materials for Bennett")
async def bennett(ctx):
    gem = "Agnidus Agate"
    boss = "Everflame Seed"
    Local ="Windwheel Aster"
    Common1 = "Treasure Hoarder Insignia"
    Common2 = "Silver Raven Insignia"
    Common3 = "Golden Raven Insignia"
    
    embed = discord.Embed(title="Bennett",colour = discord.Colour.red())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/7/7f/Character_Bennett_Card.jpg") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name = 'chongyun',aliases = ['chong'],help ="Displays ascension materials for chongyun")
async def chong(ctx):
    gem = "Shivada Jade"
    boss = "Hoarfrost Core"
    Local ="Cor Lapis"
    Common1 = "Damaged Mask"
    Common2 = "Stained Mask"
    Common3 = "Ominous Mask"
    
    embed = discord.Embed(title="Chongyun",colour = discord.Colour.teal())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/f/fa/Character_Chongyun_Card.jpg") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name ='diluc',help = "Displays ascension materials for Diluc")
async def diluc(ctx):
    gem = "Agnidus Agate"
    boss = "Everflame Seed"
    Local ="Small Lamp Grass"
    Common1 = "Recruit's Insignia"
    Common2 = "Seargent's Insignia"
    Common3 = "Lieutenant's Insignia"
    
    embed = discord.Embed(title="Diluc",colour = discord.Colour.red())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/4/45/Character_Diluc_Card.jpg") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name ='diona',help = "Displays ascension materials for Diona")
async def diluc(ctx):
    gem = "Shivada Jade"
    boss = "Hoarfrost Core"
    Local ="Calla Lily"
    Common1 = "Firm Arrowhead"
    Common2 = "Sharp Arrowhead"
    Common3 = "Weathered Arrowhead"
    
    embed = discord.Embed(title="Diona",colour = discord.Colour.teal())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/0/08/Character_Diona_Card.png") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name ='fischl', aliases =['oz'],help = "Displays ascension materials for Fischl.")
async def fischl(ctx):
    gem = "Varjada Amethyst"
    boss = "Lightning Prism"
    Local ="Small Lamp Grass"
    Common1 = "Firm Arrowhead"
    Common2 = "Sharp Arrowhead"
    Common3 = "Weathered Arrowhead"
    
    embed = discord.Embed(title="Fischl",colour = discord.Colour.purple())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/4/48/Character_Fischl_Card.jpg") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name ='jean',help = "Displays ascension materials for Jean.")
async def Jean(ctx):
    gem = "Vayuda Turquoise"
    boss = "Hurrican Seed"
    Local ="Dandelion Seed"
    Common1 = "Damaged Mask"
    Common2 = "Stained Mask"
    Common3 = "Ominous Mask"
    
    embed = discord.Embed(title="Jean",colour = discord.Colour.green())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/0/0e/Character_Jean_Card.jpg") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name ='kaeya',help = "Displays ascension materials for Kaeya")
async def kaeya(ctx):
    gem = "Shivada Jade"
    boss = "Hoarfrost Core"
    Local ="Calla Lily"
    Common1 = "Treasure Hoarder Insignia"
    Common2 = "Silver Raven Isnigia"
    Common3 = "Golden Raven Insignia"
    
    embed = discord.Embed(title="Kaeya",colour = discord.Colour.teal())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/6/64/Character_Kaeya_Card.jpg") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name ='keqing',help = "Displays ascension materials for Keqing")
async def keqing(ctx):
    gem = "Vayuda Turquoise"
    boss = "Lightning Prism"
    Local ="Cor Lapis"
    Common1 = "Whopperflower Nectar"
    Common2 = "Shimmering Nectar"
    Common3 = "Energy Nectar"
    
    embed = discord.Embed(title="Keqing",colour = discord.Colour.purple())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/f/f4/Character_Keqing_Card.jpg") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name = 'klee',help = "Displays ascension materials for Klee")
async def klee(ctx):
    gem = "Agnidus Agate"
    boss = "Everflame Seed"
    Local ="Philanemo Mushroom"
    Common1 = "Diving Scroll"
    Common2 = "Sealed Scroll"
    Common3 = "Forbidden Curse Scroll"
    
    embed = discord.Embed(title="Klee",colour = discord.Colour.red())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/7/78/Character_Klee_Card.jpg") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name = 'lisa',help = "Displays ascension materials for lisa")
async def lisa(ctx):
    gem = "Vajrada Amethyst"
    boss = "Lightning Prism"
    Local ="Valberry"
    Common1 = "Slime Condensate"
    Common2 = "Slime Secretions"
    Common3 = "Slime Concentrate"
    
    embed = discord.Embed(title="Lisa",colour = discord.Colour.purple())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/d/dc/Character_Lisa_Card.jpg") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name = 'mona',help = "Displays ascension materials for Mona")
async def mona(ctx):
    gem = "Varunada Lazurite"
    boss = "Cleansing Heart"
    Local ="Philanemo Mushroom"
    Common1 = "Whopperflower Nectar"
    Common2 = "Shimmering Nectar"
    Common3 = "Energy Nectar"
    
    embed = discord.Embed(title="Mona",colour = discord.Colour.blue())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/6/69/Character_Mona_Card.jpg") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name = 'ningguang', aliases =['ning'],help = 'Displays asecnsion materials for Ningguang')
async def ningguang(ctx):
    gem = "Prithiva Topaz"
    boss = "Basalt Pillar"
    Local ="Gaze Lily"
    Common1 = "Recruit's Insignia"
    Common2 = "Seargent's Insignia"
    Common3 = "Lieutenant's Insignia"
    
    embed = discord.Embed(title="Ningguang",colour = discord.Colour.gold())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/3/3e/Character_Ningguang_Card.jpg") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name = 'noelle', aliases =['noel'],help = 'Displays asecnsion materials for Noelle')
async def noelle(ctx):
    gem = "Prithiva Topaz"
    boss = "Basalt Pillar"
    Local ="Valberry"
    Common1 = "Damaged Mask"
    Common2 = "Stained Mask"
    Common3 = "Ominous Mask"
    
    embed = discord.Embed(title="Noelle",colour = discord.Colour.gold())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/9/92/Character_Noelle_Card.jpg/") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name = 'razor', aliases =['wolf'],help = 'Displays asecnsion materials for Razor')
async def razor(ctx):
    gem = "Vajrada Amethyst"
    boss = "Lightning Prism"
    Local ="Wolfhook"
    Common1 = "Damaged Mask"
    Common2 = "Stained Mask"
    Common3 = "Ominous Mask"
    
    embed = discord.Embed(title="Razor",colour = discord.Colour.purple())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/6/68/Character_Razor_Card.jpg") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name = 'sucrose',help = "Displays ascension materials for Sucrose")
async def sucrose(ctx):
    gem = "Vayuda Turquoise"
    boss = "Hurricane Seed"
    Local ="Windwheel Aster"
    Common1 = "Whopperflower Nectar"
    Common2 = "Shimmering Nectar"
    Common3 = "Energy Nectar"
    
    embed = discord.Embed(title="Sucrose",colour = discord.Colour.green())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/2/22/Character_Sucrose_Card.jpg") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name = 'traveler', aliases =['mc','main character'],help = "Displays ascension materials for the Traveler")
async def traveler(ctx):
    
    gem = "Brilliant Diamond"
    Local ="Windwheel Aster"
    Common1 = "Damaged Mask"
    Common2 = "Stained Mask"
    Common3 = "Ominous Mask"
    
    embed = discord.Embed(title="Traveler",colour = discord.Colour.dark_gold())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/c/cb/Character_Traveler_Introduction.png") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name = 'venti',aliases = ['barabatos'],help = 'Displays ascension materials for Venti')
async def venti(ctx):
    gem = "Vayuda Turquoise"
    boss = "Hurricane Seed"
    Local ="Cecilia"
    Common1 = "Slime Condensate"
    Common2 = "Slime Secretions"
    Common3 = "Slime Concentrate"
    
    embed = discord.Embed(title="Venti",colour = discord.Colour.green())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/7/76/Character_Venti_Card.jpg") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name = 'xiangling', aliases = ['gouba'],help ='Displays ascension materials for Xiangling')
async def gouba(ctx):
    gem = "Agnidus Agate"
    boss = "Everflame Seed"
    Local ="Jueyun Chili"
    Common1 = "Slime Condensate"
    Common2 = "Slime Secretions"
    Common3 = "Slime Concentrate"
    
    embed = discord.Embed(title="Xiangling",colour = discord.Colour.red())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/f/f1/Character_Xiangling_Card.jpg") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name = 'xingqiu',help = 'Displays ascension materials for Xingqiu')
async def xingiqu(ctx):
    gem = "Varunada Lazurite"
    boss = "Cleansing Heart"
    Local ="Silk Flower"
    Common1 = "Damaged Mask"
    Common2 = "Stained Mask"
    Common3 = "Ominous Mask"
    
    embed = discord.Embed(title="Xingqiu",colour = discord.Colour.blue())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/c/c2/Character_Xingqiu_Card.jpg") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name = 'xinyan',help = 'Displays ascension materials for Xinyan')
async def xingyan(ctx):
    gem = "Agnidus Agate"
    boss = "Everflame Seed"
    Local ="Violetgrass"
    Common1 = "Treasure Hoarder Insignia"
    Common2 = "Silver Raven Isnigia"
    Common3 = "Golden Raven Insignia"
    
    embed = discord.Embed(title="Xinyan",colour = discord.Colour.red())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/4/4c/Character_Xinyan_Card.jpeg") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
@bot.command(name = 'zhongli',aliases = ['rex lapis','morax'], help = "Displays ascension materials for Zhongli")
async def zhongli(ctx):
    gem = "Prithiva Topaz"
    boss = "Basalt Pillar"
    Local ="Cor Lapis"
    Common1 = "Slime Condensate"
    Common2 = "Slime Secretions"
    Common3 = "Slime Concentrate"
    
    embed = discord.Embed(title="Zhongli",colour = discord.Colour.gold())
    embed.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/7/79/Character_Zhongli_Card.png") 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)

    await ctx.send(embed=embed)
#End of characters
bot.run(TOKEN)