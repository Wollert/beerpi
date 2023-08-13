# Module to get data from Plaato Keg
"""
Plaato keg AuthTokens:
Fat 1: 388b2e2690f64ffe9b9953e40bf51090
Fat 2: f37a69de5b1d496686157742e35dd771
Fat 3: 8f950b3a7b5d4df39b01cc777adb0f55

Plaato pins of interest:
v49: Pouring (0 or 255)
v51: Beer left
v56: Temperature
v59: Last pour
v64: Beer name
v66: FG
v67: Keg date
v68: abv
"""

import requests

class Keg:
    def __init__(self, keg_no):
        auth_tokens = ('388b2e2690f64ffe9b9953e40bf51090',
                       'f37a69de5b1d496686157742e35dd771',
                       '8f950b3a7b5d4df39b01cc777adb0f55')

        self.token = auth_tokens[keg_no-1]
        self.pouring = self.get(49)
        self.beer_left = self.get(51)
        self.temperature = self.get(56)
        self.last_pour = self.get(59)
        self.beer_name = self.get(64)
        self.fg = self.get(66)
        self.keg_date = self.get(67)
        self.abv = self.get(68)


    def get(self, pin_no):
        # http://plaato.blynk.cc/auth_token/get/pin
        r = requests.get('http://plaato.blynk.cc/{}/get/v{}'.format(self.token, pin_no))

        # print(r.status_code)
        # print(type(r.status_code))

        if r.status_code == 200:
            data = r.content
            # print(data)
            # print(type(data))
            data = data.decode()
            # print(data)
            # print(type(data))
            data = data[2:-2]
            # print(data)
            return data
        else:
            return None

    def get_pouring(self):
        self.pouring = self.get(49)
        return self.pouring

    def get_beer_left(self):
        self.beer_left = self.get(51)
        return self.beer_left

    def get_temperature(self):
        self.temperature = self.get(56)
        return self.temperature

    def get_last_pour(self):
        self.last_pour = self.get(59)
        return self.last_pour

    def get_beer_name(self):
        self.beer_name = self.get(64)
        return self.beer_name

    def get_fg(self):
        self.fg = self.get(66)
        return self.fg

    def get_keg_date(self):
        self.keg_date = self.get(67)
        return self.keg_date

    def get_abv(self):
        self.abv = self.get(68)
        return self.abv

    def get_all(self):
        self.get_pouring()
        self.get_beer_left()
        self.get_temperature()
        self.get_last_pour()
        self.get_beer_name()
        self.get_fg()
        self.get_keg_date()
        self.get_abv()


def get_temperature(kegs):
    temperature = 0.0
    if type(kegs) is list:
        for k in kegs:
            temperature += float(k.get_temperature())
        temperature = temperature/len(kegs)
    else:
        temperature = float(kegs.get_temperature())
    return "{:.3f}".format(temperature) 


if __name__ == '__main__':
    fat1 = Keg(1)
    fat2 = Keg(2)
    fat3 = Keg(3)

    print(fat1.abv)
    print(fat1.get_pouring())

    fat = [fat1,fat2,fat3]
    
    for f in fat:
        print(f.get_temperature())

    print(get_temperature(fat))