# my_blink.py

# use the circuit from "my_blink.png"

import RPi.GPIO as GPIO
import time

###################################################################################################
def main():
    GPIO.setmode(GPIO.BCM)      # use GPIO pin numbering, not physical pin numbering

    led_gpio_pin = 18

    GPIO.setup(led_gpio_pin, GPIO.OUT)

    while True:
        GPIO.output(led_gpio_pin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_gpio_pin, GPIO.LOW)
        time.sleep(0.5)
    # end while

    return
# end main

###################################################################################################
if __name__ == "__main__":
    main()