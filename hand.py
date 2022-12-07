"""
fw = open('filedikxya.txt','w+')
fw.write("dikxya rana")
fw.writelines("\niam learning file handling \n using multiline \n this time")
fw.close()
"""
fo = open('filedikxya.txt','r+')
print(fo.read())
fo.close()
