#3)
a = ["c","b","","a"]
b = ["c","a","b","a"]

score = 0

for i in range(len(a)):
    if a[i] == b[i]:
     score += 4
    elif a[i] == "" or b[i] == "":
       score += 0
    else:
       score -= 1

print(score)            


