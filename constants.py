ATTACK_TYPES = {
    "all": "([B]Basic Attack, [A]Ability Attack, [U]Ult)".title().strip(),
    "ability": "([B]Basic Attack, [A]Ability Attack)".title().strip(),
    "basic": "([B]Basic Attack)".title().strip(),
}

TYPE_SPEED = .06

# PLAYER CHARACTERS
SETT = {
    "HP": 100,
    "DMG": 20,
    "MP": 70
}

VIEGO = {
    "HP": 90,
    "DMG": 25,
    "MP": 80
}

SYLAS = {
    "HP": 70,
    "DMG": 30,
    "MP": 90
}

SAMIRA = {
    "HP": 85,
    "DMG": 25,
    "MP": 85
}

THRESH = {
    "HP": 120,
    "DMG": 15,
    "MP": 75
}

# ENEMY CHARACTERS
ENEMY_CHARACTERS = {
    "Teemo": {
        "Ability_MP": 35,
        "Ult_MP": 55
    },
    "Evelynn": {
        "Ability_MP": 45,
        "Ult_MP": 75
    },
    "Twitch": {
        "Ability_MP": 65,
        "Ult_MP": 95
    },
    "Illaoi": {
        "Ability_MP": 85,
        "Ult_MP": 125
    },
    "Yasuo": {
        "Ability_MP": 110,
        "Ult_MP": 170
    }
}

# STATS REGENERATION
HP_REGEN = 0.1
MP_REGEN = 0.31

# ATTACKS SCALING
BASIC_ATTACK = 1.1
ABILITY = 1.4
ULT = 1.9

# STATS SCALING ON LEVEL
HP_LEVELUP_PLAYER = 1.43
DMG_LEVELUP_PLAYER = 1.34
MP_LEVELUP_PLAYER = 1.32

HP_LEVELUP_ENEMY = 1.51
DMG_LEVELUP_ENEMY = 1.44
MP_LEVELUP_ENEMY = 1.35

# ENEMY STATS GENERATION
HP_GEN = (70, 110)
DMG_GEN = (15, 25)
MP_GEN = (55, 90)
