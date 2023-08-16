import pandas as pd

# read in data
nato_data = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (_, row) in nato_data.iterrows()}
# ask user to input name
answer = input("Please enter a word: ")

# for each letter in answer, output the corresponding alphabet explanation from nato_alphabets
output_nato = [phonetic_dict[letter] for letter in answer.upper()]
print(output_nato)

