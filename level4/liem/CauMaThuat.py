#Import modules

import time
import mcpi.minecraft as Minecraft
import mcpi.block as block
from mcpi import minecraft

mc = minecraft.Minecraft.create()

def SafeFeet():
    pos = mc.player.getTilePos()
    below = mc.getBlock(pos.x, pos.y - 1, pos.z)
    if below = block.AIR.id or block.WATER.FLOWING.id or block.LAVA.FLOWING:
        safe = False
    else:
        safe = True

while True:
    time.sleep(0.5)

    SafeFeet()



