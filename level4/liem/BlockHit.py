#Import modules
import mcpi.minecraft as Minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

def setTreasure(diamond_x, diamond_y, diamond_z):
    setBlocks(diamond_x+2, diamond_y+4, diamond_z+2,diamond_x-2, block.AIR)
    setBlock(diamond_x, diamond_y, diamond_z, block.DIAMOND_BLOCK)
