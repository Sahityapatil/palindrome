import sys
print("Palindrome Checker Program")
# If user gives 1 argument → use that string
if len(sys.argv) == 2:
    text = sys.argv[1]
else:
    # Default string
    text = "madam"
    print("\nArgument not provided — using default value:")
    print("Default String = madam")

# Check palindrome
if text.lower() == text[::-1].lower():
    print(f"\n'{text}' is a palindrome.")
else:
    print(f"\n'{text}' is NOT a palindrome.")
