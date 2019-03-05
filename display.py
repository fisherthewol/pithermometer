import models
# from inky import InkyWHAT
# from PIL import Image, ImageDraw, ImageFont
from tempRead import getSensors


# display = InkyWHAT("black")
# img = Image.new("P", (display.width, display.height), display.WHITE)
# draw_context = ImageDraw.Draw(img)
# roboto = ImageFont.truetype("RobotoSlab-Regular.ttf", 22)
# draw_context.text((20, 20),
#                   "28-00000a81ec36: 18.5°C",
#                   display.BLACK,
#                   font=roboto)
# display.set_image(img)
# display.show()


def main():
    # while True:
    sensors = getSensors()
    for sensor in sensors:
        with models.db:
            query = (models.Reading.select()
                     .where(models.Reading.sensor == sensor)
                     .order_by(models.Reading.timestamp.desc()))
        print("Sensor {}: {}°C".format(sensor, query[0].temperature))
    return


if __name__ == "__main__":
    main()
