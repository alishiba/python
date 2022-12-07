print(lines)
#print(line1)
#line2 = fp.readline()
#print(line2)
#print("Length: ",len(lines))

print("Tell : ",fp.tell()) #position show
print("Seeking :", fp.seek(11)) #cursor..position ..placing
print("Tell :", fp.tell())
print("Seeking :", fp.seek(16)) 
print("Tell :", fp.tell())

#print(fp.read())
#print(fp.readlines())

fp.close()


#Writing files: create and write
fw = open('/filetest.txt','w+')
fw.write("Testing Writing to Files")
fw.writelines("\nTesting Writing to Files again and \n using multiline \n this time")
fw.close()


"""#check file is empty then append
fo = open(os.path.dirname(os.path.abspath(__file__))+'/filetest.txt','a+')
fo.write("\n ##am appending to file now")
fo.write("\n ##APPENDED Content!") #position 61 insert? TASK2#
fo.close()


#inserting content in between!
fo = open(os.path.dirname(os.path.abspath(__file__))+'/filetest.txt','r+')
fo.seek(200)
fo.write("\n ##Inserting using read+ mode## -- ") #position 61 insert? TASK2#
fo.seek(0)
print(fo.read())
fo.close()"""
