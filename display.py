import datetime
import time
from peewee import fn
import models
from inky import InkyWHAT
from PIL import Image, ImageDraw, ImageFont
from tempRead import getSensors


display = InkyWHAT("black")
roboto = ImageFont.truetype("RobotoSlab-Regular.ttf", 22)


def highlow(sensor):
    today = datetime.datetime.combine(datetime.date.today(), datetime.time())
    with models.db:
        query = models.Reading.select().where((models.Reading.timestamp >= today) & (models.Reading.sensor == sensor))
        maxtemp = query.select(fn.MAX(models.Reading.temperature))
        mintemp = query.select(fn.MIN(models.Reading.temperature))
    return (maxtemp, mintemp)


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
                query = (models.Reading.select()
                         .where(models.Reading.sensor == sensor)
                         .order_by(models.Reading.timestamp.desc()).get())
            if query:
                temps.append((sensor, query.temperature))
        drawScreen(temps)
        time.sleep(30)


if __name__ == "__main__":
    main()
