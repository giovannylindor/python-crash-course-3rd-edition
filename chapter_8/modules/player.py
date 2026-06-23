def makePlayer(firstName, lastName, **additionalInfo):
    player = {'firstName': firstName.capitalize(), 
              'lastName': lastName.capitalize() }
    return player


def printPlayer(player):
    print(f"\nFirst Name: {player['firstName']}"
          f"\nLast Name: {player['lastName']}")
    
