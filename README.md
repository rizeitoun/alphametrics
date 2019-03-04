# Alphametrics Solver in Python
#### This solves an alphametrics puzzle where you have several words that are added to equal a new word.  Each letter represents a number [0-9], numbers only appear once and leading numbers cannot be 0.  This is solved in a brute force manner using a recursive function. 

#### Implementation code is in alphametrics.py
#### Example tests from exercism where showing input and output as first and second parameters into assertEqual.
```
            assertEqual(solve("AND + A + STRONG + OFFENSE + AS + A + GOOD == DEFENSE"),
            {"A": 5,
             "D": 3,
             "E": 4,
             "F": 7,
             "G": 8,
             "N": 0,
             "O": 2,
             "R": 1,
             "S": 6,
             "T": 9})
```