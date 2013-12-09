__VERSION__ = '0.2'
__AUTHOR__ = 'Galkan'
__DATE__ = '03.12.2013'

try:
        import sys
	import re
	import os
        import argparse
	from lib.bing import Bing
	from lib.googlesearch import Google
	from lib.common import *
except ImportError,e:
        import sys
        sys.stdout.write("%s\n" %e)
        sys.exit(2)



class Main:

	def __init__(self):

		parser = argparse.ArgumentParser(description='Hasere ...')
        	parser.add_argument('-s','--subnet', help='Subnet Information', required=True)
        	parser.add_argument('-t','--timeout', help='Timeout Value', required=True)
        	parser.add_argument('-f','--filetype_path', help='Filetype_Path', required=True)
		parser.add_argument('-n', '--nmap', action = 'store_true', dest = 'nmap', default=False)
        	self.args = parser.parse_args()

		cidr_reg = re.compile("^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/([1-9]|[1-2]\d|3[0-2])$")
                
		if not os.path.exists(self.args.filetype_path):
                	print >> sys.stderr,  bcolors.OKBLUE + "Error : " + bcolors.ENDC + bcolors.FAIL + "%s: File Doesn\'t Exist On The System !!!"% (self.args.filetype_path) + bcolors.ENDC
                        sys.exit(3)

                if not ( re.search(cidr_reg, self.args.subnet) ):
                	print >> sys.stderr,  bcolors.OKBLUE + "Error : " + bcolors.ENDC + bcolors.FAIL + "Wrong Ip Usage <ip_adress/subnetmask>" + bcolors.ENDC
                        sys.exit(4)


	def print_results(self, ip_list):
		"""
			Show Results
		"""

		google = Google()
		bing = Bing()

        	ip_url = {}
                for ip in ip_list:
                	result = bing.get_result(ip, self.args.timeout)
                        if result:
                        	ip_addr = result[0]
                                url = result[1]
                                ip_url[ip_addr] = url

                file_type_list = []
                for f_type in open(self.args.filetype_path, "r"):
                	if not f_type in file_type_list:
                        	file_type_list.append(f_type)

                google.google(ip_url, file_type_list)


	def run(self):
		"""
			Main function ...
		"""

		if self.args.nmap:
			try:
        			from lib.nmap import Nmap
			except ImportError,e:
        			import sys
        			sys.stdout.write("%s\n" %e)
        			sys.exit(2)

                	nmap = Nmap()
                	nmap_result = nmap.port_scan(self.args.subnet)

	               	if nmap_result:
				self.print_results(nmap_result)
                	else:
				print >> sys.stderr,  bcolors.OKBLUE + "Warning : " + bcolors.ENDC + bcolors.FAIL + "Nmap Scan is not completed succesfully !!!" + bcolors.ENDC
                        	sys.exit(5)
		else:
			try:
				from lib.iprange import IpRange
                        except ImportError,e:
                                import sys
                                sys.stdout.write("%s\n" %e)
                                sys.exit(2)

			iprange = IpRange()
			ip_list = []
			for ip in iprange.iprange(self.args.subnet):
				ip_list.append(ip)

			self.print_results(ip_list)			
