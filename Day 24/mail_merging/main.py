from write_letters import WriteLetter

template_path = "./Input/Letters/starting_letter.txt"
names_path = "./Input/Names/invited_names.txt"
to_send_path = "./Output/ReadyToSend/"

if __name__ == "__main__":
    letter = WriteLetter(template_path, names_path, to_send_path)
    letter.write_letter()
