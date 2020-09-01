This program was built to monitor certain activities that could be taking place in a given directory AND it will log the activities that have taken place to YOU in a human readable manner.
    Activites are:
        1) Making of a directory
        2) Deletion of a directory
        3) Making of a file
        4) Deletion of a file
        5) Addition of magic texts and lines
    The logger will tell you whenever any of these acitivites take place.


How to use the program with the command line?
    If you go to the command line and type "python dirwatcher.py -h"(make sure your default terminal python is python3), it will show you series of usefull flags that you can use as you please

    For example:
        python3 dirwatcher.py -e .log -i 2.0 dirwatcher 'I love python'
    
    This tells the program to look for the magic text 'I love python' within the dirwatcher directory and only inside of 
    .log files at 2 sec pace.


    Reminder:
        If you don't specify the extension, it will default to .txt files. 
        If you don't specify the interval, it will default to 1 sec. 
        You must specify the directory
        You must specify the magic text to be searched for



--Ybrayym Abamov