#coding=utf-8  
import socket  
import time  
import sys  
  
def portScanner(ip,port):  
	server = (ip,port)  
	sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
	sockfd.settimeout(0.1)  
	ret = sockfd.connect_ex(server)  #返回0则成功  
	if not ret:  
		sockfd.close()  
		print '%s:%s is opened...' % (ip,port)  
	else:  
		sockfd.close()  
		pass  
	return ''  
  
def ip2num(ip):  
	lp = [int(x) for x in ip.split('.')]  
	return lp[0] << 24 | lp[1] << 16 | lp[2] << 8 |lp[3]  
  
def num2ip(num):  
	ip = ['','','','']  
	ip[3] = (num & 0xff)  
	ip[2] = (num & 0xff00) >> 8  
	ip[1] = (num & 0xff0000) >> 16  
	ip[0] = (num & 0xff000000) >> 24  
	return '%s.%s.%s.%s' % (ip[0],ip[1],ip[2],ip[3])  
  
def iprange(ip1,ip2):  
	num1 = ip2num(ip1)  
	num2 = ip2num(ip2)  
	tmp = num2 - num1  
	if tmp < 0:  
		return None  
	else:  
		return num1,num2,tmp  
  
  
if __name__ == '__main__':  
	print 'start time : %s' % time.ctime(time.time())  
	if len(sys.argv) < 4:  
		print 'Usage:scanner01 startip endip port'  
		sys.exit()  
	res = ()  
	startip = sys.argv[1]  
	endip = sys.argv[2]  
	port = int(sys.argv[3])  
	res = iprange(startip,endip)  
	if not res:  
		print 'endip must be bigger than startone'  
		sys.exit()  
	elif res[2] == 0:  
		portScanner(startip,port)  
	else:  
		for x in xrange(int(res[2])+1):  
			startipnum = ip2num(startip)  
			startipnum = startipnum + x  
			portScanner(num2ip(startipnum),port)  
	print 'end time : %s' % time.ctime(time.time())  
