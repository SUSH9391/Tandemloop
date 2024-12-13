def gen_series(a):
    series = [] #empty list to store the series
    for i in range(1, a + 1): #e.g: if a = 2, then range(1, 2) = 1 so 2 = 1 in series
        if i % 2 != 0:  # Include only odd numbers since mention in questions
            series.append(i) #1 is appended
    return series

# Example usage
a = int(input("Enter a number: "))
if a > 0:
    result = gen_series(a)
    print("Output:",",".join(str(i) for i in result))
else:
    print("Only positive numbers just like only positive vibes ;)")