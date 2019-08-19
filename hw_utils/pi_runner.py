from flask import Flask, request, send_file, send_from_directory
pi_runner = Flask(__name__)

import os
from datetime import datetime as dt
import sys
import atexit

import hw_driver as hd 
import RPi.GPIO as GPIO


def _clip(v, v1, v2):
    if v < v1:
        v = v1
    if v > v2:
        v = v2
    return v

def _print(s):
    sys.stdout.write( s + "\n" )
    sys.stdout.flush()


Galvo = hd.GSUB
Laser = hd.LSUB



print("Remote is enabled? "+str(hd.Utilities.remoteEnabled()))
print("Laser is armed? "+str(not Laser.disarmed))

@pi_runner.route('/setup')
    Galvo.setup()
    Laser.setup()
    Laser.enable(True)
    Laser.setpower(0)

@pi_runner.route('/target/<xy>')
def target(xy):
    x, y = xy.split(',')
    x, y = float(x), float(y)
    x, y = _clip(x, -1, 1), _clip(y, -1, 1)
    Galvo.target(x, y)

@pi_runner.route('/set_power/<p>')
def set_power(p):
    p = _clip(float(p), 0, 100) / 100 * 0.65
    Laser.setPower(p)
    return Laser.pwr

@pi_runner.route('/beat')
def beat():
    Laser.beat()
    return str(round(dt.now().timestamp()*1000))

@pi_runner.route('/is_alive')
def is_alive():
    return str(Laser.isAlive())


@pi_runner.route('/remote_is_enabled')
def remote_is_enabled():
    return str(hd.Utilities.remoteEnabled())

@pi_runner.route('/enable/<enabled>')
def enable(enabled):
    if ( enabled in ['true', 'True', 't', 'T', '1', 'TRUE', ''] ):
        Laser.enable(True)
    else:
        Laser.enable(False)

if __name__ == '__main__':
    pi_runner.debug = True
    pi_runner.run()

def cleanup():
    Galvo.cleanup()
    Laser.cleanup()

atexit.register(cleanup, 'first')