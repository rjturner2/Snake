rm "HighScores.txt"

for (($i = 0); $i -lt 50; $i++)
{
    Start-Process python Ryleybot.py
}