import models
from inky import InkyWHAT
from PIL import Image, ImageDraw, ImageFont
from tempRead import getSensors


display = InkyWHAT("black")
roboto = ImageFont.truetype("RobotoSlab-Regular.ttf", 22)
# draw_context.text((20, 20),
#                   "28-00000a81ec36: 18.5°C",
#                   display.BLACK,
#                   font=roboto)
# display.set_image(img)
# display.show()


def drawScreen(loftemps):
    img = Image.new("P", (display.width, display.height), display.WHITE)
    draw_context = ImageDraw.Draw(img)
    output = ""
    for sensor in loftemps:
        output += "{}: {}°C\n".format(sensor[0], sensor[1])
    draw_context.multiline_text((10, 10), output, display.BLACK, font=roboto)
    display.set_image(img)
    display.show()


def main():
    # while True:
    sensors = getSensors()
    temps = []
    for sensor in sensors:
        with models.db:
            query = (models.Reading.select()
                     .where(models.Reading.sensor == sensor)
                     .order_by(models.Reading.timestamp.desc()))
        if len(query) > 0:
            temps.append((sensor, query[0].temperature))
    print(temps)
    drawScreen(temps)


if __name__ == "__main__":
    main()
