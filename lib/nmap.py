__VERSION__ = '0.2'
__AUTHOR__ = 'Galkan'
__DATE__ = '03.12.2013'


try:
	import sys
	import re
	import os
	import tempfile
	import subprocess
	from lib.common import *
except ImportError,e:
        import sys
        sys.stdout.write("%s\n" %e)
        sys.exit(7)


class Nmap:

        def __init__(self):
                self.nmap = "/usr/bin/nmap"
                self.port_is_open_reg = re.compile("Host:\s([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\s\(\)\s+Ports:\s(80|443)/open/tcp//http")

		if not os.path.exists(self.nmap):
			print bcolors.OKBLUE + "Error: " + bcolors.ENDC + bcolors.FAIL + "%s: File Doesn\'t Exist On The System !!!"% (self.nmap) + bcolors.ENDC
                        sys.exit(8)


        def port_scan(self, ip_list):
                result = []

                nmap_result_file = tempfile.NamedTemporaryFile(mode='w+t')
                nmap_result_file_name = nmap_result_file.name

                nmap_scan_option = "-n -PN -sT -T4 --open -p 80,443 --host-timeout=10m --max-rtt-timeout=600ms --initial-rtt-timeout=300ms --min-rtt-timeout=300ms --max-retries=2 --min-rate=150 %s -oG %s"% (ip_list, nmap_result_file_name)
                run_nmap = "%s %s"% (self.nmap, nmap_scan_option)

                proc = subprocess.Popen([run_nmap],
                        shell=True,
                        stdout=subprocess.PIPE,
                        )

                stdout_value = str(proc.communicate())

                nmap_result_file.seek(0)
                for line in nmap_result_file:
                        if re.search(self.port_is_open_reg, line):
                                host = re.search(self.port_is_open_reg, line).group(1)
                                result.append(host)


                nmap_result_file.close()
                if result:
                        return result
                else:
                        return None
