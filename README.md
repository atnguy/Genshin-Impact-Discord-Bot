# Genshin-Impact-Discord-Bot v1.1.0
A discord bot dedicated to displaying information of the materials needed to perform ascensions or talent level ups for the game "Genshin Impact" through embeds on Discord.
(also my first time working on a discord bot)
## Files

### .env
Location of where the discord bot's token should be to make the code work. Because I'm locally hosting the bot, if you want to use these features, you'll have to make your own bot and place their token in there.

### genshin.py
Location of the code for the discord bot.

## Features
* Obtain a list of ascension materials for each ascension for the requested character in an embed
![alt text](https://i.imgur.com/NB5fmpE.png)
* Obtain a list of talent materials for each level for the requested character in an embed.
![alt text](https://i.imgur.com/QAxzHl2.png)

## How to use
I don't plan on hosting my bot via a web service and I will use my bot for personal uses. You'll have to create your own discord bot and place your bot's token into the .env file and run genshin.py locally. 
[Link to the discord developer portal documentation for how to make a discord bot](https://discord.com/developers/docs/intro)
### Commands
* the command prefix for this bot is "!genshin "
* !genshin help provides the entire list of commands. !genshin help <command> provides a detailed description of each command
* !genshin <character_name> [flags]. Replace <character_name> with the character name to obtain the list of ascension materials in an embed. [flags] is an optional parameter where you can input either  'talent' to see the talent material list instead or 'all' to see both. For the traveler, [flags] input options are 'talentanemo' to see the talent materials for the Anemo Traveler or 'talentgeo' to see the talent materials for the Geo Traveler 
## Status of this project
### Planned updates
* Weapons
* ~Talents~
* Materials avaible for current day in domains
* Domains

## Changelog
* v1.1.0: Added Talents. Added Tartaglia
* v1.0.0: Created project
