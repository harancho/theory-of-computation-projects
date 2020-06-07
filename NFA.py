
print("enter substring that contains no repeating character - ")
check=input()

print("enter the string to checked substring \"{}\" in it by the concept of NFA - ".format(check))
c=input()

check
sol=0

print("initial stage = 0")
print("final stage = ",end="")
print(len(check))

print(sol,end=" ")

for i in range(len(c)):
	if sol==len(check):
		break

	if c[i]==check[sol]:
		sol=sol+1
		print(sol,end=" ")
		continue

	if sol==1 and c[i]!=check[sol-1]:
		sol=0

	if sol!=1 and c[i]!=check[sol]:
		sol=0
	print(sol,end=" ")

if sol==len(check):
	print("\nyes")
else:
	print("\nno")




