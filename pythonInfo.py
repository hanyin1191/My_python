#python 
'''----------------------'''
print("must need the () when using the print")				#python3 

get_input = input("please input :")
get_input = raw_input("pliease input :")  	#python3 combine the /row_input and /input as input,
											#to return a string type always.

isinstance(variable,int)
isinstance(variable,str)				#Type check by /isinstance, type include: int,float,list,str,
										#tuple,dict,set.	return a bool type(True or False).
										#Consider inheritance.
type(variable) 
type(variable) == type(type)			#Type check by /type, return the type of the variable.
										#Don't consider inheritance.

"Good {}, my name is {}".format("morning","hanyh")						#the /format output by position
"{1} morning, my name is {0}, {1} bye".format("hanyh","good") 			#and the position can use any times.

"good {time}, my name is {name}".format(time = "morning",name = "han")	#the /format output by Keyword.

"{: >10}".format("hello")												#the /format other use.
"{:.5f}".format(1/3)
"{:,}".format(123456789)
"{:o}".format(34)
												
person = ['hanyh',21]													#the /format use.
"I am {0[0]}, age:{0[1]}".format(person)
age = [25,38,30]
"I am {0[0]}, and after four years my age: {1[0]}".format(person,age)

print("%.3e" % 12345.6)					#12345.6 rewrite to 1.234e+04.

for i in range(0,6):
	print(i,end = " ")					#Don't Warp when using the print, like 0 1 2 3 4 5. 
										#default print is Warp.

'''------------------------'''			#some operations for operate the files.

with open(r'C:/User/hanyh/Desktop/...','mode',True/False) as file1:		#'r','w','a','+','b', the default is 'r'.
	do_something(files)													#the usual files are text files,but python need 'b' to
																		#operate binary files like sounds files or image files.
																		#类文件对象是支持一些file类方法的对象（read/write),有时又称为流。

file1.read()		# There is a parameter indicating the number of bytes(1 byte = 8 bit). 
file1.readable()	#if read or not read.return True or False.

file1.readline()	#read the alone line.
file1.readlines()	#read all lines and return a list include all lines.

file1.write()		#exemple: file1.write("hello",encode(encoding = "utf-8"))
file1.writelines()	#需要一个字符串列表作为参数（实际上任何序列或者可迭代的对象都行），它会把所有的字符串写入文件（或流）。
					#程序不会增加新行，需要自己添加。

import fileinput						#using fileinput achieve the lazy line iteration.
for line in fileinput.input(file1):
	process(line)

for line in open(filename):				#using file iterator.
	process(line)

file1.flush()		
file1.truncate()

file1.seek()		#seek(offset[, whence])	the default whence is 0, represent the head of file.
					#whence also can choose 1 or 2.
file1.seekable()	#if seek or not seek. return True or False.
file1.tell()		#return the current file location, usual is a long int type, but not always. 

file1.close()		#close the file.

file1.encoding		#see the encoding of the file.

with open(r"C:/Users/hanyh_/Desktop/test.txt","r+",encoding = 'utf-8') as file1:		#also need a encoding parameter.
    code = file1.encoding

file1.name			#the path and name of file like"C:/Users/hanyh_/Desktop/test.txt"

'''----------------------------'''		#several encode and decode.
'''
	ASCII码（127个含有大小写字母、数字和一些符号的字符编码成对应的0-1代码，
每个字符用一个字节（byte）来表示）
	Unicode码（通过扩充字节来把全球的编码方案都添加到统一的一套方案中，
这套方案为Unicode编码方案，现为两个字节/16位）
	UTF-8码（Unicode Transformation Format-8，根据不同字符将对应Unicode码在
能唯一标识的条件下进行变短处理，使用1、2、3、4个字节表示所有的字符，在能唯一标识的
条件下，优先使用最小的字节表示某个字符）
	GB2312码（中文）、Shift-JIS（日语）、Euc-kr码（韩语）、TIS-620码（泰语）...
	
	#编辑文档--->使用Unicode码
	#存储和网络传输---->使用UTF-8码
	#在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者传输的时候，就转换为
“utf-8”编码。

	decode()  &  encode()


'''

len(u"how many charaters")			
len(b"hoow many bytes")			#bytes 类型可以是 ASCII范围内的字符和其它十六进
								#制形式的字符数据，但不能用中文等非ASCII字符。

ord('a')			#return the 'a' dex
chr(33)				#return the 33 '!'

'''----------------------------'''

x = lambda x,y : x*y
print(3,4)							#the use of lambda function.

def func(a, b):
	print(a*b)

x = map(func, [1,2,3], [3,4,5])
print(x)							#the use of map function.

def func(num):
	if(num % 2 == 0):
		return True
	else:
		return False

numbers = [1,2,3,4,5,6,7,8,9]
x = filter(func, numbers)
print(x)							#the use of filter function.

from itertools import *
def check_for_drop(x):
    print ("Checking:" , x)
    return (x < 5)					#return True or False.

for i in dropwhile(check_for_drop, [2,4,6,8,10,12]):
    print ("Result:" , i)								#the use of dropwhile function.
#itertools 模块中有一些函数可以完成这个任务。 首先介绍的是 itertools.dropwhile() 函数。
#使用时，你给它传递一个函数对象和一个可迭代对象。 它会返回一个迭代器对象，丢弃原有序列中直
#到函数返回Flase之前的所有元素，然后返回后面所有元素。


