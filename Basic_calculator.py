print('STEP 1: Enter the opertor (+ ,- ,* ,/)  \nSTEP 2: Enter first number \nSTEP 3: Enter the second number')


def oper_ations():
    global out_put
    oper=(input('OPERATOR :'))
    while True:
        if oper not in ('+','-','*','/'):
            print('Please enter any of the below operator')
            print('+,-,*,/')
            oper=(input('OPERATOR :'))    
        try:
            num1=int(input('FIRST NUMBER :'))
            num2=int(input('SECOND NUMBER :'))
        except ValueError:
            print('Enter integer only ')
            continue
        break
        
    if oper== '+':
        out_put= num1+num2
        print('RESULT: ',out_put)

    elif oper=='-':
        out_put= num1-num2
        print('RESULT: ',out_put)

    elif oper=='*':
        out_put= num1*num2
        print('RESULT: ',out_put)
    
    elif oper=='/': 
        out_put= num1/num2
        print('RESULT: ',out_put)
        
def repeat():
    global out_put
    oper=(input('OPERATOR :'))
    while oper not in ('+','-','*','/'):
        print('Please enter any of the below operator')
        print('+,-,*,/')
        oper=(input('OPERATOR :'))    
    num2=int(input('SECOND NUMBER :'))

    
    
    if oper== '+':
        out_put= out_pt+num2
        print('RESULT: ',out_put)

    elif oper=='-':
        out_put= out_pt-num2
        print('RESULT: ',out_put)

    elif oper=='*':
        out_put= out_pt*num2
        print('RESULT: ',out_put)
    
    elif oper=='/': 
        out_put= out_pt/num2
        print('RESULT: ',out_put)
        
    
    
    
def calculation():
    global out_pt
    out_pt=out_put
    condition='C'
    while True:
        condition=input('Press Enter to continue or S to stop :')
        if len(condition)==0:
            repeat()
        elif condition=='S':
            print('RESULT: ',out_put)
            print('THATS THE FINAL RESULT .BYE BYE ☺ ')
            break
            
oper_ations()
calculation()
