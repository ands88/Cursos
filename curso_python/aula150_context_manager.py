# context manager com funçao - Criando e usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def my_open(file_path, mode):
    try:
        print('Open file')
        file = open (file_path, mode, encoding = 'utf8')
        yield file
    except Exception as e:
        print('An error has occured.')
    finally:
        print('Close file')
        file.close()


with my_open('aula150.txt', 'w') as file:
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.write('Line 3\n')
    print('WITH', file)