import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive


client = discord.Client()

sad_word = ["cape euy", "susah banget", "ga mood"]

starter_encouragements = [
  "sama broo"
  "gua juga pusing"
  "semangat "
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0] ['q'] + " -" + json_data[o] ['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

@client.event
async def on_ready():
  print('Samlekom Mamank {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('!ganteng doang'):
    await message.channel.send('ngang ngang moang gang!')

  if msg.startswith('!iri'):
    await message.channel.send('bilang bos ahaay pa pale pale !')

  if msg.startswith('!punten'):
    await message.channel.send('kuy gabung sini jangan canggung!')

  if msg.startswith('!bimskuy'):
    await message.channel.send('yakali ga kuyy !')

  if msg.startswith('!pantek'):
    await message.channel.send('eh jangan ngegas dong bangsat!')

  if msg.startswith('!mgodonf'):
    await message.channel.send('ampun om hacker!')

  if msg.startswith('!galau'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_word):
    await message.channel.send(random.choice(starter_encouragements))

keep_alive()
client.run(os.getenv('TOKEN'))
