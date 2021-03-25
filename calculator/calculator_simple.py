
def calculate(*args, add=False, subtract=False, multiply=False, divide=False):
    result=0
    prev_num=1

    if multiply==True:
        for arg in args:
            result=arg*prev_num
            print(result)
            prev_num = result

    elif divide==True:
        for arg in args:
            result=arg/prev_num
            print(result)
            prev_num = result

    elif subtract==True:
        for arg in args:
            result=arg-prev_num
            print(result)
            prev_num = result

    elif add==True:
        for arg in args:
            result=arg+prev_num
            print(result)
            prev_num = result
    
calculate(2, 2, 3, 6, 7, multiply=True)

