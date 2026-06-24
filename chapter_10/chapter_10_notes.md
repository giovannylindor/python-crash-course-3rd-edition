# Chapter 10: Files and Exceptions

**Exceptions**: Special Objects Python creates to manage errors 
- - -

## Reading From a File

when working with info from a text file
- step 1 is to read the file into memory 

**Reading Contents**
`pi_digits.txt`
```
3.14592653589793238462643383279
```

`file_reader.py`
```Python
from pathlib import Path

path = Path('chapter_10/pi_digits.txt')
contents = path.read_text()
print(contents)
```
- path &rarr; exact location of a file/folder on a system
- `pathlib` is a module that makes it easier to work with files and directories 
- `Path` is a class imported from `pathlib`
- `.read_text()` is a method that reads all the contents of the file

**Relative and Absolute File Paths**

when you pass a file name, python looks into the directory its stored in
- sometimes the file may not be in the same directory
- to get python to open files from a directory, provide the _specific path_

1. **Relative File Path** tells python to looks for a given location relative to the directory where the running program is stored
    - `path = Path('text_files/filename.txt')`

2. **Absolute File Path**: telling python exactly where the file is on your computer, regardless of where the program that's being executed is stored
    - You can use an absolute path if a relative path doesn't work 
    - You can read from any location on your system 
    - `path = Path('/home/eric/data_files/text_files/filename.txt')`

_NOTE_: Windows systems use (\) when displaying file paths instead of (/)
- `pathlib` library uses the correct representation of the path regardless of the system
- use `(/)` anyways


**Accessing File Lines**

The `splitlines()` method turns a long string into a set of lines
- You can use a for loop to examine each line 

`file_reader.py`
```Python
from pathlib import Path

path = Path('chapter_10/pi_digits.txt')
contents = path.read_text().rstrip()
lines = contents.splitlines()

print(lines)
# Output: ['3.145926535', '8979323846', '2643383279']

for line in lines: 
    print(line)
```

**Working w/ a File's Contents**
`pi_string.py`
```Python
from pathlib import Path

path = Path('chapter_10/pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()

pi_string = ''
for line in lines: 
    pi_string += line

print(pi_string)
print(len(pi_string))
```

- when python reads from a text file, it interprets all text as a string
- if you read in a number and want to work with its numerical context, convert it via `int()` or `float()`

**Large Files**

If we have a large file with a large string, we can use the split notation

`large_file.text`
_Envision 1,000,000 digits of pi.._

`pi_string2.py`
```Python
from pathlib import Path 

path = Path("chapter_10/large_file.txt")
contents = path.read_text().split()

string = ''
string += string.join(contents)


print(f"{string[:52]}")
print(len(string))
```

- theres no inherent limit to how much data you can work with
- you can w/ as much data as your systems memory can handle 
- - -

_Note_: `replace(oldWord, newWord)` is a method that replaces a word in a string w/ a diff word

## Writing to a File