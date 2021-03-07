from PIL import ImageDraw as ImDr
from PIL import Image as Im


class Base:
    def __init(self):
        pass

    ry = 580
    h = ry
    n = 11
    r = ((h-8) / (n * 2)) / (3 ** 0.5 / 2)
    print(r)
    y = int(r)
    rx = int(((n - 1) * 1.5 +2 ) * r)
    x = rx // 2

    im = Im.new('RGB', (int(rx), int(ry)), 'white')
    draw = ImDr.Draw(im)


class Coord(Base):
    def __init__(self, x, y):
        self.r = Base.r
        self.x = x
        self.y = y

    def xy(self):
        r = self.r
        x = self.x
        y = self.y
        return (
            (int(x - r // 2), int(y + 3 ** 0.5 / 2 * r)),
            (int(x - r), int(y)),
            (int(x - r // 2), int(y - 3 ** 0.5 / 2 * r)),
            (int(x + r // 2), int(y - 3 ** 0.5 / 2 * r)),
            (int(x + r), int(y)),
            (int(x + r // 2), int(y + 3 ** 0.5 / 2 * r)))


class Gex(Base):
    def __init__(self):
        self.im = Base.im
        self.draw = Base.draw

    def one_gex(self):
        cr1 = Coord(Base.x, Base.y)
        self.draw.polygon(xy=cr1.xy(), outline=(0, 0, 0))

    def im_save(self):
        self.im.save("ImChess.jpg", quality=1020)

    def shim(self):
        self.im.show()
        #self.im.save('1234.jpg', quality=95)

    def pole(self):
        n = Base.n
        r = Base.r
        for i in range(-(n // 2), (n // 2) + 1):
            for j in range(n - abs(i)):
                cr_ = Coord(Base.x + i * 1.5 * r, int(Base.y + j *3 ** 0.5 * r + abs(i) * 3 ** 0.5 / 2 * r))
                self.draw.polygon(xy=cr_.xy(), outline=(0, 0, 0), fill=(255 // ((j - abs(i)) % 3 + 1), 0, 255 // ((j - abs(i)) % 3 + 1)))
#fill=(255 // ((j - abs(i)) % 3 + 1), 0, 255 // ((j - abs(i)) % 3 + 1))

gex = Gex()
# gex.one_gex()
gex.pole()
#gex.shim()
gex.im_save()
