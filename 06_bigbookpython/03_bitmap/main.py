import sys

bitmap = '''
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
'''

message = input('> ')
if message == '':
    sys.exit()

nook = '''The 
splitting
is 
done 
at 
line 
breaks.'''

# x = nook.splitlines()
# print(x)

for line in nook.splitlines():      # dzieli stringa na poszczególne linie o ile jak w naszym przykładzie są w nim entery
    for i, bit in enumerate(line):  # pętla przechodząca przez każdy znak w linii
        if bit == ' ':
            print(' ', end='')      # end='' nie kończy print() w nowej linii.
        else:
            print(message[i % len(message)], end='')
    print()

# print('Nook', end='')
# print('17', end='')