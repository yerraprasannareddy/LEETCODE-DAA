def lemonadeChange(bills):
    five = 0
    ten = 0
    
    for bill in bills:
        if bill == 5:
            
            five += 1
        elif bill == 10:
            
            if five > 0:
                five -= 1
                ten += 1
            else:
                return False
        else:   
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    
    return True
 
bills = [5, 5, 5, 10, 20]
result = lemonadeChange(bills)
print(f"Can provide correct change for all customers: {result}")
