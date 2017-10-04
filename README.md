# Play-On-Words Generator
A play-on-words generator that uses phonetics to find similar sounding words and replaces those words in sentences with a pun.

# Usage
This project uses a library called `phonetics`. You can install it with pip and find it here https://pypi.python.org/pypi/phonetics

The main file is `powGenerator.py`. Running this with a word to make the pun off of and a directory full of a bunch of .txt files will first search for a similar sounding word from the user's dictionary. Afterwards, it will search for sentence usecases in the directory's .txt files and replace the word with the subject given in the arguments.

i.e Running `python powGenerator.py cat /some/path/to/text` will generate a sentence like `The predicament was a catastrophe`
The results can vary, as choosing the pun and sentence usecase is pseudo-random to add some variety.
