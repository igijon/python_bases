import os
import shutil
from pathlib import Path

print(os.getcwd())  # Directorio actual
archivo = open('curso.txt', 'w')
archivo.write('Texto de prueba')
archivo.close()

print(os.listdir())

shutil.move('curso.txt', Path('..'))

print(os.walk(Path('.')))
ruta = Path('..')
for carpeta, subcarpeta, archivo in os.walk(Path(ruta)):
    print(f'en la carpeta:  {carpeta}')
    print(f'Las subcarpetas son: ')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')
