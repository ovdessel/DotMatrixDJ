#Import modules
import gc
import FontDictionary
gc.collect()
import max7219
gc.collect()
import time
gc.collect()
from machine import Pin, SPI
gc.collect()
import random
gc.collect()

gc.enable()

#setup spi bus connection
spi = SPI(1, baudrate=10000000, polarity=0, phase=0)
Pin(15,Pin.OUT)

led = Pin(2, Pin.OUT)

display = max7219.Matrix8x8(spi, cs=Pin(15), num=8)
display.brightness(5)
display.fill(0)
display.show()

#import jokes
try:
    while(1):
        gc.collect()
        with open("DadJokes.txt") as file:
            for i in range(random.getrandbits(9)):
                file.readline()
            line = file.readline()
            
        gc.collect()
        bitmap = FontDictionary.string_to_bitmap(line)
        gc.collect()
        for i in range(0,len(bitmap),1):
            #shift things up
            frame = bitmap[i:i+32]
            
            #recalculate display
            gc.collect()
            display_map = FontDictionary.bitmap_to_display(frame)
            for row in range(len(display_map)):
                for col in range(len(display_map[row])):
                    display.pixel(col,row,display_map[row][col])
                    
            display.show()
            gc.collect()
            if i==0:
                time.sleep(2)
            
            led.on()
            time.sleep(0.2)
            led.off()  
            time.sleep(0.2)
except KeyboardInterrupt:
    raise
except Exception:
    machine.reset()
print("completed!")