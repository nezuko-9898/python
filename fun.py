#function
def my():
    print('pravin')
my() 

#one arg
def my1(nmae):
    print(nmae,'morning')

my1('mr')

#two arg

def my2(name,gretitude):
    print(name+' '+gretitude)
my2('naruto','good morning')    


#*arg
def my4(*name):
    print("hello my name is"+' '+name[2])
my4('naruto','nezuko','tanjiro')    


#**kwarg
def my5(**name):
    print('His Last name is '+' '+name['lnmae'])

my5(lnmae='morning',fnmae='star')