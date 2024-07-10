message = input("Enter your message : ")
words = message.split(" ")
print(type (words))
code = int(input(
    "If you want to code your message then press 1 if you want to de-code it then press 0. "))
if code == 1:
    nwords = []
    code1 = "abc"
    code2 = "xyz"
    for word in words:
        if (len(word) >= 3):
            code1 = "abc"
            code2 = "xyz"
            strnew = code1 + word[1:] + word[0] + code2
            nwords.append(strnew)
        else:
            nwords.append(word[1:] + word[0])
    print(" ".join(nwords))
elif code == 0:
    nwords = []
    for word in words:
        if (len(word) >= 3):
            strnew = word[3:-3]
            strnew = strnew[-1] + strnew[:-1]
            nwords.append(strnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    print("Somthing went wrong try again. :(")
