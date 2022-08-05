string = range(0,11,2)
print(string)
print(string.__sizeof__())
su=0
for j in string:
    su=su+j.__sizeof__()
    print(j)

print(su)