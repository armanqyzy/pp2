<<<<<<< HEAD
#Print i as long as i is less than 6.
i = 1
while i < 6:
  print(i)
  i += 1


#Stop the loop if i is 3.
i = 1
while i < 6:
  if i == 3:
    break
  i += 1


#In the loop, when i is 3, jump directly to the next iteration.
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


#Print a message once the condition is false.
i = 1
while i < 6:
  print(i)
  i += 1
else:
=======
#Print i as long as i is less than 6.
i = 1
while i < 6:
  print(i)
  i += 1


#Stop the loop if i is 3.
i = 1
while i < 6:
  if i == 3:
    break
  i += 1


#In the loop, when i is 3, jump directly to the next iteration.
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


#Print a message once the condition is false.
i = 1
while i < 6:
  print(i)
  i += 1
else:
>>>>>>> 2708418ee5d55357d960df885d63c2d111776b36
  print("i is no longer less than 6")