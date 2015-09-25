# simple_servo.py

# use the circuit from "simple_servo.png"

import RPi.GPIO as GPIO

###################################################################################################
def main():
    GPIO.setmode(GPIO.BCM)      # use GPIO pin numbering, not physical pin numbering

    led_gpio_pin = 24

    GPIO.setup(led_gpio_pin, GPIO.OUT)

    pwmObject = GPIO.PWM(led_gpio_pin, 100)         # frequency = 100 Hz

    pwmObject.start(14)             # initial duty cycle = 14%

    while True:
        strAngle = raw_input("enter desired angle (0 to 180): ")
        intAngle = int(strAngle)
        dutyCycle = ((float(intAngle) * 0.01) + 0.5) * 10
        pwmObject.ChangeDutyCycle(dutyCycle)
    # end while

    return

###################################################################################################
if __name__ == "__main__":
    main()

