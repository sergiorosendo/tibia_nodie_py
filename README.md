# Under development
Tibia bot using Python. Currently under development.

Python features used: 

	- OOP
	- Threads
	- Macros
	- Keyboard control
	- .json and .ini files parsing
	among others

# Tibia NoDie
*NoDie* features macros, shortcuts and auto-healers for the PC game Tibia. Created with Python, featuring heavy OOP, modularization and scalability.

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


