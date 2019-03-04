import os
import peewee
from inky import InkyWHAT
from PIL import Image, ImageDraw, ImageFont
from tempRead import getSensors


display = InkyWHAT("black")
db = peewee.PostgresqlDatabase(os.environ.get("database"),
                               user="display",
                               password="demo")
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
        with db:
            cursor = db.execute_sql("SELECT * FROM reading WHERE sensor = ? ORDER BY timestamp DESC", (sensor,))
            x = cursor.fetchone()
        print("Sensor " + x[3] + ": " + x[4] + "°C.")
        return


if __name__ == "__main__":
    main()
