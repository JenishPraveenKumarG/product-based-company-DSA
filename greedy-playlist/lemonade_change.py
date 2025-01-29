def lemoade_change(bills):
    five = ten = 0
    for i in range(len(bills)):
        if bills[i] == 5:
            five+=1
        elif bills[i] == 10:
            ten+=1
            if five:
                five-=1
            else:
                return False
        else:
            if ten and five:
                ten-=1
                five-=1
            elif five > 3:
                five-=3
            
            else:
                return False
    return True

bills = [5,5,5,10,20]
print(lemoade_change(bills))

# TC - O(n)
# SC - O(1)