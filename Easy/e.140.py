#!/usr/bin/env python

def var_notation():
    running = True

    while running:
        mode = raw_input('>')
        vname = raw_input('>').split() 
        
        if mode == '0':
            print vname[0] + ''.join([w.capitalize() for w in vname])
        elif mode == '1':
            print '_'.join(vname)
        elif mode == '2':
            print '_'.join(w.upper() for w in vname)           
        else:
            print 'mode must be in range(0,3)'

        print ''
    
var_notation()

