
from TestCaseRigging import SBAGUITestCase

import World.WorldMap as WorldMap
from World.WorldEntities import *
from World.WorldCommands import *
from World.AIShips import *
from Game.BaubleHunt import Bauble, Outpost

import time

class TheHungerBaublesBaubleTestCases(SBAGUITestCase):
    """
    Test cases for The Hunger Baubles game baubles.
    """
    def get_config_filename(self):
        return "test_thehungerbaubles.cfg"
   
    def test_baubles_spawn_in_cornucopia(self):
        pass

    def test_pickup_baubles(self):
        pass

    def test_baubles_dropped_on_destroyed(self):
        pass

if __name__ == "__main__":
    unittest.main()