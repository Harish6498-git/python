x = True
y = False

and_result = x and y
or_result = x or y
not_result_x = not x
not_result_y = not y

print("x and y:", and_result) # x and y: False
print("x or y:", or_result) # x or y: True
print("not x:", not_result_x) # not x: False
print("not y:", not_result_y) # not y: True


# And operator --> if any operand is false then the result will be false expect both operands are true the result is true
# Or operator --> if any operand is true then the output is true except if both operands are false the output will be false
# Not operator --> it return the opposite boolean value of the operand like if the operand is true the output will be false