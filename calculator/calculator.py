

def calculate(*args, add=False, subtract=False, multiply=False, divide=False):
    argument_order= {}
    n=0
    result=0
    prev_num=1

    for arg in args:
        argument_order[n]=arg
        n+=1

    if multiply==True:
        for key in argument_order:
            result=argument_order[key] * prev_num
            print(result)
            prev_num = result

    elif divide==True:
        result=argument_order[0] / argument_order[1]
        print(result)

    elif subtract==True:
        result=argument_order[0] - argument_order[1]
        print(result)

    elif add==True:
        result=argument_order[0] + argument_order[1]
        print(result)
        
calculate(2, 2, 3, 6, 7, multiply=True)

