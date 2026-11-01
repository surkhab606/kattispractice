# if you want to take in multiple inputs that are separated by a space, 
# you can use the following code.
# what this does is it takes in two integers from the user input, 
# separated by a space, and assigns them to the variables c and n. 
# The map function applies the int function to each of the inputs, 
# converting them from strings to integers.
c, n = map(int, input().split()) 
