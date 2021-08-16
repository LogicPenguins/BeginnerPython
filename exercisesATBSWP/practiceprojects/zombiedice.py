import zombiedice
import random


class RandomZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, game_state):
        dice_roll_results = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while dice_roll_results is not None:
            brains += dice_roll_results['brains']
            decider = random.randint(0, 1)
            if decider == 1:
                dice_roll_results = zombiedice.roll()
            else:
                break


class TwoBrainZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, game_state):
        dice_roll_results = zombiedice.roll()

        brains = 0
        while dice_roll_results is not None:
            brains += dice_roll_results['brains']
            if brains < 2:
                dice_roll_results = zombiedice.roll()
            else:
                break


class TwoShotgunZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, game_state):
        dice_roll_results = zombiedice.roll()

        brains = 0
        shotguns = 0
        while dice_roll_results is not None:
            brains += dice_roll_results['brains']
            shotguns += dice_roll_results['shotgun']
            if shotguns < 2:
                dice_roll_results = zombiedice.roll()
            else:
                break


class WeirdZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, game_state):
        dice_roll_results = zombiedice.roll()
        brains = 0
        shotguns = 0
        while dice_roll_results is not None:
            brains += dice_roll_results['brains']
            shotguns += dice_roll_results['shotgun']
            amount_rolls = random.randint(1, 4)
            if shotguns < 2:
                for i in range(amount_rolls):
                    dice_roll_results = zombiedice.roll()
            else:
                break


class SafeZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, game_state):
        dice_roll_results = zombiedice.roll()

        brains = 0
        shotguns = 0
        while dice_roll_results is not None:
            brains += dice_roll_results['brains']
            shotguns += dice_roll_results['shotgun']
            if shotguns <= brains:
                dice_roll_results = zombiedice.roll()
                print(dice_roll_results)
            else:
                break


zombies = (
    TwoBrainZombie(name='Two Brain'),
    RandomZombie(name='Random'),
    TwoShotgunZombie(name='Two Shotgun'),
    WeirdZombie(name="Weird"),
    SafeZombie(name="SafeZombie")
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
# zombiedice.runWebGui(zombies=zombies, numGames=1000)
