# assumptions - cannot be a party over 20 people
# there should be at most 999 tickets

def isRowFilled(row, count):
	c = int(count)
	latestOne = 0
	for i in range(len(row)):
		if row[i] != 0:
			latestOne = i
	if latestOne + c + 3 >= 20:
		return True
	return False

def assignPeople(row, count, t):
	c = int(count)
	latestOne = 0
	for i in range(len(row)):
		if row[i] != 0:
			latestOne = i
	for j in range(c):
		if latestOne == 0:
			row[j] = t
		else:
			row[latestOne + 4 + j] = t

def place(row, count, t):
	c = int(count)
	aval = []
	for i in range(len(row)):
		if row[i] == 0:
			aval.append(i)
			if len(aval) == c:
				break
		else:
			aval = []
	if len(aval) < c:
		return False
	for i in aval:
		row[i] = t
	return True

def assignLocation(seating, count, ticket):
	t = int(ticket[1:])
	rowOrder = [4, 5, 6, 3, 2, 7, 8, 1, 0, 9]
	for i in rowOrder:
		if not isRowFilled(seating[i], count):
			assignPeople(seating[i], count, t)
			# print(ticket + " seated at row", i, "with buffers")
			return
	for j in rowOrder:
		if place(seating[j], count, t):
			# print(ticket + " seated at row", j, "withOUT buffers")
			return
	# print("The movie theater is full; " + ticket + " cannot be seated")

def rowLet(n):
	letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
	return letter[n]

seating = [[0 for i in range(20)] for j in range(10)]
seatDict = dict()

with open('test.txt') as f:
	lines = f.readlines()

output = open('out.txt', 'a')

for line in lines:
	l = line.strip().split(' ')
	ticket, count = l[0], l[1]
	assignLocation(seating, count, ticket)

for line in lines:
	l = line.strip().split(' ')
	ticket, count = l[0], l[1]
	t = int(ticket[1:])
	for row in range(len(seating)):
		for seat in range(len(seating[0])):
			if seating[row][seat] == t:
				lst = [ticket, rowLet(row) + str(seat + 1)]
				if ticket in seatDict:
					seatDict[ticket].append(lst[1])
				else:
					seatDict[ticket] = []
					seatDict[ticket].append(lst[1])

for line in lines:
	l = line.strip().split(' ')
	ticket, count = l[0], l[1]
	if ticket not in seatDict:
		seatDict[ticket] = []

for tick in seatDict:
	lst = [tick]
	lst.append(' ')
	for seat in seatDict[tick]:
		lst.append(seat)
		if seat != seatDict[tick][-1]:
			lst.append(",")
	lst.append('\n')
	output.writelines(lst)

# for row in seating:
# 	print(row)

f.close()
output.close()