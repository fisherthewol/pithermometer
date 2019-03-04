from inky import InkyWHAT
from PIL import Image

i_d = InkyWHAT("black")
i_d.set_border(i_d.WHITE)
img = Image.open("img.png")
pal_img = Image.new("P", (1, 1))
pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0) + (0, 0, 0) * 252)
img = img.conver("RGB").quantize(palette=pal_img)
i_d.set_image(img)
i_d.show()
