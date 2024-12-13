def gen_series(a):
    series = [] #empty list to store the series
    for i in range(a):
        series.append(1 + 2 * i)
    return series

# Example usage
a = int(input("Enter a number: "))
if a > 0: #only for positive numbers
    result = gen_series(a)
    print("Output:",",".join(str(i) for i in result))
else:
    print("Please enter a positive integer.")