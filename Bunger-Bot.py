from math import trunc
import re
import time
from typing import ItemsView
import discord
import random
from discord import message
from discord import channel
from discord.embeds import Embed
from discord.ext import commands
import json
import os
from discord.ext.commands import has_permissions
from discord.ext.commands import MissingPermissions
from discord.ext.commands import MissingRequiredArgument
from discord.utils import get

#from requests.api import delete

delmessages = []
Sconfmessages = []
Bconfmessages = []



#check if number command
def program():
    Trout = 0
    Cod = 0
    Bass = 0
    Crab = 0

  
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass


#1. Name (String)\n2. Description (String)\n3. Sellable (True/False)\n4. SellPrice (Number)\n5. Useable (True/False)\n6. BuyPrice (Number)

#Name, Description, sellable, Sellprice, Useable, Buyprice
fishitems = [
    {'Name': ':fish: Trout', 'Desc': 'A basic trout', 'Sellable': True, 'SellPrice': 75, 'Useable': False},
    {'Name': ':fish: Cod', 'Desc': 'A Basic Cod', 'Sellable': True, 'SellPrice': 70, 'Useable': False},
    {'Name': ':fish: Bass', 'Desc': 'Some sort of bass', 'Sellable': True, 'SellPrice': 85, 'Useable': False},
    {'Name': ':crab: Crab', 'Desc': 'How did you catch a crab', 'Sellable': True, 'SellPrice': 110, 'Useable': False},
    {'Name': ':blowfish: Pufferfish', 'Desc': 'P O F F E R', 'Sellable': True, 'SellPrice': 210, 'Useable': False},
    {'Name': ':tropical_fish: Tropical Fish', 'Desc': "A cool looking fish... Must be rare, I'd keep it personally", 'Sellable': True, 'SellPrice': 400, 'Useable': False},
    {'Name': ':crocodile: Crocidile', 'Desc': 'how... wh- w h a t', 'Sellable': True, 'SellPrice': 700, 'Useable': False},
    {'Name': ':shark: Shark', 'Desc': "Why's there a shark in this pond", 'Sellable': True, 'SellPrice': 550, 'Useable': False},
    {'Name': ':whale: Whale', 'Desc': "Jesus christ this pond isn't even big enough to fit a whale what", 'Sellable': True, 'SellPrice': 1500, 'Useable': False},
    {'Name': ':seal: Seal', 'Desc': 'Oh my lawd its him', 'Sellable': True, 'SellPrice': 400, 'Useable': False},
    {'Name': ':dolphin: Dolphin', 'Desc': 'Isa dolphin', 'Sellable': True, 'SellPrice': 500, 'Useable': False},
    {'Name': ':lobster: Lobster', 'Desc': 'fancy', 'Sellable': True, 'SellPrice': 150, 'Useable': False},
    {'Name': ':shrimp: Shrimp', 'Desc': 'very similar to the size of your di-', 'Sellable': True, 'SellPrice': 90, 'Useable': False},
    {'Name': ':octopus: Octopus', 'Desc': 'Now theres an octopus in this pond too?', 'Sellable': False, 'SellPrice': 0, 'Useable': False},
    {'Name': ':squid: Squid', 'Desc': 'I like eating the ink', 'Sellable': True, 'SellPrice': 220, 'Useable': False},
    {'Name': ':briefcase: Bag Of Cash', 'Desc': 'still in pretty good condition', 'Sellable': True, 'SellPrice': 1700, 'Useable': False},
    {'Name': ':gem: Comically Sized Diamond', 'Desc': 'wow this thing is big', 'Sellable': True, 'SellPrice': 1700, 'Useable': False},
    {'Name': ':hamburger: Soggy Bunger', 'Desc': 'Its all soggy :c', 'Sellable': True, 'SellPrice': 1, 'Useable': False}
]

def FindRatioedVals(vals):
    NewVals = []
    Total = 0

    for x in vals:
        Total += x

    for x in vals:
        NewVals.append(x / (Total / 100))

    return NewVals

def RunFishCatch():
    FishChances = random.choices(fishitems, weights = ( FindRatioedVals([50, 50, 50, 40, 40, 20, 30, 10, 3, 25, 25, 30, 55, 30, 30, 8, 8, 4]) ) )

    return FishChances[0]

async def SendErrorMessage(ctx, Title ="Error", Message="There was an error(default message)"):
    embed=discord.Embed(title="Command Error", color=0xa00a15)
    embed.add_field(name=Title, value=Message, inline=True)
    embed.set_footer(text="Error Message")
    await ctx.send(embed=embed)

#Trout Cod Bass Crab Pufferfish Tropical_Fish Crocodile Shark Whale Seal Dolphin Lobster Shrimp Octopus Squid Bag_Of_Cash Diamond Soggy_Bunger

#os.chdir("C:\\Users\\Luke\\Desktop\\Python VScode")
#os.chdir("C:\\Users\\divya\\Documents\\Desktop\\Python\\discord bot")
os.chdir("C:\\Users\\Luke\\Desktop\\Python VScode")


Bot_Name = "Bunger Bot"

async def getprefix(client,message):
    await check_prefix(message.guild,message)
    with open("Data.json", "r",) as f:
        guilds = json.load(f)
    return guilds[str(message.guild.id)]["Prefix"]

print(getprefix)

Bot = commands.Bot(case_insensitive=True, command_prefix=getprefix)
Bot.remove_command("help")

#Help command
@Bot.group(invoke_without_command=True)
async def help(ctx, type=None):
    
    if type == None:
        embed=discord.Embed(title="Help Pages", description="All the pages you can use for more info on this bot", color=0x0080ff)
        embed.set_author(name="Bunger Bot Help")
        embed.add_field(name="Economy", value="B#Help Economy", inline=True)
        embed.add_field(name="Utility", value="B#Help Utility", inline=True)
        embed.add_field(name="Admin/Setup", value="B#Help Admin", inline=True)
        embed.set_footer(text="Say any one to pull up the help page")
        await ctx.send(embed=embed)

    em=discord.Embed(title=" ", description=" ", color=0x804040)
    em.set_author(name="Bunger Bot Help:")
    
    if type.lower() == "economy":
        em.add_field(name="Work", value="Go to work and flip some Bungers! ", inline=False)
        em.add_field(name="Fish", value="Go fishing and randomly fish up one of the many fish in the sea or lake or whatever idk im not a fish", inline=False)
        em.add_field(name="Deposit {amount}", value="Deposit money from your wallet into your bank account to keep it nice and safe | (alias: dep)", inline=False)
        em.add_field(name="Withdraw {amount}", value="Take money from your bank to put it in your wallet | (aliases: with, wit)", inline=False)
        em.add_field(name="Balance", value="Check your bank & wallet balance | (alias: bal)", inline=False)
        em.add_field(name="Sell {item}", value="Sells the item you want to sell in exchange for Bungers!", inline=False)
        em.add_field(name="Inventory", value="Checks the items in your inventory | (alias: Inventory)", inline=False)
        em.add_field(name="Use {Item}", value="Use a certain item in your inventory", inline=False)
        em.add_field(name="Shop", value="Checks the server shop and displays all items", inline=False)
        em.add_field(name="TradeIn", value="If a certain channel has a trade offer, you can use this command, remove a certain amount of X item from your inventory, and get something in return.", inline=False)
        em.add_field(name="ChannelShop", value="Checks the shop dedicated to the channel you're in, if there is one", inline=False)
        em.add_field(name="ChannelShopBuy {Item}", value="Buys an item from a ChannelShop", inline=False)

    if type.lower() == "utility":
        em.add_field(name="Ping", value="Checks the ping between you and the bot", inline=False)
        em.add_field(name="Say {words}", value="Makes the bot say something", inline=False)

    if type.lower() == "admin":
        em.add_field(name="Purge {Mesage Amount}", value="Deletes a certain amount of messages in the channel you're in", inline=False)
        em.add_field(name="NewPrefix", value="Newprefix {newprefix} - Changes the default ", inline=False)
        em.add_field(name="ItemSetup {Item_Name, Item_Description, Sellable, SellPrice, Useable, Buy_Price, Item_Visible_In_Shop, Shop_Channel}", value="Creates a new item, for more info say B#Itemsetup", inline=False)
        em.add_field(name="ItemConfig {Item_To_Config, Old_Setting, New_Setting}", value="Changes a feature of an item such as name, description, price, etc.", inline=False)
        em.add_field(name="ItemModifier {Item_Name, Modifier, Adjustment1, Adjustment2, Adjustment3}", value="Adds a certain modifier, for more info use B#ItemModifier", inline=False)
        em.add_field(name="TradeInChannel {Item_Trading_In, Trade_In_Item_Amount, Channel_ID, Give_Item}", value="Sets up a Tradein, useable with B#TradeIn", inline=False)
        em.add_field(name="NewShop {Channel_ID}", value="Makes a shop only accesible to a specific channel", inline=False)
        em.add_field(name="SetFishingChannel {Channel_ID}", value="Makes it so you can only fish in a certain channel", inline=False)
        em.add_field(name="EditList {ItemName, Modifier, Adjustment1, Adjustment2, Adjustment3}", value="Edits a list used for the 'Scavenging' Modifier, say B#EditList for more info", inline=False)


    await ctx.send(embed=em)

print("SPACER -----------------------------------------------------")

#AddItem Function
async def AddItemToInventory(UserID, ItemName, AddAmnt, AddItem = None):
    inven = await getinven()
    inv = inven[str(UserID)]

    if not ItemName in inv:
        inv[ItemName] = AddItem
        inv[ItemName]["Amount"] = AddAmnt

    elif ItemName in inv:
        inv[ItemName]["Amount"] += AddAmnt

    if inv[ItemName]["Amount"] <= 0:
        inv.pop(ItemName)

    with open("InvData.json", "w") as f:
             json.dump(inven, f)


# Prefix saving
@Bot.command()
async def prefixcheck(ctx):
    message = ctx.message
    await check_prefix(message.guild, message)

    guilds = await get_guilds()
    guild = message.guild

    prefix = guilds[str(guild.id)]["Prefix"]


async def check_prefix(guild, message):
    # guilds = get_prefix_data() #<coroutine object get_prefix_data at 0x0000028A86789A40>
    guilds = await get_guilds()

    if str(guild.id) in guilds:
        prefix = guilds[str(guild.id)]["Prefix"]

    else:
        guilds[str(guild.id)] = {}
        guilds[str(guild.id)]["Prefix"] = "B#" 

    with open("Data.json", "w",) as f:
        json.dump(guilds, f)


async def get_guilds():
    with open("Data.json", "r",) as f:
        guilds = json.load(f)
    return guilds


# Bot Print Ready
@Bot.event
async def on_ready():
    print("Bot Be The Do Ready")
    await Bot.change_presence(activity=discord.Game("B#Help"))


# Secret amogus command
@Bot.command()
async def amogus(ctx):
    await ctx.send("Red sus.😳 Red suuuus.😳 I said red, sus, hahahahaha.😳 Why arent you laughing?😳 I just made a reference to the popular video game 'Among Us'! 😳How can you not laugh at it? 😳Emergeny meeting!😳 Guys, this here guy doesnt laugh at my funny Among Us memes! 😳Lets beat him to death! Dead body reported! Skip! Skip! Vote blue!😳 Blue was not an impostor😳. Among us in a nutshell hahahaha. 😳What?! Youre still not laughing your ass off? I made SEVERAL funny references to Among Us and YOU STILL ARENT LAUGHING??!!! Bruh. Ya hear that? Wooooooosh. Whats woooosh? Oh, nothing. Just the sound of a joke flying over your head. Whats that? You think im annoying? Kinda sus, bro. Hahahaha! Anyway, yea, gotta go do tasks. Hahahaha! funny amogus ahha")
    # ChangePrefix

# Ping command
@Bot.command()
async def ping(ctx):
    await ctx.send(f'Current ping: {round(Bot.latency * 1000)}ms')

# Purge Command
@Bot.command()
@has_permissions(administrator=True)
async def purge(ctx, amount=0):
    if amount == None or amount == 0:  # and :
        await ctx.send("Amount not recognized, please put a valid number.")
    elif amount != None and amount != 0:
        amount = amount + 1
        await ctx.channel.purge(limit=amount)

# Change Prefix command
@Bot.command(aliases=['newprefix', 'setprefix'])
async def changeprefix(ctx, *, usersPrefix):
    print(ctx, "IS THE CTX")
    Bot.command_prefix = usersPrefix

    with open("Data.json", "r",) as f:
        guilds = json.load(f)

    guild = ctx.guild

    guilds[str(guild.id)]["Prefix"] = str(usersPrefix)

    with open("Data.json", "w",) as f:
        json.dump(guilds, f)

    prefixjson = guilds[str(guild.id)]['Prefix']
    await ctx.send(f'Prefix successfully changed \nNew prefix is "{prefixjson}"')

@Bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'{ctx.author.mention}, This command is on cooldown, you can use it in: `{round(error.retry_after, 2)}` Seconds')

# Work Command
@Bot.command()
@commands.cooldown(1, 25, commands.BucketType.user)
async def work(ctx):
    await makeacc(ctx)
    users = await getusers()

    if str(ctx.author.id) in users:
     winamnt = random.randint(50,185)
     users[str(ctx.author.id)]["wallet"] += winamnt

     with open("Data.json", "w") as f:
          json.dump(users, f)

     users = await getusers() 

     new_wallet = users[str(ctx.author.id)]["wallet"] 
     new_bank = users[str(ctx.author.id)]["bank"] 
     winembed = discord.Embed(title=f"{ctx.author.display_name}'s Winnings", color=discord.Color.blurple())
     winembed.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar_url)
     winembed.add_field(name="Bungers Made", value=f":hamburger:{str(winamnt*1.5)} Bungers Were flipped, and :hamburger:***{winamnt}*** Bungers were kept!", inline=False)
     winembed.add_field(name="Total Bungers", value=f":hamburger:{new_wallet} in wallet\n:hamburger:{new_bank} In bank", inline=False)
     
     await ctx.send(embed=winembed)

#deposit comand
@Bot.command(aliases=['deposit', 'depo'])
@commands.cooldown(1, 3, commands.BucketType.user)
async def dep(ctx, num):
    
    await makeacc(ctx)
    users = await getusers()

    if num == "all":
        num = inwallet = users[str(ctx.author.id)]["wallet"]
        num = round(num)
    if num == "half":
        num = inwallet = users[str(ctx.author.id)]["wallet"] / 2 
        num = round(num)

    inwallet = users[str(ctx.author.id)]["wallet"]
    inbank = users[str(ctx.author.id)]["bank"]

    if num != 0 and inwallet >= float(num):
       users[str(ctx.author.id)]["wallet"] -= float(num)
       users[str(ctx.author.id)]["bank"] += float(num)
       with open("Data.json", "w") as f:
          json.dump(users, f)

       users = await getusers()
       inwallet = users[str(ctx.author.id)]["wallet"]
       inbank = users[str(ctx.author.id)]["bank"]

       winembed = discord.Embed(title=f"{ctx.author.display_name}'s Balance", color=discord.Color.blurple(), description = f"Succesfully deposited :hamburger:{num} into the bank!")
       winembed.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar_url)
       winembed.add_field(name="In Wallet", value=f":hamburger:{inwallet}", inline=False)
       winembed.add_field(name="In Bank", value=f":hamburger:{inbank}", inline=False)

       await ctx.send(embed=winembed)
    else:
        await ctx.send("You do not have enough money to do that")

#withdraw comand
@Bot.command(aliases=['wit', 'with'])
@commands.cooldown(1, 3, commands.BucketType.user)
async def withdraw(ctx, num):
    await makeacc(ctx)
    users = await getusers()

    if num == "all":
        num = inbank = users[str(ctx.author.id)]["bank"]
        num = round(num)
    if num == "half":
        num = inbank = users[str(ctx.author.id)]["bank"] / 2 
        num = round(num)

    inwallet = users[str(ctx.author.id)]["wallet"]
    inbank = users[str(ctx.author.id)]["bank"]

    if num != 0 and inbank >= float(num):
       users[str(ctx.author.id)]["wallet"] += float(num)
       users[str(ctx.author.id)]["bank"] -= float(num)
       with open("Data.json", "w") as f:
          json.dump(users, f)

       users = await getusers()
       inwallet = users[str(ctx.author.id)]["wallet"]
       inbank = users[str(ctx.author.id)]["bank"]

       winembed = discord.Embed(title=f"{ctx.author.display_name}'s Balance", color=discord.Color.blurple(), description = f"Succesfully withdrew :hamburger:{num}!")
       winembed.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar_url)
       winembed.add_field(name="In Wallet", value=f":hamburger:{inwallet}", inline=False)
       winembed.add_field(name="In Bank", value=f":hamburger:{inbank}", inline=False)

       await ctx.send(embed=winembed)
    else:
        await ctx.send("You do not have enough money to do that")

#checkbal command
@Bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def bal(ctx):
    await makeacc(ctx)

    users = await getusers()

    inwallet = users[str(ctx.author.id)]["wallet"]
    inbank = users[str(ctx.author.id)]["bank"]

    winembed = discord.Embed(title=f"{ctx.author.display_name}'s Balance", color=discord.Color.blurple())
    winembed.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar_url)
    winembed.add_field(name="In Wallet", value=f":hamburger:{inwallet}", inline=False)
    winembed.add_field(name="In Bank", value=f":hamburger:{inbank}", inline=False)

    await ctx.send(embed=winembed)

#fish command
@Bot.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def fish(ctx):
    await makeinv(ctx)
    guilds = await get_guilds()
    inv = await getinven()
    inv = inv[str(ctx.author.id)]


    if "Fishing Rod :fishing_pole_and_fish:" in inv and ("Fishing_Channel" not in guilds[str(ctx.guild.id)] or ctx.channel.id == guilds[str(ctx.guild.id)]["Fishing_Channel"]):

        randnum = RunFishCatch()

        await AddItemToInventory(str(ctx.author.id), randnum['Name'], 1, randnum)

        await ctx.send(f"{ctx.author.mention}, You feel a bite... You Reel in... \nYou caught a **{randnum['Name']}**!")

    elif "Fishing_Channel" in guilds[str(ctx.guild.id)] and guilds[str(ctx.guild.id)]["Fishing_Channel"] != ctx.channel.id:
        await SendErrorMessage(ctx, "Wrong Channel", f"You must be in '{Bot.get_channel(guilds[str(ctx.guild.id)]['Fishing_Channel'])}' to use B#fish")

    else:
        await ctx.send(f"{ctx.author.mention}, You don't have a fishing rod,\nYou can buy one using `b#shop`")
 
#checkinv command
@Bot.command(aliases=["inventory"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def inv(ctx):
    
    await makeinv(ctx)
    
    emb = discord.Embed(title=f"{ctx.author.display_name}'s Inventory", color=discord.Color.blurple())
    emb.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar_url)

    inven = await getinven()
    print(ctx.author.id)
    inv = inven[str(ctx.author.id)]
    num = 0

    for x in inven[str(ctx.author.id)]:

        if "Amount" in inv[x] and inv[x]["Amount"] > 1 and inv[x]["Useable"] == True:
            emb.add_field(name=f"[{num + 1}]: {x} - `Useable`", value=f"--<Amount: {inv[x]['Amount']}>--\n{inv[x]['Desc']}", inline=False)

        elif "Amount" in inv[x] and inv[x]["Amount"] > 1 and inv[x]["Useable"] != True:
            emb.add_field(name=f"[{num + 1}]: {x}", value=f"--<Amount: {inv[x]['Amount']}>--\n{inv[x]['Desc']}", inline=False)

        elif "Amount" in inv[x] and inv[x]["Amount"] == 1 and inv[x]["Useable"] == True:
            emb.add_field(name=f"[{num + 1}]: {x} - `Useable`", value=f"--<Amount: {inv[x]['Amount']}>--\n{inv[x]['Desc']}", inline=False)

        else:
            emb.add_field(name=f"[{num + 1}]: {x}", value=f"{inv[x]['Desc']}", inline=False)
        num = num + 1

    await ctx.send(embed=emb)

#make inventory thing
async def makeinv(ctx):
    inven = await getinven()

    if str(ctx.author.id) in inven:
        pass

    else:
          inven[str(ctx.author.id)] = {}
          inven[str(ctx.author.id)] = {}
          with open("InvData.json", "w") as f:
             json.dump(inven, f)

#sell command
@Bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def sell(ctx, *, item):
    await makeinv(ctx)
    await makeacc(ctx)
    inven = await getinven()

    FoundItem = False
    FoundNum = None
    Sellingitem = None
    Sellable = None
    Num = 0

    isnum = is_number(item)

    if isnum == True:
        item = round(float(item))
        print("wasNum")
        print(isnum, item)

    values = []
    for x in inven[str(ctx.author.id)]:
        values.append(inven[str(ctx.author.id)][x])
        print(inven[str(ctx.author.id)])

    

    for x in values:
        print(isnum)
        if isnum == None and x["Name"].lower().find(item.lower()) != -1:

            #changes "Sebllable" variable to false if it is false
            if x["Sellable"] == False:
                Sellable = False
            
            #Runs if can be sold
            if x["Sellable"] == True:
                Sellable = True
                FoundItem = True
                FoundNum = Num
                Sellingitem = values[FoundNum]
            break

        elif isnum == True and values[round(item - 1)] != None:

            print("str")
            
            #Changes sellable to "False" but still processes
            if values[round(item - 1)]["Sellable"] == False:
                Sellable = False

            print("pass")
            
            #Runs if can be sold
            if values[round(item - 1)]["Sellable"] == True:
                Sellable = True
                FoundItem = True
                FoundNum = item - 1
                print("br")
                Sellingitem = values[FoundNum]
                print("k")
            break

        Num = Num + 1

    #If the item is false/unsellable
    print(Sellingitem, "Is the selling item")
    if FoundItem == False and Sellable == None:
        msg = await ctx.send(f"{ctx.author.mention}, Item `not found`")
        await msg.add_reaction("❌")
        msgreaction = "❌"
        sender = ctx.author
        delmessages.append([msg, msgreaction, sender])

    elif Sellable == False:
        msg = await ctx.send(f"{ctx.author.mention}, Item `Unsellable`")
        await msg.add_reaction("❌")
        msgreaction = "❌"
        sender = ctx.author
        delmessages.append([msg, msgreaction, sender])

    else: 
        if values[FoundNum]["Sellable"] != None:
        
            print("k")
            users = await getusers()
            print("wrt")
            name = values[FoundNum]["Name"]
            print("hr")
            price = int(values[FoundNum]["SellPrice"])
            print("almos")

            

            newbal = users[str(ctx.author.id)]["wallet"]
            msg = await ctx.send(f'{ctx.author.mention}, Are you sure you want to sell "{name}" for :hamburger:{price} Bungers?')
            #msg = await ctx.send(f"Succesfully sold {name} for :hamburger:{price} Bungers!\nNew Wallet Balance: :Hamburger:***{newbal}*** Bungers")
            await msg.add_reaction("✔️")
            await msg.add_reaction("❌")

            decreact = "❌"
            confreact = "✔️"
            sender = ctx.author
            print("k")
            Sconfmessages.append([msg, confreact, decreact , sender, name, price, FoundNum, Sellingitem])
            print("dun")
        else:
            await ctx.send("Item not sellable")
#msg, confreact, decreact , sender, name, price, FoundNum, BuyingItem, guild, othername

#Reactions Handler       
@Bot.event
async def on_reaction_add(reaction, user):

    #Deletes certain messages
    num = 0
    for x in delmessages:
        if x[0] == reaction.message and x[2] == user and str(reaction) == x[1]:
            delmessages.remove(delmessages[num])
            await reaction.message.delete()
            break
        num = num + 1

    num = 0
    for x in Sconfmessages:
        inven = await getinven()

        if x[3] == user and str(x[4]) in inven[str(user.id)]:
          sellthing = inven[str(user.id)][x[4]]

          if x[0] == reaction.message and str(reaction) == x[1] and str(x[4]) in inven[str(user.id)] and sellthing["Name"] == x[4]:
             users = await getusers()
             inven = await getinven()

             users[str(user.id)]["wallet"] += float(inven[str(user.id)][x[4]]["SellPrice"])

             with open("Data.json", "w") as f:
                 json.dump(users, f)
            
             Inv = inven[str(user.id)]

             #removes item
             await AddItemToInventory(str(user.id), x[4], -1)
            
             users = await getusers()
             bal = users[str(user.id)]["wallet"]
             await reaction.message.edit(content=f'{user.mention}\nSuccesfully sold "{x[4]}" for :hamburger:`{float(x[5])}` Bungers!\nNew Wallet Balance: :hamburger:{int(bal)} Bungers!')
             Sconfmessages.remove(Sconfmessages[num])
            

          elif x[0] == reaction.message and x[3] == user and str(reaction) == x[2]:
             Sconfmessages.remove(Sconfmessages[num])
             await reaction.message.edit(content="Sell Action Canceled")
    
    num = 0
    for x in Bconfmessages:
        print("1")
        #Gets all the values -- ctx, Message, ConfirmReaction, DeclineReation, Price, Name, BuyThing
        ctx = x[0]
        msg = x[1]
        ConfReact = x[2]
        DecReact = x[3]
        Price = x[4]
        Name = x[5]
        Buything = x[6]
        #got all the values
        print("2")

        shops = await getshops()
        users = await getusers()
        inven = await getinven()
        print(Name)

        if reaction.message == msg and ctx.author == user:
            print("5")
            
            if str(reaction) == ConfReact and users[str(ctx.author.id)]["wallet"] >= Price:
                print("yeah")

                #Removes money
                users[str(ctx.author.id)]["wallet"] -= Price
                
                #Dumps data
                with open("Data.json", "w") as f:
                    json.dump(users, f)
                
                #adds it to the inventory and dumps data
                print(inven[str(ctx.author.id)])
                
                #gets table of inv keys
                invkeys = []
                for k in inven[str(ctx.author.id)].keys():
                    invkeys.append(k.lower())
                
                #if its not found, it adds it, otherwise it makes a new one with a number at the end
                if inven[str(ctx.author.id)].get(Buything["Name"].lower()) == None:
                    await AddItemToInventory(str(user.id), Buything["Name"], 1, Buything)
                    print("1")

                #adds number and adds it to prevent overwriting
                elif inven[str(ctx.author.id)].get(Buything["Name"].lower()) != None:
                    fnum = 1
                    print("1")
                    while inven[str(ctx.author.id)].get( str(Buything['Name'].lower()) + str(fnum) ) != None:
                        fnum = fnum + 1
                        print("1")
                    
                    #Makes the new name and adds it
                    NewName = str(Buything['Name'].lower()) + str(fnum)
                    print(Buything["Name"])
                    await AddItemToInventory(str(user.id), Buything["Name"], 1, Buything)
                    print("1")

                #Gets balance and sends success message
                bal = users[str(user.id)]["wallet"]
                await reaction.message.edit(content=f'{user.mention}\nSuccesfully bought "{Name}" for :hamburger:{Price} Bungers!\nNew Wallet Balance: :hamburger:{bal} Bungers!')
                Bconfmessages.remove(Bconfmessages[num])

                Snum = -1
                for i in x:
                    Snum += 1
                
                if Snum >= 7 and x[7] == True:
                    await reaction.message.delete()
                    
                    channel = await ctx.author.create_dm()
                    await channel.send(content=f'{user.mention}\nSuccesfully bought "{Name}" for :hamburger:{Price} Bungers!\nNew Wallet Balance: :hamburger:{bal} Bungers!')

                    await ctx.message.delete()

            #Not enough money message
            elif users[str(user.id)]["wallet"] < Price:
                await reaction.message.edit(content=f"{user.mention}, Not enough :hamburger:`Bungers` to purchase this item\nhaha broke lol")

            #Cancel message
            elif msg == reaction.message and ctx.author == user and str(reaction) == DecReact:
                Bconfmessages.remove(Bconfmessages[num])
                await reaction.message.edit(content="Sell Action Canceled")

                Snum = -1
                for i in x:
                    Snum += 1
                
                if Snum >= 7 and x[7] == True:
                    await reaction.message.delete()
                    
                    channel = await ctx.author.create_dm()
                    await channel.send(content='Sell Action Canceled')

                    await ctx.message.delete()

    num = num + 1

#Check Shop command
@Bot.command()
async def shop(ctx):
    await makeshop(ctx)
    await makeacc(ctx)

    emb = discord.Embed(color=discord.Color.blurple())
    emb.set_author(name="Server Shop", icon_url = ctx.guild.icon_url)

    shops = await getshops()
    guilds = await get_guilds()

    num = 0
    for x in shops[str(ctx.guild.id)]:

        if "ShowInShop" not in shops[str(ctx.guild.id)][x] or shops[str(ctx.guild.id)][x]['ShowInShop'] == True:
            emb.add_field(name=f"[{num + 1}]: {shops[str(ctx.guild.id)][x]['Name']} - :hamburger:{shops[str(ctx.guild.id)][x]['BuyPrice']}", value = shops[str(ctx.guild.id)][x]['Desc'], inline=False)
            num = num + 1

    emb.set_footer(text=f"Buy items using the 'B#buy' command! || you have x{int(guilds[str(ctx.author.id)]['wallet'])} Bungers")
    await ctx.send(embed=emb)

async def addmessagemdeletebutton(ctx, msg):
    #adds reactiong
    await msg.add_reaction("❌")
    delmessages.append([msg, "❌", ctx.author])

#Buy Command
@Bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def Buy(ctx, *, item):

    NewItem = None
    await makeshop(ctx)
    await makeinv(ctx)
    await makeacc(ctx)
    shops = await getshops()
    users = await getusers()

    #formats all items into a table
    values = []
    for x in shops[str(ctx.guild.id)].keys():
        if "ShowInShop" not in shops[str(ctx.guild.id)][x] or shops[str(ctx.guild.id)][x]["ShowInShop"] == True:
            values.append(x)

    if is_number(item) == True:
        print(values)

    if is_number(item) != True:
        for x in values:
            if x.lower().find(item.lower()) != -1:
                NewItem = x

    #if the item is in the shop

    if NewItem in shops[str(ctx.guild.id)]:
        
        print(NewItem, item)
        if "ShowInShop" not in shops[str(ctx.guild.id)][NewItem] or shops[str(ctx.guild.id)][NewItem]["ShowInShop"] == True:

            #gets variables
            Name = shops[str(ctx.guild.id)][NewItem]["Name"]
            Price = shops[str(ctx.guild.id)][NewItem]["BuyPrice"]
            #got variables

            msg = await ctx.send(f'{ctx.author.mention}, Are you sure you want to buy "{Name}" for :hamburger:{Price} Bungers?')
            await msg.add_reaction("✔️")
            await msg.add_reaction("❌")

            Bconfmessages.append([ctx, msg, "✔️", "❌", Price, Name, shops[str(ctx.guild.id)][NewItem]])

        else:
            delmes = await ctx.send("Item was not found")
            await addmessagemdeletebutton(ctx, delmes)

    #Does this if number
    elif is_number(item) == True and values[int(item) - 1] != None:
        print("ok")
        #gets item 
        item = shops[str(ctx.guild.id)][values[int(item) - 1]]

        #gets variables
        Name = item["Name"]
        Price = item["BuyPrice"]
        #got variables
        print("ok")
        if "ShowInShop" not in shops[str(ctx.guild.id)][Name] or shops[str(ctx.guild.id)][Name]["ShowInShop"] == True:
            print("ok")
            msg = await ctx.send(f'{ctx.author.mention}, Are you sure you want to buy "{Name}" for :hamburger:{Price} Bungers?')
            await msg.add_reaction("✔️")
            await msg.add_reaction("❌")

            Bconfmessages.append([ctx, msg, "✔️", "❌", Price, Name, item])
        
        else:
            delmes = await ctx.send("Item not found")
            await addmessagemdeletebutton(ctx, delmes)

    elif is_number(item) == False and item not in shops[str(ctx.guild.id)]:
        #sends message with a delete button
        delmes = await ctx.send("Item not found")
        await addmessagemdeletebutton(ctx, delmes)


#Itemsetup Command
@Bot.command()
@has_permissions(administrator=True)
async def ItemSetup(ctx, Name, Desc, Sellable, SellPrice, Useable, BuyPrice, BuyInShop, ChannelID=None):
    guilds = await get_guilds()
    await makeshop(ctx)
    shops = await getshops()

    print(Name, Desc, Sellable, SellPrice, Useable, BuyPrice, BuyInShop, ChannelID)

    if ChannelID == None:
        if type(Name) == str and type(Desc) == str and type(Sellable) == bool or Sellable == "True" or Sellable == "true" or Sellable == "False" or Sellable == "false" and type(SellPrice) == int and type(Useable) == bool or Useable == "True" or Useable == "true" or Useable == "False" or Sellable == "false" and type(BuyPrice) == int and BuyInShop.lower() == "false" or BuyInShop.lower() == "true":
            print(ChannelID)
            #Changes Sellable to true/false if it was originally a string
            if Sellable == "True" or Sellable == "true":
                Sellable = True 
            elif Sellable == "False" or Sellable == "false":
                Sellable = False
            
            #Changes Useable to true/false if it was originally a string
            if Useable == "True" or Useable == "true":
                Useable = True    
            elif Useable == "False" or Useable == "false":
                Useable = False

            if BuyInShop.lower() == "true":
                BuyInShop = True

            elif BuyInShop.lower() == "false":
                BuyInShop = False

            if Name in shops[str(ctx.guild.id)]:
                em = discord.Embed(title="Item Error", color=discord.Color.dark_red())
                em.add_field(name="Item already exists", value=f'The item {Name} already exists lol', inline=False)
                await ctx.send(embed=em)

            else:
                NewItem = {"Name" : str(Name), "Desc" : str(Desc), "Sellable" : Sellable, "SellPrice" : int(SellPrice), "Useable" : Useable, "BuyPrice" : int(BuyPrice), "ShowInShop" : BuyInShop}
                shops[str(ctx.guild.id)][Name] = NewItem

            await ctx.send("Added loool")

            with open("Shopdata.json", "w") as f:
                json.dump(shops, f)

    elif ChannelID != None and ChannelID in guilds[str(ctx.guild.id)]["ChannelShops"] and type(Name) == str and type(Desc) == str and type(Sellable) == bool or Sellable == "True" or Sellable == "true" or Sellable == "False" or Sellable == "false" and type(SellPrice) == int and type(Useable) == bool or Useable == "True" or Useable == "true" or Useable == "False" or Sellable == "false" and type(BuyPrice) == int and BuyInShop.lower() == "false" or BuyInShop.lower() == "true":
        print("yeah yeah")
        #Changes Sellable to true/false if it was originally a string
        if Sellable == "True" or Sellable == "true":
            Sellable = True 
        elif Sellable == "False" or Sellable == "false":
            Sellable = False
        
        #Changes Useable to true/false if it was originally a string
        if Useable == "True" or Useable == "true":
            Useable = True    
        elif Useable == "False" or Useable == "false":
            Useable = False

        if BuyInShop.lower() == "true":
            BuyInShop = True

        elif BuyInShop.lower() == "false":
            BuyInShop = False

        if Name in guilds[str(ctx.guild.id)]["ChannelShops"][ChannelID]:
            em = discord.Embed(title="Item Error", color=discord.Color.dark_red())
            em.add_field(name="Item already exists", value=f'The item {Name} already exists lol', inline=False)
            await ctx.send(embed=em)

        else:
            NewItem = {"Name" : str(Name), "Desc" : str(Desc), "Sellable" : Sellable, "SellPrice" : int(SellPrice), "Useable" : Useable, "BuyPrice" : int(BuyPrice), "ShowInShop" : BuyInShop}
            guilds[str(ctx.guild.id)]["ChannelShops"][ChannelID][Name] = NewItem

        await ctx.send("Added loool")

        with open("Data.json", "w") as f:
            json.dump(guilds, f)

DiffVars = {
    "name" : "String", #0
    "desc" : "String", #1
    "description" : "String", #1
    "sellable" : "Bool", #2
    "sellprice" : "Number", #3
    "useable" : "Bool", #4
    "buyprice" : "Number" #5
}

VarNums = {
    "name" : 0, #0
    "desc" : 1, #1
    "description" : 1, #1
    "sellable" : 2, #2
    "sellprice" : 3, #3
    "useable" : 4, #4
    "buyprice" : 5 #5
}

#Detects flaws and stuf
def GetNewSettingError(givensetting, Word):

    print(givensetting)
    #Both sides of bool
    if givensetting == "Bool" and Word.lower() not in {"false":False, "true":True}:
        return "BoolNameError"
    elif givensetting == "Bool" and Word.lower() in {"false":False, "true":True}:
        return ["Bool", bool(Word)]
                        
    #Both sides of number
    if givensetting == "Number" and Word.isdigit() == True:
        return ["Number", int(Word)]
    elif givensetting == "Number" and Word.isdigit() != True:
        return "NumberNameError"

    #Both sides of string
    if givensetting == "String" and isinstance(Word, str) == True:
        return ["String", Word]
    elif givensetting == "String" and isinstance(Word, str) != True:
        return "StringNameError"

#Itemconfig
@Bot.command()
@has_permissions(administrator=True)
async def ItemConfig(ctx, Name, Setting, Newsetting):
    #makes shop if it isnt there, and gets shops
    await makeshop(ctx)
    shops = await getshops()

    
    
    #If the name is found it will continue
    if shops[str(ctx.guild.id)].get(Name) != None:

        #Makes sure the setting is an actual changeable setting
        if Setting.lower() in DiffVars:

            #gets the setting in the table
            givensetting = DiffVars[Setting.lower()]

            #Does this if nothing is wrong
            if GetNewSettingError(givensetting, Newsetting) != "StringNameError" and GetNewSettingError(givensetting, Newsetting) != "NumberNameError" and GetNewSettingError(givensetting, Newsetting) != "BoolNameError":
                Newsetting = GetNewSettingError(givensetting, Newsetting)[1]
                #Changes and writes it in
                shops[str(ctx.guild.id)].get(Name)[VarNums[Setting.lower()]] = Newsetting

                with open("Shopdata.json", "w") as f:
                    json.dump(shops, f)

                await ctx.send(f"{ctx.author.mention}, successfully changed `{Name}'s` property of `{Setting}` into `{Newsetting}`!")

            
            #Sends the String error message
            elif GetNewSettingError(givensetting, Newsetting) == "StringNameError":
                em = discord.Embed(title="NewSetting Error", color=discord.Color.dark_red())
                em.add_field(name="String error", value=f'A string value is legit just words, so if you want to change a `description` for example, you could put a single word such as `Pan` but if it is more than just one word you must use parenthesis `"this is a pan"`', inline=False)
                await ctx.send(embed=em)
            
            #Sends the Number error message
            elif GetNewSettingError(givensetting, Newsetting) == "NumberNameError":
                em = discord.Embed(title="NewSetting Error", color=discord.Color.dark_red())
                em.add_field(name="Number error", value=f'A Number value is a number, so if you want to change a `BuyPrice` for example, you could put `any number`, such as `"850"` This goes with every number', inline=False)
                await ctx.send(embed=em)
            
            #Sends the Bool error message
            elif GetNewSettingError(givensetting, Newsetting) == "BoolNameError":
                em = discord.Embed(title="NewSetting Error", color=discord.Color.dark_red())
                em.add_field(name="Boolean error", value=f'A Boolean is a `True/False` statement so if you want to change the `Useable` property on an item for example, you could put any Bool, such as `"True"` or `"False"`', inline=False)
                await ctx.send(embed=em)

            
        #If Setting not found it sends error message
        else:
            #Makes error embed and sends it
            em = discord.Embed(title="NewSetting Error", color=discord.Color.dark_red())
            em.add_field(name="Setting not found", value=f"Setting of **'{str(Setting)}'** was not found \n`below is a list of settings you can change tho lol`", inline=False)
            em.add_field(name="Setting List", value=" `Name` *(String)*\n `Description` *(String)*\n `Sellable` *(True/False)*\n `SellPrice` *(Number)*\n `Useable` *(True/False)*\n `BuyPrice` *(Number)*", inline=False)
            await ctx.send(embed=em)

    #If name not found it sends error message
    else:
        #Makes error embed and sends it
        em = discord.Embed(title="", color=discord.Color.dark_red())
        em.add_field(name="Item not found", value="`Must be exact name with correct capitilazation`", inline=False)
        await ctx.send(embed=em)

#ItemModifier Command
@Bot.command()
@has_permissions(administrator=True)
async def ItemModifier(ctx, ItemName, Modifier, Adjustment1 = None, Adjustment2 = None, Adjustment3 = None):
    #makes shop if it isnt there, and gets shops\

    await makeshop(ctx)
    shops = await getshops()

    Modifiers = {
        "scavenging",
        "role giving",
        "role removing",
        "message sending",
        "destroying"
    }


    guilds = await get_guilds()

    print("1")
    if shops[str(ctx.guild.id)].get(ItemName) != None and Modifier.lower() in Modifiers:
        #Valid Syntax
        print("2")


        if Modifier.lower() == "scavenging" and Adjustment1 != None and Adjustment2 != None and is_number(Adjustment2) == True: # and Adjustment1.lower() not in guilds[str(ctx.guild.id)]["ChanceLists"]:
            guilds = await get_guilds()
            print("4")

            if "ChanceLists" not in guilds[str(ctx.guild.id)]:
                guilds[str(ctx.guild.id)]["ChanceLists"] = {}

                with open("Data.json", "w") as f:
                    json.dump(guilds, f)

            guilds = await get_guilds()

            guilds[str(ctx.guild.id)]["ChanceLists"][Adjustment1.lower()] = []
            shops[str(ctx.guild.id)][ItemName]["scavenging"] = Adjustment1.lower()
            shops[str(ctx.guild.id)][ItemName]["scavengingcooldown"] = float(Adjustment2)
            shops[str(ctx.guild.id)][ItemName]["scavengingcdlastuse"] = time.time()
            shops[str(ctx.guild.id)][ItemName]["Useable"] = True

            with open("Shopdata.json", "w") as f:
                json.dump(shops, f)

            with open("Data.json", "w") as f:
                json.dump(guilds, f)

            print("5")

            await ctx.send("Ight the list was made")

        elif Modifier.lower() == "scavenging" and Adjustment1 == None and Adjustment1.lower() not in guilds[str(ctx.guild.id)]["ChanceLists"]:
            await SendErrorMessage(ctx, "No 1st Modifier Input", "You need to put a name for the new list to be created ")

        elif Modifier.lower() == "scavenging" and Adjustment1 != None and Adjustment2 == None and Adjustment1.lower() in guilds[str(ctx.guild.id)]["ChanceLists"]:
            await SendErrorMessage(ctx, "No 2nd Modifier Input", "You need to put a cooldown (in seconds) for the second variable")

        elif Modifier.lower() == "scavenging" and Adjustment1 != None and Adjustment1.lower() not in guilds[str(ctx.guild.id)]["ChanceLists"]:
            await ctx.send(f"{ctx.author.mention}, This list already exists")


        elif Modifier.lower() == "role giving" and Adjustment1 != None and discord.utils.get(ctx.guild.roles, id=int(Adjustment1)) != None:

            shops[str(ctx.guild.id)][ItemName]["role giving"] = int(Adjustment1)
            shops[str(ctx.guild.id)][ItemName]["Useable"] = True

            with open("Shopdata.json", "w") as f:
                json.dump(shops, f)

            with open("Data.json", "w") as f:
                json.dump(guilds, f)

            print("5")

            await ctx.send("Ight the list was made")

        elif Modifier.lower() == "role giving" and Adjustment1 == None:
            await SendErrorMessage(ctx, "No Role Given", "You need to put a role ID to give to the user")

        elif Modifier.lower() == "role giving" and Adjustment1 != None and discord.utils.get(ctx.guild.roles, id=Adjustment1) != None:
            await SendErrorMessage(ctx, "Invalid ID", "The given ID is an invalid role ID")


        elif Modifier.lower() == "destroying":
            shops[str(ctx.guild.id)][ItemName]["destroying"] = True
            shops[str(ctx.guild.id)][ItemName]["Useable"] = True

            with open("Shopdata.json", "w") as f:
                json.dump(shops, f)

            with open("Data.json", "w") as f:
                json.dump(guilds, f)
        
@ItemModifier.error
async def Item_Modifier_Error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):

        embed=discord.Embed(title="Item Modifier List", description="Different modifiers you can add to items to make them useable")
        embed.add_field(name="Scavenging", value="Things like a fishing rod, where you can use the item and get a random item in return from a range of different items", inline=True)
        embed.add_field(name="Role Giving", value="Gives the user a role when used", inline=True)
        embed.add_field(name="Role Removing", value="Removes a role if the user has it when used", inline=True)
        embed.add_field(name="Message Sending", value="Sends a message when used", inline=True)
        embed.add_field(name="Destroying", value="Item dissapears from the inventory after use", inline=True)
        embed.set_footer(text="Item Modifiers")

        await ctx.send(embed=embed)
            

#1. Name (String)\n2. Description (String)\n3. Sellable (True/False)\n4. SellPrice (Number)\n5. Useable (True/False)\n6. BuyPrice (Number)
@Bot.command()
@has_permissions(administrator=True)
async def editlist(ctx, List_Name, NewItemName, ItemChance, ItemDescription, ItemSellable, ItemSellPrice, FromShop=None):
    guilds = await get_guilds()
    shops = await getshops()

    print(List_Name, NewItemName, ItemChance, ItemDescription, ItemSellable, ItemSellPrice)

    if FromShop != None and List_Name.lower() in guilds[str(ctx.guild.id)]["ChanceLists"] and NewItemName in shops[str(ctx.guild.id)]:
        Table = [shops[str(ctx.guild.id)][NewItemName], float(ItemChance)]

        guilds[str(ctx.guild.id)]["ChanceLists"][List_Name.lower()].append(Table)
        with open("Data.json", "w") as f:
            json.dump(guilds, f)

        await ctx.send("all done")

    elif List_Name.lower() in guilds[str(ctx.guild.id)]["ChanceLists"] and is_number(ItemChance) == True and type(NewItemName) == str and type(ItemDescription) == str and ItemSellable.lower() == "true" or ItemSellable.lower() == "false" and is_number(ItemSellPrice) == True:
        print("1")
        Table = [{'Name' : NewItemName, 'Desc' : ItemDescription, 'Sellable' : ItemSellable, "SellPrice" : ItemSellPrice, 'Sellable' : False, 'Useable' : False}, float(ItemChance)]
        guilds[str(ctx.guild.id)]["ChanceLists"][List_Name.lower()].append(Table)

        with open("Data.json", "w") as f:
            json.dump(guilds, f)

        await ctx.send("all done")

    elif List_Name.lower() not in guilds[str(ctx.guild.id)]["ChanceLists"]:
        await SendErrorMessage(ctx, "Wrong Name", "This is not a valid name for any existing list")

    elif List_Name.lower() in guilds[str(ctx.guild.id)]["ChanceLists"] and is_number(ItemChance) != True:
        await SendErrorMessage(ctx, "Not A Number", "The 'ItemChance' Section needs to be a number")

    elif List_Name.lower() in guilds[str(ctx.guild.id)]["ChanceLists"] and is_number(ItemChance) == True and type(NewItemName) != str:
        await SendErrorMessage(ctx, "Not A String", "The 'ItemName' Section needs to be a String made up of words")

    elif List_Name.lower() in guilds[str(ctx.guild.id)]["ChanceLists"] and is_number(ItemChance) == True and type(NewItemName) == str and type(ItemDescription) != str:
        await SendErrorMessage(ctx, "Not A String", "The 'ItemDescription' Section needs to be a string made up of words")

    elif List_Name.lower() in guilds[str(ctx.guild.id)]["ChanceLists"] and is_number(ItemChance) == True and type(NewItemName) == str and type(ItemDescription) == str and ItemSellable.lower() != "true" or ItemSellable.lower() != "false":
        await SendErrorMessage(ctx, "Not A Bool", "The 'ItemSellable' Section needs to be a True/False Bool value")

    elif List_Name.lower() in guilds[str(ctx.guild.id)]["ChanceLists"] and is_number(ItemChance) == True and type(NewItemName) == str and type(ItemDescription) == str and ItemSellable.lower() == "true" or ItemSellable.lower() == "false" and is_number(ItemSellPrice) != True:
        await SendErrorMessage(ctx, "Not A Number", "The 'ItemSellPrice' Section needs to be a number")

@Bot.command()
async def SetFishingChannel(ctx, Channel_ID):
    guilds = await get_guilds()
    CancelWords = {"none", "null", "nil", "nochannel", "stop", "zero"}

    if is_number(Channel_ID):
        guilds[str(ctx.guild.id)]["Fishing_Channel"] = Channel_ID
        await ctx.send("You can now only fish in that channel (B#SetFishingChannel None) to cancel this action")
        with open("Data.json", "w") as f:
            json.dump(guilds, f)

    elif Channel_ID.lower() in CancelWords:
        guilds[str(ctx.guild.id)]["Fishing_Channel"] = None
        await ctx.send("Fishing no longer needs a specific channel")

        with open("Data.json", "w") as f:
            json.dump(guilds, f)

    else:
        await SendErrorMessage(ctx, "Not a channel Id", "This is not a valid channel ID")

@Bot.command()
async def use(ctx, item):
    await makeinv(ctx)
    inven = await getinven()
    guilds = await get_guilds()

    FoundItem = False
    UsingItem = None
    userinv = inven[str(ctx.author.id)]

    isnum = is_number(item)

    if isnum == True:
        item = round(float(item))

    values = []
    for x in inven[str(ctx.author.id)]:
        values.append(inven[str(ctx.author.id)][x])

    print("here")

    for x in values:
        if isnum == None and x["Name"].lower().find(item.lower()) != -1:
            FoundItem = True
            UsingItem = x["Name"]

        elif isnum == True and values[round(item - 1)] != None:
            FoundItem = True
            UsingItem = values[round(item - 1)]["Name"]
    print("here")
    if FoundItem == False:
        await ctx.send("Item Not Found")

    else:
        print(UsingItem)
        if "scavenging" in userinv[UsingItem]:
            print("here")
            UsingList = guilds[str(ctx.guild.id)]["ChanceLists"][userinv[UsingItem]["scavenging"]]

            ValTable = []
            ItemTable = []

            for x in UsingList:
                ValTable.append(x[1])
                ItemTable.append(x[0])


            FormattedTable = FindRatioedVals(ValTable)
            print(FormattedTable, time.time())
            GotItem = random.choices(ItemTable, weights = (FormattedTable))
            
            if userinv[UsingItem]["scavengingcdlastuse"] + userinv[UsingItem]["scavengingcooldown"] <= time.time():

                userinv[UsingItem]["scavengingcdlastuse"] = time.time()

                with open("InvData.json", "w") as f:
                    json.dump(inven, f)

                await AddItemToInventory(str(ctx.author.id), GotItem[0]["Name"], 1, GotItem[0])

                embed=discord.Embed(title="Item Found", color=0x7dc0e8)
                embed.add_field(name=GotItem[0]["Name"], value=f"You found a '{GotItem[0]['Name']}'!", inline=True)
                embed.set_footer(text="Item Added To Inventory")
                await ctx.send(embed=embed)

            
            else:
                await SendErrorMessage(ctx, "On Cooldown", f"This item is on cooldown, you must wait {round(userinv[UsingItem]['scavengingcdlastuse'] + userinv[UsingItem]['scavengingcooldown'] - time.time())} Seconds!")

        if "role giving" in userinv[UsingItem]:
            ID = userinv[UsingItem]["role giving"]
            role = discord.utils.get(ctx.guild.roles, id = ID)
            await ctx.author.add_roles(role)

            await ctx.send(f"{ctx.author.mention}, You were given the '{role}' Role")

        if "destroying" in userinv[UsingItem]:
            await AddItemToInventory(ctx.author.id, UsingItem, -1)

@Bot.command()
async def TradeIn(ctx):
    guilds = await get_guilds()
    await makeinv(ctx)
    inv = await getinven()
    shops = await getshops()

    print(ctx.channel.id)
    if "Trade-In Channels" in guilds[str(ctx.guild.id)] and str(ctx.channel.id) in guilds[str(ctx.guild.id)]["Trade-In Channels"]:

        TradeInItem = guilds[str(ctx.guild.id)]["Trade-In Channels"][str(ctx.channel.id)][0]
        Amnt = guilds[str(ctx.guild.id)]["Trade-In Channels"][str(ctx.channel.id)][1]
        GiveItem = guilds[str(ctx.guild.id)]["Trade-In Channels"][str(ctx.channel.id)][2]

        if TradeInItem in inv[str(ctx.author.id)] and inv[str(ctx.author.id)][TradeInItem]["Amount"] >= int(Amnt):
            
            await AddItemToInventory(ctx.author.id, TradeInItem, -int(Amnt))
            await AddItemToInventory(ctx.author.id, GiveItem, 1, shops[str(ctx.guild.id)][GiveItem])


            embed=discord.Embed(color=0x7272cf)
            embed.set_author(name=ctx.guild.name, icon_url = ctx.guild.icon_url)
            embed.add_field(name="Traded In Item", value=f"x{Amnt} {TradeInItem}", inline=True)
            embed.add_field(name="Given Item", value=GiveItem, inline=True)
            embed.set_footer(text="Item Added To Inventory")

            channel = await ctx.author.create_dm()
            await channel.send(embed=embed)

            await ctx.message.delete()

        else:
            channel = await ctx.author.create_dm()
            await channel.send("You don't Have enough of this item to trade in")

            await ctx.message.delete()

    else:
        await SendErrorMessage(ctx, "Wrong Channel", "There is no item to trade in with this channel")

@Bot.command()
async def say(ctx, *, Msg):
    await ctx.send(Msg)

@Bot.command()
async def TradeInChannel(ctx, TradeInItem, Amnt, Channel_ID, GiveItem):
    guilds = await get_guilds()

    if "Trade-In Channels" not in guilds[str(ctx.guild.id)]:
        guilds[str(ctx.guild.id)]["Trade-In Channels"] = {}

        with open("Data.json", "w") as f:
            json.dump(guilds, f)
        

    if is_number(Channel_ID) and is_number(Amnt):
        guilds[str(ctx.guild.id)]["Trade-In Channels"][int(Channel_ID)] = [TradeInItem, Amnt, GiveItem]
        await ctx.send(f"You can now trade in x{Amnt} {TradeInItem} for {GiveItem} ")

        with open("Data.json", "w") as f:
            json.dump(guilds, f)

    else:
        await SendErrorMessage(ctx, "Not a channel Id", "This is not a valid channel ID (or the amnt isnt a number)")

@Bot.command()
async def NewShop(ctx, ChannelID):
    guilds = await get_guilds()

    if "ChannelShops" not in guilds[str(ctx.guild.id)]:
        guilds[str(ctx.guild.id)]["ChannelShops"] = {}

        with open("Data.json", "w") as f:
            json.dump(guilds, f)

    if ChannelID not in guilds[str(ctx.guild.id)]["ChannelShops"]:
        guilds[str(ctx.guild.id)]["ChannelShops"][ChannelID] = {}

        with open("Data.json", "w") as f:
            json.dump(guilds, f)


@Bot.command()
async def ChannelShop(ctx):
    guilds = await get_guilds()

    if str(ctx.channel.id) in guilds[str(ctx.guild.id)]["ChannelShops"]:

        emb = discord.Embed(color=discord.Color.blurple())
        emb.set_author(name="Channel Shop", icon_url = ctx.guild.icon_url)

        num = 0
        for x in guilds[str(ctx.guild.id)]["ChannelShops"][str(ctx.channel.id)]:

            if "ShowInShop" not in guilds[str(ctx.guild.id)]["ChannelShops"][str(ctx.channel.id)][x] or guilds[str(ctx.guild.id)]["ChannelShops"][str(ctx.channel.id)][x]['ShowInShop'] == True:
                emb.add_field(name=f"[{num + 1}]: {guilds[str(ctx.guild.id)]['ChannelShops'][str(ctx.channel.id)][x]['Name']} - :hamburger:{guilds[str(ctx.guild.id)]['ChannelShops'][str(ctx.channel.id)][x]['BuyPrice']}", value = guilds[str(ctx.guild.id)]["ChannelShops"][str(ctx.channel.id)][x]['Desc'], inline=False)
                num = num + 1

        emb.set_footer(text="Buy items using the 'B#ChannelShopBuy' command!")
        await ctx.send(embed=emb)
    
    else:
        await SendErrorMessage(ctx, "No Channel Shop", "There is no shop for this specific channel")

@Bot.command()
async def FuckYourself(ctx):
    await ctx.send("https://www.youtube.com/watch?v=cbrP2LCoOfA")

#Buy Command
@Bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def ChannelShopBuy(ctx, *, item):

    NewItem = None
    await makeinv(ctx)
    await makeacc(ctx)
    guilds = await get_guilds()
    users = await getusers()

    if str(ctx.channel.id) in guilds[str(ctx.guild.id)]["ChannelShops"]:

        #formats all items into a table
        values = []
        for x in guilds[str(ctx.guild.id)]["ChannelShops"][str(ctx.channel.id)].keys():
            if "ShowInShop" not in guilds[str(ctx.guild.id)]["ChannelShops"][str(ctx.channel.id)][x] or guilds[str(ctx.guild.id)]["ChannelShops"][str(ctx.channel.id)][x]["ShowInShop"] == True:
                values.append(x)

        if is_number(item) != True:
            for x in values:
                if x.lower().find(item.lower()) != -1:
                    NewItem = x

        #if the item is in the shop

        if NewItem in guilds[str(ctx.guild.id)]["ChannelShops"][str(ctx.channel.id)]:
            
            print(NewItem, item)
            if "ShowInShop" not in guilds[str(ctx.guild.id)]["ChannelShops"][str(ctx.channel.id)][NewItem] or guilds[str(ctx.guild.id)]["ChannelShops"][str(ctx.channel.id)][NewItem]["ShowInShop"] == True:

                #gets variables
                Name = guilds[str(ctx.guild.id)]["ChannelShops"][str(ctx.channel.id)][NewItem]["Name"]
                Price = guilds[str(ctx.guild.id)]["ChannelShops"][str(ctx.channel.id)][NewItem]["BuyPrice"]
                #got variables

                msg = await ctx.send(f'{ctx.author.mention}, Are you sure you want to buy "{Name}" for :hamburger:{Price} Bungers?')
                await msg.add_reaction("✔️")
                await msg.add_reaction("❌")

                Bconfmessages.append([ctx, msg, "✔️", "❌", Price, Name, guilds[str(ctx.guild.id)]["ChannelShops"][str(ctx.channel.id)][NewItem], True])

            else:
                delmes = await ctx.send("Item was not found")
                await addmessagemdeletebutton(ctx, delmes)

        #Does this if number
        elif is_number(item) == True and values[int(item) - 1] != None:
            
            #gets item 
            item = guilds[str(ctx.guild.id)]["ChannelShops"][str(ctx.channel.id)][values[int(item) - 1]]

            #gets variables
            Name = item["Name"]
            Price = item["BuyPrice"]
            #got variables

            if "ShowInShop" not in guilds[str(ctx.guild.id)]["ChannelShops"][str(ctx.channel.id)][Name] or guilds[str(ctx.guild.id)]["ChannelShops"][str(ctx.channel.id)][Name]["ShowInShop"] == True:

                msg = await ctx.send(f'{ctx.author.mention}, Are you sure you want to buy "{Name}" for :hamburger:{Price} Bungers?')
                await msg.add_reaction("✔️")
                await msg.add_reaction("❌")

                Bconfmessages.append([ctx, msg, "✔️", "❌", Price, Name, item, True])
            
            else:
                delmes = await ctx.send("Item not found")
                await addmessagemdeletebutton(ctx, delmes)

        elif is_number(item) == False and item not in guilds[str(ctx.guild.id)]["ChannelShops"][str(ctx.channel.id)]:
            #sends message with a delete button
            channel = await ctx.author.create_dm()
            await channel.send(f"Item '{item}' in channel '{ctx.channel} was not found ")

    else:
        await SendErrorMessage(ctx, "No shop in this channel", "You must be in a channel with a shop to use this command")


@dep.error
async def deposit_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await SendErrorMessage(ctx, "Missing Argument", "B#deposit {Amount}")

@withdraw.error
async def withdraw_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await SendErrorMessage(ctx, "Missing Argument", "B#withdraw {Amount}")

@sell.error
async def sell_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await SendErrorMessage(ctx, "Missing Argument", "B#sell {item name/item number}")

@editlist.error
async def edit_list_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        guilds = await get_guilds()

        if "ChanceLists" not in guilds[str(ctx.guild.id)]:
            guilds[str(ctx.guild.id)]["ChanceLists"] = {}
        

        embed=discord.Embed(title="Lists")
        embed.add_field(name = "How To Setup", value = "B#EditList \n**1:** `List Name` (String), \n**2:** `New Item Name` (String), \n**3:** `Item Drop Chance` (Number), \n**4:** `Item Description` (String), \n**5:** `Item Sellable` (True/False), \n**6:** `Item Sell Price` (Number)", inline= True)
        embed.add_field(name = "Display", value = "Below are all the current lists in this discord servre\n to the left, you'll see the command to set it up yourself, as well as the syntax")
        
        # "ListName" = { ["Shrimp", 50], ["Shark", 25] }

        if guilds[str(ctx.guild.id)]["ChanceLists"] == {}:
            embed.add_field(name="No Lists yet", value="You Need to add a list first", inline=False)

        else:
            for x in guilds[str(ctx.guild.id)]["ChanceLists"]:

                FieldString = "<--Items-->\n"
                num = 1
                for i in guilds[str(ctx.guild.id)]["ChanceLists"][x]:
                    

                    print(f"THE THING IS: {i[0]['Name']}")

                    Name = str(i[0]["Name"])
                    Chance = str(i[1])
                    Description = str(i[0]["Desc"])
                    Sellable = str(i[0]["Sellable"])
                    SellPrice = str(i[0]["SellPrice"])
                    Useable = str(i[0]["Useable"])

                    print(Name, Description, Sellable, SellPrice, Useable)

                    FieldString += f"    ***[{num}]:*** *Name: {Name}*\n"
                    FieldString += f"       `Drop Chance: {Chance}`\n"
                    FieldString += f"       `Description: {Description}`\n"
                    FieldString += f"       `Sellable: {Sellable}`\n"
                    FieldString += f"       `SellPrice: {SellPrice}`\n"
                    FieldString += f"       `Useable: {Useable  }`\n"

                    num += 1
                    print(FieldString)
                    
                    
                embed.add_field(name=f" [ListName]: {x}", value = FieldString, inline=False)

        await ctx.send(embed=embed)

#itemsetup missing permisions error
@ItemSetup.error
async def item_setup_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You don't have permission to make new items\nLOOK AT THIS IDIOT HE THOUGHT HE COULD MAKE ITEMS\nHAHHAHAHA WHAT AN IDIOT")

#Itemsetup help missing argument error
@ItemSetup.error
async def item_setup_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        print("yeees")
        #Makes error embed
        em = discord.Embed(title="ItemSetup Help", color=0x2754a7)
        em.add_field(name="Variable List", value="**1.** `Name` *(String)*\n**2.** `Description` *(String)*\n**3.** `Sellable` *(True/False)*\n**4.** `SellPrice` *(Number)*\n**5.** `Useable` *(True/False)*\n**6.** `BuyPrice` *(Number)*\n**7.** `ShowInShop` *(True/False)*", inline=True)
        em.add_field(name="How to adjust settings", value="You can use B#ItemConfig to change an items values\n***Ex:*** `B#ItemConfig <Name> <Setting> <NewSetting>`", inline=True)
        em.add_field(name="Example:", value='*B#Itemsetup "Void Token" "A neat token from the void, cool!" true 220 false 165*\n`Note: You must use "" for things you want to be longer than one word, as seen in example` ', inline=False)
      
        #sends error embed
        await ctx.send(embed=em)

#Itemconfig help setup error
@ItemConfig.error
async def item_config_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        
        em = discord.Embed(title="ItemConfig Help", color=0x2754a7)
        em.add_field(name="Variable List", value=" `Name` *(String)*\n `Description` *(String)*\n `Sellable` *(True/False)*\n `SellPrice` *(Number)*\n `Useable` *(True/False)*\n `BuyPrice` *(Number)*", inline=True)
        em.add_field(name="How to adjust settings", value="You can use B#ItemConfig to change an items values\n***Ex:*** `B#ItemConfig <Name> <Setting> <NewSetting>`", inline=True)
        em.add_field(name="Example:", value='*B#ItemConfig "Void Token" BuyPrice 899*\n`Note: You must use "" for things you want to be longer than one word, as seen in example` ', inline=False)
       
        await ctx.send(embed=em)       
        
#itemconfig missing permisions error
@ItemConfig.error
async def item_config_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You don't have permission to adjust items\nLOOK AT THIS IDIOT HE THOUGHT HE COULD MAKE ITEMS\nHAHHAHAHA WHAT AN IDIOT")         

#Makes bank account
async def makeacc(ctx):
    users = await getusers()

    if str(ctx.author.id) in users:
        return False

    else:
        users[str(ctx.author.id)] = {}
        users[str(ctx.author.id)]["wallet"] = 0
        users[str(ctx.author.id)]["bank"] = 0
        with open("Data.json", "w") as f:
            json.dump(users, f)
        return True

#Gets users
async def getusers():
    with open("Data.json", "r") as f:
            users = json.load(f)
    return users

#Gets Inven
async  def getinven():
    with open("InvData.json", "r") as f:
        inven = json.load(f)
    return inven

#Gets Shop
async  def getshops():
    with open("Shopdata.json", "r") as f:
        shops = json.load(f)
    return shops

#Makes shop
async def makeshop(ctx):
    shops = await getshops()

    if str(ctx.guild.id) in shops:
        return False

    else:
        
        shops[str(ctx.guild.id)] = {}
        shops[str(ctx.guild.id)]["Fishing Rod :fishing_pole_and_fish:"] = {"Name": "Fishing Rod :fishing_pole_and_fish:","Desc": "A basic fishing rod! can be used to fish with the 'B#fish' Command!","Sellable": True,"SellPrice": 200,"Useable": False,"BuyPrice": 250}

        with open("Shopdata.json", "w") as f:
            json.dump(shops, f)

# KEEP THIS SECRET (hes joking tell it to everyone)
Bot.run('Bot Token')
