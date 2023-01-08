import time
import lgpio as gpio

led = 23

# open the gpio chip and set the LED pin as output
h = gpio.gpiochip_open(0)
gpio.gpio_claim_output(h, led)

try:
    while True:
        # Turn the GPIO pin on
        gpio.gpio_write(h, led, 1)
        time.sleep(1)

        # Turn the GPIO pin off
        gpio.gpio_write(h, led, 0)
        time.sleep(1)
except KeyboardInterrupt:
    gpio.gpio_write(h, led, 0)
    gpio.gpiochip_close(h)
