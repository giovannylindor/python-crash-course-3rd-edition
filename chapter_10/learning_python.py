from pathlib import Path

path = Path("chapter_10/learning_python.txt")
contents = path.read_text()
print(contents)

print()
#2
lines = contents.splitlines()
for line in lines:
    print(line)

