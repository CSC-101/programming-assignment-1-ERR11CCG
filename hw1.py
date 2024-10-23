from data import *

# Write your functions for each part in the space below.

# Part 1
def vowel_count(in_str:str) -> int:
    vowels = 'aAeEiIoOuU'
    count = 0
    for let in in_str:
         if let in vowels:
             count+= 1
    return count


# Part 2
def short_lists(in_list: list[list[int]]) -> list[list[int]]:
    result = []
    for sublist in in_list:
        if len(sublist) >= 2:
            result.append(sublist)
    return result


# Part 3
def ascending_pairs(input_list: list[list[int]]) -> list[list[int]]:
    result = []
    for sublist in input_list:
        if len(sublist) >= 2:
            result.append(sorted(sublist))
        else:
            result.append(sublist)
    return result



# Part 4
def add_prices(price1: Price, price2: Price) -> Price:
    total_dollars = price1.dollars + price2.dollars
    total_cents = price1.cents + price2.cents

    if total_cents >= 100:
        extra_dollars = total_cents // 100
        total_dollars += extra_dollars
        total_cents = total_cents % 100

    return Price(total_dollars, total_cents)


# Part 5
def rectangle_area(rect: Rectangle) -> int:
    width = rect.bottom_right_x - rect.top_left_x
    height = rect.top_left_y - rect.bottom_right_y

    return width * height

# Part 6
def books_by_author(author_name: str, books: list[Book]) -> list[Book]:
    result = []
    for book in books:
        if book.author == author_name:
            result.append(book)
    return result

# Part 7
def circle_bound(rect: Rectangle) -> Circle:
    center_x = (rect.top_left_x + rect.bottom_right_x) / 2
    center_y = (rect.top_left_y + rect.bottom_right_y) / 2
    dx = rect.bottom_right_x - center_x
    dy = rect.bottom_right_y - center_y
    radius = math.sqrt(dx**2 + dy**2)
    return Circle(center_x, center_y, radius)

# Part 8


def below_pay_average(employees: list[Employee]) -> list[str]:
    if not employees:
        return []
    total_pay = sum(employee.pay_rate for employee in employees)
    average_pay = total_pay / len(employees)
    result = []
    for employee in employees:
        if employee.pay_rate < average_pay:
            result.append(employee.name)

    return result


