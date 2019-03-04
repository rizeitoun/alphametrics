# This solves an alphametrics puzzle where you have several words that are added to equal a new word.  Each letter represents a number [0-9], numbers only appear once and leading numbers cannot be 0.  This is solved in a brute force manner using a recursive function. 

def solve(puzzle):

    # Parses letters and sets up which letters cannot be 0
    p = puzzle.split(' ')
    var = p[slice(0,len(p),2)]
    letters = list(set(''.join(var)))
    value_counter = len(letters)*[0]
    value_start = len(letters)*[False]
    start_letters = list(set([i[0] for i in var]))

    for i in range(len(letters)):
        if letters[i] in start_letters:
            value_start[i] = True

  # Iterates through correct solution until value is found.
    need_solution = True
    while need_solution:
        value_counter, value_start = shift(value_counter, value_start, 0)

        if value_start is None:
            return dict()

        if len(set(value_counter)) == len(value_counter):
            data = 0
            for j in range(len(var)):
                value = [str(value_counter[letters.index(var[j][i])]) for i in range(len(var[j]))]
                if j+1 < len(var):
                    data += int(''.join(value))
                elif (data == int(''.join(value))):
                    need_solution = False

    print(dict(zip(letters, value_counter)))

# Recursive function used to cycle through all permutations of unique numbers.  Did it this way to not store all permuatations in memory.
def shift(value_counter, value_start, n):
    value_counter[n] += 1
    if value_counter[n] > 9:
        if n == len(value_counter)-1:
            value_start = None
        else:
            if value_start[n]:
                value_counter[n] = 1
            else:
                value_counter[n] = 0
            value_counter, value_start = shift(value_counter, value_start, n+1)
    return value_counter, value_start


if __name__ == '__main__':
    solve(
        "SEND + MORE == MONEY"
    )
