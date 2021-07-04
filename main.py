import os

# https://docs.python.org/3/library/os.path.html?highlight=os%20path#module-os.path
from os.path import join

# STUFE 1 - Wir suchen alle Dateien zusammen

# Hier sammeln wir unsere Dateien
file_paths = []

# wir laufen durch alle ordner an unserem aktuellen ort
# damit ist der punkt gemeint!
for root, dirs, files in os.walk('.'):
    # das aktuelle verzeichnis ausgeben, also root
    # print(root, "consumes", end=" ")
    #print("Wir sind gerade in " + root)
    #print("Hier liegen diese Dateien: " + str(files))
    #print("Hier gibt es diese Ordner: " + str(dirs))

    # Innerer Loop: Wir sammeln Dateien in einem Ordner
    for file_name in files:
        #print("Hier liegt Datei: " + file_name)
        file_path = join(root, file_name)
        #print("Der Pfad lautet: " + file_path)
        file_paths.append(file_path)

    #print("__________________")
    #print()

#print("Ergebnis Stufe 1")
#print(file_paths)

# STUFE 2 - Unteruschen auf gleiche Dateien

# https://docs.python.org/3/library/itertools.html
import itertools

# Idee: Zwei Dateien sind dann gleich, wenn alle Bytes der
# Datei gleich sind

for combination in itertools.combinations(file_paths, 2):
    # print(combination)
    path_one, path_two = combination

    handle_one = open(path_one, 'r')
    handle_two = open(path_two, 'r')

    if handle_one.read() == handle_two.read():
        print("Dublette gefunden!")
        print(combination)