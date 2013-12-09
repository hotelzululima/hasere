HASERE
================

Hasere is a tool that can discovery the virtual hosts and related filetype using google and bing search engines. Optionally, it uses the nmap to determine the ip addresses which have 80 or 443 opened port. After that it uses the bing search engine to determine which domains were hosted or have been hosted on this ip address. Finally, it search the filetype which was confiured via filetype_path parameters for this domain. So you can discovery the hole for your web pentesting easily.

Install the needed libraries:

    # apt-get install python-setuptools  
    # wget https://github.com/pkrumins/xgoogle/archive/master.zip
    # cd xgoogle-master
    # python setup.py install
    # wget https://github.com/galkan/hasere/archive/master.zip
    # unzip master.zip
    # cd hasere-master
    # ./hasere.py -h
    
Usage;

     -s : Subnet Information
     -t : Timeout Value
     -f : FileType
     -n : Use nmap (optional)
     
     
    # cat data/filetype
    php
    asp
    
 
 if you want to determine which ip addresses have opened port 80 or 443, use -n option.
   
    # ./hasere.py  -s 209.92.24.80/28 -t 3 -f data/filetype -n
    Ip Address:                      Host_Name:                    Google_Output:
    -----------                      ----------                    --------------
    209.92.24.80			         www.linux.org		           ---
    209.92.24.80			         www.linux.org		           ---
    209.92.24.90			         www.fobusholster.com		   ---
    209.92.24.90			         www.fobusholster.com		   ---
    209.92.24.86			         www.couturecreations.net	   www.couturecreations.net/site/cart.php
    209.92.24.86			         www.couturecreations.net	   www.couturecreations.net/site/cart.php,        
    www.couturecreations.net/site/cart.php
    209.92.24.95			         www.mccaffreys.com		       www.couturecreations.net/site/cart.php,  
    www.couturecreations.net/site/cart.php, www.couturecreations.net/site/cart.php
 
    
 
NOTE: It was tested on Kali Linux.

--------------------------------------------------------------------------------------------------------------------------

WEB sizma testlerinin ilk adimi olarak hedef subnet bilgisi uzerinde barindirilan uygulamalarin tespit edilmesidir. Ardindan belirtilen dosya turune sahip url bilgileri tespit edilerek belirtilen subnet uzerindeki uygulamalarin tespit edilerek farkli girdi noktalarinin kesfedilmesidir. Secimlik olarak once nmap uygulamasi ile 80 veya 443 portu acik olan ip adres bilgisi icin kesif islemi gerceklestirilebilmektedir.

Kurulum icin oncelikle gerekli kutuphanelerin kurulmasi gereklidir. Bunun icin;
     
      # apt-get install python-setuptools  
      # wget https://github.com/pkrumins/xgoogle/archive/master.zip
      # cd xgoogle-master
      # python setup.py install

Kullanim icin;
      -s : Subnet Information
      -t : Timeout Value
      -f : FileType
      -n : Use nmap (optional)

      # cat data/filetype
      php
      asp

Ip adreslerinden 80 ve 443 portu acik olanlarin belirlenmesi icin -n parametresi kullanilabilir.
      
      # ./hasere.py  -s 209.92.24.80/28 -t 3 -f data/filetype -n
      Ip Address:                      Host_Name:                    Google_Output:
      -----------                      ----------                    --------------
      209.92.24.80                     www.linux.org                 ---
      209.92.24.80                     www.linux.org                 ---
      209.92.24.90                     www.fobusholster.com          ---
      209.92.24.90                     www.fobusholster.com          ---
      209.92.24.86                     www.couturecreations.net      www.couturecreations.net/site/cart.php
      209.92.24.86                     www.couturecreations.net      www.couturecreations.net/site/cart.php,        
      www.couturecreations.net/site/cart.php
      209.92.24.95                     www.mccaffreys.com            www.couturecreations.net/site/cart.php,  
      www.couturecreations.net/site/cart.php, www.couturecreations.net/site/cart.php


NOT: Kali Linux uzerinde test edilmistir. /32 ile tek bir ip adres bilgisi kullanilabilir.
