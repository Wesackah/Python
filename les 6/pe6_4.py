studentencijfers = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]
antw = []
def gemiddelde_per_student(studentencijfers):
    for i in studentencijfers:
        antw.append((sum(i)/len(i)))
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    antw2 = sum(antw)/len(antw)
    return antw2

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
