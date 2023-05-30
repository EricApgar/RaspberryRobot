# RaspberryRobot
Basic remotely controlled raspberry pi robot.

# Requirements:

## Hardware:

* Raspberry Pi.
    * Confirmed working on Rasperry Pi Zero W.
* RPi Adafruit DC & Stepper Motor Bonnet.
    * DC motors connected to the Motor Bonnet.
* RPi Camera Module v. 1.3 (ArduCam).



## Software:

Confirmed working with Python >=3.9.2.

## Create Virtual Environment:

Do these commands in the cloned repo folder.

```
>> python -m venv ./.venv
>> source ./.venv/bin/activate
(.venv) >> pip install -r requirements.txt
```

# Usage:

```
>> python main.py
```

A window should pop up showing the video feed. Clicking on the window and using the main arrow keys will allow control of the robot.
