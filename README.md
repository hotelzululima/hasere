HASERE
================

Hasere is a tool that can discovery the virtual hosts and related filetype using google and bing search engines. Optionally, it uses the nmap to determine the ip addresses which have 80 or 443 opened port. After that it uses the bing search engine to determine which domains were hosted or have been hosted on this ip address. Finally, it search the filetype which was confiured via filetype_path parameters for this domain. So you can discovery the hole for your web pentesting easily.

Install the needed libraries:

    # apt-get install python-setuptools  
    # wget https://github.com/pkrumins/xgoogle/archive/master.zip
    # cd xgoogle-master
    # python setup.py install
    
Usage;

     -s : Subnet Information
     -t : Timeout Value
     -f : FileType
     -n : Use nmap (optional)
     
     
    # cat data/filetype
    php
    asp
    
    # ./hasere.py -s 85.111.27.88/32 -t 2 -f data/filetype 
    Ip Address:                      Host_Name:                    Google_Output:
    -----------                      ----------                    --------------
    85.111.27.88			         www.milliyet.com.tr		   ---
    85.111.27.88			         www.milliyet.com.tr		   www.milliyet.com.tr/ozel/edebiyat/forum/form.asp
 
    if you want to determine which ip addresses have opened port 80 or 443, use -n option.
 
    # ./hasere.py -s 85.111.27.88/32 -t 2 -f data/filetype 
    Ip Address:                      Host_Name:                    Google_Output:
    -----------                      ----------                    --------------
    85.111.27.88			         www.milliyet.com.tr		   ---
    85.111.27.88			         www.milliyet.com.tr		   www.milliyet.com.tr/ozel/edebiyat/forum/form.asp
 
 
NOTE: It was tested on Kali Linux.
