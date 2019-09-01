import sys
W='\033[0;47m'
B = '\033[94m'
ENDC = '\033[0m'
for x in open('challenge.txt','rb'):
   sp=x.split('+')
   for s in sp:  
     c=s[0]
     e=int(s[2:])
     if(c=='0'):
        sys.stdout.write(' '*e)
     else:
        sys.stdout.write('1'*e)
   print
