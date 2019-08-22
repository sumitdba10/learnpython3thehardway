def cheese_and_cracker(cheese_count,boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for party!")
    print("Get a blanket.\n")



print("We can just give the function numbers directly:")
cheese_and_cracker(10,20)

print("Or, We can use variables from our script:")
amount_of_cheese =  30
amount_of_cracker = 40
cheese_and_cracker(amount_of_cheese,amount_of_cracker)


print("We can even do math inside: ")
cheese_and_cracker(10+12,12+10)


print("We can combine two, variable and math")
cheese_and_cracker(amount_of_cheese+20,amount_of_cracker+100)

print("We can create a conditional function")
def riches(cash):
    if cash >=0 and cash <=100000:
        print(f"So you've got ${cash}. It's good that you're saving but work hard and save more. Next milestone is thousandlliare, not a word but just made it.")

    elif cash >=500000 and cash<=999999:
        print(f"So you've got ${cash}. Good Job! Keep growing. You're towards milestone of millionarre.")
    elif cash >=1000000 and cash<=9999999:
        print(f"So you've got ${cash}. Wooh! you're a millionare. Love to date with you.")
    elif cash >=1000000000 and cash<=9999999999:
        print(f"So you've got ${cash}. You're a billioniarre, what to say? you've already got it.")
    else:
        print(f"So you've got ${cash}. You're a trillionare or bigger, what to say? you must be a prince or a king .... wooooow.")
riches(int(input("How much money you've got? ")))
