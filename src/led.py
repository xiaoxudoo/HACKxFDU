import RPi.GPIO as GPIO

class TrafficLight:
    def __init__(self, r_pins, y_pins, g_pins):
        GPIO.setmode(GPIO.BCM)
        for pins in [r_pins, y_pins, g_pins]:
            for p in pins:
                GPIO.setup(p, GPIO.OUT)
        self.r_pwm, self.y_pwm, self.g_pwm = [], [], []
        self.initPWM(r_pins, y_pins, g_pins)

    def initPWM(self, r_pins, y_pins, g_pins):
        for _pins, _pwm in zip([r_pins, y_pins, g_pins], [self.r_pwm, self.y_pwm, self.g_pwm]):
            for p in _pins:
                pwm = GPIO.PWM(p, 70)
                pwm.start(0)
                _pwm.append(pwm)

    def red_up(self):
        self.r_pwm[0].ChangeDutyCycle(100)
        self.r_pwm[1].ChangeDutyCycle(0)
        self.r_pwm[2].ChangeDutyCycle(0)

        self.y_pwm[0].ChangeDutyCycle(0)
        self.y_pwm[1].ChangeDutyCycle(0)
        self.y_pwm[2].ChangeDutyCycle(0)

        self.g_pwm[0].ChangeDutyCycle(0)
        self.g_pwm[1].ChangeDutyCycle(0)
        self.g_pwm[2].ChangeDutyCycle(0)

    def yellow_up(self):
        self.r_pwm[0].ChangeDutyCycle(0)
        self.r_pwm[1].ChangeDutyCycle(0)
        self.r_pwm[2].ChangeDutyCycle(0)

        self.y_pwm[0].ChangeDutyCycle(60)
        self.y_pwm[1].ChangeDutyCycle(60)
        self.y_pwm[2].ChangeDutyCycle(0)

        self.g_pwm[0].ChangeDutyCycle(0)
        self.g_pwm[1].ChangeDutyCycle(0)
        self.g_pwm[2].ChangeDutyCycle(0)

    def green_up(self):
        self.r_pwm[0].ChangeDutyCycle(0)
        self.r_pwm[1].ChangeDutyCycle(0)
        self.r_pwm[2].ChangeDutyCycle(0)

        self.y_pwm[0].ChangeDutyCycle(0)
        self.y_pwm[1].ChangeDutyCycle(0)
        self.y_pwm[2].ChangeDutyCycle(0)

        self.g_pwm[0].ChangeDutyCycle(0)
        self.g_pwm[1].ChangeDutyCycle(100)
        self.g_pwm[2].ChangeDutyCycle(0)

    def all_on(self):
        self.r_pwm[0].ChangeDutyCycle(100)
        self.r_pwm[1].ChangeDutyCycle(100)
        self.r_pwm[2].ChangeDutyCycle(100)

        self.y_pwm[0].ChangeDutyCycle(100)
        self.y_pwm[1].ChangeDutyCycle(100)
        self.y_pwm[2].ChangeDutyCycle(100)

        self.g_pwm[0].ChangeDutyCycle(100)
        self.g_pwm[1].ChangeDutyCycle(100)
        self.g_pwm[2].ChangeDutyCycle(100)

    def all_off(self):
        self.r_pwm[0].ChangeDutyCycle(0)
        self.r_pwm[1].ChangeDutyCycle(0)
        self.r_pwm[2].ChangeDutyCycle(0)

        self.y_pwm[0].ChangeDutyCycle(0)
        self.y_pwm[1].ChangeDutyCycle(0)
        self.y_pwm[2].ChangeDutyCycle(0)

        self.g_pwm[0].ChangeDutyCycle(0)
        self.g_pwm[1].ChangeDutyCycle(0)
        self.g_pwm[2].ChangeDutyCycle(0)

    def clean_up(self):
        for _pwm in [self.r_pwm, self.y_pwm, self.g_pwm]:
            for p in _pwm:
                p.stop()
        GPIO.cleanup()