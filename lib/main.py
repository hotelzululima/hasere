__VERSION__ = '0.3'
__AUTHOR__ = 'Galkan'
__DATE__ = '2014'

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
	"""	
		Main Class ...
	"""

	def __init__(self):

		parser = argparse.ArgumentParser(description='Hasere. Discover the virtual hosts ...')
        	parser.add_argument('-s','--subnet', help = 'Subnet Information', required = True)
        	parser.add_argument('-t','--timeout', help = 'Timeout Value', default = 3, required = False)
        	parser.add_argument('-f','--filetype_path', help = 'Filetype Path', required = True)
		parser.add_argument('-n', '--nmap', action = 'store_true', dest = 'nmap', default = False)

        	self.args = parser.parse_args()

		self.subnet_cidr_file = 0	
		self.filetype = 0	

		cidr_reg = re.compile("^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/([1-9]|[1-2]\d|3[0-2])$")
		filetype_reg = re.compile("^[a-zA-Z]+(,[a-zA-Z]+)*$")


		if (not re.search(filetype_reg, self.args.filetype_path)) and (not os.path.exists(self.args.filetype_path)):
			print >> sys.stderr, bcolors.OKBLUE + "Error : " + bcolors.ENDC + bcolors.FAIL + "File type must be FILE or FILE EXT - </tmp/file.txt | php,asp>"
                        sys.exit(3)

		if not re.search(filetype_reg, self.args.filetype_path):
			self.filetype = 1


                if (not re.search(cidr_reg, self.args.subnet)) and (not os.path.exists(self.args.subnet)):
			print >> sys.stderr, bcolors.OKBLUE + "Error : " + bcolors.ENDC + bcolors.FAIL + "Subnet must be CIDR or FILE - <192.168.1.0/24 | /tmp/subnet.txt>" + bcolors.ENDC
                        sys.exit(4)


		if not re.search(cidr_reg, self.args.subnet):
			subnet_file = open(self.args.subnet, "r").read().splitlines()
                        for subnet in subnet_file:
                        	if (not re.search(cidr_reg, subnet)):
                                	print >> sys.stderr,  bcolors.OKBLUE + "Error : " + bcolors.ENDC + bcolors.FAIL + "Subnet: %s - must be CIDR format - <192.168.37.0/24|192.168.37.37/32>"% (subnet) + bcolors.ENDC
                                        sys.exit(5)

			self.subnet_cidr_file = 1	



	def print_results(self, ip_list):
		"""
			Show Results
		"""

		# create instances for googling and binging ...
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
		if self.filetype == 1:
                	for f_type in open(self.args.filetype_path, "r"):
                		if not f_type in file_type_list:
                        		file_type_list.append(f_type)

                	google.google(ip_url, file_type_list)
		else:
			for f_type in  self.args.filetype_path.split(","):
				file_type_list.append(f_type)
			
                	google.google(ip_url, file_type_list)
		

	def run(self):
		"""
			Main function ...
		"""

		if self.args.nmap:
			try:
        			from lib.nmap import Nmap
				import sys
			except ImportError,e:
        			import sys
        			sys.stdout.write("%s\n" %e)
        			sys.exit(6)

                	nmap = Nmap()
			if self.subnet_cidr_file == 1:
				subnet_file = open(self.args.subnet, "r").read().splitlines()
     				for subnet in subnet_file:
                			nmap_result = nmap.port_scan(subnet)
	               			if nmap_result:
						self.print_results(nmap_result)
                			else:
						print >> sys.stderr,  bcolors.OKBLUE + "Warning : " + bcolors.ENDC + bcolors.FAIL + "Nmap Scan is not completed succesfully !!!" + bcolors.ENDC
                        			sys.exit(7)
			else:
                		nmap_result = nmap.port_scan(self.args.subnet)
	               		if nmap_result:
					self.print_results(nmap_result)
                		else:
					print >> sys.stderr,  bcolors.OKBLUE + "Warning : " + bcolors.ENDC + bcolors.FAIL + "Nmap Scan is not completed succesfully !!!" + bcolors.ENDC
                        		sys.exit(8)
		else:
			try:
				from lib.iprange import IpRange
				import sys
                        except ImportError,e:
                                import sys
                                sys.stdout.write("%s\n" %e)
                                sys.exit(9)

			iprange = IpRange()
			ip_list = []
			if self.subnet_cidr_file == 1:
                                subnet_file = open(self.args.subnet, "r").read().splitlines()
                                for subnet in subnet_file:
					for ip in iprange.iprange(subnet):
						ip_list.append(ip)

				self.print_results(ip_list)			
			else:
				for ip in iprange.iprange(self.args.subnet):
                                        ip_list.append(ip)

                                self.print_results(ip_list)	
