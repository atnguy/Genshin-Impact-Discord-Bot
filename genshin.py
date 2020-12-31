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
def ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink):
    embed = discord.Embed(title= f"{name} Ascension Materials",colour = color)
    embed.set_thumbnail(url =imagelink) 
    embed.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
    embed.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 2x {boss}, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
    embed.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 4x {boss}, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
    embed.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 8x {boss}, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
    embed.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 12x {boss}, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
    embed.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 20x {boss}, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)
    return embed
def talent(name,book,boss,Common1,Common2,Common3,color,imagelink):
    embed = discord.Embed(title= f"{name} Talent Materials",colour = color)
    embed.set_thumbnail(url = imagelink)
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
def talent_traveler(element):
    #setting default values to anemo traveler
    book1 = "Freedom"
    book2 = "Resistance"
    book3 = "Ballad"
    Common1 = "Divining Scroll"
    Common2 = "Sealed Scroll"
    Common3 = "Forbidden Curse Scroll"
    name = "Anemo Traveler"
    boss = "Dvalin's Sigh"
    color = discord.Colour.green()
    description = "Talent materials for Traveler's Normal/charged attack and Anemo Traveler's Elemental skill and Elemental Burst."
    #creathing this function allows for easily adding in information and code when Traveler unlocks more elements
    if(element == 'geo'):
        name = "Geo Traveler"
        Common1 = "Firm Arrowhead"
        Common2 = "Sharp Arrowhead"
        Common3 = "Weathered Arrowhead"
        book1 = "Prosperity"
        book2 = "Dilligence"
        book3 = "Gold"
        boss = "Tail of Boreas"
        description ="Talent materials for Geo Traveler's Element skill and Elemental Burst. Refer to anemo traveler for Normal/charged attack."
        color = discord.Colour.gold()

    embed = discord.Embed(title= f"{name} Talent Materials",colour = color,description = description)
    embed.set_thumbnail(url = "https://static.wikia.nocookie.net/gensin-impact/images/c/cb/Character_Traveler_Introduction.png")
    embed.add_field(name = "Talent level 2",value = f'6x {Common1}, 3x Teachings of "{book1}", 12,500 Mora',inline = False)
    embed.add_field(name = "Talent level 3",value = f'3x {Common2}, 2x Guide to "{book2}", 17,500 Mora',inline = False)
    embed.add_field(name = "Talent level 4",value = f'4x {Common2}, 4x Guide to "{book3}", 25,000 Mora',inline = False)
    embed.add_field(name = "Talent level 5",value = f'6x {Common2}, 6x Guide to "{book1}", 30,000 Mora',inline = False)
    embed.add_field(name = "Talent level 6",value = f'9x {Common2}, 9x Guide to "{book2}", 37,500 Mora',inline = False)
    embed.add_field(name = "Talent level 7",value = f'4x {Common3}, 4x Philosophies of "{book3}", 1x {boss}, 120,000 Mora',inline = False)
    embed.add_field(name = "Talent level 8",value = f'6x {Common3}, 6x Philosophies of "{book1}", 1x {boss}, 260,000 Mora',inline = False)
    embed.add_field(name = "Talent level 9",value = f'9x {Common3}, 12x Philosophies of "{book2}", 2x {boss}, 450,000 Mora',inline = False)
    embed.add_field(name = "Talent level 10",value = f'12x {Common3}, 16x Philosophies of "{book3}", 2x {boss}, 700,000 Mora',inline = False)          
    return embed
@bot.command(name='qiqi',help ="Displays ascension materials for Qiqi. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def qiqi(ctx,flags:str=None):
    Common1 = "Divining Scroll"
    Common2 = "Sealed Scroll"
    Common3 = "Forbidden Curse Scroll"
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/b/b9/Character_Qiqi_Card.jpg"
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent("Qiqi","Prosperity","Tail of Boreas",Common1,Common2,Common3,discord.Colour.teal(),imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension("Qiqi","Shivada Jade","Hoarfrost Core","Violetgrass",Common1,Common2,Common3,discord.Colour.teal(),imagelink)
            await ctx.send(embed=embed)
            embed = talent("Qiqi","Prosperity","Tail of Boreas",Common1,Common2,Common3,discord.Colour.teal(),imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension("Qiqi","Shivada Jade","Hoarfrost Core","Violetgrass",Common1,Common2,Common3,discord.Colour.teal(),imagelink)
        await ctx.send(embed=embed)

@bot.command(name ='albedo',help ="Displays ascension materials for Albedo. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def albedo(ctx, flags: str=None):
    gem = "Prithiva Topaz"
    boss = "Basalt Pillar"
    Local ="Cecilia"
    Common1 = "Divining Scroll"
    Common2 = "Sealed Scroll"
    Common3 = "Forbidden Curse Scroll"
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/f/f8/Character_Albedo_Card.png"
    name = "Albedo"
    book = "Ballad"
    weekly_boss = "Tusk of Monoceros Caeli"
    color = discord.Colour.gold()
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name ='amber',help = "Displays ascension materials for Amber. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def amber(ctx, flags: str=None):
    gem = "Agnidus Agate"
    boss = "Everflame Seed"
    Local ="Small Lamp Grass"
    Common1 = "Firm Arrowhead"
    Common2 = "Sharp Arrowhead"
    Common3 = "Weathered Arrowhead"
    name = "Amber"
    color = discord.Colour.red()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/2/26/Character_Amber_Card.jpg"
    weekly_boss = "Dvalin's Sigh"
    book = "Freedom"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name ='barbara',help = "Displays ascension materials for Barbara. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def barbara(ctx, flags: str = None):
    gem = "Varunada Lazurite"
    boss = "Cleansing Heart"
    Local ="Philanemo Mushroom"
    Common1 = "Divining Scroll"
    Common2 = "Sealed Scroll"
    Common3 = "Forbidden Curse Scroll"
    name = "Barbara"
    color = discord.Colour.blue()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/9/93/Character_Barbara_Card.jpg"
    weekly_boss = "Ring of Boreas"
    book = "Freedom"
    
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name = 'beidou',help ="Displays ascension materials for Beidou. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def beidou(ctx, flags: str= None):
    gem = "Varjada Amethust"
    boss = "Lightning Prism"
    Local ="Noctilucous Jade"
    Common1 = "Treasure Hoarder Insignia"
    Common2 = "Silver Raven Insignia"
    Common3 = "Golden Raven Insignia"
    name = "Beidou"
    color = discord.Colour.purple()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/8/84/Character_Beidou_Card.jpg"
    weekly_boss = "Dvalin's Sigh"
    book = "Gold"
    
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)

@bot.command(name ='bennett',help = "Displays ascension materials for Bennett. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def bennett(ctx, flags: str=None):
    gem = "Agnidus Agate"
    boss = "Everflame Seed"
    Local ="Windwheel Aster"
    Common1 = "Treasure Hoarder Insignia"
    Common2 = "Silver Raven Insignia"
    Common3 = "Golden Raven Insignia"
    name = "Bennett"
    color = discord.Colour.red()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/7/7f/Character_Bennett_Card.jpg"
    weekly_boss = "Dvalin's Plume"
    book = "Resistance"
    
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name = 'chongyun',aliases = ['chong'],help ="Displays ascension materials for chongyun. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def chong(ctx, flags:str = None):
    gem = "Shivada Jade"
    boss = "Hoarfrost Core"
    Local ="Cor Lapis"
    Common1 = "Damaged Mask"
    Common2 = "Stained Mask"
    Common3 = "Ominous Mask"
    name = "Chongyun"
    color = discord.Colour.teal()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/f/fa/Character_Chongyun_Card.jpg"
    weekly_boss = "Dvalin's Sigh"
    book = "Dilligence"
    
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name ='diluc',help = "Displays ascension materials for Diluc. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def diluc(ctx,flags: str = None):
    gem = "Agnidus Agate"
    boss = "Everflame Seed"
    Local ="Small Lamp Grass"
    Common1 = "Recruit's Insignia"
    Common2 = "Seargent's Insignia"
    Common3 = "Lieutenant's Insignia"
    name = "Diluc"
    color = discord.Colour.red()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/4/45/Character_Diluc_Card.jpg"
    weekly_boss = "Dvalin's Plume"
    book = "Resistance"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name ='diona',help = "Displays ascension materials for Diona. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def diona(ctx,  flags: str = None):
    gem = "Shivada Jade"
    boss = "Hoarfrost Core"
    Local ="Calla Lily"
    Common1 = "Firm Arrowhead"
    Common2 = "Sharp Arrowhead"
    Common3 = "Weathered Arrowhead"
    name = "Diona"
    color = discord.Colour.teal()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/0/08/Character_Diona_Card.png"
    weekly_boss = "Shard of a Foul Legacy"
    book = "Freedom"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name ='fischl', aliases =['oz','amy'],help = "Displays ascension materials for Fischl. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def fischl(ctx, flags: str = None):
    gem = "Varjada Amethyst"
    boss = "Lightning Prism"
    Local ="Small Lamp Grass"
    Common1 = "Firm Arrowhead"
    Common2 = "Sharp Arrowhead"
    Common3 = "Weathered Arrowhead"
    name = "Fischl"
    color = discord.Colour.purple()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/4/48/Character_Fischl_Card.jpg"
    weekly_boss = "Spirit Locket of Boreas"
    book = "Ballad"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name ='jean',help = "Displays ascension materials for Jean. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def Jean(ctx, flags: str = None):
    gem = "Vayuda Turquoise"
    boss = "Hurrican Seed"
    Local ="Dandelion Seed"
    Common1 = "Damaged Mask"
    Common2 = "Stained Mask"
    Common3 = "Ominous Mask"
    name = "Jean"
    color = discord.Colour.green()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/0/0e/Character_Jean_Card.jpg"
    weekly_boss = "Dvalin's Plume"
    book = "Resistance"
    
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name ='kaeya',help = "Displays ascension materials for Kaeya. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def kaeya(ctx, flags: str = None):
    gem = "Shivada Jade"
    boss = "Hoarfrost Core"
    Local ="Calla Lily"
    Common1 = "Treasure Hoarder Insignia"
    Common2 = "Silver Raven Isnigia"
    Common3 = "Golden Raven Insignia"
    name = "Kaeya"
    color = discord.Colour.teal()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/6/64/Character_Kaeya_Card.jpg"
    weekly_boss = "Spirit Locket of Boreas"
    book = "Ballad"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name ='keqing',help = "Displays ascension materials for Keqing. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def keqing(ctx, flags: str = None):
    gem = "Vayuda Turquoise"
    boss = "Lightning Prism"
    Local ="Cor Lapis"
    Common1 = "Whopperflower Nectar"
    Common2 = "Shimmering Nectar"
    Common3 = "Energy Nectar"
    name = "Keqing"
    color = discord.Colour.dark_purple()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/f/f4/Character_Keqing_Card.jpg"
    weekly_boss = "Ring of Boreas"
    book = "Prosperity"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name = 'klee',help = "Displays ascension materials for Klee. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def klee(ctx, flags: str = None):
    gem = "Agnidus Agate"
    boss = "Everflame Seed"
    Local ="Philanemo Mushroom"
    Common1 = "Diving Scroll"
    Common2 = "Sealed Scroll"
    Common3 = "Forbidden Curse Scroll"
    name = "Klee"
    color = discord.Colour.red()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/7/78/Character_Klee_Card.jpg"
    weekly_boss = "Ring of Boreas"
    book = "Freedom"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name = 'lisa',help = "Displays ascension materials for lisa. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def lisa(ctx, flags: str = None):
    gem = "Vajrada Amethyst"
    boss = "Lightning Prism"
    Local ="Valberry"
    Common1 = "Slime Condensate"
    Common2 = "Slime Secretions"
    Common3 = "Slime Concentrate"
    name = "Lisa"
    color = discord.Colour.dark_purple()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/d/dc/Character_Lisa_Card.jpg"
    weekly_boss = "Dvalin's Claw"
    book = "Ballad"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name = 'mona',help = "Displays ascension materials for Mona. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def mona(ctx, flags: str = None):
    gem = "Varunada Lazurite"
    boss = "Cleansing Heart"
    Local ="Philanemo Mushroom"
    Common1 = "Whopperflower Nectar"
    Common2 = "Shimmering Nectar"
    Common3 = "Energy Nectar"
    name = "Mona"
    color = discord.Colour.blue()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/6/69/Character_Mona_Card.jpg"
    weekly_boss = "Ring of Boreas"
    book = "Resistance"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name = 'ningguang', aliases =['ning'],help = "Displays asecnsion materials for Ningguang. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def ningguang(ctx, flags: str = None):
    gem = "Prithiva Topaz"
    boss = "Basalt Pillar"
    Local ="Gaze Lily"
    Common1 = "Recruit's Insignia"
    Common2 = "Seargent's Insignia"
    Common3 = "Lieutenant's Insignia"
    name = "Ningguang"
    color = discord.Colour.gold()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/3/3e/Character_Ningguang_Card.jpg"
    weekly_boss = "Spirit Locket of Boreas"
    book = "Prosperity"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name = 'noelle', aliases =['noel'],help = "Displays asecnsion materials for Noelle. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def noelle(ctx, flags: str = None):
    gem = "Prithiva Topaz"
    boss = "Basalt Pillar"
    Local ="Valberry"
    Common1 = "Damaged Mask"
    Common2 = "Stained Mask"
    Common3 = "Ominous Mask"
    name = "Noelle"
    color = discord.Colour.gold()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/9/92/Character_Noelle_Card.jpg"
    weekly_boss = "Dvalin's Claw"
    book = "Resistance"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name = 'razor', aliases =['wolf'],help = "Displays asecnsion materials for Razor. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def razor(ctx, flags: str = None):
    gem = "Vajrada Amethyst"
    boss = "Lightning Prism"
    Local ="Wolfhook"
    Common1 = "Damaged Mask"
    Common2 = "Stained Mask"
    Common3 = "Ominous Mask"
    name = "Razor"
    color = discord.Colour.purple()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/6/68/Character_Razor_Card.jpg"
    weekly_boss = "Dvalin's Claw"
    book = "Resistance"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name = 'sucrose',help = "Displays ascension materials for Sucrose. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def sucrose(ctx, flags: str = None):
    gem = "Vayuda Turquoise"
    boss = "Hurricane Seed"
    Local ="Windwheel Aster"
    Common1 = "Whopperflower Nectar"
    Common2 = "Shimmering Nectar"
    Common3 = "Energy Nectar"
    name = "Sucrose"
    color = discord.Colour.green()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/2/22/Character_Sucrose_Card.jpg"
    weekly_boss = "Spirit Locket of Boreas"
    book = "Freedom"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
#todo, CHILDE!!!!
@bot.command(name = 'tartaglia', aliases =['childe','ajax'],help = "Displays asecnsion materials for Tartaglia. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def childe(ctx, flags: str = None):
    gem = "Varunada Lazurite"
    boss = "Cleansing Heart"
    Local ="Starconch"
    Common1 = "Recruit's Insignia"
    Common2 = "Sergeant's Insignia"
    Common3 = "Lieutenatn's Insignia"
    name = "Tartaglia"
    color = discord.Colour.blue()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/4/4c/Character_Tartaglia_Card.png"
    weekly_boss = "Shard of a Foul Legacy"
    book = "Freedom"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
#Traveler is a nasty case for talents. Based on which element he's resonated with, it changes the materials needed. Skip for now
#Traveler also doesn't have a local boss material so.... can't use ascension() and talent() on them
@bot.command(name = 'traveler', aliases =['mc','Aether','Lumine'],help = "Displays ascension materials for the Traveler. Replace [flags] with 'talentgeo' to see talent materials for Geo Traveler instead or 'talentanemo' to see talent materials for Anemo Traveler.")
async def traveler(ctx,  flags: str = None):
    
    gem = "Brilliant Diamond"
    Local ="Windwheel Aster"
    Common1 = "Damaged Mask"
    Common2 = "Stained Mask"
    Common3 = "Ominous Mask"
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talentgeo'):
            embed = talent_traveler("geo")
            await ctx.send(embed=embed)
        if(lowercase == 'talentanemo'):
            embed = talent_traveler("anemo")
            await ctx.send(embed=embed)   
    else:
        embed_asc = discord.Embed(title="Traveler",colour = discord.Colour.dark_gold())
        embed_asc.set_thumbnail(url ="https://static.wikia.nocookie.net/gensin-impact/images/c/cb/Character_Traveler_Introduction.png") 
        embed_asc.add_field(name="Ascension 1", value =f"1x {gem} Silver, 3x {Local}, 3x {Common1}, 20,000 Mora", inline= False)
        embed_asc.add_field(name="Ascension 2", value =f"3x {gem} Fragment, 10x {Local}, 15x {Common1}, 40,000 Mora ", inline = False)
        embed_asc.add_field(name="Ascension 3", value =f"6x {gem} Fragment, 20x {Local}, 12x {Common2}, 60,000 Mora ", inline = False)
        embed_asc.add_field(name="Ascension 4", value =f"3x {gem} Chunk, 30x {Local}, 18x {Common2}, 80,000 Mora", inline = False)
        embed_asc.add_field(name="Ascension 5", value =f"6x {gem} Chunk, 45x {Local}, 12x {Common3}, 100,000 Mora", inline = False)
        embed_asc.add_field(name="Ascension 6", value =f"6x {gem} Gemstone, 60x {Local}, 24x {Common3}, 120,000 Mora", inline = False)
        await ctx.send(embed=embed_asc)
@bot.command(name = 'venti',aliases = ['barabatos'],help = "Displays ascension materials for Venti. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def venti(ctx,  flags: str = None):
    gem = "Vayuda Turquoise"
    boss = "Hurricane Seed"
    Local ="Cecilia"
    Common1 = "Slime Condensate"
    Common2 = "Slime Secretions"
    Common3 = "Slime Concentrate"
    name = "Venti"
    color = discord.Colour.green()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/7/76/Character_Venti_Card.jpg"
    weekly_boss = "Tail of Boreas"
    book = "Ballad"
    
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name = 'xiangling', aliases = ['gouba'],help ="Displays ascension materials for Xiangling. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def gouba(ctx,  flags: str = None):
    gem = "Agnidus Agate"
    boss = "Everflame Seed"
    Local ="Jueyun Chili"
    Common1 = "Slime Condensate"
    Common2 = "Slime Secretions"
    Common3 = "Slime Concentrate"
    name = "Xiangling"
    color = discord.Colour.red()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/f/f1/Character_Xiangling_Card.jpg"
    weekly_boss = "Dvalin's Claw"
    book = "Dilligence"
    
    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name = 'xingqiu',help = "Displays ascension materials for Xingqiu. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def xingiqu(ctx,  flags: str = None):
    gem = "Varunada Lazurite"
    boss = "Cleansing Heart"
    Local ="Silk Flower"
    Common1 = "Damaged Mask"
    Common2 = "Stained Mask"
    Common3 = "Ominous Mask"
    name = "Xingqiu"
    color = discord.Colour.blue()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/c/c2/Character_Xingqiu_Card.jpg"
    weekly_boss = "Tail of Boreas"
    book = "Gold"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name = 'xinyan',help = "Displays ascension materials for Xinyan. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def xingyan(ctx, flags: str = None):
    gem = "Agnidus Agate"
    boss = "Everflame Seed"
    Local ="Violetgrass"
    Common1 = "Treasure Hoarder Insignia"
    Common2 = "Silver Raven Isnigia"
    Common3 = "Golden Raven Insignia"
    name = "Xinyan"
    color = discord.Colour.red()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/4/4c/Character_Xinyan_Card.jpeg"
    weekly_boss = "Tusk of Monoceros Caeli"
    book = "Gold"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
@bot.command(name = 'zhongli',aliases = ['rex lapis','morax'], help = "Displays ascension materials for Zhongli. Replace [flags] with 'talent' to see talent materials instead or 'all' to see both.")
async def zhongli(ctx, flags: str = None):
    gem = "Prithiva Topaz"
    boss = "Basalt Pillar"
    Local ="Cor Lapis"
    Common1 = "Slime Condensate"
    Common2 = "Slime Secretions"
    Common3 = "Slime Concentrate"
    name = "Zhongli"
    color = discord.Colour.gold()
    imagelink = "https://static.wikia.nocookie.net/gensin-impact/images/7/79/Character_Zhongli_Card.png"
    weekly_boss = "Tusk of Monoceros Caeli"
    book = "Gold"

    if(flags is not None):
        lowercase = flags.lower()
        lowercase = lowercase.strip()
        if(lowercase == 'talent'):
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
        if(lowercase == 'all'):
            embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
            embed = talent(name,book,weekly_boss,Common1,Common2,Common3,color,imagelink)
            await ctx.send(embed=embed)
    else:
        embed = ascension(name,gem,boss,Local,Common1,Common2,Common3,color,imagelink)
        await ctx.send(embed=embed)
#End of characters
bot.run(TOKEN)