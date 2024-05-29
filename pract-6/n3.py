Grisha = {'russian', 'chinese', 'german'}
Maksim = {'russian', 'english'}
Masha = {'french', 'russian', 'english'}
Anya = {'german', 'chinese', 'russian'}
Kolya = {'english', 'chinese', 'japanese', 'russian'}
language = Grisha | Maksim | Masha | Anya | Kolya
students = { "Grisha": Grisha, "Maxim": Maksim, "Masha": Masha, "Anya": Anya, "Kolya": Kolya }

print ('Solko yazikov znayut studenty: ', len(language))
print(sorted(language))

print(students)

for i in students:
    if 'chinese' in students[i]:
        print(i)