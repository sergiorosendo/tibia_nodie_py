Python version of [Tibia NoDie](https://github.com/sergiorosendo/tibia_no_die).

## Under development

Currently under development. Python features used: 

- OOP
- Threads
- Macros
- Keyboard control
- .json and .ini files parsing

### Objective

The python version aspires to be a more scalable, maintanable version of the ahk bot. 

NoDie Py aspires to be a game inside the game. It should have access to player vocation, resources, hotkeys, game window and be able to take the best action in every scenario.

#### Avoiding Detection

The bot should also try to hide itself. It will avoid repetitive behavior while still being extremely efficient in assisting the player.

#### Auto Healer - Global Server vs Ot Servers

The main Tibia server does not allow external software to directly access the game window, which is a invaluable source of information for the auto healer. 
A workaround for this exists but the healer should have slower reaction times due to its limited acess. So for now, for the main Tibia Client, the plan is to develop a auto mana healer, as this healer can be useful even if acting with slightly higher delays.

As for Otservers, if the bot has unrestriscted access to the game window, the healer should be extremely fast and smart, managing both hp and mp. 

## Tibia NoDie
*NoDie* features macros, shortcuts and auto-healers for the PC game Tibia. 

## Main Features

### Magic Level Training in Protection Zone
As you may know, with some daily rewards you receive the ability to regenerate mana and soul points while in protection zones.

Set keys, up to four, for each of these actions:

- Equip boots
	- *Pair of Soft Boots*
- Equip ring
	- *Ring of Healing* or *Life Ring*
- Eat Food
	- *brown mushrooms*
- Use spell to create rune
	- *Sudden Death*, *Avalanche*, *Paralyze*, etc.
- Use spell to waste excessive mana 
	- Any support spell, default is Haste.

Setting up multiple keys for each of these allows *NoDie* to use a random key everytime it makes an action. This prevents the Tibia client from identifying repetitive keypressing patterns, a common issue with simple macros.

Performing these actions, in a protection zone, your character will safely train magic level while crafting runes and making a profit. 

###### Works while minimized

These actions will be performed even if your Tibia window is minimized, so you can freely use your computer while your character safely improves its magic level.

Wanna watch a movie or play Dota while still training magic level? With *NoDie* you can do just that!

Keys are sent directly to your Tibia Client, so *NoDie*'s actions will not interfere with anything that you are doing or typing.

#### Tips and Tricks

###### Refill your character
Make sure to refill your character with the necessary resources to keep crafting runes and regenerating mana. For instance, for 24 hours of *sudden death rune* making, your character should need:

- 6 to 7 *soft boots*
- 192 *rings of healing*
- ~300 *brown mushrooms*
- ~1k *blank runes*

###### Try to make a profit

If you sell your runes for the same price as npcs do and buy Rings of Healing for up to 1.5k each, you should be able get some daily profit.

Always renew your buying offers for RoH in market and try to keep their price as low as possible. Do note that, as *NoDie* and other similar bots become common place, RoH demand may increase substantially and, if so, its price will rise.

###### Avoid unnecessary attention
Rent a house with at least one SQM that is not visible from anywhere outside the house and train ML in that spot.

As you might want to stay afk and train ml for hours on end, you don't want other players to notice that your character is standing still and performing repetitive actions.

If other players notice that you are botting, they might report you. This may not always lead to a ban but it is better to avoid it.

###### Remember to deactivate
When you wish to leave protection zone or go hunting, always remember to deactivate the script with the proper hotkey so that the rune maker does not interfere with your gameplay.

## Avoiding BattleEye Detection

As BattleEye does not allow bots to be used, every feature in *NoDie* uses some sort of randomness to make it harder for external software to identify any repetitive patterns.

- for some actions, up to 4 keys can be registered. In every call, the corresponding method will randomly select one of these to use.
- the auto-healer's healing period continually changes using *exhaustion_time + small\_random\_number*
- every action has a *very small random delay* before being performed. This delay is unnoticeable for human eyes. 


## Planned Features
Features under development:
	
- Tray Menu 
- Auto Loot 
- Auto Heal 
- Auto Mana 
- Main Menu

## Known Bugs
Check the *Issues* Tab for known bugs.


