# NBA-Data-Collector
The NBA Data Collector is a Python program which accesses data tables in Basketball Reference using Inspect Element.
Users can enter the team/teams they want and the season/seasons they want.
The program creates a table with detailed information about each game played by each inputted team in the regular season. 
For further viewing, users can name and download a CSV file which creates a spreadsheet with the table for easy access.
Users can also create a visual graph of the points scored by the select teams in each year

## Installation
1. Go to tags and select your version.
2. Download the source code (the zip file)
3. Upload the code file INSIDE the folder to your editor/IDE.
4. If your program does not have the libraries pandas or matplotlib, you must install them.
5. To continue with step 4, download Python from python.org. Once installed, in the terminal, type pip install matplotlib (to install matplotlib) and pip install pandas (to install pandas).

### Usage
7. Once/if your program has the libraries installed, you can run the program on your IDE by pressing the run/execute button.
8. The program starts by displaying all 30 NBA teams with their abbreviations. You can use this website: 
   https://en.wikipedia.org/wiki/Wikipedia:WikiProject_National_Basketball_Association/National_Basketball_Association_team_abbreviations to translate abbreviation -> team.
9. You can then enter the abbreviations you want. Separate multiple by a comma (and don't add any spaces).
10. After that, enter the years you want to look through, separating them using commas and no spaces.
   As of Version1 and Version2, the program uses 2015-2025. Before 2015, some teams had different names and abbreviations not in the list of 30.
11. Once the team(s) and year(s) are input, the program will create URLs of the teams & years and use pandas to extract the game logs on the website.
12. It takes approximately 6 seconds to extract information (time.sleep(6)) to prevent overloading the servers with too many requests at a time.
13. Then, the table of information is printed (which contains every team & year you input). It then prompts you to enter anything except for 'n' (meaning no) to create a CSV file and then name it.
    .csv will be added by the program, so don't worry about adding it yourself.
14. The CSV file will be put in the directory where your Python script is running. If you want to find that, you can create a new page, import os (it is already included with Python), set a variable = os.getcwd(), and then print the variable.
15. If you want to change the location, you can change: mainDataFrame.to_csv(f'{csvName}.csv',index=False) to ---> mainDataFrame.to_csv(r'C:\path\to\your\directory\myfile.csv', index=False) where you put the directory path.
16. After entering either 'n' or something other than 'n', the program then asks you if you want to create a graph. Entering 'y' will create that graph. Anything else does not create a graph.
17. Depending on version:
    Version2 allows you to select different stats to graph (as a bar graph).
    Version1 does only points (as a line graph).
