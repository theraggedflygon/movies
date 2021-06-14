import os
from PIL import Image

collage = Image.new("RGBA", (2000, 3150))
x = 0
y = 0
for i in range(22):
    for j in range(1, 21):
        for poster in os.listdir("posters"):
            if poster.startswith("{}_".format(i * 20 + j)):
                img = Image.open("posters/" + poster)
                img = img.resize((100, 150))
                collage.paste(img, (x, y))
                x += 100
                break
    x = 0
    y += 150

collage.save("collage/collage2020.png")
