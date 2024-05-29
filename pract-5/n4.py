import random
myGroup = ['Matsenko','Polyakova','Ulyanova','Emelyanov','Kergan','Petrosyan','Ivanov','Nosikov','Pisushkin','Chikatilo']
otherGroup = ['Putin','Pichushkin','Gad','Pryshev','Voldyryov','Kadyrov','Husky','San-Loran','Tsoi','Lumumba']
def chooseStudents(studentsList, studentsNum):
    chosenStudents = []
    while len(chosenStudents) < studentsNum:
        student = random.choice(studentsList)
        if student not in chosenStudents:
            chosenStudents.append(student)
    return chosenStudents

sportTeam = tuple(chooseStudents(myGroup,5) + chooseStudents(otherGroup,5))
sportTeamSorted = tuple(sorted(sportTeam))

print(myGroup, '\n', otherGroup, '\n', sportTeam, '\n', sportTeamSorted)
print('Ivanov v komande? Esli da to skolko ruz?')
if 'Ivanov' in sportTeam:
    print(sportTeam.count('Ivanov'))
else:
    print('Ivanova ne zavezli')

