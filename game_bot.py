import discord
import random
import string

client = discord.Client()
game = False
curr_letter = ""


def load_data(f, data_list):
    data = open(f)
    for d in data:
        data_list.append(d.strip().lower())


# Load female names
f_name_list = []
load_data("datasets/female.txt", f_name_list)

# Load male names
m_name_list = []
load_data("datasets/male.txt", m_name_list)

# Load movies data
movies_list = []
load_data("datasets/movies.txt", movies_list)

# Load animals data
animals_list = []
load_data("datasets/animals.txt", animals_list)

# Load countries.txt data
countries_list = []
load_data("datasets/countries.txt", countries_list)


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

        if message.content.startswith('!'):
            if message.content == "!q":
                game = False
                await message.channel.send("Game ended!")
                return
        # Check if formatting is correct
        if len(answer) != 5:
            await message.channel.send(message.author.name + ", "
                                       "invalid answer! "
                                       "(There should be 5 elements)")
            return

        # Check if first letters are correct
        for a in answer:
            if (a[0] != curr_letter) and (a[0] != curr_letter.upper()):
                await message.channel.send(message.author.name + ", "
                                           "invalid answer! ")
                return

        # Check if Boy Name is correct
        if answer[0].lower() not in m_name_list:
            await message.channel.send(message.author.name + ", "
                                       "incorrect boy name!")
            return

        # Check if Boy Name is correct
        if answer[1].lower() not in f_name_list:
            await message.channel.send(message.author.name + ", "
                                       "incorrect girl name!")
            return

        # Check if Animal is correct
        if answer[2].lower() not in animals_list:
            await message.channel.send(message.author.name + ", "
                                       "incorrect animal!")
            return

        # Check if Country is correct
        if answer[3].lower() not in countries_list:
            await message.channel.send(message.author.name + ", "
                                       "incorrect country!")
            return

        # Check if Movie is correct
        if answer[4].lower() not in movies_list:
            await message.channel.send(message.author.name + ", "
                                       "incorrect movie!")
            return

        await message.channel.send(message.author.name + " is the winner! "
                                                         ":trophy:")
        game = False

    if message.content.startswith('!'):
        if message.content == "!rules":
            await message.channel.send(" When the game starts, a random "
                                       "letter will be chosen. \n Give a "
                                       "**Boy Name**, "
                                       "**Girl Name**, "
                                       "**Animal**, **Country**, **Movie**, "
                                       "that start with that letter, in "
                                       "this order, and separated by commas. \n"
                                       " "
                                       "The first player to get these wins! \n"
                                       " \n To "
                                       "start a "
                                       "game, type `!game` \n To " 
                                       "quit the game, type `!q`")

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
