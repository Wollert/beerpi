import os
import subprocess
import time

# Set $DISPLAY to allow running scripts over ssh
os.environ['DISPLAY'] = ':0.0'

# Control screensaver: DISPLAY=:0 xset
# Turn screen off: subprocess.call('xset dpms force off', shell=True)
# Turn screen on: subprocess.call('xset dpms force on', shell=True)

def screen_status():
    """Checks with xset and returns True if screen is on, False if screen is off"""
    cmd = ['xset', 'dpms', 'q']
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if 'Monitor is On' in res.stdout:
        return True
    elif 'Monitor is Off' in res.stdout:
        return False
    else:
        return None


def screen_on():
    """Forces dpms to turn on screen"""
    # cmd = ['xset', 'dpms', 'force', 'on']
    cmd = ['xscreensaver-command', '-deactivate']
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


def screen_off():
    """Forces dpms to turn off screen"""
    cmd = ['xset', 'dpms', 'force', 'off']
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    cmd = ['xscreensaver-command', '-activate']
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)



if __name__ == '__main__':

    screen_on()
    print(screen_status())
    time.sleep(5)
    screen_off()
    print(screen_status())