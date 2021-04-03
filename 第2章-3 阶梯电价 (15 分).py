quantity=float(input())
if quantity>=0 and quantity<=50:
    print("cost = %.2f"%(quantity*0.53))
elif(quantity>50):
    print("cost = %.2f"%(50*0.53+(quantity-50)*0.58))
else:
    print("Invalid Value!")