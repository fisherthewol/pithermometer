import datetime
import time
import models
from inky import InkyWHAT
from PIL import Image, ImageDraw, ImageFont
from tempRead import getSensors


display = InkyWHAT("black")
roboto = ImageFont.truetype("RobotoSlab-Regular.ttf", 22)


def highlow(sensor):
    today = datetime.datetime.combine(datetime.date.today(), datetime.time())
    with models.db:
        maxtmp = (models.Reading.select(models.Reading.temperature)
                  .where((models.Reading.timestamp >= today) & (models.Reading.sensor == sensor))
                  .order_by(models.Reading.temperature.desc()).get())
        mintmp = (models.Reading.select(models.Reading.temperature)
                  .where((models.Reading.timestamp >= today) & (models.Reading.sensor == sensor))
                  .order_by(models.Reading.temperature.asc()).get())
    if maxtmp:
        return (maxtmp, mintmp)
    else:
        return None


def drawScreen(loftemps):
    img = Image.new("P", (display.width, display.height), display.WHITE)
    draw_context = ImageDraw.Draw(img)
    output = ""
    for sensor in loftemps:
        output += "{}: {}°C\n".format(sensor[0], sensor[1])
        output += "High: {} || Low: {}".format(sensor[2], sensor[3])
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
                highlo = highlow(sensor)
                if highlo:
                    temps.append((sensor,
                                  query.temperature,
                                  highlo[0],
                                  highlo[1]))
        drawScreen(temps)
        time.sleep(30)


if __name__ == "__main__":
    main()
