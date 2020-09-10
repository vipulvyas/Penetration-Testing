count = 0
import sys
with open(sys.argv[1],"r") as f:
	
	for f.readline in f:
		
		for i in f.readline:
			
			if (i=='0'):
				print("f",end="")
			if (i=='1'):
				print("e",end="")
			if (i=='2'):
				print("d",end="")
			if (i=='3'):
				print("c",end="")
			if (i=='4'):
				print("b",end="")
				
				
			if (i=='5'):
				print("a",end="")
			if (i=='6'):
				print("9",end="")
			if (i=='7'):
				print("8",end="")
			if (i=='8'):
				print("7",end="")
			if (i=='9'):
				print("6",end="")
			if (i=='a'):
				print("5",end="")
			if (i=='b'):
				print("4",end="")
			if (i=='c'):
				print("3",end="")
			if (i=='d'):
				print("2",end="")
			if (i=='e'):
				print("1",end="")
			if (i=='f'):
				print("0",end="")
			count +=1
			#print(count,end=":::")
			if (count % 3== 0):
				print("",end=" ")	
		print("")
			

