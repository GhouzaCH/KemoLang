import json
import re
import os
st=open("setting.json","r")
stdata=json.load(st)
import warnings
if stdata["pyerrmes"]==0:
	warnings.filterwarnings('ignore')
program=open(stdata["filelist"]+os.environ.get('fltlfile')+".fltl","r").readlines()
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
					print("計算エラー または 型エラー")
					print("計算が間違っているか、型が間違っている可能性があります。")
					exit()
	elif "if" in program[b]:
		equal=re.sub(r'\d','',program[b].replace("if ",""))
		iaf=program[b].replace("if ","").split("=")
		if int(iaf[0])==int(iaf[1]):
			print("True")
		else:
			print("False")
	elif "?" in program[b]:
		variab=program[b].replace("?","").split("=")
		os.system(variab[0]+"="+variab[1])
		print(variab[0]+"="+variab[1])
		os.system("echo "+"\"$"+variab[0]+"\"")
	else:
		if(program!=""):
			if(stdata["errmessage"]==1):
				print("構文エラー")
				print("構文が間違っています。")
				exit()
			
			
	b=b+1

print("OK")
