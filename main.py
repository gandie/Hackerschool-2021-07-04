import sys
import os

# https://docs.python.org/3/library/itertools.html
import itertools

# https://docs.python.org/3/library/os.path.html?highlight=os%20path#module-os.path
from os.path import join


'''
- 2. ) Wie mit bearbeiteten Bildern umgehen?
- 1. ) Wie auf andere Orte anwenden? 
'''

def find_files(start_path):
    '''
    STUFE 1 - Wir suchen alle Dateien zusammen

    Argumente:
    
    start_path : Der Ort im Dateisystem, ab dem das Programm laufen soll
    '''

    # Hier sammeln wir unsere Dateien
    file_paths = []

    # wir laufen durch alle ordner an unserem
    # eingegebenen start_path
    for root, dirs, files in os.walk(start_path):

        # Innerer Loop: Wir sammeln Dateien in einem Ordner
        for file_name in files:
            #print("Hier liegt Datei: " + file_name)
            file_path = join(root, file_name)
            #print("Der Pfad lautet: " + file_path)
            file_paths.append(file_path)

    return file_paths

def check_double_files(files):
    '''
    STUFE 2 - Unteruschen auf gleiche Dateien

    Idee: Zwei Dateien sind dann gleich, wenn alle Bytes der Datei gleich sind

    Argumente:
    files: Liste mit Dateien, die geprüft werden sollen
    '''

    for combination in itertools.combinations(files, 2):
        # print(combination)
        path_one, path_two = combination

        handle_one = open(path_one, 'rb')
        handle_two = open(path_two, 'rb')

        if handle_one.read() == handle_two.read():
            print("Dublette gefunden!")
            print(combination)


if __name__ == '__main__':
    start = sys.argv[1]
    print(start)
    files = find_files(start)
    check_double_files(files)
