README

Test.ps1 is a powershell script that you can use to run your bot as many times as your machine can handle 
simultaneously. After it finishes it will automatically run the AverageScores python script and output it to the 
terminal.

HOWEVER, to use this script you do need to enable powershell scripts for your machine. you can do this by:

1. Open Powershell as Administrator (right click on it, you'll see the option)

2. type the command: "set-executionpolicy remotesigned" THIS WILL ALLOW YOU TO RUN UNSIGNED SCRIPTS IN POWERSHELL
Which is a security risk, so don't run anything you don't trust.

In the Test.ps1 script, there's a couple variables you'll want to change, they're right at the top.

First, you'll definitely want to change the $nameOfBot variable to the actaual name of your bot, that way 
powershell knows what script it's looking to run.

You may also want to adjust the $numberOfTests variable, it of course allows you to run more or less tests 
depending on what your specific computer can handle.

Also, sorry Brandon. Since you're different and on a mac, this script will not run for you. You can make a very 
similar thing using UNIX, but that's a little outside of my paygrade since I don't have a machine I can run that
on.

If you have any other questions let me know!