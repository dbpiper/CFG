# CFG
Tools related to CFGs

# Generating Random String from a CFG


Functionality provided by the GenerateStringFromCFG\GenerateStringFromCFG.py file.

Requires Python 3 and nltk.

Once Python 3 and pip are installed you can install nltk like this:

```
pip install nltk
```

## CFG input
Put the CFG in the GenerateStringFromCFG\config\CFG.txt file, following the
example provided.

For augmented CFGs (like the one provided) I have chosen to use A instead of S'
because CFG.fromstring does not like S' as a production head.

However, any non-terminal can be used.

Furthermore, terminals and non-terminals must be separated by a spaces, and
terminals should be enclosed by single quotes as in the example provided.

## config
The project supports setting a max length for the string to make
testing the parsing process (or whatever you are using the CFG string for)
easier. I personally like to have the shortest strings possible to test
my parse table which is my use case. 

To configure this please set the max_len property in the
GenerateStringFromCFG\config\config.ini.

This will be the maximum length of the generated string, inclusive.

If you do not wish to have a maximum length, then simply set
this value to -1.
