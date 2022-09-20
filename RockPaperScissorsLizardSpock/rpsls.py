
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Error"
  
  def number_to_name(num):
    if num == 0:
        return "rock"
    elif num == 1:
        return "Spock"
    elif num == 2:
        return "paper"
    elif num == 3:
        return "lizard"
    elif num == 4:
        return "scissors"
    else:
        return "Error"
    
def rpsls(player_choice):
    print("")
    print("Player chooses {}".format(player_choice)) #The platform wouldn't work with f-strings.  Very annoying.  
    playernum = name_to_number(player_choice)
    compnum = random.randrange(4)   
    compchoice = number_to_name(compnum)
    print("Computer chooses {}".format(compchoice))
    diff = (playernum - compnum) % 5
    if diff == 1 or diff == 2:
        print("Player Wins!")
    elif diff > 2:
        print("Computer Wins!")
    else:
        print("Player and Computer Tie")
    
    
    
          
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



