amt = int(input("Enter Price of Bike : "))

if amt > 100000:
    tax = amt * (15/100)
    insc = amt * (20/100)
    T_amt = amt + tax + insc
    print(f"""For Purchase of,\n Amount : {amt} \n Tax to be paid at rate of 15% amounting : {tax} \n Insurance to be paid at rate of 20% amounting : {insc} \n Total Amount to be paid : {T_amt}""")
elif  100000 >= amt > 50000 :
    tax = amt * (10/100)
    insc = amt * (8/100)
    T_amt = amt + tax + insc
    print(f"""For Purchase of,\n Amount : {amt} \n Tax to be paid at rate of 10% amounting : {tax} \n Insurance to be paid at rate of 8% amounting : {insc} \n Total Amount to be paid : {T_amt}""") 
elif 50000 >= amt:
    tax = amt * (5/100)
    insc = amt * (5/100)
    T_amt = amt + tax + insc
    print(f"""For Purchase of,\n Amount : {amt} \n Tax to be paid at rate of 5% amounting : {tax} \n Insurance to be paid at rate of 5% amounting : {insc} \n Total Amount to be paid : {T_amt}""")  
else:
    print("Somethig Went Wrong")