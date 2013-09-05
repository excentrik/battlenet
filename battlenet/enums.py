RACE = {
    1: 'Human',
    2: 'Orc',
    3: 'Dwarf',
    4: 'Night Elf',
    5: 'Undead',
    6: 'Tauren',
    7: 'Gnome',
    8: 'Troll',
    9: 'Goblin',
    10: 'Blood Elf',
    11: 'Draenei',
    22: 'Worgen',
    24: 'Pandaren',
    25: 'Pandaren',
    26: 'Pandaren',
}

CLASS = {
    1: 'Warrior',
    2: 'Paladin',
    3: 'Hunter',
    4: 'Rogue',
    5: 'Priest',
    6: 'Death Knight',
    7: 'Shaman',
    8: 'Mage',
    9: 'Warlock',
    10: 'Monk',
    11: 'Druid',
}

QUALITY = {
    1: 'Common',
    2: 'Uncommon',
    3: 'Rare',
    4: 'Epic',
    5: 'Legendary',
    6: 'Artifact',
    7: 'Heirloom',
    8: 'Quality 8',
    9: 'Quality 9',
}


RACE_TO_FACTION = {
    1: 'Alliance',
    2: 'Horde',
    3: 'Alliance',
    4: 'Alliance',
    5: 'Horde',
    6: 'Horde',
    7: 'Alliance',
    8: 'Horde',
    9: 'Horde',
    10: 'Horde',
    11: 'Alliance',
    22: 'Alliance',
    24: '?',
    25: 'Alliance',
    26: 'Horde',
}

EXPANSION = {
    0: ('wow', 'World of Warcraft'),
    1: ('bc', 'The Burning Crusade'),
    2: ('lk', 'Wrath of the Lich King'),
    3: ('cata', 'Cataclysm'),
    4: ('mop', 'Mists of Pandaria'),
}

RAIDS = {
    'wow': (2717, 2677, 3429, 3428),
    'bc': (3457, 3836, 3923, 3607, 3845, 3606, 3959, 4075),
    'lk': (4603, 3456, 4493, 4500, 4273, 2159, 4722, 4812, 4987),
    'cata': (5600, 5094, 5334, 5638, 5723, 5892),
    'mop': (6125, 6297, 6067, 6622),
}

ITEMTYPE = {
	1 : 'Head',
	2 : 'Neck',
	3 : 'Shoulder',
	4 : 'Shirt',
	5 : 'Chest',
	6 : 'Waist',
	7 : 'Legs',
	8 : 'Feet',
	9 : 'Wrist',
	10 : 'Hands',
	11 : 'Finger',
	12 : 'Trinket',
	13 : 'One-Hand',
	14 : 'Shield',
	15 : 'Ranged',
	16 : 'Cloak',
	17 : 'Two-Hand',
	18 : 'Bag',
	19 : 'Tabard',
	20 : 'Robe',
	21 : 'Main Hand',
	22 : 'Off Hand',
	23 : 'Held In Off-hand',
	24 : 'Ammo',
	25 : 'Thrown',
	26 : 'Ranged Right',
	28 : 'Relic',
}


# itemClass
# '0","Consumable"
# "1","Container"
# "2","Weapon"
# "3","Gem"
# "4","Armor"
# "5","Reagent"
# "6","Projectile"
# "7","Trade Goods"
# "8","Generic"
# "9","Book"
# "10","Money"
# "11","Quiver"
# "12","Quest"
# "13","Key"
# "14","Permanent"
# "15","Junk"
# "16","Glyph"

# itemSubClass
# "classid","subclassid","subclassname","subclassfullname"
# "0","0","Consumable",NULL
# "0","5","Food & Drink",NULL
# "0","1","Potion",NULL
# "0","2","Elixir",NULL
# "0","3","Flask",NULL
# "0","7","Bandage",NULL
# "0","6","Item Enhancement",NULL
# "0","4","Scroll",NULL
# "0","8","Other",NULL
# "1","0","Bag",NULL
# "1","1","Soul Bag",NULL
# "1","2","Herb Bag",NULL
# "1","3","Enchanting Bag",NULL
# "1","4","Engineering Bag",NULL
# "1","5","Gem Bag",NULL
# "1","6","Mining Bag",NULL
# "1","7","Leatherworking Bag",NULL
# "1","8","Inscription Bag",NULL
# "1","9","Tackle Box",NULL
# "2","0","Axe","One-Handed Axes"
# "2","1","Axe","Two-Handed Axes"
# "2","2","Bow","Bows"
# "2","3","Gun","Guns"
# "2","4","Mace","One-Handed Maces"
# "2","5","Mace","Two-Handed Maces"
# "2","6","Polearm","Polearms"
# "2","7","Sword","One-Handed Swords"
# "2","8","Sword","Two-Handed Swords"
# "2","9","Obsolete",NULL
# "2","10","Staff","Staves"
# "2","11","Exotic","One-Handed Exotics"
# "2","12","Exotic","Two-Handed Exotics"
# "2","13","Fist Weapon","Fist Weapons"
# "2","14","Miscellaneous",NULL
# "2","15","Dagger","Daggers"
# "2","16","Thrown","Thrown"
# "2","17","Spear","Spears"
# "2","18","Crossbow","Crossbows"
# "2","19","Wand","Wands"
# "2","20","Fishing Pole","Fishing Poles"
# "3","0","Red",NULL
# "3","1","Blue",NULL
# "3","2","Yellow",NULL
# "3","3","Purple",NULL
# "3","4","Green",NULL
# "3","5","Orange",NULL
# "3","6","Meta",NULL
# "3","7","Simple",NULL
# "3","8","Prismatic",NULL
# "3","9","Hydraulic",NULL
# "3","10","Cogwheel",NULL
# "4","0","Miscellaneous",NULL
# "4","1","Cloth","Cloth"
# "4","2","Leather","Leather"
# "4","3","Mail","Mail"
# "4","4","Plate","Plate"
# "4","5","Buckler(OBSOLETE)","Bucklers"
# "4","6","Shield","Shields"
# "4","7","Libram","Librams"
# "4","8","Idol","Idols"
# "4","9","Totem","Totems"
# "4","10","Sigil","Sigils"
# "4","11","Relic",NULL
# "5","0","Reagent",NULL
# "6","0","Wand(OBSOLETE)",NULL
# "6","1","Bolt(OBSOLETE)",NULL
# "6","2","Arrow",NULL
# "6","3","Bullet",NULL
# "6","4","Thrown(OBSOLETE)",NULL
# "7","0","Trade Goods",NULL
# "7","10","Elemental",NULL
# "7","15","Weapon Enchantment - Obsolete","Weapon Enchantment - Obsolete"
# "7","5","Cloth",NULL
# "7","6","Leather",NULL
# "7","7","Metal & Stone",NULL
# "7","8","Meat",NULL
# "7","9","Herb",NULL
# "7","12","Enchanting",NULL
# "7","4","Jewelcrafting",NULL
# "7","1","Parts",NULL
# "7","3","Devices",NULL
# "7","2","Explosives",NULL
# "7","13","Materials",NULL
# "7","11","Other",NULL
# "7","14","Item Enchantment","Item Enchantment"
# "8","0","Generic(OBSOLETE)",NULL
# "9","0","Book",NULL
# "9","1","Leatherworking",NULL
# "9","2","Tailoring",NULL
# "9","3","Engineering",NULL
# "9","4","Blacksmithing",NULL
# "9","5","Cooking",NULL
# "9","6","Alchemy",NULL
# "9","7","First Aid",NULL
# "9","8","Enchanting",NULL
# "9","9","Fishing",NULL
# "9","10","Jewelcrafting",NULL
# "9","11","Inscription","Inscription"
# "10","0","Money(OBSOLETE)",NULL
# "11","0","Quiver(OBSOLETE)",NULL
# "11","1","Quiver(OBSOLETE)",NULL
# "11","2","Quiver",NULL
# "11","3","Ammo Pouch",NULL
# "12","0","Quest",NULL
# "13","0","Key",NULL
# "13","1","Lockpick",NULL
# "14","0","Permanent",NULL
# "15","0","Junk",NULL
# "15","1","Reagent",NULL
# "15","2","Pet",NULL
# "15","3","Holiday",NULL
# "15","4","Other",NULL
# "15","5","Mount","Mount"
# "16","1","Warrior","Warrior"
# "16","2","Paladin","Paladin"
# "16","3","Hunter","Hunter"
# "16","4","Rogue","Rogue"
# "16","5","Priest","Priest"
# "16","6","Death Knight","Death Knight"
# "16","7","Shaman","Shaman"
# "16","8","Mage","Mage"
# "16","9","Warlock","Warlock"
# "16","11","Druid","Druid"
#
#
# inventoryType
#
# "0","None"
# "1","Head"
# "2","Neck"
# "3","Shoulder"
# "4","Shirt"
# "5","Chest"
# "6","Waist"
# "7","Legs"
# "8","Feet"
# "9","Wrist"
# "10","Hands"
# "11","Finger"
# "12","Trinket"
# "13","One-Hand"
# "14","Shield"
# "15","Ranged"
# "16","Cloak"
# "17","Two-Hand"
# "18","Bag"
# "19","Tabard"
# "20","Robe"
# "21","Main Hand"
# "22","Off Hand"
# "23","Held In Off-hand"
# "24","Ammo"
# "25","Thrown"
# "26","Ranged Right"
# "28","Relic"
#
#
# itemQuality
# "qualityid","qualityname","qualitycolor"
# "0","Poor","9D9D9D"
# "1","Common","FFFFFF"
# "2","Uncommon","1EFF00"
# "3","Rare","0070DD"
# "4","Epic","A335EE"
# "5","Legendary","FF8000"
# "6","Artifact","E5CC80"
# "7","Heirloom","E5CC80"
# "8","Quality 8","FFFF98"
# "9","Quality 9","71D5FF"
#
#
# skillLines
# "185","Cooking"
# "773","Inscription"
# "755","Jewelcrafting"
# "393","Skinning"
# "333","Enchanting"
# "202","Engineering"
# "197","Tailoring"
# "186","Mining"
# "182","Herbalism"
# "171","Alchemy"
# "165","Leatherworking"
# "164","Blacksmithing"
#
# player class
# "classid","classname","talentname1","talentname2","talentname3","talenticon1","talenticon2","talenticon3"
# "1","Warrior","Arms","Fury","Protection","INV_Sword_27","Ability_Warrior_BattleShout","INV_Shield_06"
# "2","Paladin","Holy","Protection","Retribution","Spell_Holy_HolyBolt","Spell_Holy_DevotionAura","Spell_Holy_AuraOfLight"
# "3","Hunter","Beast Mastery","Marksmanship","Survival","Ability_Hunter_BeastTaming","Ability_Marksmanship","Ability_Hunter_SwiftStrike"
# "4","Rogue","Assassination","Combat","Subtlety","Ability_Rogue_Garrote","INV_Weapon_ShortBlade_14","Ability_Ambush"
# "5","Priest","Discipline","Holy","Shadow","Spell_Holy_AuraOfLight","Spell_Holy_LayOnHands","Spell_Shadow_Possession"
# "6","Death Knight","Blood","Frost","Unholy","Spell_Deathknight_BloodPresence","Spell_Deathknight_FrostPresence","Spell_Deathknight_UnholyPresence"
# "7","Shaman","Elemental","Enhancement","Restoration","Spell_Fire_Volcano","Spell_Nature_UnyeildingStamina","Spell_Nature_HealingWaveGreater"
# "8","Mage","Arcane","Fire","Frost","Spell_Nature_WispSplode","Spell_Fire_Fire","Spell_Frost_FreezingBreath"
# "9","Warlock","Affliction","Demonology","Destruction","Spell_Shadow_UnsummonBuilding","Spell_Shadow_CurseOfTounges","Spell_Fire_Incinerate"
# "11","Druid","Balance","Feral Combat","Restoration","Spell_Nature_Lightning","Ability_Physical_Taunt","Spell_Nature_HealingTouch"
#
#
# stat types
# "id","statname"
# "1","Health"
# "2","Mana"
# "3","Agility"
# "4","Strength"
# "5","Intellect"
# "6","Spirit"
# "7","Stamina"
# "12","Defense Rating"
# "13","Dodge Rating"
# "14","Parry Rating"
# "15","Shield Block Rating"
# "16","Melee Hit Rating"
# "17","Ranged Hit Rating"
# "18","Spell Hit Rating"
# "19","Melee Critical Strike Rating"
# "20","Ranged Critical Strike Rating"
# "21","Spell Critical Strike Rating"
# "22","Melee Hit Avoidance Rating"
# "23","Ranged Hit Avoidance Rating"
# "24","Spell Hit Avoidance Rating"
# "25","Melee Critical Avoidance Rating"
# "26","Ranged Critical Avoidance Rating"
# "27","Spell Critical Avoidance Rating"
# "28","Melee Haste Rating"
# "29","Ranged Haste Rating"
# "30","Spell Haste Rating"
# "31","Hit Rating"
# "32","Critical Strike Rating"
# "33","Hit Avoidance Rating"
# "34","Critical Avoidance Rating"
# "35","Resilience Rating"
# "36","Haste Rating"
# "37","Expertise Rating"
# "38","Attack Power"
# "39","Ranged Power"
# "40","Feral Attack Power"
# "41","Damage Done"
# "42","Healing Done"
# "43","Mana Per 5 Seconds"
# "44","Armor Penetration Rating"
# "45","Spell Power"
# "46","Health every 5 seconds"
# "47","Spell Penetration"
# "48","Block Value"
# "49","Mastery"
# "50","EXTRA_ARMOR"
# "51","FIRE_RESISTANCE"
#		52: "FROST_RESISTANCE",
#		54: "SHADOW_RESISTANCE",
#		55: "NATURE_RESISTANCE",
#		56: "ARCANE_RESISTANCE",
