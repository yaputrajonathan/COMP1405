#Jonathan 10116272



#initialization
all_stats=[0,1]
no_stats= 0
def readStats(filename):
    '''Reads a .csv file and turns it into 
    a nested list. '''
    f = open(filename,'r')
    line = f.readlines()
    statList = []
    for i in range(1, len(line)):
        x = []
        y = 0
        for j in range(0, len(line[i])):
            #stop when reached "/n" but append all the values in between the previous comma and "\n"
            if line[i][j] == "\n":
                x.append(line[i][y:j])  
                y = 0
                continue 
            #stop when reached a comma, and append all the sliced values since the previous comma
            elif line[i][j] == ",":     
                x.append(line[i][y:j])
                y = j+1 
                
        statList.append(x)
        
    f.close()    
    return statList
    
def statsForPlayer(n,name): 
    '''Searches through a nested list for a player by the name, returns a list of the stats'''   
    if type(n) != list:
        print("Please type in \"all_stats\" in the first argument.")        
        return
    d = readStats("nhl_2018.csv")
    for i in range(1,len(d)):
        x = []
        for j in range(0,len(d[i])):
            if name == d[i][j]:
                x.append(d[i])
                return x
    return x        #returns an empty list if the player's name is not in the list

def filterByPos(n,position):
    '''Takes a position as an argument, search through the list 
    and returns a list of players with the same position, and their stats'''
    d = readStats("nhl_2018.csv")
    playerList = []
    
    for i in range(1,len(d)):
        positionList = []
        if d[i][2] == position:         #d[i][2] = where the information of the players' positions are located
            positionList.append(d[i])
            playerList.append(positionList)

    return playerList

def sortByPoints(n):
    '''Sort the players,decendingly, by their points'''
    if type(n) != list:
        print("Please type in \"all_stats\" in the first argument.")   
        return     

    d = readStats("nhl_2018.csv")

    for i in range(0,len(d)):  
        d[i][6] = int(d[i][6])
    #make a copy to prevent mutation
    d = d[:]

    #start with an empty output list
    out = []

    #insertion sort
    #until the input is empty
    while len(d)>0:

        #take the first item out of the input
        item = d.pop(0)

        #add it to the end of output
        out.append(item)

        currentIndex = len(out)-1

        #while that item is out of order
        while currentIndex > 0 and out[currentIndex-1][6] < out[currentIndex][6]:

            #swap left
            temp = out[currentIndex]
            out[currentIndex] = out[currentIndex-1]
            out[currentIndex-1] = temp

            currentIndex -= 1

    #return the output list
    return out

       
def buildBestTeam(n,filename):
    '''Builds a list of the players with the highest points, 
    the team consists of 1 Centre, 1 Left Wing, 1 Right Wing, and 2 Defenders.'''
    if type(n) != list:
        print("Please type in \"all_stats\" in the first argument.")        
        return
    try:
        f = open(filename,"w")
    except:
        print(f"Error writing to the file: {filename}")
        return

    bestTeamList = []
    sortedList = sortByPoints(n)
    Centre = 0
    rightWing = 0
    leftWing = 0
    Defender = 0

    for i in range(0,len(sortedList)):
        
        if Defender == 2:      #writes the best team in desired file
            f.write(f"\
{bestTeamList[0][0]}\n\
{bestTeamList[1][0]}\n\
{bestTeamList[2][0]}\n\
{bestTeamList[3][0]}\n\
{bestTeamList[4][0]}\n\
")
            return
    
        #searches for 1 C
        elif sortedList[i][2] == 'C' and Centre == 0:
            bestTeamList.append(sortedList[i])
            Centre += 1
        #searches for 1 RW
        elif sortedList[i][2] == 'RW' and rightWing == 0:
            bestTeamList.append(sortedList[i])
            rightWing += 1
        #searches for 1 LW
        elif sortedList[i][2] == 'LW' and leftWing ==0:
            bestTeamList.append(sortedList[i])
            leftWing += 1
        #searches for 2 D
        elif sortedList[i][2] == 'D':
            bestTeamList.append(sortedList[i])
            Defender += 1

    f.close()


def displayTeamStats(n,filename):
    '''Builds a table for the players and their stats'''
    if type(n) != list:
        print("Please type in \"all_stats\" in the first argument.")        
        return
    f = open(filename,"r")
    sampleTeamList = f.readlines()
    newSampleTeamList = []
    for i in range(0,len(sampleTeamList)):          #turns the names of the players in the file into a list
        newSampleTeamList.append(sampleTeamList[i][:len(sampleTeamList[i])-1])
        
    print("Name"+"\t"*3+ "Team"+"\t"+"Pos"+"\t"+"Games"+"\t"+"G"+"\t"+"A"+"\t"+"Pts"+"\t"+"PIM"+"\t"+"SOG"+"\t"+"Hits"+"\t"+"BS\n\
"+"="*99)           #builds the headers

    L = readStats("nhl_2018.csv")
    
    for i in range(0, len(newSampleTeamList)):
        w = newSampleTeamList[i]
        for j in range(0,len(L)):
            if w == L[j][0]:
                print(f"{L[j][0]}\t\t{L[j][1]}\t{L[j][2]}\t{L[j][3]}\t{L[j][4]}\t{L[j][5]}\t{L[j][6]}\t{L[j][7]}\t{L[j][8]}\t{L[j][9]}\t{L[j][10]}")
        
    f.close()
    

def pointsPerTeam(n,filename):
    '''Sums up all the player's points in the team'''
    if n == 0:
        return 0
    if type(n) != list:
        print("Please type in \"all_stats\" in the first argument.")        
        return
    f = open(filename,"r")
    sampleTeamList = f.readlines()
    newSampleTeamList = []
    for i in range(0,len(sampleTeamList)):      #turns the names of the players in the file into a list
        newSampleTeamList.append(sampleTeamList[i][:len(sampleTeamList[i])-1])
        
    L = readStats("nhl_2018.csv")
    teamPoints = 0
    for i in range(0, len(newSampleTeamList)):
        playerPoint = []
        w = newSampleTeamList[i]
        for j in range(0,len(L)):
            if w == L[j][0]:                    #searches through the nhl_2018 file for the players' points
                playerPoint.append(L[j][6])
        teamPoints+=int(playerPoint[0])         #appended the points into a list and then sums all the numbers in the list
    return teamPoints
