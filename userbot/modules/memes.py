# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
""" Userbot module for having some fun with people. """

from asyncio import sleep
from random import choice, getrandbits, randint
from re import sub
import time

from collections import deque

import requests

from cowpy import cow

from userbot import CMD_HELP, BOT_NAME
from userbot.events import register
from userbot.modules.admin import get_user_from_event

# ================= CONSTANT =================
METOOSTR = [
    "Me too thanks",
    "Haha yes, me too",
    "Same lol",
    "Me irl",
    "Same here",
    "Haha yes",
    "Me rn",
]

ZALG_LIST = [[
    "̖",
    " ̗",
    " ̘",
    " ̙",
    " ̜",
    " ̝",
    " ̞",
    " ̟",
    " ̠",
    " ̤",
    " ̥",
    " ̦",
    " ̩",
    " ̪",
    " ̫",
    " ̬",
    " ̭",
    " ̮",
    " ̯",
    " ̰",
    " ̱",
    " ̲",
    " ̳",
    " ̹",
    " ̺",
    " ̻",
    " ̼",
    " ͅ",
    " ͇",
    " ͈",
    " ͉",
    " ͍",
    " ͎",
    " ͓",
    " ͔",
    " ͕",
    " ͖",
    " ͙",
    " ͚",
    " ",
],
             [
                 " ̍",
                 " ̎",
                 " ̄",
                 " ̅",
                 " ̿",
                 " ̑",
                 " ̆",
                 " ̐",
                 " ͒",
                 " ͗",
                 " ͑",
                 " ̇",
                 " ̈",
                 " ̊",
                 " ͂",
                 " ̓",
                 " ̈́",
                 " ͊",
                 " ͋",
                 " ͌",
                 " ̃",
                 " ̂",
                 " ̌",
                 " ͐",
                 " ́",
                 " ̋",
                 " ̏",
                 " ̽",
                 " ̉",
                 " ͣ",
                 " ͤ",
                 " ͥ",
                 " ͦ",
                 " ͧ",
                 " ͨ",
                 " ͩ",
                 " ͪ",
                 " ͫ",
                 " ͬ",
                 " ͭ",
                 " ͮ",
                 " ͯ",
                 " ̾",
                 " ͛",
                 " ͆",
                 " ̚",
             ],
             [
                 " ̕",
                 " ̛",
                 " ̀",
                 " ́",
                 " ͘",
                 " ̡",
                 " ̢",
                 " ̧",
                 " ̨",
                 " ̴",
                 " ̵",
                 " ̶",
                 " ͜",
                 " ͝",
                 " ͞",
                 " ͟",
                 " ͠",
                 " ͢",
                 " ̸",
                 " ̷",
                 " ͡",
             ]]

EMOJIS = [
    "😂",
    "😂",
    "👌",
    "✌",
    "💞",
    "👍",
    "👌",
    "💯",
    "🎶",
    "👀",
    "😂",
    "👓",
    "👏",
    "👐",
    "🍕",
    "💥",
    "🍴",
    "💦",
    "💦",
    "🍑",
    "🍆",
    "😩",
    "😏",
    "👉👌",
    "👀",
    "👅",
    "😩",
    "🚰",
]

INSULT_STRINGS = [
    "Owww ... Such a stupid idiot.\n\nBy: {BOT_NAME}",
    "Don't drink and type.\n\nBy: {BOT_NAME}",
    "I think you should go home or better a mental asylum.\n\nBy: {BOT_NAME}",
    "Command not found. Just like your brain.\n\nBy: {BOT_NAME}",
    "Do you realize you are making a fool of yourself? Apparently not.\n\nBy: {BOT_NAME}",
    "You can type better than that.\n\nBy: {BOT_NAME}",
    "Bot rule 544 section 9 prevents me from replying to stupid humans like you.\n\nBy: {BOT_NAME}",
    "Sorry, we do not sell brains.\n\nBy: {BOT_NAME}",
    "Believe me you are not normal.\n\nBy: {BOT_NAME}",
    "I bet your brain feels as good as new, seeing that you never use it.\n\nBy: {BOT_NAME}",
    "If I wanted to kill myself I'd climb your ego and jump to your IQ.\n\nBy: {BOT_NAME}",
    "Zombies eat brains... you're safe.\n\nBy: {BOT_NAME}",
    "You didn't evolve from apes, they evolved from you.\n\nBy: {BOT_NAME}",
    "Come back and talk to me when your I.Q. exceeds your age.\n\nBy: {BOT_NAME}",
    "I'm not saying you're stupid, I'm just saying you've got bad luck when it comes to thinking.\n\nBy: {BOT_NAME}",
    "What language are you speaking? Cause it sounds like bullshit.\n\nBy: {BOT_NAME}",
    "Stupidity == not a crime so you are free to go.\n\nBy: {BOT_NAME}",
    "You are proof that evolution CAN go in reverse.\n\nBy: {BOT_NAME}",
    "I would ask you how old you are but I know you can't count that high.\n\nBy: {BOT_NAME}",
    "As an outsider, what do you think of the human race?\n\nBy: {BOT_NAME}",
    "Brains aren't everything. In your case they're nothing.\n\nBy: {BOT_NAME}",
    "Ordinarily people live and learn. You just live.\n\nBy: {BOT_NAME}",
    "I don't know what makes you so stupid, but it really works.\n\nBy: {BOT_NAME}",
    "Keep talking, someday you'll say something intelligent! (I doubt it though)\n\nBy: {BOT_NAME}",
    "Shock me, say something intelligent.\n\nBy: {BOT_NAME}",
    "Your IQ's lower than your shoe size.\n\nBy: {BOT_NAME}",
    "Alas! Your neurotransmitters are no more working.\n\nBy: {BOT_NAME}",
    "Are you crazy you fool.\n\nBy: {BOT_NAME}",
    "Everyone has the right to be stupid but you are abusing the privilege.\n\nBy: {BOT_NAME}",
    "I'm sorry I hurt your feelings when I called you stupid. I thought you already knew that.\n\nBy: {BOT_NAME}",
    "You should try tasting cyanide.\n\nBy: {BOT_NAME}",
    "Your enzymes are meant to digest rat poison.\n\nBy: {BOT_NAME}",
    "You should try sleeping forever.\n\nBy: {BOT_NAME}",
    "Pick up a gun and shoot yourself.\n\nBy: {BOT_NAME}",
    "You could make a world record by jumping from a plane without parachute.\n\nBy: {BOT_NAME}",
    "Stop talking BS and jump in front of a running bullet train.\n\nBy: {BOT_NAME}",
    "Try bathing with Hydrochloric Acid instead of water.\n\nBy: {BOT_NAME}",
    "Try this: if you hold your breath underwater for an hour, you can then hold it forever.\n\nBy: {BOT_NAME}",
    "Go Green! Stop inhaling Oxygen.\n\nBy: {BOT_NAME}",
    "God was searching for you. You should leave to meet him.\n\nBy: {BOT_NAME}",
    "give your 100%. Now, go donate blood.\n\nBy: {BOT_NAME}",
    "Try jumping from a hundred story building but you can do it only once.\n\nBy: {BOT_NAME}",
    "You should donate your brain seeing that you never used it.\n\nBy: {BOT_NAME}",
    "Volunteer for target in an firing range.\n\nBy: {BOT_NAME}",
    "Head shots are fun. Get yourself one.\n\nBy: {BOT_NAME}",
    "You should try swimming with great white sharks.\n\nBy: {BOT_NAME}",
    "You should paint yourself red and run in a bull marathon.\n\nBy: {BOT_NAME}",
    "You can stay underwater for the rest of your life without coming back up.\n\nBy: {BOT_NAME}",
    "How about you stop breathing for like 1 day? That'll be great.\n\nBy: {BOT_NAME}",
    "Try provoking a tiger while you both are in a cage.\n\nBy: {BOT_NAME}",
    "Have you tried shooting yourself as high as 100m using a canon.\n\nBy: {BOT_NAME}",
    "You should try holding TNT in your mouth and igniting it.\n\nBy: {BOT_NAME}",
    "Try playing catch and throw with RDX its fun.\n\nBy: {BOT_NAME}",
    "I heard phogine == poisonous but i guess you wont mind inhaling it for fun.\n\nBy: {BOT_NAME}",
    "Launch yourself into outer space while forgetting oxygen on Earth.\n\nBy: {BOT_NAME}",
    "You should try playing snake and ladders, with real snakes and no ladders.\n\nBy: {BOT_NAME}",
    "Dance naked on a couple of HT wires.\n\nBy: {BOT_NAME}",
    "Active Volcano == the best swimming pool for you.\n\nBy: {BOT_NAME}",
    "You should try hot bath in a volcano.\n\nBy: {BOT_NAME}",
    "Try to spend one day in a coffin and it will be yours forever.\n\nBy: {BOT_NAME}",
    "Hit Uranium with a slow moving neutron in your presence. It will be a worthwhile experience.\n\nBy: {BOT_NAME}",
    "You can be the first person to step on sun. Have a try.\n\nBy: {BOT_NAME}",
]

UWUS = [
    "(・`ω´・)",
    ";;w;;",
    "owo",
    "UwU",
    ">w<",
    "^w^",
    r"\(^o\) (/o^)/",
    "( ^ _ ^)∠☆",
    "(ô_ô)",
    "~:o",
    ";-;",
    "(*^*)",
    "(>_",
    "(♥_♥)",
    "*(^O^)*",
    "((+_+))",
]

FACEREACTS = [
    "ʘ‿ʘ",
    "ヾ(-_- )ゞ",
    "(っ˘ڡ˘ς)",
    "(´ж｀ς)",
    "( ಠ ʖ̯ ಠ)",
    "(° ͜ʖ͡°)╭∩╮",
    "(ᵟຶ︵ ᵟຶ)",
    "(งツ)ว",
    "ʚ(•｀",
    "(っ▀¯▀)つ",
    "(◠﹏◠)",
    "( ͡ಠ ʖ̯ ͡ಠ)",
    "( ఠ ͟ʖ ఠ)",
    "(∩｀-´)⊃━☆ﾟ.*･｡ﾟ",
    "(⊃｡•́‿•̀｡)⊃",
    "(._.)",
    "{•̃_•̃}",
    "(ᵔᴥᵔ)",
    "♨_♨",
    "⥀.⥀",
    "ح˚௰˚づ ",
    "(҂◡_◡)",
    "ƪ(ړײ)‎ƪ​​",
    "(っ•́｡•́)♪♬",
    "◖ᵔᴥᵔ◗ ♪ ♫ ",
    "(☞ﾟヮﾟ)☞",
    "[¬º-°]¬",
    "(Ծ‸ Ծ)",
    "(•̀ᴗ•́)و ̑̑",
    "ヾ(´〇`)ﾉ♪♪♪",
    "(ง'̀-'́)ง",
    "ლ(•́•́ლ)",
    "ʕ •́؈•̀ ₎",
    "♪♪ ヽ(ˇ∀ˇ )ゞ",
    "щ（ﾟДﾟщ）",
    "( ˇ෴ˇ )",
    "눈_눈",
    "(๑•́ ₃ •̀๑) ",
    "( ˘ ³˘)♥ ",
    "ԅ(≖‿≖ԅ)",
    "♥‿♥",
    "◔_◔",
    "⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾",
    "乁( ◔ ౪◔)「      ┑(￣Д ￣)┍",
    "( ఠൠఠ )ﾉ",
    "٩(๏_๏)۶",
    "┌(ㆆ㉨ㆆ)ʃ",
    "ఠ_ఠ",
    "(づ｡◕‿‿◕｡)づ",
    "(ノಠ ∩ಠ)ノ彡( \\o°o)\\",
    "“ヽ(´▽｀)ノ”",
    "༼ ༎ຶ ෴ ༎ຶ༽",
    "｡ﾟ( ﾟஇ‸இﾟ)ﾟ｡",
    "(づ￣ ³￣)づ",
    "(⊙.☉)7",
    "ᕕ( ᐛ )ᕗ",
    "t(-_-t)",
    "(ಥ⌣ಥ)",
    "ヽ༼ ಠ益ಠ ༽ﾉ",
    "༼∵༽ ༼⍨༽ ༼⍢༽ ༼⍤༽",
    "ミ●﹏☉ミ",
    "(⊙_◎)",
    "¿ⓧ_ⓧﮌ",
    "ಠ_ಠ",
    "(´･_･`)",
    "ᕦ(ò_óˇ)ᕤ",
    "⊙﹏⊙",
    "(╯°□°）╯︵ ┻━┻",
    r"¯\_(⊙︿⊙)_/¯",
    "٩◔̯◔۶",
    "°‿‿°",
    "ᕙ(⇀‸↼‶)ᕗ",
    "⊂(◉‿◉)つ",
    "V•ᴥ•V",
    "q(❂‿❂)p",
    "ಥ_ಥ",
    "ฅ^•ﻌ•^ฅ",
    "ಥ﹏ಥ",
    "（ ^_^）o自自o（^_^ ）",
    "ಠ‿ಠ",
    "ヽ(´▽`)/",
    "ᵒᴥᵒ#",
    "( ͡° ͜ʖ ͡°)",
    "┬─┬﻿ ノ( ゜-゜ノ)",
    "ヽ(´ー｀)ノ",
    "☜(⌒▽⌒)☞",
    "ε=ε=ε=┌(;*´Д`)ﾉ",
    "(╬ ಠ益ಠ)",
    "┬─┬⃰͡ (ᵔᵕᵔ͜ )",
    "┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻",
    r"¯\_(ツ)_/¯",
    "ʕᵔᴥᵔʔ",
    "(`･ω･´)",
    "ʕ•ᴥ•ʔ",
    "ლ(｀ー´ლ)",
    "ʕʘ̅͜ʘ̅ʔ",
    "（　ﾟДﾟ）",
    r"¯\(°_o)/¯",
    "(｡◕‿◕｡)",
]

RUNS_STR = [
    "Runs to Thanos..\n\nBy: {BOT_NAME}",
    "Runs far, far away from earth..\n\nBy: {BOT_NAME}",
    "Running faster than Bolt coz i'mma userbot !!\n\nBy: {BOT_NAME}",
    "Runs to Marie..\n\nBy: {BOT_NAME}",
    "This Group == too cancerous to deal with.\n\nBy: {BOT_NAME}",
    "Cya bois\n\nBy: {BOT_NAME}",
    "Kys\n\nBy: {BOT_NAME}",
    "I go away\n\nBy: {BOT_NAME}",
    "I am just walking off, coz me == too fat.\n\nBy: {BOT_NAME}",
    "I Fugged off!\n\nBy: {BOT_NAME}",
    "Will run for chocolate.\n\nBy: {BOT_NAME}",
    "I run because I really like food.\n\nBy: {BOT_NAME}",
    "Running...\nbecause dieting == not an option.\n\nBy: {BOT_NAME}",
    "Wicked fast runnah\n\nBy: {BOT_NAME}",
    "If you wanna catch me, you got to be fast...\nIf you wanna stay with me, you got to be good...\nBut if you wanna pass me...\nYou've got to be kidding.\n\nBy: {BOT_NAME}",
    "Anyone can run a hundred meters, it's the next forty-two thousand and two hundred that count.\n\nBy: {BOT_NAME}",
    "Why are all these people following me?\n\nBy: {BOT_NAME}",
    "Are the kids still chasing me?\n\nBy: {BOT_NAME}",
    "Running a marathon...there's an app for that.\n\nBy: {BOT_NAME}",
]

CHASE_STR = [
    "Where do you think you're going?\n\nBy: {BOT_NAME}",
    "Huh? what? did they get away?\n\nBy: {BOT_NAME}",
    "ZZzzZZzz... Huh? what? oh, just them again, nevermind.\n\nBy: {BOT_NAME}",
    "Get back here!\n\nBy: {BOT_NAME}",
    "Not so fast...\n\nBy: {BOT_NAME}",
    "Look out for the wall!\n\nBy: {BOT_NAME}",
    "Don't leave me alone with them!!\n\nBy: {BOT_NAME}",
    "You run, you die.\n\nBy: {BOT_NAME}",
    "Jokes on you, I'm everywhere\n\nBy: {BOT_NAME}",
    "You're gonna regret that...\n\nBy: {BOT_NAME}",
    "You could also try /kickme, I hear that's fun.\n\nBy: {BOT_NAME}",
    "Go bother someone else, no-one here cares.\n\nBy: {BOT_NAME}",
    "You can run, but you can't hide.\n\nBy: {BOT_NAME}",
    "Is that all you've got?\n\nBy: {BOT_NAME}",
    "I'm behind you...\n\nBy: {BOT_NAME}",
    "You've got company!\n\nBy: {BOT_NAME}",
    "We can do this the easy way, or the hard way.\n\nBy: {BOT_NAME}",
    "You just don't get it, do you?\n\nBy: {BOT_NAME}",
    "Yeah, you better run!\n\nBy: {BOT_NAME}",
    "Please, remind me how much I care?\n\nBy: {BOT_NAME}",
    "I'd run faster if I were you.\n\nBy: {BOT_NAME}",
    "That's definitely the droid we're looking for.\n\nBy: {BOT_NAME}",
    "May the odds be ever in your favour.\n\nBy: {BOT_NAME}",
    "Famous last words.\n\nBy: {BOT_NAME}",
    "And they disappeared forever, never to be seen again.\n\nBy: {BOT_NAME}",
    "\"Oh, look at me! I'm so cool, I can run from a bot!\" - this person\n\nBy: {BOT_NAME}",
    "Yeah yeah, just tap /kickme already.\n\nBy: {BOT_NAME}",
    "Here, take this ring and head to Mordor while you're at it.\n\nBy: {BOT_NAME}",
    "Legend has it, they're still running...\n\nBy: {BOT_NAME}",
    "Unlike Harry Potter, your parents can't protect you from me.\n\nBy: {BOT_NAME}",
    "Fear leads to anger. Anger leads to hate. Hate leads to suffering. If you keep running in fear, you might \n\nBy: {BOT_NAME}",
    "be the next Vader.\n\nBy: {BOT_NAME}",
    "Multiple calculations later, I have decided my interest in your shenanigans == exactly 0.\n\nBy: {BOT_NAME}",
    "Legend has it, they're still running.\n\nBy: {BOT_NAME}",
    "Keep it up, not sure we want you here anyway.\n\nBy: {BOT_NAME}",
    "You're a wiza- Oh. Wait. You're not Harry, keep moving.\n\nBy: {BOT_NAME}",
    "NO RUNNING IN THE HALLWAYS!\n\nBy: {BOT_NAME}",
    "Hasta la vista, baby.\n\nBy: {BOT_NAME}",
    "Who let the dogs out?\n\nBy: {BOT_NAME}",
    "It's funny, because no one cares.\n\nBy: {BOT_NAME}",
    "Ah, what a waste. I liked that one.\n\nBy: {BOT_NAME}",
    "Frankly, my dear, I don't give a damn.\n\nBy: {BOT_NAME}",
    "My milkshake brings all the boys to yard... So run faster!\n\nBy: {BOT_NAME}",
    "You can't HANDLE the truth!\n\nBy: {BOT_NAME}",
    "A long time ago, in a galaxy far far away... Someone would've cared about that. Not anymore though.\n\nBy: {BOT_NAME}",
    "Hey, look at them! They're running from the inevitable banhammer... Cute.\n\nBy: {BOT_NAME}",
    "Han shot first. So will I.\n\nBy: {BOT_NAME}",
    "What are you running after, a white rabbit?\n\nBy: {BOT_NAME}",
    "As The Doctor would say... RUN!\n\nBy: {BOT_NAME}",
]

HELLOSTR = [
    "Hi !",
    "‘Ello, gov'nor!",
    "What’s crackin’?",
    "‘Sup, homeslice?",
    "Howdy, howdy ,howdy!",
    "Hello, who's there, I'm talking.",
    "You know who this is.",
    "Yo!",
    "Whaddup.",
    "Greetings and salutations!",
    "Hello, sunshine!",
    "Hey, howdy, hi!",
    "What’s kickin’, little chicken?",
    "Peek-a-boo!",
    "Howdy-doody!",
    "Hey there, freshman!",
    "I come in peace!",
    "Ahoy, matey!",
    "Hiya!",
]

SHGS = [
    "┐(´д｀)┌",
    "┐(´～｀)┌",
    "┐(´ー｀)┌",
    "┐(￣ヘ￣)┌",
    "╮(╯∀╰)╭",
    "╮(╯_╰)╭",
    "┐(´д`)┌",
    "┐(´∀｀)┌",
    "ʅ(́◡◝)ʃ",
    "┐(ﾟ～ﾟ)┌",
    "┐('д')┌",
    "┐(‘～`;)┌",
    "ヘ(´－｀;)ヘ",
    "┐( -“-)┌",
    "ʅ（´◔౪◔）ʃ",
    "ヽ(゜～゜o)ノ",
    "ヽ(~～~ )ノ",
    "┐(~ー~;)┌",
    "┐(-。ー;)┌",
    r"¯\_(ツ)_/¯",
    r"¯\_(⊙_ʖ⊙)_/¯",
    r"¯\_༼ ಥ ‿ ಥ ༽_/¯",
    "乁( ⁰͡  Ĺ̯ ⁰͡ ) ㄏ",
]

CRI = [
    "أ‿أ",
    "╥﹏╥",
    "(;﹏;)",
    "(ToT)",
    "(┳Д┳)",
    "(ಥ﹏ಥ)",
    "（；へ：）",
    "(T＿T)",
    "（πーπ）",
    "(Ｔ▽Ｔ)",
    "(⋟﹏⋞)",
    "（ｉДｉ）",
    "(´Д⊂ヽ",
    "(;Д;)",
    "（>﹏<）",
    "(TдT)",
    "(つ﹏⊂)",
    "༼☯﹏☯༽",
    "(ノ﹏ヽ)",
    "(ノAヽ)",
    "(╥_╥)",
    "(T⌓T)",
    "(༎ຶ⌑༎ຶ)",
    "(☍﹏⁰)｡",
    "(ಥ_ʖಥ)",
    "(つд⊂)",
    "(≖͞_≖̥)",
    "(இ﹏இ`｡)",
    "༼ಢ_ಢ༽",
    "༼ ༎ຶ ෴ ༎ຶ༽",
]

SLAP_TEMPLATES = [
    "{hits} {victim} with a {item}.\n\nBy: {BOT_NAME}",
    "{hits} {victim} in the face with a {item}.\n\nBy: {BOT_NAME}",
    "{hits} {victim} around a bit with a {item}.\n\nBy: {BOT_NAME}",
    "{throws} a {item} at {victim}.\n\nBy: {BOT_NAME}",
    "grabs a {item} and {throws} it at {victim}'s face.\n\nBy: {BOT_NAME}",
    "{hits} a {item} at {victim}.\n\nBy: {BOT_NAME}",
    "{throws} a few {item} at {victim}.\n\nBy: {BOT_NAME}",
    "grabs a {item} and {throws} it in {victim}'s face.\n\nBy: {BOT_NAME}",
    "launches a {item} in {victim}'s general direction.\n\nBy: {BOT_NAME}",
    "sits on {victim}'s face while slamming a {item} {where}.\n\nBy: {BOT_NAME}",
    "starts slapping {victim} silly with a {item}.\n\nBy: {BOT_NAME}",
    "pins {victim} down and repeatedly {hits} them with a {item}.\n\nBy: {BOT_NAME}",
    "grabs up a {item} and {hits} {victim} with it.\n\nBy: {BOT_NAME}",
    "starts slapping {victim} silly with a {item}.\n\nBy: {BOT_NAME}",
    "holds {victim} down and repeatedly {hits} them with a {item}.\n\nBy: {BOT_NAME}",
    "prods {victim} with a {item}.\n\nBy: {BOT_NAME}",
    "picks up a {item} and {hits} {victim} with it.\n\nBy: {BOT_NAME}",
    "ties {victim} to a chair and {throws} a {item} at them.\n\nBy: {BOT_NAME}",
    "{hits} {victim} {where} with a {item}.\n\nBy: {BOT_NAME}",
    "ties {victim} to a pole and whips them {where} with a {item}\n\nBy: {BOT_NAME}."
    "gave a friendly push to help {victim} learn to swim in lava.\n\nBy: {BOT_NAME}",
    "sent {victim} to /dev/null.\n\nBy: {BOT_NAME}",
    "sent {victim} down the memory hole.\n\nBy: {BOT_NAME}",
    "beheaded {victim}.\n\nBy: {BOT_NAME}", 
    "threw {victim} off a building.\n\nBy: {BOT_NAME}",
    "replaced all of {victim}'s music with Nickelback.\n\nBy: {BOT_NAME}",
    "spammed {victim}'s email.\n\nBy: {BOT_NAME}",
    "made {victim} a knuckle sandwich.\n\nBy: {BOT_NAME}",
    "slapped {victim} with pure nothing.\n\nBy: {BOT_NAME}",
    "hit {victim} with a small, interstellar spaceship.\n\nBy: {BOT_NAME}",
    "quickscoped {victim}.\n\nBy: {BOT_NAME}",
    "put {victim} in check-mate.\n\nBy: {BOT_NAME}",
    "RSA-encrypted {victim} and deleted the private key.\n\nBy: {BOT_NAME}",
    "put {victim} in the friendzone.\n\nBy: {BOT_NAME}",
    "slaps {victim} with a DMCA takedown request!\n\nBy: {BOT_NAME}"
]

ITEMS = [
    "cast iron skillet",
    "large trout",
    "baseball bat",
    "cricket bat",
    "wooden cane",
    "nail",
    "printer",
    "shovel",
    "pair of trousers",
    "CRT monitor",
    "diamond sword",
    "baguette",
    "physics textbook",
    "toaster",
    "portrait of Richard Stallman",
    "television",
    "mau5head",
    "five ton truck",
    "roll of duct tape",
    "book",
    "laptop",
    "old television",
    "sack of rocks",
    "rainbow trout",
    "cobblestone block",
    "lava bucket",
    "rubber chicken",
    "spiked bat",
    "gold block",
    "fire extinguisher",
    "heavy rock",
    "chunk of dirt",
    "beehive",
    "piece of rotten meat",
    "bear",
    "ton of bricks",
]

THROW = [
    "throws",
    "flings",
    "chucks",
    "hurls",
]

HIT = [
    "hits",
    "whacks",
    "slaps",
    "smacks",
    "bashes",
]

WHERE = ["in the chest", "on the head", "on the butt", "on the crotch"]

# ===========================================


@register(outgoing=True, pattern=r"^.(\w+)say (.*)")
async def univsaye(cowmsg):
    """ For .cowsay module, userbot wrapper for cow which says things. """
    arg = cowmsg.pattern_match.group(1).lower()
    text = cowmsg.pattern_match.group(2)

    if arg == "cow":
        arg = "default"
    if arg not in cow.COWACTERS:
        return
    cheese = cow.get_cow(arg)
    cheese = cheese()

    await cowmsg.edit(f"`{cheese.milk(text).replace('`', '´')}`")


@register(outgoing=True, pattern="^:/$", ignore_unsafe=True)
async def kek(keks):
    """ Check yourself ;)"""
    uio = ["/", "\\"]
    for i in range(1, 15):
        time.sleep(0.3)
        await keks.edit(":" + uio[i % 2])


@register(outgoing=True, pattern=r"^.coinflip (.*)")
async def coin(event):
    r = choice(["heads", "tails"])
    input_str = event.pattern_match.group(1)
    if input_str:
        input_str = input_str.lower()
    if r == "heads":
        if input_str == "heads":
            await event.edit(
                "The coin landed on: **Heads**.\nYou were correct.")
        elif input_str == "tails":
            await event.edit(
                "The coin landed on: **Heads**.\nYou weren't correct, try again ..."
            )
        else:
            await event.edit("The coin landed on: **Heads**.")
    elif r == "tails":
        if input_str == "tails":
            await event.edit(
                "The coin landed on: **Tails**.\nYou were correct.")
        elif input_str == "heads":
            await event.edit(
                "The coin landed on: **Tails**.\nYou weren't correct, try again ..."
            )
        else:
            await event.edit("The coin landed on: **Tails**.")


@register(pattern="^.slap(?: |$)(.*)", outgoing=True)
async def who(event):
    """ slaps a user, or get slapped if not a reply. """
    replied_user = await get_user_from_event(event)
    if replied_user:
        replied_user = replied_user[0]
    else:
        return
    caption = await slap(replied_user, event)

    try:
        await event.edit(caption)

    except BaseException:
        await event.edit(
            "`Can't slap this person, need to fetch some sticks and stones !!`"
        )


async def slap(replied_user, event):
    """ Construct a funny slap sentence !! """
    user_id = replied_user.id
    first_name = replied_user.first_name
    username = replied_user.username
    global BOT_NAME

    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"

    temp = choice(SLAP_TEMPLATES)
    item = choice(ITEMS)
    hit = choice(HIT)
    throw = choice(THROW)
    where = choice(WHERE)

    caption = "..." + temp.format(
        victim=slapped, item=item, hits=hit, throws=throw, where=where,BOT_NAME=BOT_NAME)

    return caption


@register(outgoing=True, pattern="^-_-$", ignore_unsafe=True)
async def lol(lel):
    """ Ok... """
    okay = "-_-"
    for i in range(10):
        okay = okay[:-1] + "_-"
        await lel.edit(okay)


@register(outgoing=True, pattern="^.(yes|no|maybe|decide)$")
async def decide(event):
    decision = event.pattern_match.group(1).lower()
    message_id = event.reply_to_msg_id if event.reply_to_msg_id else None
    if decision != "decide":
        r = requests.get(f"https://yesno.wtf/api?force={decision}").json()
    else:
        r = requests.get(f"https://yesno.wtf/api").json()
    await event.delete()
    await event.client.send_message(event.chat_id,
                                    str(r["answer"]).upper(),
                                    reply_to=message_id,
                                    file=r["image"])


@register(outgoing=True, pattern="^;_;$", ignore_unsafe=True)
async def fun(e):
    t = ";_;"
    for j in range(10):
        t = t[:-1] + "_;"
        await e.edit(t)


@register(outgoing=True, pattern="^.fp$")
async def facepalm(e):
    """ Facepalm  🤦‍♂ """
    await e.edit("🤦‍♂")


@register(outgoing=True, pattern="^.cry$")
async def cry(e):
    """ y u du dis, i cry everytime !! """
    await e.edit(choice(CRI))


@register(outgoing=True, pattern="^.insult$")
async def insult(e):
    """ I make you cry !! """
    global BOT_NAME
    await e.edit(choice(INSULT_STRINGS))


@register(outgoing=True, pattern="^.cp(?: |$)(.*)")
async def copypasta(cp_e):
    """ Copypasta the famous meme """
    textx = await cp_e.get_reply_message()
    message = cp_e.pattern_match.group(1)

    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await cp_e.edit("`😂🅱️IvE👐sOME👅text👅for✌️Me👌tO👐MAkE👀iT💞funNy!💦`")
        return

    reply_text = choice(EMOJIS)
    # choose a random character in the message to be substituted with 🅱️
    b_char = choice(message).lower()
    for owo in message:
        if owo == " ":
            reply_text += choice(EMOJIS)
        elif owo in EMOJIS:
            reply_text += owo
            reply_text += choice(EMOJIS)
        elif owo.lower() == b_char:
            reply_text += "🅱️"
        else:
            if bool(getrandbits(1)):
                reply_text += owo.upper()
            else:
                reply_text += owo.lower()
    reply_text += choice(EMOJIS)
    await cp_e.edit(reply_text)


@register(outgoing=True, pattern="^.vapor(?: |$)(.*)")
async def vapor(vpr):
    """ Vaporize everything! """
    reply_text = list()
    textx = await vpr.get_reply_message()
    message = vpr.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await vpr.edit("`Ｇｉｖｅ ｓｏｍｅ ｔｅｘｔ ｆｏｒ ｖａｐｏｒ！`")
        return

    for charac in message:
        if 0x21 <= ord(charac) <= 0x7F:
            reply_text.append(chr(ord(charac) + 0xFEE0))
        elif ord(charac) == 0x20:
            reply_text.append(chr(0x3000))
        else:
            reply_text.append(charac)

    await vpr.edit("".join(reply_text))


@register(outgoing=True, pattern="^.str(?: |$)(.*)")
async def stretch(stret):
    """ Stretch it."""
    textx = await stret.get_reply_message()
    message = stret.text
    message = stret.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await stret.edit("`GiiiiiiiB sooooooomeeeeeee teeeeeeext!`")
        return

    count = randint(3, 10)
    reply_text = sub(r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵаеиоуюяыэё])", (r"\1" * count),
                     message)
    await stret.edit(reply_text)


@register(outgoing=True, pattern="^.zal(?: |$)(.*)")
async def zal(zgfy):
    """ Invoke the feeling of chaos. """
    reply_text = list()
    textx = await zgfy.get_reply_message()
    message = zgfy.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await zgfy.edit(
            "`gͫ ̆ i̛ ̺ v͇̆ ȅͅ   a̢ͦ   s̴̪ c̸̢ ä̸ rͩͣ y͖͞   t̨͚ é̠ x̢͖  t͔͛`"
        )
        return

    for charac in message:
        if not charac.isalpha():
            reply_text.append(charac)
            continue

        for _ in range(0, 3):
            randint = randint(0, 2)

            if randint == 0:
                charac = charac.strip() + \
                    choice(ZALG_LIST[0]).strip()
            elif randint == 1:
                charac = charac.strip() + \
                    choice(ZALG_LIST[1]).strip()
            else:
                charac = charac.strip() + \
                    choice(ZALG_LIST[2]).strip()

        reply_text.append(charac)

    await zgfy.edit("".join(reply_text))


@register(outgoing=True, pattern="^.hi$")
async def hoi(hello):
    """ Greet everyone! """
    await hello.edit(choice(HELLOSTR))


@register(outgoing=True, pattern="^.owo(?: |$)(.*)")
async def faces(owo):
    """ UwU """
    textx = await owo.get_reply_message()
    message = owo.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await owo.edit("` UwU no text given! `")
        return

    reply_text = sub(r"(r|l)", "w", message)
    reply_text = sub(r"(R|L)", "W", reply_text)
    reply_text = sub(r"n([aeiou])", r"ny\1", reply_text)
    reply_text = sub(r"N([aeiouAEIOU])", r"Ny\1", reply_text)
    reply_text = sub(r"\!+", " " + choice(UWUS), reply_text)
    reply_text = reply_text.replace("ove", "uv")
    reply_text += " " + choice(UWUS)
    await owo.edit(reply_text)


@register(outgoing=True, pattern="^.react$")
async def react_meme(react):
    """ Make your userbot react to everything. """
    await react.edit(choice(FACEREACTS))


@register(outgoing=True, pattern="^.shg$")
async def shrugger(shg):
    r""" ¯\_(ツ)_/¯ """
    await shg.edit(choice(SHGS))


@register(outgoing=True, pattern="^.chase$")
async def police(chase):
    """ Run boi run, i'm gonna catch you !! """
    global BOT_NAME
    await chase.edit(choice(CHASE_STR))


@register(outgoing=True, pattern="^.run$")
async def runner_lol(run):
    """ Run, run, RUNNN! """
    global BOT_NAME
    await run.edit(choice(RUNS_STR))


@register(outgoing=True, pattern="^.metoo$")
async def metoo(hahayes):
    """ Haha yes """
    await hahayes.edit(choice(METOOSTR))


@register(outgoing=True, pattern="^.Oof$")
async def Oof(e):
    t = "Oof"
    for j in range(16):
        t = t[:-1] + "of"
        await e.edit(t)

                      
@register(outgoing=True, pattern="^.oem$")
async def Oem(e):
    t = "Oem"
    for j in range(16):
        t = t[:-1] + "em"
        await e.edit(t)




@register(outgoing=True, pattern="^.Oem$")
async def Oem(e):
    t = "Oem"
    for j in range(16):
        t = t[:-1] + "em"
        await e.edit(t)



@register(outgoing=True, pattern="^.10iq$")
async def iqless(e):
    await e.edit("♿")


@register(outgoing=True, pattern="^.moon$")
async def moon(event):
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.clock$")
async def clock(event):
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.mock(?: |$)(.*)")
async def spongemocktext(mock):
    """ Do it and find the real fun. """
    reply_text = list()
    textx = await mock.get_reply_message()
    message = mock.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await mock.edit("`gIvE sOMEtHInG tO MoCk!`")
        return

    for charac in message:
        if charac.isalpha() and randint(0, 1):
            to_app = charac.upper() if charac.islower() else charac.lower()
            reply_text.append(to_app)
        else:
            reply_text.append(charac)

    await mock.edit("".join(reply_text))


@register(outgoing=True, pattern="^.clap(?: |$)(.*)")
async def claptext(memereview):
    """ Praise people! """
    textx = await memereview.get_reply_message()
    message = memereview.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await memereview.edit("`Hah, I don't clap pointlessly!`")
        return
    reply_text = "👏 "
    reply_text += message.replace(" ", " 👏 ")
    reply_text += " 👏"
    await memereview.edit(reply_text)


@register(outgoing=True, pattern="^.bt$")
async def bluetext(bt_e):
    """ Believe me, you will find this useful. """
    if await bt_e.get_reply_message() and bt_e.is_group:
        await bt_e.edit(
            "/BLUETEXT /MUST /CLICK.\n"
            "/ARE /YOU /A /STUPID /ANIMAL /WHICH /IS /ATTRACTED /TO /COLOURS?")


@register(outgoing=True, pattern=r"^.f (.*)")
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8, paytext * 8, paytext * 2, paytext * 2, paytext * 2,
        paytext * 6, paytext * 6, paytext * 2, paytext * 2, paytext * 2,
        paytext * 2, paytext * 2)
    await event.edit(pay)


@register(outgoing=True, pattern="^.lfy (.*)")
async def let_me_google_that_for_you(lmgtfy_q):
    textx = await lmgtfy_q.get_reply_message()
    qry = lmgtfy_q.pattern_match.group(1)
    if qry:
        query = str(qry)
    elif textx:
        query = textx
        query = query.message
    query_encoded = query.replace(" ", "+")
    lfy_url = f"http://lmgtfy.com/?s=g&iie=1&q={query_encoded}"
    payload = {'format': 'json', 'url': lfy_url}
    r = requests.get('http://is.gd/create.php', params=payload)
    await lmgtfy_q.edit(f"Here you are, help yourself.\
    \n[{query}]({r.json()['shorturl']})")


@register(pattern=r".scam(?: |$)(.*)", outgoing=True)
async def scam(event):
    """ Just a small command to fake chat actions for fun !! """
    options = [
        'typing', 'contact', 'game', 'location', 'voice', 'round', 'video',
        'photo', 'document', 'cancel'
    ]
    input_str = event.pattern_match.group(1)
    args = input_str.split()
    if len(args) == 0:  # Let bot decide action and time
        scam_action = choice(options)
        scam_time = randint(30, 60)
    elif len(args) == 1:  # User decides time/action, bot decides the other.
        try:
            scam_action = str(args[0]).lower()
            scam_time = randint(30, 60)
        except ValueError:
            scam_action = choice(options)
            scam_time = int(args[0])
    elif len(args) == 2:  # User decides both action and time
        scam_action = str(args[0]).lower()
        scam_time = int(args[1])
    else:
        await event.edit("`Invalid Syntax !!`")
        return
    try:
        if (scam_time > 0):
            await event.delete()
            async with event.client.action(event.chat_id, scam_action):
                await sleep(scam_time)
    except BaseException:
        return


@register(pattern=r".type(?: |$)(.*)", outgoing=True)
async def typewriter(typew):
    """ Just a small command to make your keyboard become a typewriter! """
    textx = await typew.get_reply_message()
    message = typew.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await typew.edit("`Give a text to type!`")
        return
    sleep_time = 0.03
    typing_symbol = "|"
    old_text = ""
    await typew.edit(typing_symbol)
    await sleep(sleep_time)
    for character in message:
        old_text = old_text + "" + character
        typing_text = old_text + "" + typing_symbol
        await typew.edit(typing_text)
        await sleep(sleep_time)
        await typew.edit(old_text)
        await sleep(sleep_time)


CMD_HELP.update({
    "memes":
    ".cowsay\
\nUsage: cow which says things.\
\n\n:/\
\nUsage: Check yourself ;)\
\n\n-_-\
\nUsage: Ok...\
\n\n;_;\
\nUsage: Like `-_-` but crying.\
\n\n.cp\
\nUsage: Copypasta the famous meme\
\n\n.vapor\
\nUsage: Vaporize everything!\
\n\n.str\
\nUsage: Stretch it.\
\n\n.10iq\
\nUsage: You retard !!\
\n\n.zal\
\nUsage: Invoke the feeling of chaos.\
\n\nOem\
\nUsage: Oeeeem\
\n\nOof\
\nUsage: Ooooof\
\n\n.fp\
\nUsage: Facepalm :P\
\n\n.moon\
\nUsage: kensar moon animation.\
\n\n.clock\
\nUsage: kensar clock animation.\
\n\n.hi\
\nUsage: Greet everyone!\
\n\n.coinflip <heads/tails>\
\nUsage: Flip a coin !!\
\n\n.owo\
\nUsage: UwU\
\n\n.react\
\nUsage: Make your userbot react to everything.\
\n\n.slap\
\nUsage: reply to slap them with random objects !!\
\n\n.cry\
\nUsage: y u du dis, i cri.\
\n\n.shg\
\nUsage: Shrug at it !!\
\n\n.run\
\nUsage: Let Me Run, run, RUNNN!\
\n\n.chase\
\nUsage: You better start running\
\n\n.metoo\
\nUsage: Haha yes\
\n\n.mock\
\nUsage: Do it and find the real fun.\
\n\n.clap\
\nUsage: Praise people!\
\n\n.f <emoji/character>\
\nUsage: Pay Respects.\
\n\n.bt\
\nUsage: Believe me, you will find this useful.\
\n\n.type\
\nUsage: Just a small command to make your keyboard become a typewriter!\
\n\n.lfy <query>\
\nUsage: Let me Google that for you real quick !!\
\n\n.decide [Alternates: (.yes, .no, .maybe)]\
\nUsage: Make a quick decision.\
\n\n.scam <action> <time>\
\n[Available Actions: (typing, contact, game, location, voice, round, video, photo, document, cancel)]\
\nUsage: Create fake chat actions, for fun. (Default action: typing)\
\n\n\nThanks to 🅱️ottom🅱️ext🅱️ot (@NotAMemeBot) for some of these."
})
