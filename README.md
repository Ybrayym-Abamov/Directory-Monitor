# Directory Monitor


A CLI Python long-running program that was built to monitor certain activities that could be taking place in a given directory AND it will log the activities that have taken place to YOU in a human readable manner.
    Activites are:
        1) Making of a directory
        2) Deletion of a directory
        3) Making of a file
        4) Deletion of a file
        5) Addition of magic texts and lines
    The logger will tell you whenever any of these acitivites take place.


How to use the program with the command line?
    If you go to the command line and type "python dirwatcher.py -h"(make sure your default terminal python is python3), it will show you series of usefull flags that you can use as you please

    ### Demonstration

    For example:
        python3 dirwatcher.py -e .log -i 2.0 dirwatcher 'I love python'
    
    This tells the program to look for the magic text 'I love python' within the dirwatcher directory and only inside of 
    .log files at 2 sec pace.


    Reminder:
        If you don't specify the extension, it will default to .txt files. 
        If you don't specify the interval, it will default to 1 sec. 
        You must specify the directory
        You must specify the magic text to be searched for




## Getting Started

After forking and cloning the repository, a requirements.txt document can be used to create a Python virtual environment with the appropriate packages.

### Python Packages

```
entrypoints==0.3
flake8==3.7.9
mccabe==0.6.1
pycodestyle==2.5.0
pyflakes==2.1.1
```

### Command-Line Arguments

#### CLI Usage

```
python3 dirwatcher.py [-h] [-i,--interval] [-l,--loglevel] dir ext text
```

#### Positional/Required Arguments

```
dir ~ The directory the program needs to monitor
ext ~ The extension of the files the program will read
text ~ The string of text the program should look for in file data
```

#### Optional Arguments

```
-h ~ Display the help menu
-i, --interval ~ The frequency that the program looks at file data (defaults to every 1 second)
-l, --loglevel ~ Determines the verbosity of program logging (defaults to INFO)
```

#### CLI Example

```
python3 dirwatcher.py -i 3 -l 1 . .txt "Hello World"
```

The above example will:

- Search the current directory
- Dynamically read lines in .txt files
- Look for 'Hello World' in .txt file lines
- Look for appended lines and new files every 3 seconds
- Log on a DEBUG level, providing the most possible information

## Author

- **Ybrayym Abamov** - [Ybrayym Abamov](https://github.com/Ybrayym-Abamov)