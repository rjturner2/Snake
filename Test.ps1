$numberOfTests = 10
$nameOfBot = "RyleyBot.py"
$processRunning = 1
$processRunning2 = 1


if (Test-Path "./HighScores.txt") {
    rm "HighScores.txt"
}

for (($i = 0); $i -lt $numberOfTests; $i++)
{
    Start-Process python $nameOfBot
}

try {
while (($processRunning -ne $null) -or ($processRunning2 -ne $null)) {
        $processRunning2 = Get-Process -Name "python" -ErrorAction silentlycontinue
        $processRunning = Get-Process -Name "python3.9" -ErrorAction silentlycontinue
    }
}

catch {
    echo "Small Error"
}

finally {

Sleep 0.5
echo -n "Finished tests. The average was:"
python AverageScores.py

}


