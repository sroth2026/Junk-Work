import random

def advanced_innings():
    bases = [0, 0, 0] #The base indices are the base numbers minus 1. So first base has index 0, and the value of the list element determines if someone is on base or not, the final index (index 3) represents homeplate which will simply be the sum of all the runs scored in an inning, so this element can take on any value depending on how many runs are scored
    plays = {0 : "Out", 1 : "Single", 2 : "Double", 3 : "Triple", 4 : "Homerun", 5 : "Out", 6 : "Out", 7 : "Out"} #Different possible plays with extra out ints to make probability more realistic
    outs = 0
    runs = 0
    while outs != 3: #3 out rule like before
        atbat = plays[random.randint(0,7)]
        if atbat == "Out": #If the runner is out nothing happens
            outs += 1
        elif atbat == "Homerun":
            runs += 1 + sum(bases)
            bases = [0, 0, 0]
        elif atbat == "Triple":
            runs += sum(bases)
            bases = [0,0,1]
        elif atbat == "Single": #If single, we need to account for if there are runners already on base. If there are we need to update the orientation of the bases list
            if bases[0] == 0 and bases[1] == 0 and bases[2] == 0: #empty bases
                bases[0] = 1
            elif bases[0] == 1 and bases[1] == 0 and bases[2] == 0: #if someone is already on first base
                bases[0] = 1 
                bases[1] = 1
            elif bases[0] == 0 and bases[1] == 1 and bases[2] == 0: #if someone is already on second base
                #pass
                bases[0] = 1
                bases[2] = 1
            elif bases[0] == 0 and bases[1] == 0 and bases[2] == 1: #if someone is already on third base
                bases[0] = 1
                bases[2] = 0
                runs += 1
            elif bases[0] == 1 and bases[1] == 1 and bases[2] == 0: #first and second
                bases[0] = 1
                bases[1] = 1
                bases[2] = 1
                #print("bases are loaded")
            elif bases[0] == 0 and bases[1] == 1 and bases[2] == 1: #second and third
                bases[0] = 1
                bases[1] = 0
                bases[2] = 1
                runs +=1
            elif bases[0] == 1 and bases[1] == 0 and bases[2] == 1: #first and third
                bases[0] = 1
                bases[1] = 1
                bases[2] = 0
                runs +=1
    return(runs)

        

def run_game(): #No changes made to run game
    count = 0
    top = True
    Away_score = 0
    Home_score = 0
    
    home_team = input("Enter Home Team: ")
    away_team = input("Enter Away Team: ")
    while count < 9:
        if top == True:
            Away_score += advanced_innings()
            count += 0.5
            top = False
        else:
            if count == 8.5:
                if Home_score > Away_score:
                    break
            Home_score += advanced_innings()
            count += 0.5
            top = True
    if Home_score == Away_score:
        while Home_score == Away_score:
            if top == True:
                Away_score += advanced_innings()
            else:
                Home_score += advanced_innings()
    if Home_score > Away_score:
        return(home_team + f' Win! {Home_score}-{Away_score}')
    else:
        return(away_team + f' Win! {Away_score}-{Home_score}')


        


    
#The MLB Season Class
#This class represents one year of baseball and implements run_game in the simulate_day method
#Only parameter of class object initialization is year
#Each season has three attributes: year, winner, standings
#simulate_day(): The way this works is it uses run_game() and adds the winner to the standings attribute dictionary if the team is not yet in there
#If the team is in the standings dict then the win is added onto the current total
#get_winner(): This is a property method that determines the max value in standings dict, or the team with the most wins
#Improvement ideas: could be a tie, maybe we can add the losses in as well, etc.


class MLB_Season:
    
    def __init__(self, year):
        self.year = year
        self.winner = None
        self.standings = {}
    
    def simulate_day(self):
        string = run_game()
        string = string.split('Win!') 
        name = string[0]
        if name in self.standings:
            self.standings[name] += 1
        else:
            self.standings[name] = 1
    
    
    @property
    def get_winner(self):
        if self.standings == {}:
            return
        maximum = 0
        winner = None
        for key in self.standings:
            if self.standings[key] >= maximum:
                maximum = self.standings[key]
                winner = key
        self.winner = winner
        return(self.winner)
            
        
        

#names will be a list of names that are MLB_Season objects
#This method displays a dictionary with the years of each season and the associated winners of each season
def season_display(names):
    print_dict = {}
    for j in range(len(names)):
        if isinstance(names, MLB_Season):
            print_dict[MLB_Season.year] = MLB_Season.get_winner
    return(print_dict)
            
        
        