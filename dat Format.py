#Basically to control

print("{}".format(42))
print("{}".format("Hello World"))
print("{}".format(10.0119))

print("{} {} {}".format(42, "Hello World", 10.0))
print("{:.1}".format("Ghetto World"))

print("{:.3}".format("Wazza"))
print("{:.4} {:.2}".format("Rainbow","Eric"))
name = "Erinphant"
card = "1234567890"
print("{:.4} {:.3}".format(name,card))
print("Your initial is {:.4} and your number is {:.3}".format(name,card))

name = input("What is your name? ")
card = input("What is your card number? ")
print("Your initial is {:.4}".format(name))
print("Your number is {:.3}".format(card))
print("Finish")