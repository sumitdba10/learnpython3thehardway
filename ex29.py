# assigning the variables
hot = 20
cold = 30
rain = 15

# if condition, if it's true and the next argument will be printing or executing
if hot < cold:
    print("Already, Winter is coming")

if hot > cold:
    print("Ahh, It's still, open the rooftop and have a ride")

if hot < rain:
    print("Let's have a coffee, It's already pouring")

if hot > rain:
    print("Although it may be raining or it's gonna be cold sooner, but for now enjoy summer time")

# "increment by" operator 
rain += 5

if hot >= rain:
    print("It's more hotter than raining")

if hot <= rain:
    print("It's more raining than hot summer")


if hot == rain:
    print("hot as well rain, wow!")
