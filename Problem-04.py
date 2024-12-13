def count_mul(numbers):
    mul_count = {} #empty dictionary to store the count of multiples
    for i in range(1, 10):  # Iterate through numbers 1 to 9 as mention in question
        count = 0
        for num in numbers:#iterate through the input stream provided by user 
            if num % i == 0:  # Check if the number is a multiple of i
                count += 1 #increment the count if so
        mul_count[i] = count #we store the count with i as the key e.g:if input stream is (1,2) then {1:2, 2:1, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    return mul_count

# Example usage
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
#numbers = list(int(input("Enter numbers separated by spaces: ")).split()) if you want to take input from user
result = count_mul(numbers)
print("Output:", result)