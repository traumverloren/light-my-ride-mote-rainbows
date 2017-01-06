#!/usr/bin/env python

import time
from colorsys import hsv_to_rgb

from mote import Mote

num_pixels = 16

print("""Rainbow

Press Ctrl+C to exit.
""")

mote = Mote()

num_pixels = 16

mote.configure_channel(1, num_pixels, False)
mote.configure_channel(2, num_pixels, False)
mote.configure_channel(3, num_pixels, False)
mote.configure_channel(4, num_pixels, False)

try:
    while True:
        brightness = 0
        for h in range(1000):
            for channel in range(4):
                for pixel in range(mote.get_pixel_count(channel + 1)):
                    hue = (h + (channel * num_pixels * 4) + (pixel * 4)) % 360
                    r, g, b = [int(c * brightness) for c in hsv_to_rgb(hue/360.0, 1.0, 0.02)]
                    mote.set_pixel(channel + 1, pixel, r, g, b)
            mote.show()
            time.sleep(0.01)
            if brightness < 255: brightness += 1


except KeyboardInterrupt:
    mote.clear()
    mote.show()
