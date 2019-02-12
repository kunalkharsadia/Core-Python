import os

location = 'C:\\Users\\kunal.j.kharsadia\\Documents\\PythonPrograms'
filename = 'test.txt'

with open(os.path.join(location, filename)) as f:
    print(f.read())
    
