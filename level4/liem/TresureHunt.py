#Import modules
import mcpi.minecraft as Minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

def setTreasure(diamond_x, diamond_y, diamond_z):
    mc.setBlocks(diamond_x+2, diamond_y+4, diamond_z+2,diamond_x-2, diamond_y, diamond_z-2 block.AIR)
    mc.setBlock(diamond_x, diamond_y, diamond_z, block.DIAMOND_BLOCK)

def checkIfHit(diamond_x, diamond_y, diamond_z):
    events = mc.events.pollBlockHits()
    for event in events:
        print(events)
        #Get coordinates of wish the diamong was hit
        pos = event.pos
    #If player hit diamond
    if pos.x == [diamond_x - 2, diamond_x - 1, diamond_x, diamond_x + 1, diamond_x + 2] and  pos.y == [diamond_y - 2, diamond_y - 1, diamond_y, diamond_y + 1, diamond_y + 2] and  pos.x == [diamond_z - 2, diamond_z - 1, diamond_z, diamond_z + 1, diamond_z + 2]:
        mc.postToChat('HIT')

setTreasure(50,50,50)
while True:
    #A short delay
    time.sleep(1)
    #Check if diamond hit
    checkHit()



#END
