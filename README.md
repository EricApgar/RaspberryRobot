# RaspberryRobot
Basic remotely controlled raspberry pi robot.

# Basic Commands:

```
from adafruit_motorkit import MotorKit
kit = MotorKit()

kit.motor1.throttle = 1.0  # Range is -1:1. Negative is opposite direction.
kit.motor1.throttle = None  # Set motor to coast.
```