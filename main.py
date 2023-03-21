import discord


intents = discord.Intents.default()
intents.message_content = True
# poem == credentials k?    Split makes an \n appear
# poem = open('C:/horseman/cred.txt').read().split(',')
poem = open('C:/horseman/cred.txt').read().replace(' ',
                                                   '').replace('\n', '').split(',')
poem = {'key': poem[0], 'srv': poem[1]}

# Generate instance of Discord Client
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == poem['srv']:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    # Checks if message is written by the bot, if it is by the bot, then it won't respond
    if message.author == client.user:
        return

    await message.channel.send(f'The loser {message.author.name} exclaimed: {message.content} 🤓')

client.run(poem['key'])
# print(poem, "\n The poem, your majesty")
