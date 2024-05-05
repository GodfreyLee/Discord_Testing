import discord
import requests
import json

# Define your intents
intents = discord.Intents.default()

# Pass the intents to the client constructor
client = discord.Client(intents=intents)

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return(quote)

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')


# Event handler for when a message is sent
@client.event
async def on_message(message):
    # Check if the message was sent by the bot itself to avoid infinite loops
    if message.author == client.user:
        return
    quote = get_quote()
    # Respond with "Hello!" whenever any message is sent
    await message.channel.send(quote)

# Enter the discord bot key below
client.run("")