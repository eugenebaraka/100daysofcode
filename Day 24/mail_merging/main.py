from write_letters import WriteLetter

template_path = "/Users/ebaraka/Desktop/Github/100daysofcode/Day 24/mail_merging/Input/Letters/starting_letter.txt"
names_path = "/Users/ebaraka/Desktop/Github/100daysofcode/Day 24/mail_merging/Input/Names/invited_names.txt"
to_send_path = "/Users/ebaraka/Desktop/Github/100daysofcode/Day 24/mail_merging/Output/ReadyToSend"

if __name__ == "__main__":
    letter = WriteLetter(template_path, names_path, to_send_path)
    letter.write_letter()
