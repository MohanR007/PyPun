# pip install qrcode
#  pip install qrcode[pil]

import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=BsEqI1NZA-E")
img.save("qrcode.png")