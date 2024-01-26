$numberOfTests = 50;
$nameOfBot = "Ryleybot.py"
$processRunning = 1;


if (Test-Path "./HighScores.txt") {
    rm "HighScores.txt"
}

for (($i = 0); $i -lt $numberOfTests; $i++)
{
    Start-Process python $nameOfBot
}

try {
while ($processRunning -ne $null){
        $processRunning = Get-Process -Name "python" -ErrorAction Stop
    }
}

catch {
    echo -n "Finished tests. The average was:"
    python AverageScores.py
}
