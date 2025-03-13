

print ("これは簡単な計算機です")
x = int(input("最初の数字は？"))
y = int(input("次の数字は？"))

ope = int(input("何をする？\n1.足し算\n2.引き算\n3.掛け算\n4.割り算\n"))

if ope == 1:
  z = x+y
  
elif ope == 2:
  z = x-y

elif ope == 3:
  z =x*y

elif ope == 4:
  if y == 0:
   print("0で割ることはできないよ")
   exit()
  else :
   z=x/y

else :
 print ("その操作には対応していないよ")

print("結果=",z)


    