from array import *

ne = array ('i', [] )
vals = array (ne.typecode, (a for a in ne)) 
n=int (input ("Enter The length Of The Array "))

for i in range(n):
        x=int ( input ("Enter the element") )
        vals.append( x )

for i in range(n):
        for j in range(i+1):
                if ( vals[i] < vals[j] ):
                        vals[i] , vals[j] =vals[j] , vals[i]
for i in vals:
        print ( i ,end = " " )        
