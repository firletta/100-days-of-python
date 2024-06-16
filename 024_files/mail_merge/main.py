def prepare_letters(names_file_path, letter_template_path, output_folder_path, placeholder):
    with open(names_file_path, 'r') as names_file:
        names = names_file.read().splitlines()

    with open(letter_template_path, 'r') as letter_file:
        letter_template = letter_file.read()

    for name in names:
        personalized_letter = letter_template.replace(placeholder, name.strip())
        output_file_path = f"{output_folder_path}/letter_for_{name.strip()}.txt"

        with open(output_file_path, 'w') as output_file:
            output_file.write(personalized_letter)

def main():
    names_file_path = "Input/Names/invited_names.txt"
    letter_template_path = "Input/Letters/starting_letter.txt"
    output_folder_path = "Output/ReadyToSend"
    placeholder = "[name]"
    prepare_letters(names_file_path, letter_template_path, output_folder_path, placeholder)

if __name__ == "__main__":
    main()