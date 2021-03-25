
def calculate(*args):
    argument_order= {}
    n=0
    n_n=0
    result=0
    prev_num=0
    prev_result=0

    for arg in args:
            argument_order[n]=arg
            n+=1

    for nums in argument_order:

        if argument_order[nums]=="*":
            next_num=nums+1
            prev_num=nums-1
            n_n=argument_order[next_num]
            p_n=argument_order[prev_num]

            if nums>1:
                p_n=prev_result

            result=p_n*n_n

            print(result)
            prev_result=result

        elif argument_order[nums]=="/":
            next_num=nums+1
            prev_num=nums-1
            n_n=argument_order[next_num]
            p_n=argument_order[prev_num]

            if nums>1:
                p_n=prev_result

            result=p_n/n_n
            
            print(result)
            prev_result=result
        
        elif argument_order[nums]=="+":
            next_num=nums+1
            prev_num=nums-1
            n_n=argument_order[next_num]
            p_n=argument_order[prev_num]

            if nums>1:
                p_n=prev_result

            result=p_n+n_n

            print(result)
            prev_result=result
        
        elif argument_order[nums]=="-":
            next_num=nums+1
            prev_num=nums-1
            n_n=argument_order[next_num]
            p_n=argument_order[prev_num]

            if nums>1:
                p_n=prev_result
            
            result=p_n-n_n

            print(result)
            prev_result=result
        
        


calculate(2, "-", 2, "*", 5,"+",10,"/", 5, "*", 100 )
