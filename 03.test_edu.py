#let's do this!!!!
print('What day it is?')
date =input()
print('Number of calories in your breakfast')
breakfast = int(input())
print('Number of calories in your lunch')
lunch = int(input())
print('Number of calories in your dinner')
dinner = int(input())
print('Number of calories in your snacks')
snack = int(input())
totalCalories = breakfast + lunch + dinner + snack
print('Calories of '+date +' are: '+str(totalCalories))