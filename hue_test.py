from huesdk import Hue
import time

YOUR_BRIDGE_IP = '192.168.68.100'
YOUR_USERNAME = 'zyHk3r8jEvvpLw9CYjScpYbqgY0U7mrUog7zaG2K'

# username = Hue.connect(bridge_ip=YOUR_BRIDGE_IP)
# print(username)

hue = Hue(bridge_ip=YOUR_BRIDGE_IP, username=YOUR_USERNAME)

lights = hue.get_lights()
print(type(lights))

for light in lights:
    print("{}  {}  {}".format(light.id_, light.name, light.is_on))

l = hue.get_light(id_=12)

hold_bri = l.bri
# hold_bri = 180

l.off()
time.sleep(3)
# l.set_brightness(hold_bri)
l.on()
l.set_brightness(hold_bri)


# for i in range(25):
#     l.set_brightness(i*10)
#     time.sleep(1)