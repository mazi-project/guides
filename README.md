# INURA
guide of image INURA 


# Requirements 

* Raspberry pi
* mazizone_v1 image . You can download from these link http://nitlab.inf.uth.gr/mazi-guides/download.html

# Set up

**Download INURA code**                                                                                                           
                                                                                                                     
At  **/home/pi** directory                                                                                                     
**$ sudo git clone https://github.com/mazi-project/guides.git**                                                                 
Now you have all scripts from INURA image into the file **/INURA**                                                             
Rename it to  mazi                                                                                                             
**$ sudo mv /INURA /mazi**

**Run check.sh when a DHCP lease is created**                                                                                     
                                                                                                                               
Go to dnsmasq.conf file                                                                                                       
**$ cd  /etc/dnsmasq.conf**                                                                                                  
Add the follow code at line 541                                                                                                 
**hcp-script=/home/pi/mazi/check.sh**                                                                                           

**Make inot2.sh to run every time the system starts**                                                                             

Move internet-forward script to /etc/init.d directory                                                                         
**$ sudo mv internet-forward /etc/init.d**                                                                                   

Make it executable                                                                                                           
**$ chmod ugo+x /etc/init.d/internet-forward**                                                                               

Configure the init system to run this script at startup.                                                                     
**$ update-rc.d internet-forward defaults**


# Description

![inura](https://cloud.githubusercontent.com/assets/17981858/20176463/9360721e-a750-11e6-9b84-b40dd55cb143.png)
