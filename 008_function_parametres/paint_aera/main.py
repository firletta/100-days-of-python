import math

def main():
    test_h = int(input("Height of wall: "))
    test_w = int(input("Width of wall: "))
    coverage = 5
    print(paint_calc(height=test_h, width=test_w, cover=coverage))

def paint_calc(height, width, cover):
    area = height * width
    number_of_cans = math.ceil(area / cover)
    return f"You'll need {number_of_cans} cans of paint."

if __name__ == "__main__":
    main()