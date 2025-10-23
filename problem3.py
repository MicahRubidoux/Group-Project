def is_even (number):
  half = number / 2
    if half == int(half):
        return "even"
    else:
        return "odd"
    
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"{num} is {is_even(num)}")
    
