import discord
import random
import string

client = discord.Client()
game = False
curr_letter = ""

# Load animals data
animals = open("animals.txt")
animals_list = []
for animal in animals:
    animals_list.append(animal.strip())
    animals_list.append(animal.strip().lower())

# Load countries data
countries = open("countries")
countries_list = []
for country in countries:
    countries_list.append(country.strip())
    countries_list.append(country.strip().lower())


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global game
    global curr_letter

    if message.author == client.user:
        return

    if game:
        global curr_letter
        answer = message.content.split(", ")

        # Check if formatting is correct
        if len(answer) != 4:
            await message.channel.send(message.author.name + ", "
                                       "incorrect answer!")
            return

        # Check if first letters are correct
        for a in answer:
            if (a[0] != curr_letter) and (a[0] != curr_letter.upper()):
                await message.channel.send(message.author.name + ", "
                                           "incorrect answer!")
                return

        # Check if Animal is correct
        if answer[1] not in animals_list:
            await message.channel.send(message.author.name + ", "
                                       "incorrect answer!")
            return

        # Check if Country is correct
        if answer[2] not in countries_list:
            await message.channel.send(message.author.name + ", "
                                       "incorrect answer!")
            return

        await message.channel.send(message.author.name + " is the winner! "
                                   ":trophy:")
        game = False

    if message.content.startswith('!'):

        if message.content == "!rules":
            await message.channel.send("When the game starts, give a Name, "
                                       "Animal, Country, Movie/TV Show, in"
                                       "order and separated by commas. ")

        if message.content == "!game":
            game = True
            round_letter = random.choice(string.ascii_lowercase)
            await message.channel.send("Game starting! "
                                       "The letter is :regional_indicator"
                                       "_{0}:".format(round_letter))
            curr_letter = round_letter

secret_f = open("secret")
secret = secret_f.readline()

client.run(secret)

