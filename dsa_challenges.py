def filter_and_sort_evens(numbers):
    evens = []

    for num in numbers:
        if num % 2 == 0:
            evens.append(num)

    evens.sort()
    return evens


def count_character_frequency(text):
    text = text.lower()
    frequency = {}

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency



print(filter_and_sort_evens([3, 1, 4, 1, 5, 9, 2, 6]))
print(count_character_frequency("Hello World"))

