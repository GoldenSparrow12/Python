from array import *

vals=array( 'i', [25,21,6,8,74] )

for i in range(0,len ( vals ) ):
        for j in range(i+1, len ( vals )):
                if( vals[i] > vals[j] ):
                        vals[i] , vals[j] = vals[j] , vals[i]



for i in vals:
        print ( i, end=" " )
