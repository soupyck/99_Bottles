# GOAL
#
# Create a program that prints out every line to the song "99 bottles of beer on the wall."
# This should be a pretty simple program, so to make it a bit harder, here are some rules to follow.
#
# RULES
#
# If you are going to use a list for all of the numbers, do not manually type them all in. Instead, use a built in function.
#
# Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
#
# Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
# Put a blank line between each verse of the song.

i = 99
if i > 1:
    print i + " bottles of beer on the wall, " + i + " bottles of beer! Take one down, pass it around..."
    i = i - 1
    print i + "bottles of beer on the wall!"
elif i == 1:
    print i + "bottles of beer on the wall, " + i + " bottles of beer! Take one down, pass it around..." + i + "bottles of beer on the wall!"


