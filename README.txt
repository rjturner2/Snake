README

Test.ps1 is a powershell script that you can use to run your bot as many times as your machine can handle 
simultaneously. After it finishes it will automatically run the AverageScores python script and output it to the 
terminal.

HOWEVER, to use this script you do need to enable powershell scripts for your machine. you can do this by:

1. Open Powershell as Administrator (right click on it, you'll see the option)

2. type the command: "set-executionpolicy remotesigned" THIS WILL ALLOW YOU TO RUN UNSIGNED SCRIPTS IN POWERSHELL
Which is a security risk, so don't run anything you don't trust.

I have changed the Test.ps1 script to use command line arguments now, the full syntax of running that script
while in it's directory will be:

"./Test.ps1 <nameOfBot> <numberOfTest(INTEGER)>"

when I want to run my bot 10 times I will write:

"./Test.ps1 RyleyBot.py 10"

Also, sorry Brandon. Since you're different and on a mac, this script will not run for you. You can make a very 
similar thing using UNIX, but that's a little outside of my paygrade since I don't have a machine I can run that
on.

One more note, if for some reason your terminal says HighScores.txt not found, let me know and I'll take a look at
it. I know what's going on but I can't figure out a way to make sure it works on every machine flawlessly. I just 
have to add another pseudonym for python to the PS1 script for your specific instance of python.

If you have any other questions let me know!