import json
import re
import os
os.system("clear")
st=open("setting.json","r")
stdata=json.load(st)
import warnings
if stdata["pyerrmes"]==0:
	warnings.filterwarnings('ignore')
print("Hello!\nWelcome to けもラング 1.0.0beta")
print("1.コンパイルして実行")
print("2.サンプルを実行")
cmd=input("何する？:")
if cmd=="1":
	program1=input("コンパイル先ファイルを選んでください（拡張子無し）:")
	program=open(stdata["filelist"]+program1+".fltl","r").readlines()
if cmd=="2":
	program=open("sample/sample.fltl").readlines()
else:
	print("Error")
	exit()
b=0
for i in program:
	if "ctput" in program[b]:
		if "\"" in program[b]:
			os.system("echo "+program[b].replace("ctput ","").replace(";","").replace("\"","").replace("\n","").replace("#ent","\necho ").replace("#tab","\t"))
		else:
			if "+" in program[b]:
				plus=program[b].replace("ctput ","").replace("\n","").split("+")
				p=0
				for i in range(int(len(plus))):
					os.system("echo "+str(int(plus[p])+int(plus[p])))
					p=p+1
					if p!=len(plus):
						break
			elif "-" in program[b]:
				minus=program[b].replace("ctput ","").replace("\n","").split("-")
				for i in range(int(len(minus))):
					os.system("echo "+str(int(minus[0])-int(minus[1])))
					break
			elif "*" in program[b]:
				kake=program[b].replace("ctput ","").replace("\n","").split("*")
				for i in range(int(len(kake))):
					os.system("echo "+str(int(kake[0])*int(kake[1])))
					break
			elif "/" in program[b]:
				waru=program[b].replace("ctput ","").replace("\n","").split("/")
				for i in range(int(len(waru))):
					os.system("echo "+str(float(waru[0])/float(waru[1])))
					break
			else:
				if(stdata["errmessage"]==1):
					print("CalcErr")
	elif "if" in program[b]:
		equal=re.sub(r'\d','',program[b].replace("if ",""))
		if equal=="=":
			ifa=program[b].replace("if ","").split("=")
			if ifa[0]==ifa[1]:
				print("True")
			else:
				print("False")
	elif "?" in program[b]:
		variab=program[b].replace("?","").split("=")
		os.system(variab[0]+"="+variab[1])
		print(variab[0]+"="+variab[1])
		os.system("echo "+"\"$"+variab[0]+"\"")
	else:
		if(stdata["errmessage"]==1):
			print("SyntaxErr")
			
	b=b+1

print("OK")