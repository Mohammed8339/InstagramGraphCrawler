@echo off


echo [1] instagramGraphCrawler
echo [2] graph suggester

set /p choice=""
goto %choice%


:1
echo name of what graph you are trying to look for?
set /p query=">:"


echo enter country code of the country your trying to find the data in, ex: USA is US, Canada is CA
set /p country=">:"

python dataExtraction.py --query "%query%" --location %country%

pause
exit


:2
python suggestions.py