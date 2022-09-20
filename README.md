# Servo with Metro
Using PWMio I connected an object to the 3 pin. What that means, I have no clue, but thats how it works. From there, it's fairly simple to just use the adafruit motor library. Using .Servo() I moved it back and forth. If I could do this assignment again, I probably would have just googled it a lot earlier and then I wouldn't have spent so much time trying to figure out the code.
# Rainbow Neopixel with Ultrasonic Sensor
Using a few different libraries I connected to the ultrasonic sensor, and managed to get a running distance. However, that was only the easiest part. Finding the right bounds and ways to shade from red to blue and blue to green took quite a while, as there are a lot of way which have varying levels of workingness. However, the way that I finally went with seemed to have work the best. By defining ranges, I made the light shade correctly.
## Use
### Every new project:
1. Make a GitHub account if you don't have one with your normal school credentials and sign into it.
2. Click the big green Use This Template button at the top of this page.
3. Name the new repository something appropriate to the purpose of your project (Your first one should probably be named `CircuitPython`).
4. Hit "Create repository from template." (The default settings should be fine.)
5. Open VS Code on your machine. Click Clone Repository.
6. Paste in the link to the new repository you've just created from the template and hit enter.
7. For the location, select the "STUDENT" drive if you have it or the document folder if you don't.
8. Hit "Open Cloned Directory."
9. Install the reccomended extensions when you get that popup in the lower right corner.
### To commit from VS Code:
1. Go to the little branch icon in the left bar of VS Code.
2. Click the + icon next  to the files you want to commit.
3. Write a message that descibes your changes in the "Message" box and hit commit.
4. If you get an error about user.name and user.email, see the next section.
5. Click the "Sync changes" button.
### If you get an error about user.name and user.email
1. In VS Code, hit `` Ctrl+Shift+` ``
2. Filling in your actual information, run the following commands one line at a time. The paste shortcut is `Ctrl+V` or you can right click then hit paste. Spelling must match exactly:
```
git config --global user.name YOURUSERNAME
git config --global user.email YOURSCHOOLEMAIL
```
3. Return to step 3 of the previous section.
