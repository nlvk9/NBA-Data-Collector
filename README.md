# NBA-Data-Collector
The NBA Data Collector is a Python program which accesses data tables in Basketball Reference using Inspect Element.
Users can enter the team/teams they want and the season/seasons they want.
The program creates a table with detailed information about each game played by each inputted team in the regular season. 
For further viewing, users can name and download a CSV file which creates a spreadsheet with the table for easy access.
Users can also create a visual graph of the points scored by the selected teams in each year

## Installation
1. Go to tags and select your version.
2. Download the source code (the zip file)
3. Upload the code file INSIDE the folder to your editor/IDE.
4. If your program does not have the libraries pandas or matplotlib, you must install them.
5. To continue with step 4, download Python from python.org. Once installed, in the terminal, type pip install matplotlib (to install matplotlib) and pip install pandas (to install pandas).

### Usage
7. Once or if your program has the libraries installed, you can run the program on your IDE by pressing the run/execute button.
8. The program starts by displaying all 30 NBA teams with their abbreviations. You can use this website: 
   https://en.wikipedia.org/wiki/Wikipedia:WikiProject_National_Basketball_Association/National_Basketball_Association_team_abbreviations to translate abbreviation -> team.
9. You can then enter the abbreviations you want. Separate multiple by a comma (and don't add any spaces).
10. After that, enter the years you want to look through, separating them using commas and no spaces.
11. As of Version4, the program allows users to enter any years they want. However, keep in mind, it cleans out years before 1947 (counted as the first year for the NBA on Basketball Reference).
12. Once the team(s) and year(s) are input, the program will create URLs of the teams & years and use pandas to extract the game logs on the website.
13. It takes 4-6 seconds to extract information to prevent overloading the servers with too many requests.
15. Then, the table of information is printed (which contains every team & year you input). It then prompts you to enter anything except for 'n' (meaning no) to create a CSV file and then name it.
    .csv will be added by the program, so don't worry about adding it yourself.
16. The CSV file will be put in the directory where your Python script is running. If you want to find that, you can create a new page, import os (it is already included with Python), set a variable = os.getcwd(), and then print the variable.
17. If you want to change the location, you can change: mainDataFrame.to_csv(f'{csvName}.csv',index=False) to ---> mainDataFrame.to_csv(r'C:\path\to\your\directory\myfile.csv', index=False) where you put the directory path.
18. After entering either 'n' or something other than 'n', the program then asks you if you want to create a graph. Entering 'y' will create that graph. Anything else does not create a graph.
19. You can also choose to save each graph as a .png file (as of Version4).
20. At the same time, the program shows the average of each stat per graph.
