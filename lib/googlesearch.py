__VERSION__ = '0.3'
__AUTHOR__ = 'Galkan'
__DATE__ = '2014'


try:
	import re
	import time
	import urllib2
	import sys
	import socket
	import random
	from lib.common import *
except ImportError,e:
        import sys
        sys.stdout.write("%s\n" %e)
        sys.exit(12)


socket.setdefaulttimeout(30)

class Google: 

	def __init__(self):
		"""
			Define some variables related to googling ...
		"""

		self.google_url = "https://www.google.com/search?q="
		self.uas = [
                        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11',
                        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:17.0) Gecko/20100101 Firefox/17.0',
                        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/536.26.17 (KHTML, like Gecko) Version/6.0.2 Safari/536.26.17',
                        'Mozilla/5.0 (Linux; U; Android 2.2; fr-fr; Desire_A8181 Build/FRF91) App3leWebKit/53.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322; PeoplePal 6.2)',
                        'Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20100101 Firefox/13.0.1',
                        'Opera/9.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.01',
                        'Mozilla/5.0 (Windows NT 5.1; rv:5.0.1) Gecko/20100101 Firefox/5.0.1',
                        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 3.5.30729)'
      		      ]
		

	def extract_url(self, res_page, host, f_type):
		"""
			Extract urls from web page
		"""

		url_list = []
		url_reg = re.compile("<a href=\"https?://(%s[^\"]+\.%s)\" "% (host, f_type))
           	if re.findall(url_reg, res_page):
			for resp in re.findall(url_reg, res_page):
				url_list.append(resp)

		return url_list



        def google_search(self, host, f_type):
		"""
			Google Search with given keyword ...
		"""

		keyword = "site:%s+filetype:%s"% (host, f_type)
		url = self.google_url + keyword 
		user_agent = random.choice(self.uas)
		headers = {'User-Agent': user_agent}

		try:
			req = urllib2.Request(url, None, headers)
			page = urllib2.urlopen(req)
		except:
			pass

		random_interval = random.randrange(7, 12, 1)
		time.sleep(random_interval)
	
		if page.getcode() == 200:
			res_page = page.read()
			if res_page:
				return self.extract_url(res_page, host, f_type)
			else:
				return None
		else:
			print "Error : Fetching Url - %s"% url
			return None



        def google(self, ip_url, file_type_list):

                print  bcolors.OKBLUE + "Ip Address:                      Host_Name:                    Google_Output:" + bcolors.ENDC
                print  bcolors.FAIL  + "-----------                      ----------                    --------------" + bcolors.ENDC

                for ip in ip_url.keys():
			for host in ip_url[ip]:
                        	for _f_type in file_type_list:
                                	f_type = _f_type.split("\n")[0]
					resp = self.google_search(host, f_type)

					if resp:
						result_str = ""
						for res_host in resp:
							if not result_str:
								result_str = "%s : %s"% (f_type, res_host)
							else:
								result_str = result_str + "," + res_host
                                                print "%s\t\t\t%s\t\t%s"% (ip, host, result_str)
                                        else:   
                                                result_str = "---"
                                                print "%s\t\t\t%s\t\t%s : %s "% (ip, host, f_type, result_str)
