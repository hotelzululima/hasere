HASERE
================

Hasere is a tool that can discovery the virtual hosts and related filetype using google and bing search engines. At first, it uses the nmap to determine the ip addresses which have 80 or 443 opened port. After that it uses the bing search engine to determine which domains were hosted or have been hosted on this ip address. Finally, it search the filetype which was confiured via filetype_path parameters for this domain. So you can discovery the hole for your web pentesting easily.

Install the needed libraries:

    # apt-get install python-setuptools  
    # wget https://github.com/pkrumins/xgoogle/archive/master.zip
    # cd xgoogle-master
    # python setup.py install
    
Usage;

     -s : Subnet Information
     -t : Timeout Value
     -f : FileType   

    # ./hasere.py -s X.X.X.X/24 -t 3 -f data/filetype
 
NOTE: It was tested on Kali Linux.
