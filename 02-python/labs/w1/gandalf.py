#import itertools
import itertools
#list definition
gandalf_spells = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman_spells = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]
for (a,b) in zip(gandalf_spells,saruman_spells):
    if a == b:
        print('empate')
    elif a < b:
        print('Saruman gana')
    else:
        print('Gandal gana')