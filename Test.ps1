rm "HighScores.txt"

for (($i = 0); $i -lt 50; $i++)
{
    Start-Process python Ryleybot.py
}

$val = 1;
try {
while ($val -ne $null){
        $val = Get-Process -Name "python" -ErrorAction Stop
    }
}
catch {
    echo "Finished tests. The average was:"
    python AverageScores.py
}
