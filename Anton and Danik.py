#Initialization block
input()
games=input()
games_anton_won=0
games_danik_won=0

#Checking block
for i in games:
    if(i=='A'):
        games_anton_won += 1
    else:
        games_danik_won += 1

#Output block
if(games_anton_won > games_danik_won):
    print("Anton")
elif(games_anton_won < games_danik_won):
    print("Danik")
else:
    print("Friendship") 