#Practices:
#==========

print("Boolean Logic Expressions\n =======================")
print("Logic","<------>","Result")


print("True and True :",True and True)

#True

print("False and True:",False and True)

#False

print("1 == 1 and 2 == 1:",1 == 1 and 2 == 1)

"""True and False
    False """

"test" == "test"

#True

print("1 == 1 or 2 != 1:",1 == 1 or 2 != 1)

"""    True or True
    True """

print("True and 1 == 1:",True and 1 == 1)

#True

print("False and 0 != 0:",False and 0 != 0)

#False and False
#False

print("True or 1 == 1:",True or 1 == 1)

"""    True or True
    True """

"test" == "testing"

#False

print("1 != 0 and 2 == 1:",1 != 0 and 2 == 1)

"""    True and False
    False """

"test" != "testing"

#True

print('"test" == 1:',"test" == 1)

#False

print("not (True and False):",not (True and False))

"""not(False)
True"""

print("not (1 == 1 and 0 != 1):",not (1 == 1 and 0 != 1))

"""not(True and True)
False"""

print("not (10 == 1 or 1000 == 1000):",not (10 == 1 or 1000 == 1000))

#    """ not(False or True)
#    not(True)
#    False """
# error:  """not(False or True)
#    ^
#IndentationError: unexpected indent
print("not (1 != 10 or 3 == 4):",not (1 != 10 or 3 == 4))

"""not(True or False)
    not(True)
False"""

print("not (\"testing\" == \"testing\" and \"Zed\" == \"Cool Guy\"):",not ("testing" == "testing" and "Zed" == "Cool Guy"))

"""not(True and False)
    not(False)
    True"""

print("1 == 1 and (not (\"testing\" == 1 or 1 == 0):",1 == 1 and (not ("testing" == 1 or 1 == 0)))

"""True and (not(False or False))
    True and (not(False))
    True and True
    True"""

print("\"chunky\" == \"bacon\" and (not (3 == 4 or 3 == 3):","chunky" == "bacon" and (not (3 == 4 or 3 == 3)))

"""False and (not(False or True))
    False and (not(True))
    False and False
    False"""

print("3 == 3 and (not (\"testing\" == \"testing\" or \"Python\" == \"Fun\":",3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))

"""True and (not(True or False))
    True and (not(True))
    True and False
    False"""
