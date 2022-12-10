"""
    Easy problem so far, how do I set up unit testing? Plus code coverage
    would be good.
"""

def run():
    """ Runs code for AoC answers """
    with open("./input.txt", 'r', encoding='UTF-8') as file:
        lines = [line.rstrip() for line in file]

    max_calories = []
    current_calories = 0

    for line in lines:
        if line == '':
            max_calories.append(current_calories)
            current_calories = 0
            continue

        current_calories += int(line)

    # 195561 too low
    max_calories.sort(reverse=True)
    print (f'Answer 2: {sum(max_calories[0:3])}')

if __name__ == '__main__':
    run()
