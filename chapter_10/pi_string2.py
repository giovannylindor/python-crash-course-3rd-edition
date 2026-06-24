from pathlib import Path 

path = Path('chapter_10/large_file.txt')
contents = path.read_text().strip()


bday = input("Enter BDAY (MMDDYY): ")

if bday in contents:
    print('Yes!')
else:
    print('No!')
