class MovingDot:
    def __init__(self, int1=50, int2=50, int3=50):
        self._color = (int1, int2, int3)
        print(self._color)

    def get_color(self):
        return self._color[0], self._color[1], self._color[2]