while True:

    prompt = input("Enter a number to check whether it is a palindrome: ")

    if prompt == prompt[::-1]:
        print(f'{prompt} is a palindrome')
    else:
        print(f'{prompt} is not a palindrome')
