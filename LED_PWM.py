# LED_PWM.py

# use the circuit from "LED_PWM.png"

import RPi.GPIO as GPIO

###################################################################################################
def main():
    GPIO.setmode(GPIO.BCM)      # use GPIO pin numbering, not physical pin numbering

    led_gpio_pin = 18

    GPIO.setup(led_gpio_pin, GPIO.OUT)

    pwmObject = GPIO.PWM(led_gpio_pin, 500)         # frequency = 500 Hz

    pwmObject.start(50)             # initial duty cycle = 50%

    print "press Ctrl+C to exit"

    try:
        while True:
            strDutyCycle = raw_input("enter brightness (0 to 100): ")
            intDutyCycle = int(strDutyCycle)
            pwmObject.ChangeDutyCycle(intDutyCycle)
        # end while
    except KeyboardInterrupt:       # exit cleanly when Ctrl+C is pressed
        pwmObject.stop()
        GPIO.cleanup()
    # end try except

    return
# end main

###################################################################################################
if __name__ == "__main__":
    main()

