import pandas as pd

# read in data
nato_data = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (_, row) in nato_data.iterrows()}
# ask user to input name


# for each letter in answer, output the corresponding alphabet explanation from nato_alphabets

def generate_phonetic():
    answer = input("Please enter a word: ")
    try:
        output_nato = [phonetic_dict[letter] for letter in answer.upper()]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic() # recursively call the function until acceptable input
    else:
        print(output_nato)

generate_phonetic()



