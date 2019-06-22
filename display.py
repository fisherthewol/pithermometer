import models
from inky import InkyWHAT
from PIL import Image, ImageDraw, ImageFont
from tempRead import getSensors
import time
import datetime


display = InkyWHAT("black")
roboto = ImageFont.truetype("RobotoSlab-Regular.ttf", 22)


def drawScreen(loftemps):
    img = Image.new("P", (display.width, display.height), display.WHITE)
    draw_context = ImageDraw.Draw(img)
    output = ""
    for sensor in loftemps:
        output += "{}: {}°C\n".format(sensor[0], sensor[1])
    output += "Last updated at\n{}".format(str(datetime.datetime.now()))
    draw_context.multiline_text((10, 10), output, display.BLACK, font=roboto)
    display.set_image(img)
    display.show()


def main():
    while True:
        sensors = getSensors()
        temps = []
        for sensor in sensors:
            with models.db:
                query = models.Reading.get_or_none(models.Reading.sensor == sensor).order_by(models.Reading.timestamp.desc())
            if query:
                temps.append((sensor, query.temperature))
        drawScreen(temps)
        time.sleep(30)


if __name__ == "__main__":
    main()
