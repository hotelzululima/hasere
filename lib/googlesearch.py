__VERSION__ = '0.2'
__AUTHOR__ = 'Galkan'
__DATE__ = '03.12.2013'


try:
	import re
	from lib.common import *
        from xgoogle.search import GoogleSearch
except ImportError,e:
        import sys
        sys.stdout.write("%s\n" %e)
        sys.exit(8)


class Google: 

	def __init__(self):
		self.per_page = 10000
		

        def google_search(self, keyword):

                search_keyword = keyword
                gs = GoogleSearch(search_keyword)
                gs.results_per_page = self.per_page
                results = gs.get_results()

                return results


        def google(self, ip_url, file_type_list):

                print  bcolors.OKBLUE + "Ip Address:                      Host_Name:                    Google_Output:" + bcolors.ENDC
                print  bcolors.FAIL  + "-----------                      ----------                    --------------" + bcolors.ENDC

                result_list = []
                result_str = ""
                for ip in ip_url.keys():
                        for _f_type in file_type_list:
                                f_type = _f_type.split("\n")[0]
                                keyword = "filetype:%s site:%s"% (f_type,ip_url[ip][0])

                                try:
                                        results = self.google_search(keyword)
                                        for _res in results:
                                                res =  _res.url.encode('utf8')
                                                hostname_reg = re.compile("https?://(.*%s)"% (f_type))

                                                if re.search(hostname_reg, res):
                                                        res = re.search(hostname_reg, res).groups(1)[0]
                                                        if not res in result_list:
                                                                result_list.append(res)

                                except Exception,e:
                                        print e.message
                                        pass


                                for host in result_list:
                                        if not result_str:
                                                result_str = host
                                        else:
                                                result_str = result_str + ", " + host

                                if result_str:
                                        print "%s\t\t\t%s\t\t%s"% (ip, ip_url[ip][0],result_str)
                                else:
                                        result_str = "---"
                                        print "%s\t\t\t%s\t\t%s"% (ip, ip_url[ip][0],result_str)
                                        result_str = ""

