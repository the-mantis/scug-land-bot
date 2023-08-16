import discord as dis
import random
import time
from asyncio import sleep

wait = time.sleep
client = dis.Client(intents=dis.Intents.all())
sopids = []
cooldown = []
sopdict = {}
sopallids = []
sopalldict = {}
sopalltime = {}
prefix = "&"


def get_token(line):
    return open("bot token owo.txt").readlines()[line - 1]


token = get_token(20)


@client.event
async def on_message(msg: dis.Message):
    async def send(text):
        await sleep(0.25)
        await msg.channel.send(text)

    global sopids, sopfile, sopallids, sopallchoice, cooldown, lvl, xp
    command = msg.content.split()[0]
    if command == (prefix) + "roll":
        if len(msg.content.split()) == 1:
            await send("Please enter the dice-sides count and what you are rolling for.")
        elif len(msg.content.split()) == 2:
            await send("Please enter what you are rolling for.")
        else:
            rng = random.randint(1, int(msg.content.split()[1]) + 1)
            grammar = "a"
            endtext = ""
            if (float(msg.content.split()[1]) / 2) > rng:
                endtext = "do not "
            text = " ".join(msg.content.split()[words + 2] for words in range(len(msg.content.split()) - 2))
            msgdice = await msg.channel.send(
                f"""<@{msg.author.id}> Rolls a {msg.content.split()[1]} Sided dice to see if they {text}""")
            await sleep(1)

            await msgdice.edit(
                content=f"""<@{msg.author.id}> Rolls a {msg.content.split()[1]} Sided dice to see if they {text}
...""")
            await sleep(1)
            await msgdice.edit(
                content=f"""<@{msg.author.id}> Rolls a {msg.content.split()[1]} Sided dice to see if they {text}
...
They roll {grammar} {rng}""")
            await sleep(1)
            await msgdice.edit(
                content=f"""<@{msg.author.id}> Rolls a {msg.content.split()[1]} Sided dice to see if they {text}
...
They roll {grammar} {rng}
...""")
            await sleep(1)
            await msgdice.edit(
                content=f"""<@{msg.author.id}> Rolls a {msg.content.split()[1]} Sided dice to see if they {text}
...
They roll {grammar} {rng}
...
They {endtext}{text}""")
    if command == (prefix) + "log" and (msg.author.id == 790276876626296833 or msg.author.id == 1030070846234054758):
        await send(
            f"<t:{round(time.time())}:d> <t:{round(time.time())}:T> (<t:{round(time.time())}:R>) - {(msg.content[len(msg.content.split()[0]) + 1:])}")
        await msg.delete()
    if msg.channel.id == 1124414874454339715:
        a = 0
        try:
            int(msg.content.split()[0])
        except:
            try:
                await msg.delete()
                user = await client.fetch_user(int(msg.author.id))
                await user.send("This message is not formatted properly ({number in sequence} - )")
                a = 1
            except Exception as exc:
                print(exc)
        try:
            if msg.content.split()[1] != "-" and a == 0:
                await msg.delete()
                user = await client.fetch_user(int(msg.author.id))
                await user.send("This message is not formatted properly ({number in sequence} - )")
                a = 1
        except:
            pass

    try:
        if (msg.content.removeprefix(prefix) == "smashorpass" and msg.author.id not in sopids):
            sopfile = open("sop.ca").readlines()
            sopsplit = []
            for line in range(len(open("sop.ca").readlines())):
                sopsplit.append(sopfile[line - 1].split(","))
            sopdict[msg.author.id] = random.randint(0, len(open("sop.ca").readlines()) - 1)
            await send(f"""<@{msg.author.id}>
    Smash -- or -- Pass
        {sopsplit[sopdict[msg.author.id]][2]}""")
            await send(sopsplit[sopdict[msg.author.id]][3])
            await send(f"{prefix}smash - {prefix}pass")
            sopids += [msg.author.id]
        elif msg.content.removeprefix(prefix) == "smashorpass" and msg.author.id in sopids:
            await send(
                "You already have an ongoing game, if this is false, please contact an admin to restart the bot to fix the issue")
        if msg.content.removeprefix(prefix).lower() == "smash" and msg.author.id in sopids:
            sopids.remove(msg.author.id)
            sopsplit = []
            for line in range(len(open("sop.ca").readlines())):
                sopsplit.append(sopfile[line].split(","))
            (sopsplit[sopdict[msg.author.id] - 1][0]) = int(sopsplit[sopdict[msg.author.id] - 1][0]) + 1
            sopsplitfinal = []
            for line in range(len(sopsplit)):
                sopsplitfinal.append(f"{sopsplit[line][0]},{sopsplit[line][1]},{sopsplit[line][2]},{sopsplit[line][3]}")
            open("sop.ca", "w").writelines(sopsplitfinal)
            sopfile = open("sop.ca").readlines()
            sopsplit = []
            for line in range(len(open("sop.ca").readlines())):
                sopsplit.append(sopfile[line - 1].split(","))
            await send(sopsplit[sopdict[msg.author.id]][2])
            await send(sopsplit[sopdict[msg.author.id]][3])
            await send(f"""You(<@{msg.author.id}>) Said: **smash**
            You agree with {round(((float(sopsplit[sopdict[msg.author.id]][0]) - 1) / ((float(sopsplit[sopdict[msg.author.id]][0]) - 1) + (float(sopsplit[sopdict[msg.author.id]][1])))) * 100)}% of people ({int(sopsplit[sopdict[msg.author.id]][0]) - 1} people)
            {prefix}smash - {round(((float(sopsplit[sopdict[msg.author.id]][0]) - 1) / ((float(sopsplit[sopdict[msg.author.id]][0]) - 1) + (float(sopsplit[sopdict[msg.author.id]][1])))) * 100)}% ({int(sopsplit[sopdict[msg.author.id]][0]) - 1} people)  {prefix}pass - {round(((float(sopsplit[sopdict[msg.author.id]][1])) / ((float(sopsplit[sopdict[msg.author.id]][0]) - 1) + (float(sopsplit[sopdict[msg.author.id]][1])))) * 100)}% ({int(sopsplit[sopdict[msg.author.id]][1])} people)""")
        if msg.content.removeprefix(prefix).lower() == "pass" and msg.author.id in sopids:
            sopids.remove(msg.author.id)
            sopsplit = []
            for line in range(len(open("sop.ca").readlines())):
                sopsplit.append(sopfile[line].split(","))
            (sopsplit[sopdict[msg.author.id] - 1][1]) = int(sopsplit[sopdict[msg.author.id] - 1][1]) + 1
            sopsplitfinal = []
            for line in range(len(sopsplit)):
                sopsplitfinal.append(f"{sopsplit[line][0]},{sopsplit[line][1]},{sopsplit[line][2]},{sopsplit[line][3]}")
            open("sop.ca", "w").writelines(sopsplitfinal)
            sopfile = open("sop.ca").readlines()
            sopsplit = []
            for line in range(len(open("sop.ca").readlines())):
                sopsplit.append(sopfile[line - 1].split(","))
            await send(sopsplit[sopdict[msg.author.id]][2])
            await send(sopsplit[sopdict[msg.author.id]][3])
            await send(f"""You(<@{msg.author.id}>) Said: **pass**
            You agree with {round(((float(sopsplit[sopdict[msg.author.id]][1]) - 1) / ((float(sopsplit[sopdict[msg.author.id]][0])) + (float(sopsplit[sopdict[msg.author.id]][1]) - 1))) * 100)}% of people ({int(sopsplit[sopdict[msg.author.id]][1]) - 1} people)
            {prefix}smash - {round((float(sopsplit[sopdict[msg.author.id]][0]) / ((float(sopsplit[sopdict[msg.author.id]][0])) + (float(sopsplit[sopdict[msg.author.id]][1]) - 1))) * 100)}% ({int(sopsplit[sopdict[msg.author.id]][0])} people)  {prefix}pass - {round(((float(sopsplit[sopdict[msg.author.id]][1]) - 1) / ((float(sopsplit[sopdict[msg.author.id]][0])) + (float(sopsplit[sopdict[msg.author.id]][1]) - 1))) * 100)}% ({int(sopsplit[sopdict[msg.author.id]][1]) - 1} people)""")
        if msg.content.split()[0] == f"{prefix}smashorpass" and msg.content.split()[1] == "all":
            sopalldict[msg.author.id] = -1
            sopalltime[msg.author.id] = -1
    
        if msg.content.removeprefix(prefix).lower() == "smash" and msg.author.id in sopallids:
            sopallids.remove(msg.author.id)
            sopsplit = []
            for line in range(len(open("sop.ca").readlines())):
                sopsplit.append(sopfile[line].split(","))
            (sopsplit[sopalldict[msg.author.id] - 1][0]) = int(sopsplit[sopalldict[msg.author.id] - 1][0]) + 1
            sopsplitfinal = []
            for line in range(len(sopsplit)):
                sopsplitfinal.append(f"{sopsplit[line][0]},{sopsplit[line][1]},{sopsplit[line][2]},{sopsplit[line][3]}")
            open("sop.ca", "w").writelines(sopsplitfinal)
            sopfile = open("sop.ca").readlines()
            sopsplit = []
            for line in range(len(open("sop.ca").readlines())):
                sopsplit.append(sopfile[line - 1].split(","))
            await send(sopsplit[sopalldict[msg.author.id]][2])
            await send(sopsplit[sopalldict[msg.author.id]][3])
            await send(f"""You(<@{msg.author.id}>) Said: **smash**
            You agree with {round(((float(sopsplit[sopalldict[msg.author.id]][0]) - 1) / ((float(sopsplit[sopalldict[msg.author.id]][0]) - 1) + (float(sopsplit[sopalldict[msg.author.id]][1])))) * 100)}% of people ({int(sopsplit[sopalldict[msg.author.id]][0]) - 1} people)
            {prefix}smash - {round(((float(sopsplit[sopalldict[msg.author.id]][0]) - 1) / ((float(sopsplit[sopalldict[msg.author.id]][0]) - 1) + (float(sopsplit[sopalldict[msg.author.id]][1])))) * 100)}% ({int(sopsplit[sopalldict[msg.author.id]][0]) - 1} people)  {prefix}pass - {round(((float(sopsplit[sopalldict[msg.author.id]][1])) / ((float(sopsplit[sopalldict[msg.author.id]][0]) - 1) + (float(sopsplit[sopalldict[msg.author.id]][1])))) * 100)}% ({int(sopsplit[sopalldict[msg.author.id]][1])} people)""")
            await send("‎")
        if msg.content.removeprefix(prefix).lower() == "pass" and msg.author.id in sopallids:
            sopallids.remove(msg.author.id)
            sopsplit = []
            for line in range(len(open("sop.ca").readlines())):
                sopsplit.append(sopfile[line].split(","))
            (sopsplit[sopalldict[msg.author.id] - 1][1]) = int(sopsplit[sopalldict[msg.author.id] - 1][1]) + 1
            sopsplitfinal = []
            for line in range(len(sopsplit)):
                sopsplitfinal.append(f"{sopsplit[line][0]},{sopsplit[line][1]},{sopsplit[line][2]},{sopsplit[line][3]}")
            open("sop.ca", "w").writelines(sopsplitfinal)
            sopfile = open("sop.ca").readlines()
            sopsplit = []
            for line in range(len(open("sop.ca").readlines())):
                sopsplit.append(sopfile[line - 1].split(","))
            await send(sopsplit[sopalldict[msg.author.id]][2])
            await send(sopsplit[sopalldict[msg.author.id]][3])
            await send(f"""You(<@{msg.author.id}>) Said: **pass**
            You agree with {round(((float(sopsplit[sopalldict[msg.author.id]][1]) - 1) / ((float(sopsplit[sopalldict[msg.author.id]][0])) + (float(sopsplit[sopalldict[msg.author.id]][1]) - 1))) * 100)}% of people ({int(sopsplit[sopalldict[msg.author.id]][1]) - 1} people)
            {prefix}smash - {round((float(sopsplit[sopalldict[msg.author.id]][0]) / ((float(sopsplit[sopalldict[msg.author.id]][0])) + (float(sopsplit[sopalldict[msg.author.id]][1]) - 1))) * 100)}% ({int(sopsplit[sopalldict[msg.author.id]][0])} people)  {prefix}pass - {round(((float(sopsplit[sopalldict[msg.author.id]][1]) - 1) / ((float(sopsplit[sopalldict[msg.author.id]][0])) + (float(sopsplit[sopalldict[msg.author.id]][1]) - 1))) * 100)}% ({int(sopsplit[sopalldict[msg.author.id]][1]) - 1} people)""")
            await send("‎")
        if msg.content.removeprefix(prefix).lower() == "stop" and msg.author.id in sopallids:
            await send("Stopped!")
            sopallids.remove(msg.author.id)
            sopalltime[msg.author.id] = len(open("sop.ca").readlines()) - 1
            msg.content = 0
        if (sopalltime[msg.author.id] != len(
                open("sop.ca").readlines()) - 1) and msg.author.id not in sopallids:
            sopallids += [msg.author.id]
            if sopalltime[msg.author.id] == -1:
                sopallchoice = []
                sopallchoice = random.sample(range(0, len(open("sop.ca").readlines())),
                                             len(open("sop.ca").readlines()))
            sopalltime[msg.author.id] += 1
            sopalldict[msg.author.id] = sopallchoice[sopalltime[msg.author.id]]
            sopfile = open("sop.ca").readlines()
            sopsplit = []
            for line in range(len(open("sop.ca").readlines())):
                sopsplit.append(sopfile[line - 1].split(","))
            await send(f"""<@{msg.author.id}>
            Smash -- or -- Pass [{sopalltime[msg.author.id] + 1}/{len(open("sop.ca").readlines())}]
                {sopsplit[sopalldict[msg.author.id]][2]}""")
            await send(sopsplit[sopalldict[msg.author.id]][3])
            await send(f"{prefix}smash - {prefix}pass - {prefix}stop")
        elif msg.content.removeprefix(prefix) == "smashorpassall" and (sopalltime[msg.author.id] > -1):
            await send(
                "You already have an ongoing game, if this is false, please contact an admin to restart the bot to fix the issue")
    except:
        pass
    with open("lvl.ca") as levelpre:
        level = eval(levelpre.read())
        if msg.content.removeprefix(prefix) == "profile":
            await msg.channel.send(f"""{msg.author.display_name} (ID: {msg.author.id}),
          > Level: {level[msg.author.id]["lvl"]}
          > XP: {level[msg.author.id]["xp"]} (from {level[msg.author.id]["xp"] / 10} messages)
          > You need {(level[msg.author.id]["lvl"] * (level[msg.author.id]["lvl"] + 1) / 2) * 100}xp to advance to level {level[msg.author.id]["lvl"] + 1} ({((level[msg.author.id]["lvl"] * (level[msg.author.id]["lvl"] + 1) / 2) * 100) - level[msg.author.id]["lvl"]}xp Left)""")

        if msg.channel.id != 1119527152807858246 and msg.author.id not in cooldown:
            cooldown += [msg.author.id]
            if msg.author.id not in level:
                level[msg.author.id] = {"xp": 0, "lvl": 1}
            level[msg.author.id]["xp"] += 10
            if level[msg.author.id]["xp"] >= (
                    level[msg.author.id]["lvl"] * (level[msg.author.id]["lvl"] + 1) / 2) * 100:
                level[msg.author.id]["lvl"] += 1
                preid = msg.channel.id
                msg.channel.id = 1126477320014811206
                await msg.channel.send(
                    f"""{msg.author.display_name} You have advanced to Level {level[msg.author.id]["lvl"]}
You need {(level[msg.author.id]["lvl"] * (level[msg.author.id]["lvl"] + 1) / 2) * 100}xp to advance to level {level[msg.author.id]["lvl"] + 1} ({((level[msg.author.id]["lvl"] * (level[msg.author.id]["lvl"] + 1) / 2) * 100) - level[msg.author.id]["lvl"]}xp Left)""")
                msg.channel.id = preid

            if level[msg.author.id]["lvl"] >= 5:
                await msg.author.add_roles(dis.utils.get(msg.guild.roles, id=1126140699578998794))
            if level[msg.author.id]["lvl"] >= 15:
                await msg.author.add_roles(dis.utils.get(msg.guild.roles, id=1126152109390319687))
            if level[msg.author.id]["lvl"] >= 30:
                await msg.author.add_roles(dis.utils.get(msg.guild.roles, id=1126145789538865213))
            if level[msg.author.id]["lvl"] >= 50:
                await msg.author.add_roles(dis.utils.get(msg.guild.roles, id=1126153339583864842))
            open("lvl.ca", 'w').write(f"{level}")

            await sleep(10)
            cooldown.remove(msg.author.id)


client.run(token)
