import datetime
import inkex
from math import floor

class Gregorian:
    def __init__(self, year, month, day, adjust):
        self.year = year
        self.month = month
        self.day = day
        self.adjust = adjust
        
    def to_julian(self):
        adjust = datetime.datetime(self.year, self.month, self.day) - datetime.timedelta(self.adjust)
        jd = adjust.toordinal() + 1721425
        return jd

    def to_hijri(self):
        date = self.to_julian()
        return Julian(date).to_hijri()

class Julian:
    def __init__(self, jd, adjust=0):
        self.jd = jd
        self.adjust = adjust

    def to_hijri(self):
        iyear = 10631.0/30.0
        epochastro = 1948084
        shift1 = 8.01/60.0

        z = self.jd - epochastro
        cyc = floor(z / 10631.0)
        z -= 10631 * cyc
        j = floor((z - shift1) / iyear)
        iy = 30 * cyc + j
        z -= floor(j * iyear + shift1)
        im = floor((z + 28.5001) / 29.5)
        if(im==13):
            im = 12
        id = z - floor(29.5001 * im - 29)

        date = [iy, im, id]
        return date

    def to_gregorian(self):
        gdate = datetime.date.fromordinal(self.jd - 1721425) - datetime.timedelta(self.adjust)
        yg = gdate.year
        mg = gdate.month
        dg = gdate.day

        date = [yg, mg, dg]
        return date

class Hijri:
    def __init__(self, year, month, day, adjust):
        self.year = year
        self.month = month
        self.day = day
        self.adjust = adjust

    def to_julian(self):
        jd = floor((11 * self.year + 3) / 30) + floor(354 * self.year) + floor(30 * self.month) - floor((self.month - 1) / 2) + self.day + 1948440 - 386
        return jd

    def to_gregorian(self):
        date = self.to_julian()
        return Julian(date, self.adjust).to_gregorian()