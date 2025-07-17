try:
    a = int(input("Enter The First number:"))

    b = int(input("Enter The Second number:"))

    print("What operation you want to do?\nPress + for Additon \nPress - for Substraction\nPress * for multiplication\nPress / for Division\nPress % for remainder")

    o = input("Enter Operation To Perform:")

    match o:
        case "+":
            print(f"The Addition is {a+b}")
        case "-":
            print(f"The Substraction is {a-b}")
        case "*":
            print(f"The Multiplication is {a*b}")
        case "/":
            print(f"The Division is {a/b}")
        case "%":
            print(f"The Remainder is {a%b}")
        case default:
            print("Invalid Input....")
except Exception as e:
    print("Please, Enter The Valid Number....")