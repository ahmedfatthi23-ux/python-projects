t = int(input('The total question in the test ') )

a = int(input('The total attempted questions ') )

if a > t:
    print('invalid input ')
    exit( )

c = int(input('The total correct questions ') )

if c > a:
    print('invalid input ')
    exit()

#overall accuracy
z = round(c / t * 100, 2)
#attempted accuracy
y = round(c / a * 100, 2)

print('your overall accuracy is', z)
print('your attempted accuracy is', y)

if z < 50:
    print('your accucary is bad you need to study more ')
elif z < 70:
    print('your accuracy is not so bad neither so good you still have to study hard')
elif z < 90:
    print('your accuracy is good but still need studying')
elif z > 90:
    print('your accuracy is fantastic keep it like that')