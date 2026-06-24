from pathlib import Path

path = Path("chapter_10/learning_python.txt")
contents = path.read_text()

lines = contents.splitlines()

for line in lines:
    if 'Python' in line:
        line = line.replace('Python', 'C')
    
    print(line)