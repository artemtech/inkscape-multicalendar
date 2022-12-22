import datetime
from math import floor

class Gregorian:
    def __init__(self, year, month, day, adjust):
        self.year = year
        self.month = month
        self.day = day
        self.adjust = adjust

    def to_julian(self):
        adjust = datetime.datetime(self.year, self.month, self.day) - datetime.timedelta(self.adjust+1)
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
        gdate = datetime.date.fromordinal(self.jd - 1721425) - datetime.timedelta(1)
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

    def weekday(self):
        jd = self.to_julian()
        return int(jd % 7)

    def month_length(self):
        c = Hijri(self.year, self.month + 1 , 1, self.adjust).to_julian()
        b = Hijri(self.year, self.month , 1, self.adjust).to_julian()
        return int(c - b)

    def to_julian(self):
        jd = floor((11 * self.year + 3) / 30) + floor(354 * self.year) + floor(30 * self.month) - floor((self.month - 1) / 2) + (self.day+self.adjust+2) + 1948440 - 386
        return jd

    def to_gregorian(self):
        date = self.to_julian()
        return Julian(date, self.adjust).to_gregorian()

class Jawa:
    acuan = datetime.date(2022,1,1)
    pasaran = ["pahing", "pon", "wage", "kliwon", "legi"]
    acuan_pasaran = 0
    i_pasaran = acuan_pasaran
    def __init__ (self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_day_pasaran(self):
        if self.year >= 2022:
            days = (datetime.date(self.year, self.month, self.day) - self.acuan).days
            i_pasaran = days % len(self.pasaran)
        else:
            self.pasaran.reverse()
            days = (self.acuan - datetime.date(self.year, self.month, self.day)).days
            i_pasaran = days % len(self.pasaran) - 1

        return self.pasaran[i_pasaran]

    def __str__(self):
        return self.get_day_pasaran()