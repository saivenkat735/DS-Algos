def is_palindrome(string):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    string = string.replace(" ", "").lower()
    
    # Reverse the string
    reversed_string = string[::-1]
    
    # Compare the original and reversed strings
    if string == reversed_string:
        return True
    else:
        return False

# Test the function
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
