subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])

// calcula nota media
suma = 0
for i in range(len(subjects)):
    suma +=  scores[i]

print("La suma de las notas es:", suma/len(subjects))

// calcular asignaturas con nota máxima y mínima
nota_maxima = scores[0]
nota_minima = scores[0]

for i in range(len(subjects)):
    if scores[i] > nota_maxima:
        nota_maxima = scores[i]
    if scores[i] < nota_minima:
        nota_minima = scores[i]
for i in range(len(subjects)):
    if scores[i] == nota_maxima:
        print("La asignatura con la nota máxima es:", subjects[i], "con una nota de", scores[i])
    if scores[i] == nota_minima:
        print("La asignatura con la nota mínima es:", subjects[i], "con una nota de", scores[i])
