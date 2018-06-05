from hw_utils import rpimcp4822 as mcp
import RPi.GPIO as GPIO

# Pin Definitions (BCM)
PIN_MODE = GPIO.BCM
GPIO.setmode(PIN_MODE)
LEN = 26
DISARMED = 19
HBM = 13
HBT = 6
ENREM = 5


'''
##############################################################
'''
class Utilities():
    def remoteEnabled():
        GPIO.setup(ENREM, GPIO.IN)
        enrem = GPIO.input(ENREM)
        GPIO.cleanup(ENREM)
        return enrem

'''
##############################################################
Laser Subcircuit (LSUB) Driver Class

Methods:
    setup
    enable
    setPower
    beat
    isAlive
    cleanup
'''
class LSUB():
    isSetup = False
    len = False
    disarmed = True
    pwr = 0
    hbtState = False
    Laser = "LSUB.setup() must be called before laser exists."

    @classmethod
    def setup(cls):
        if not LSUB.isSetup:
            LSUB.Laser = mcp.RPiMCP4822(device_num=1)
            for pin in [LEN, HBT]:
                GPIO.setup(pin, GPIO.OUT)
            for pin in [DISARMED, HBM]:
                GPIO.setup(pin, GPIO.IN)
            LSUB.isSetup = True

    @classmethod
    def enable(cls, enabled=True):
        if(enabled):
            len = True
            GPIO.output(LEN, GPIO.HIGH)
        else:
            len = False
            GPIO.output(LEN, GPIO.LOW)
    
    @classmethod
    def setPower(cls, val):
        pwr = val
        LSUB.Laser.write(val * 4096 - 1, 1) # LSUB uses ADC channel B
        
    @classmethod
    def beat(cls):
        LSUB.hbtState = not LSUB.hbtState
        GPIO.output(HBT, int(LSUB.hbtState))
        
    @classmethod
    def isAlive(cls):
        return GPIO.input(HBM)
        
    @classmethod
    def cleanup(cls):
        for pin in [LEN, DISARMED, HBM, HBT]:
            GPIO.cleanup(pin)
        LSUB.Laser.shutdown()
        LSUB.Laser.cleanup()
        LSUB.isSetup = False
   
   
'''
##############################################################
Galvo Subcircuit (GSUB) Driver Class

Methods:
    setup
    target
    position
    cleanup
'''
class GSUB():
    isSetup = False
    posx = 0
    posy = 0
    galvo = "GSUB.setup() must be called before galvo exists."
    
    @classmethod
    def setup(cls):
        if not LSUB.isSetup:
            GSUB.galvo = mcp.RPiMCP4822(device_num=0)
            GSUB.galvo.setup_output_latch()
            LSUB.isSetup = True
    
    # Takes input from [-1, 1]
    @classmethod
    def target(cls, x_coord = posx, y_coord = posy):
        GSUB.galvo.write(int((x_coord +1) * 2047), 0) # x is ADC channel A
        GSUB.galvo.write(int((y_coord + 1) * 2047), 1) # y is ADC channel B
        GSUB.galvo.update_output()
        
    @classmethod
    def position(cls):
        return (posx, posy)
        
    @classmethod
    def cleanup(cls):
        GSUB.galvo.shutdown()
        GSUB.galvo.cleanup()
        LSUB.isSetup = False
