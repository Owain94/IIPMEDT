import math
import time

from lib.Adafruit_LED_Backpack.Matrix8x8 import Matrix8x8

display = Matrix8x8()

display.begin()
display.clear()

gezcijfeind = 6.7

frac, whole = math.modf(gezcijfeind)

cijf1 = int(whole)
cijf2 = int(frac*10)

print(cijf1)
print(cijf2)


#display.set_pixel(x,y,1/0)
#1/0 = Aan of uit

#Komma 
display.set_pixel(3,7,1)



#1e cijfer
if cijf1 == 0:
#0 = 
	display.set_pixel(2,2,1)
	display.set_pixel(2,3,1)
	display.set_pixel(2,4,1)
	display.set_pixel(2,5,1)
	display.set_pixel(2,6,1)
	display.set_pixel(0,2,1)
	display.set_pixel(0,3,1)
	display.set_pixel(0,4,1)
	display.set_pixel(0,5,1)
	display.set_pixel(0,6,1)
	display.set_pixel(1,2,1)
	display.set_pixel(1,6,1)

	display.write_display()
	#time.sleep(2)
	#display.clear()

elif cijf1 == 1:
#1 = 
	display.set_pixel(2,2,1)
	display.set_pixel(2,3,1)
	display.set_pixel(2,4,1)
	display.set_pixel(2,5,1)
	display.set_pixel(2,6,1)

	display.write_display()
	#time.sleep(2)
	#display.clear()
	
elif cijf1 == 2:
#2 =
	display.set_pixel(0,2,1)
	display.set_pixel(1,2,1)
	display.set_pixel(2,2,1)
	display.set_pixel(2,3,1)
	display.set_pixel(2,4,1)
	display.set_pixel(1,4,1)
	display.set_pixel(0,4,1)
	display.set_pixel(0,5,1)
	display.set_pixel(0,6,1)
	display.set_pixel(1,6,1)
	display.set_pixel(2,6,1) 

	display.write_display()
	#time.sleep(2)
	#display.clear()
	

elif cijf1 == 3:
#3 =
	display.set_pixel(2,2,1)
	display.set_pixel(2,3,1)
	display.set_pixel(2,4,1)
	display.set_pixel(2,5,1)
	display.set_pixel(2,6,1)
	display.set_pixel(0,2,1)
	display.set_pixel(1,2,1)
	display.set_pixel(1,4,1)
	display.set_pixel(0,4,1)
	display.set_pixel(1,6,1)
	display.set_pixel(0,6,1)

	display.write_display()
	#time.sleep(2)
	#display.clear()

elif cijf1 == 4:	
#4 = 
	display.set_pixel(0,2,1)
	display.set_pixel(0,3,1)
	display.set_pixel(0,4,1)
	display.set_pixel(1,4,1)
	display.set_pixel(2,4,1)
	display.set_pixel(2,2,1)
	display.set_pixel(2,3,1)
	display.set_pixel(2,4,1)
	display.set_pixel(2,5,1)
	display.set_pixel(2,6,1)

	display.write_display()
	#time.sleep(2)
	#display.clear()

elif cijf1 == 5:	
#5 =
	display.set_pixel(0,6,1)
	display.set_pixel(1,6,1)
	display.set_pixel(2,6,1)
	display.set_pixel(2,5,1)
	display.set_pixel(2,4,1)
	display.set_pixel(1,4,1)
	display.set_pixel(0,4,1)
	display.set_pixel(0,3,1)
	display.set_pixel(0,2,1)
	display.set_pixel(1,2,1)
	display.set_pixel(2,2,1)
	 
	display.write_display()
	#time.sleep(2) 
	#display.clear()

elif cijf1 == 6:	
#6 = 
	display.set_pixel(2,2,1)
	display.set_pixel(1,2,1)
	display.set_pixel(0,2,1)
	display.set_pixel(0,3,1)
	display.set_pixel(0,4,1)
	display.set_pixel(0,5,1)
	display.set_pixel(0,6,1)
	display.set_pixel(1,6,1)
	display.set_pixel(2,6,1)
	display.set_pixel(2,5,1)
	display.set_pixel(2,4,1)
	display.set_pixel(1,4,1)

	display.write_display()
	#time.sleep(2)
	#display.clear()

elif cijf1 == 7:	
#7 = 
	display.set_pixel(0,2,1)
	display.set_pixel(1,2,1)
	display.set_pixel(2,2,1)
	display.set_pixel(2,2,1)
	display.set_pixel(2,3,1)
	display.set_pixel(2,4,1)
	display.set_pixel(2,5,1)
	display.set_pixel(2,6,1)

	display.write_display()
	#time.sleep(2)
	#display.clear()

elif cijf1 == 8:
#8 =
#(RECHTS)
	display.set_pixel(2,2,1)
	display.set_pixel(2,3,1)
	display.set_pixel(2,4,1)
	display.set_pixel(2,5,1)
	display.set_pixel(2,6,1)
	#LINKS)
	display.set_pixel(0,2,1)
	display.set_pixel(0,3,1)
	display.set_pixel(0,4,1)
	display.set_pixel(0,5,1)
	display.set_pixel(0,6,1)
	#Mid()
	display.set_pixel(1,2,1)
	display.set_pixel(1,4,1)
	display.set_pixel(1,6,1)

	display.write_display()
	#time.sleep(2)
	#display.clear()

elif cijf1 == 9:
#9 =
	display.set_pixel(2,2,1)
	display.set_pixel(2,3,1)
	display.set_pixel(2,4,1)
	display.set_pixel(2,5,1)
	display.set_pixel(2,6,1)
	#LINKS)
	display.set_pixel(0,2,1)
	display.set_pixel(0,3,1)
	display.set_pixel(0,4,1)
	display.set_pixel(0,6,1)
	#Mid()
	display.set_pixel(1,2,1)
	display.set_pixel(1,4,1)
	display.set_pixel(1,6,1)

	display.write_display()
	#time.sleep(2)
	#display.clear()


if cijf2 == 0:
#2e cijfer
#0 = 
	#(RECHTS)
	display.set_pixel(7,2,1)
	display.set_pixel(7,3,1)
	display.set_pixel(7,4,1)
	display.set_pixel(7,5,1)
	display.set_pixel(7,6,1)
	#LINKS)
	display.set_pixel(5,2,1)
	display.set_pixel(5,3,1)
	display.set_pixel(5,4,1)
	display.set_pixel(5,5,1)
	display.set_pixel(5,6,1)
	display.set_pixel(1,2,1)
	display.set_pixel(1,6,1)

	display.write_display()
	#time.sleep(2)
	#display.clear()

elif cijf2 == 1:
#1 = 
	display.set_pixel(7,2,1)
	display.set_pixel(7,3,1)
	display.set_pixel(7,4,1)
	display.set_pixel(7,5,1)
	display.set_pixel(7,6,1)

	display.write_display()
	#time.sleep(2)
	#display.clear()

elif cijf2 == 2:
#2 = 
	display.set_pixel(5,2,1)
	display.set_pixel(6,2,1)
	display.set_pixel(7,2,1)
	display.set_pixel(7,3,1)
	display.set_pixel(7,4,1)
	display.set_pixel(6,4,1)
	display.set_pixel(5,4,1)
	display.set_pixel(5,5,1)
	display.set_pixel(5,6,1)
	display.set_pixel(6,6,1)
	display.set_pixel(7,6,1) 

	display.write_display()
	#time.sleep(2)
	#display.clear()

elif cijf2 == 3:	
#3 =
	display.set_pixel(7,2,1)
	display.set_pixel(7,3,1)
	display.set_pixel(7,4,1)
	display.set_pixel(7,5,1)
	display.set_pixel(7,6,1)
	display.set_pixel(5,2,1)
	display.set_pixel(6,2,1)
	display.set_pixel(6,4,1)
	display.set_pixel(5,4,1)
	display.set_pixel(6,6,1)
	display.set_pixel(5,6,1)
	 
	display.write_display()
	#time.sleep(2)
	#display.clear()
 
elif cijf2 == 4: 
#4 = 
	display.set_pixel(5,2,1)
	display.set_pixel(5,3,1)
	display.set_pixel(5,4,1)
	display.set_pixel(6,4,1)
	display.set_pixel(7,4,1)
	display.set_pixel(7,2,1)
	display.set_pixel(7,3,1)
	display.set_pixel(7,4,1)
	display.set_pixel(7,5,1)
	display.set_pixel(7,6,1)

	display.write_display()
	#time.sleep(2)
	#display.clear()

elif cijf2 == 5:	
#5 = 
	display.set_pixel(7,2,1)
	display.set_pixel(6,2,1)
	display.set_pixel(5,2,1)
	display.set_pixel(5,3,1)
	display.set_pixel(5,4,1)
	display.set_pixel(6,4,1)
	display.set_pixel(7,4,1)
	display.set_pixel(7,5,1)
	display.set_pixel(7,6,1)
	display.set_pixel(6,6,1)
	display.set_pixel(5,6,1)

	display.write_display()
	#time.sleep(2)
	#display.clear()

elif cijf2 == 6:	
#6 = 
	display.set_pixel(7,2,1)
	display.set_pixel(6,2,1)
	display.set_pixel(5,2,1)
	display.set_pixel(5,3,1)
	display.set_pixel(5,4,1)
	display.set_pixel(5,5,1)
	display.set_pixel(5,6,1)
	display.set_pixel(6,6,1)
	display.set_pixel(7,6,1)
	display.set_pixel(7,5,1)
	display.set_pixel(7,4,1)
	display.set_pixel(6,4,1)

	display.write_display()
	#time.sleep(2)
	#display.clear()

elif cijf2 == 7:	
#7 = 
	display.set_pixel(5,2,1)
	display.set_pixel(6,2,1)
	display.set_pixel(7,2,1)
	display.set_pixel(7,2,1)
	display.set_pixel(7,3,1)
	display.set_pixel(7,4,1)
	display.set_pixel(7,5,1)
	display.set_pixel(7,6,1)

	display.write_display()
	#time.sleep(2)
	

elif cijf2 == 8:	
#8 =
	#(RECHTS)
	display.set_pixel(7,2,1)
	display.set_pixel(7,3,1)
	display.set_pixel(7,4,1)
	display.set_pixel(7,5,1)
	display.set_pixel(7,6,1)
	#LINKS)
	display.set_pixel(5,2,1)
	display.set_pixel(5,3,1)
	display.set_pixel(5,4,1)
	display.set_pixel(5,5,1)
	display.set_pixel(5,6,1)
	#Mid()
	display.set_pixel(6,2,1)
	display.set_pixel(6,4,1)
	display.set_pixel(6,6,1)

	display.write_display()
	#time.sleep(2)

elif cijf2 == 9:	
#9 =

	display.set_pixel(7,2,1)
	display.set_pixel(7,3,1)
	display.set_pixel(7,4,1)
	display.set_pixel(7,5,1)
	display.set_pixel(7,6,1)
	#LINKS)
	display.set_pixel(5,2,1)
	display.set_pixel(5,3,1)
	display.set_pixel(5,4,1)
	display.set_pixel(5,6,1)
	#Mid()
	display.set_pixel(6,2,1)
	display.set_pixel(6,4,1)
	display.set_pixel(6,6,1)

	display.write_display()
	#time.sleep(2)
	
	
	
	
time.sleep(10)
for x in range(8):
	for y in range(8):
		# Clear the display buffer.
		display.clear()
		# Set pixel at position i, j to on.  To turn off a pixel set
		# the last parameter to 0.
		display.set_pixel(x, y, 0)
		# Write the display buffer to the hardware.  This must be called to
		# update the actual display LEDs.
		display.write_display()
		# Delay for half a second.
		#time.sleep(0.5)
