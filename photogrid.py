import json
import math
import os

import PIL
from PIL import Image


class Photogrid:
    def __init__(self, config_filename):
        with open(f"config/{config_filename}.json", 'r') as file:
            config = json.load(file)
        self.name = config['Name']
        self.movie_count = len(os.listdir(f"posters/{self.name}"))
        count_root = math.sqrt(self.movie_count)
        if count_root % 1 < 50:
            self.width_ctr = math.floor(count_root)
        else:
            self.width_ctr = math.ceil(count_root)
        self.row_ctr = math.ceil(self.movie_count / self.width_ctr)
        self.make_collage()

    def make_collage(self, save_collage=True):
        collage = Image.new("RGBA", (self.width_ctr * 100, self.row_ctr * 150))
        x = 0
        y = 0
        for i in range(self.row_ctr + 1):
            for j in range(1, self.width_ctr + 1):
                for poster in os.listdir(f"posters/{self.name}"):
                    if poster.startswith("{}_".format(i * self.width_ctr + j)):
                        try:
                            img = Image.open(f"posters/{self.name}/" + poster)
                            img = img.resize((100, 150))
                            collage.paste(img, (x, y))
                            x += 100
                            break
                        except PIL.UnidentifiedImageError:
                            x += 100
                            break
            x = 0
            y += 150

        if save_collage:
            collage.save(f"collage/{self.name}_collage.png")

