def main():
    """
    Reads numbers from two files and prints a list of numbers that appear in both files.
    """
    with open('file1.txt', 'r') as file_1, open('file2.txt', 'r') as file_2:
        numbers_1 = {line.strip() for line in file_1}
        numbers_2 = {line.strip() for line in file_2}

    matching_numbers = [int(number) for number in numbers_1.intersection(numbers_2)]

    print(matching_numbers)

if __name__ == "__main__":
    main()