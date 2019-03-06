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
    for idx, sensor in enumerate(loftemps):
        posy = 10  # + idx * size of font
        draw_context.text((10, posy), "{}: {}°C".format(sensor[0], sensor[1]), display.BLACK, font=roboto)


def main():
    # while True:
    sensors = getSensors()
    temps = []
    for sensor in sensors:
        with models.db:
            query = (models.Reading.select()
                     .where(models.Reading.sensor == sensor)
                     .order_by(models.Reading.timestamp.desc()))
        temps.append((sensor, query[0].temperature))
    print(temps)
    # return


if __name__ == "__main__":
    main()
