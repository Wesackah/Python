x = input('naam')
y = input('beginstation')
z= input('eindstation')
invoerstring = x + y + z

def code(invoerstring):
    for i in invoerstring:
        print(chr(ord(i)+3), sep ='', end = '')

code(invoerstring)