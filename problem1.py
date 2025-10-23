def reverse_string(s):
    # Initialize an empty string to hold the reversed result
    reversed_s = ""

    # Loop through each character in the input string
    for char in s:
        # Add the character to the result string
        reversed_s = char + reversed_s

    # Return the reversed string
    return reversed_s

# Example usage:
user_input = input("Enter a string to reverse: ")
print("Reversed string:", reverse_string(user_input))


