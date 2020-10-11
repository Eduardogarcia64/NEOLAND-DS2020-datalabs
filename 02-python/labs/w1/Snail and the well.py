#Defining Variables
well = 125
day=30
night=-20
run = day+night
goal = 0
days = []
#Loop
while goal < well:
    print(goal)
    days.append(str(goal))
    goal+=run
    if goal > well:
        print('Total number of days is: '+str(len(days)))