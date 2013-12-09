#!/usr/bin/python
# -*- coding: utf-8 -*-

__VERSION__ = '0.2'
__AUTHOR__ = 'Galkan'
__DATE__ = '03.12.2013'


try:
	from lib.main 	import Main
except ImportError,e:
  	import sys
  	sys.stdout.write("%s\n" %e)
  	sys.exit(1)

##	
### Main ...
##

if __name__ == '__main__':

	main = Main()
	main.run()
