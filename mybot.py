import discord 
import random

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$halo'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        handler = random.randint(1, 3)
        if handler == 1:
            await message.channel.send("\\U0001f642")
        elif handler == 2:
            await message.channel.send("Bye friend")
        elif handler == 3:
            await message.channel.send('jumpa lagi')
    elif message.content.startswith('$deleteme'):
        msg = await message.channel.send('I will delete myself now...')
        await msg.delete() # bot menghapus pesan
    else:
        await message.channel.send(message.content)

@client.event
async def on_message_delete(message):
    # untuk memberi tahu siapa yang menghapus pesan
    msg = f'{message.author} has deleted the message: {message.content}'
    await message.channel.send(msg)

@client.event
async def on_member_remove(member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Goodbye from the {guild.name}!'
            await guild.system_channel.send(to_send)
