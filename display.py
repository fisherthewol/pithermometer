from inky import InkyWHAT
from PIL import Image, ImageDraw, ImageFont

display = InkyWHAT("black")
img = Image.new("P", (display.width, display.height), display.WHITE)
draw_context = ImageDraw.Draw(img)
font = ImageFont.truetype("RobotoSlab-Regular.ttf", 22)
draw_context.text((20, 20), "28-00000a81ec36: 18.5°C", display.BLACK, font)
display.set_image(img)
display.show()
