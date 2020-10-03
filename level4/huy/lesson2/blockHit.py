import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

GAP =block.AIR.id
WALL =block.GOLD_BLOCK.id
FLOOR =block.GRASS.id

FILENAME = "Data.txt"

f = open(FILENAME,"r")

pos = mc.player.getTilePos()
ORIGIN_X= pos.x+1
ORIGIN_Y= pos.y
ORIGIN_Z= pos.z+1

z = ORIGIN_Z

for line in f.readlines():
    data = line.split(" ")

    x = ORIGIN_X

    for cell in data:
        if cell == "0":
            b = GAP
        else:
            b = WALL

        mc.setBlock(x, ORIGIN_Y, z, b)
        mc.setBlock(x, ORIGIN_Y + 1, z, b)
        mc.setBlock(x, ORIGIN_Y - 1, z, FLOOR)

        x = x + 1
    z = z + 1