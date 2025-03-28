'''
Scrapyard Ottawa 2025 Project
The purpose of this project is to collect data from Basketball Reference.
It uses pandas, time, random and matplotlib to extract information and visualize it.
Users enter the abbreviation(s) of desired team(s) and the desired year(s).
The program then obtains information about each time in each season.
It prints out a simplified version of the data in the terminal, and
gives the user the option to get the data in a csv file (a spreadsheet)
with all of the data. The program then asks the user if they want to see
the stats of each team in a graph (using matplotlib).
Neel Vinayak
2025-03-15 (Y-M-D)
'''

# importing the necessary libraries
import pandas as pd # to read the tables from basketball reference
import time, random # to stall collection
import matplotlib.pyplot as plt # to create visual graphs

# function to check if teams are correct and years are correct
def teamAndYearClean(desiredTeams,desiredYears,yearsList,teamsList):

    # check each year
    for year in desiredYears:
        if year not in yearsList:
            desiredYears.remove(year) # clean out all the years not between 2015-2025

    # check each team        
    for team in desiredTeams:
        if team not in teamsList:
            desiredTeams.remove(team) # clean out all teams not in the list of 30

    # return the cleaned teams and years lists
    return desiredTeams,desiredYears

# this will extract the data from Basketball Reference
def obtainData(desiredTeams,desiredYears):

    # this will help label the columns with either team (tm) or opponent (opp)
    stats = ['PTS','AST','STL','BLK','FG%','3P%','FG','FGA',
             'FT','FTA','FT%','ORB','DRB','TRB','TOV','PF']
    
    # create a dictonary to store the stats for the team
    # for each team stat add Tm_ in front
    teamStatsDictionary = {stat: 'Tm_' + str(stat) for stat in stats}

    # dictonary to store opponent stats
    # for each opponent stat add Opp_ in front and .1 to differentiate with team stats
    # .1 might not be necessary
    opponentStatsDictionary = {stat + '.1': 'Opp_' + str(stat) for stat in stats}

    mainDataFrame = pd.DataFrame() # create an empty dataframe w/ Pandas into which the program appends data

    loopNum = 0 # this is just to show the number of urls the program has gone through 

    for year in desiredYears: # iterate through all the years the user wants
        
        for team in desiredTeams: # during each year iterate through each team

            # create the url from which the data will be collected
            # basketball reference uses the team abbreviations and years in the url
            url = f'https://basketball-reference.com/teams/{team}/{year}/gamelog/'
            # show progress in the program
            loopNum+=1
            print(f'Url #{loopNum}: {url}')

            # use pd to read the url; header=1 means row 2 (first row has no stats)
            # id in inspect element is team_game_log_reg; [0] will take just the first table from the page
            teamDataFrame = pd.read_html(url,header=1,attrs={'id':'team_game_log_reg'})[0] # use pandas to read the url 

            # keep only the rows in 'Rk' where there is a string or number
            teamDataFrame = teamDataFrame[(teamDataFrame['Rk'].str != '') & (teamDataFrame['Rk'].str.isnumeric())]

            # there was a problem with 'Unnamed 24' appearing as an extra column
            # so remove it if it appears
            if 'Unnamed: 24' in teamDataFrame.columns:
                teamDataFrame.drop(columns=['Unnamed: 24'])

            # rename Unnamed: 3 to Home; 'Tm' to 'Tm_Pts'; 'Opp.1' to 'Opp_Pts'
            teamDataFrame = teamDataFrame.rename(columns={'Unnamed: 3': 'Home', 'Tm': 'Tm_Pts','Opp.1': 'Opp_Pts'})

            # to rename the columns (by adding the Tm_ set by the dictonary earlier)
            teamDataFrame = teamDataFrame.rename(columns=teamStatsDictionary)

            # to rename the columns (by adding the Opp_ set by the dictionary earlier)
            teamDataFrame = teamDataFrame.rename(columns=opponentStatsDictionary)

            # now add the team and year information to the main dataframe (the one created earlier)
            mainDataFrame = pd.concat([mainDataFrame,teamDataFrame],ignore_index=True)

            time.sleep(6) # wait 6 seconds so as not to overload servers

    # print out the simplified table of stats to the terminal
    print(mainDataFrame)

    # ask user if they want the csv file
    print('Would you like to get the data in a csv file?')
    csvChoice=input('n for no and anything else for yes: ')
    #if yes
    if csvChoice != 'n':
        # creating the csv file and telling the user the name of it
        csvName = input("Enter name for file: ") # get name the user wants
        print(f'csv file has been stored in: {csvName}.csv')
        # create the csv file and store it in the user's files
        mainDataFrame.to_csv(f'{csvName}.csv',index=False)
    return # return back to the main code

# this will create the graph for the user
def graphData(desiredTeams,desiredYears):
        
    # list of stats
    stats = ['PTS','AST','STL','BLK','FG%','3P%','FG','FGA',
             'FT','FTA','FT%','ORB','DRB','TRB','TOV','PF']    

    # creating the team stat dictonary
    # adding Tm_ to each stat
    teamStatsDictionaryGraph = {stat: 'Tm_' + str(stat) for stat in stats}

    # creating the opponent stat dictonary
    # adding Opp_ and .1 to each stat
    opponentStatsDictionaryGraph = {stat + '.1': 'Opp_' + str(stat) for stat in stats}

    loopNum = 0 # to show the url count

    # iterate through each year and team
    for year in desiredYears:
        for team in desiredTeams:
            loopNum+=1
            # create the url and print it
            url = f'https://www.basketball-reference.com/teams/{team}/{year}/gamelog/'
            print(f'URL #{loopNum}: {url}')

            # create the data frame from which the program will extract just the desired data
            teamDataFrameGraph = pd.read_html(url,header=1,attrs={'id':'team_game_log_reg'})[0]
            
            # drop the rows with 'Rk' where there is no value
            teamDataFrameGraph = teamDataFrameGraph[(teamDataFrameGraph['Rk'].str != '') & (teamDataFrameGraph['Rk'].str.isnumeric())]

            # drop Unnamed: 24 if it appears
            if 'Unnamed: 24' in teamDataFrameGraph.columns:
                teamDataFrameGraph = teamDataFrameGraph.drop(columns=['Unnamed: 24'])
                
            # renaming Unnamed: 3 to Home; Tm to Tm_Pts; Opp.1 to Opp_Pts    
            teamDataFrameGraph = teamDataFrameGraph.rename(columns={'Unnamed: 3': 'Home', 'Tm': f'Tm_Pts', 'Opp.1': f'Opp_Pts'})

            # replacing the stats with those that have Tm_ in front
            teamDataFrameGraph = teamDataFrameGraph.rename(columns=teamStatsDictionaryGraph)

            # replacing the stats with those that have Opp_ in front
            teamDataFrameGraph = teamDataFrameGraph.rename(columns=opponentStatsDictionaryGraph)

            # turn the desired data (points scored by team) into numeric values
            # errors='coerce' turns non-numeric values into NaN (Not a Number) without causing an error
            teamDataFrameGraph[f'Tm_Pts'] = pd.to_numeric(teamDataFrameGraph[f'Tm_Pts'],errors='coerce')
            # print(teamDataFrameGraph[f'Tm_Pts']) # for debugging 

            # now creating the x-axis of the graph which will store the game numbers
            gameNumberList = []                                                                                
                
            # loop the length of the list of data 
            for gameNumber in range(len(teamDataFrameGraph[f'Tm_Pts'])):
                # creating game numbers
                gameNumber+=1
                # adding to the list of game numbers
                gameNumberList.append(gameNumber)

            # adding the game number and points scored (with 'Tm_Pts')
            plt.plot(gameNumberList,teamDataFrameGraph['Tm_Pts'])
            # for each team and year show the title
            # so they are easily distinguishable
            plt.title(f'{team}, {year} Points Per Game')
            plt.xlabel('Game Number')
            plt.ylabel(f'Points')
            plt.show() # to print the graph(s)

            # time.sleep(2)

if __name__ == '__main__': # main code

    # list of all the teams in the NBA (from 2015-2025/current)
    teamsList = ['atl','bos','bkn','cha','chi','cle','dal','den','det','gsw','hou','ind','lac','lal','mem',
                 'mia','mil','min','nop','nyk','orl','okc','phi','pho','por','sac','sas','tor','uta','was']
    
    # split into 3 lists and print each on screen
    teamsList1 = ['atl','bos','bkn','cha','chi','cle','dal','den','det','gsw']
    teamsList2 = ['hou','ind','lac','lal','mem','mia','mil','min','nop','nyk']
    teamsList3 = ['orl','okc','phi','pho','por','sac','sas','tor','uta','was']
    print(f'Teams: \n{teamsList1}\n{teamsList2}\n{teamsList3}')
    print('') # create a space in the terminal

    # obtain the team(s)
    desiredTeams = input('Enter the team(s) you want with the abbreviation(s). Use all lowercase. Split by comma: ').split(',')
    
    # create list of possible years and print the list to the screen
    yearsList = ['2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','2025']
    print('') # create a space in the terminal
    print(f'Years: {yearsList}')
    print('') # create a space in the terminal
    
    # obtain the year(s)
    desiredYears = input('Enter the year(s) you want. Split by comma: ').split(',')

    # ensure only years from 2015-2025 and teams in the list of 30
    desiredTeams,desiredYears = teamAndYearClean(desiredTeams,desiredYears,yearsList,teamsList) # checking for incorrect teams & years
    
    print('')

    # if after checking NO years and/or teams were correct then don't go forward
    if len(desiredTeams) == 0 or len(desiredYears) == 0: 
        print("Please only choose from the teams and years printed above.")
        print(desiredTeams, desiredYears)

    # meaning there are still teams and years to work with
    else: 
        # tell user what they selected
        print(f'Team(s) selected: {desiredTeams}. Year(s) selected: {desiredYears}')

        # the obtainData function collects the gamelogs from Basketball Reference
        obtainData(desiredTeams,desiredYears)

        # once the data has been collected and shown to user
        # ask them if they want to see a graph of the stats of each team
        graphChoice = input('Enter y to create graph of points (enter anything else for no): ')

        if graphChoice == 'y': # meaning user wants to create a graph
            graphData(desiredTeams,desiredYears)
