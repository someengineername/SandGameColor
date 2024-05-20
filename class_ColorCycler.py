class ColorCycler:
    def __init__(self):
        self._color = [255, 0, 0]
        self._speed = 5

    def get_color_cycle(self):

        if self._color[0] == 255 and 255 > self._color[1] >= 0 and self._color[2] == 0:
            self._color[1] += self._speed
            return self._color[0], self._color[1], self._color[2]

        elif 0 < self._color[0] <= 255 and self._color[1] == 255 and self._color[2] == 0:
            self._color[0] -= self._speed
            return self._color[0], self._color[1], self._color[2]

        elif self._color[0] == 0 and self._color[1] == 255 and 255 > self._color[2] >= 0:
            self._color[2] += self._speed
            return self._color[0], self._color[1], self._color[2]

        elif self._color[0] == 0 and 0 < self._color[1] <= 255 and self._color[2] == 255:
            self._color[1] -= self._speed
            return self._color[0], self._color[1], self._color[2]

        elif 0 <= self._color[0] < 255 and self._color[1] == 0 and self._color[2] == 255:
            self._color[0] += self._speed
            return self._color[0], self._color[1], self._color[2]

        elif self._color[0] == 255 and self._color[1] == 0 and 0 <= self._color[2] <= 255:
            self._color[2] -= self._speed
            return self._color[0], self._color[1], self._color[2]
