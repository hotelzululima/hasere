__VERSION__ = '0.3'
__AUTHOR__ = 'Galkan'
__DATE__ = '2014'



try:
	import sys
	import urllib2
	import re
	import tempfile
except ImportError,e:
        import sys
        sys.stdout.write("%s\n" %e)
        sys.exit(13)

		
class Bing:

        def __init__(self):
                """
                        Define regex
                """

                self.regex_url = re.compile("<h3><a href=\"http(s)?://([^/]+)")
                self.regex_count = re.compile("<span class=\"sb_count\" id=\"count\">([0-9]+)")


        def get_webpage(self, url, ip, count_or_data, timeout):
                """
                        Fetch web page and return url extracted
                """
                # count_or_data = 1 -> return count value

                result_list = []
                page_count = 30

                output_file = tempfile.TemporaryFile(mode='w+t')
               	web_page_url_1 = urllib2.Request(url)

		try:
			web_page_url_2 = urllib2.urlopen(web_page_url_1, timeout = int(timeout))
		except Exception,e:
			web_page_url_2.close()
			output_file.close()


                try:
                        page_result = str(web_page_url_2.read())
                except Exception,e:
                        output_file.close()
                        web_page_url_2.close()

                        return None


                output_file.writelines(page_result)
                web_page_url_2.close()


                output_file.seek(0)
                for line in output_file:
                        if count_or_data == 1:
                                if ( re.search(self.regex_count, line) ):
                                        page_count = re.search(self.regex_count, line).group(1)


                        result = re.findall(self.regex_url, line)
                        if result:
                                for res in result:
                                        if not res[1] in result_list:
                                                result_list.append(res[1])

                output_file.close()

		if count_or_data == 1:
                        return page_count, result_list
                else:
                        return result_list

	
	def get_result(self, ip, timeout):
               	"""
                       	Main function
               	"""

               	result = []
               	init_result = []
               	main_result = []

               	ip_regex = re.compile("^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$")
               	init_url = "http://www.bing.com/search?q=ip%3a" + ip + "&go=&qs=n&first=00&FORM=PERE"

		try:
                        page_count, init_result = self.get_webpage(init_url, ip, 1, timeout)

                        if page_count and init_result:
                                for tmp_res in init_result:
                                        if not tmp_res in main_result:
                                                if not re.search(ip_regex, tmp_res):
                                                        main_result.append(tmp_res)


                                if  int(page_count) % 10 == 0:
                                        for page in range(10, int(page_count) + 1, 10):
                                                url = "http://www.bing.com/search?q=ip%3a" + ip + "&go=&qs=n&first=" + str(page) + "&FORM=PERE"
                                                result = self.get_webpage(url, ip, 0, timeout)

                                                if result:
                                                        for tmp_res in result:
                                                                if not tmp_res in main_result:
                                                                        if not re.search(ip_regex, tmp_res):
                                                                                main_result.append(tmp_res)

                                else:
                                        total_page_count = (int(page_count) + ( 10 - (int(page_count) % 10)))

                                        for page in range(10, total_page_count + 1, 10):
                                                url = "http://www.bing.com/search?q=ip%3a" + ip + "&go=&qs=n&first=" + str(page) + "&FORM=PERE"
                                                result = self.get_webpage(url, ip, 0, timeout)

                                                if result:
                                                        for tmp_res in result:
                                                                if not tmp_res in main_result:
                                                                        if not re.search(ip_regex, tmp_res):
                                                                                main_result.append(tmp_res)
                                url_list = []
                                if main_result:
                                        for ip_domain in main_result:
                                                url_list.append(ip_domain)

                                        return ip,url_list

                        else:
                                return None
		except:
			pass

