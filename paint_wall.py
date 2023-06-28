import math

test_w = int(input("what is height of wall? "))
test_h = int(input("what is width of wall? "))
coverage = 5

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"you are going to need {num_of_cans} cans of paint")


paint_calc(height=test_h, width=test_w, cover=coverage)



