letters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
points = [
    1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
    4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10
]

letters_points_zipped = zip(letters, points)
letter_to_points = {key: value for key, value in letters_points_zipped}

# Add blank space key value pair to the dictionary
letter_to_points[" "] = 0

# Create function score_word that takes in a word and returns its point value.


def score_word(word):
    score = 0
    word_to_upper = word.upper()

    for c in word_to_upper:
        score += letter_to_points[c]
    return score


# Lets test this function.
brownie_points = score_word("BROWNIE")
print(f"brownie: {brownie_points}")
