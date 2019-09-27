#Spencer Paquette 9/26/19
word = input("Word to be translated:")
vowels = ["a","e","i","o","u"]
if(word[0:1] in vowels):
    print(word + "yay")
else:
    print(word[1:] + word[0:1] + "ay")
