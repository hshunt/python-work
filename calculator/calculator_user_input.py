
def calculate_user_input(num_1=0, operator="", num_2=0):

    print("Please input a number: ")
    num_1=int(input())

    print("Please input an operator: ")
    operator=input()

    print("Please input a number: ")
    num_2=int(input())

    if operator=="*":
        result=num_1*num_2
        print(f"Your result is: ",result)

calculate_user_input()


