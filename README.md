# Servo with Metro
Using PWMio I connected an object to the 3 pin. What that means, I have no clue, but thats how it works. From there, it's fairly simple to just use the adafruit motor library. Using .Servo() I moved it back and forth. If I could do this assignment again, I probably would have just googled it a lot earlier and then I wouldn't have spent so much time trying to figure out the code.
# Rainbow Neopixel with Ultrasonic Sensor
Using a few different libraries I connected to the ultrasonic sensor, and managed to get a running distance. However, that was only the easiest part. Finding the right bounds and ways to shade from red to blue and blue to green took quite a while, as there are a lot of way which have varying levels of workingness. However, the way that I finally went with seemed to have work the best. By defining ranges, I made the light shade correctly.

![gif](https://github.com/kshinoz98/CircuitPython/blob/master/ezgifgif.gif?raw=true) ![png](https://raw.githubusercontent.com/kshinoz98/CircuitPython/f4be6df7eb8828500e94754d2ccb5b5c8cd2b276/Screenshot%202022-09-19%20154243.png)

# Counting LCD
Using some libraries, I connected the LCD screen and the buttons (Which was much harder than I expected). For the first button I had to "debounce" the counting button, and then the second button was a single if statement to tell it to count up or down. I feel like I had a pretty good grasp of this asssignment, as I had done one that was just like it in engineering 2, however I did get stuck on something for 30 mins when I only had to add .value. If I had to do this assignment again, I would have actually read the directions so I wouldn't have to redo the code because it did the wrong thing.

