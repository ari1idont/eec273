import pickle
import json 
import pprint
import time
# import threading
# import multiprocessing
import numpy as np
import requests



def stat_enable():
	try:
		stat=requests.put("http://localhost:8080/wm/statistics/config/enable/json")
		print("enabled_statistics")
	except Exception as e:
		print("error"+e)

time.sleep(10)

lamda=np.ones([10,20])


with open('model_nn.pkl','rb') as f:
	mlp = pickle.load(f)



def switch1 ():
	
	p=requests.get("http://localhost:8080/wm/core/switch/00:00:00:00:00:00:00:01/flow/json")
	if p.status_code==200:
		p1=json.loads(p.text)
		return p1

def switch2 ():
	
	p=requests.get("http://localhost:8080/wm/core/switch/00:00:00:00:00:00:00:02/flow/json")
	if p.status_code==200:
		#print('sucess')
		p1=json.loads(p.text)
		return p1

def switch3 ():
	
	p=requests.get("http://localhost:8080/wm/core/switch/00:00:00:00:00:00:00:03/flow/json")
	if p.status_code==200:
		p1=json.loads(p.text)
		return p1

def switch4 ():
	
	p=requests.get("http://localhost:8080/wm/core/switch/00:00:00:00:00:00:00:04/flow/json")
	if p.status_code==200:
		p1=json.loads(p.text)
		return p1

def switch5 ():
	
	p=requests.get("http://localhost:8080/wm/core/switch/00:00:00:00:00:00:00:05/flow/json")
	if p.status_code==200:
		p1=json.loads(p.text)
		return p1

def switch6 ():
	
	p=requests.get("http://localhost:8080/wm/core/switch/00:00:00:00:00:00:00:06/flow/json")
	if p.status_code==200:
		p1=json.loads(p.text)
		return p1

def switch7 ():
	
	p=requests.get("http://localhost:8080/wm/core/switch/00:00:00:00:00:00:00:07/flow/json")
	if p.status_code==200:
		p1=json.loads(p.text)
		return p1

def switch8 ():
	
	p=requests.get("http://localhost:8080/wm/core/switch/00:00:00:00:00:00:00:08/flow/json")
	if p.status_code==200:
		p1=json.loads(p.text)
		return p1

def switch9 ():
	
	p=requests.get("http://localhost:8080/wm/core/switch/00:00:00:00:00:00:00:09/flow/json")
	if p.status_code==200:
		p1=json.loads(p.text)
		return p1

def switch10 ():

	p=requests.get("http://localhost:8080/wm/core/switch/00:00:00:00:00:00:00:0a/flow/json")
	if p.status_code==200:
		p1=json.loads(p.text)
		return p1

def rate_cal(data,index):
	if(len(data['flows'])>index):


	#print(data['flows'][index]['match'])
		if (len(data['flows'][index]['match'])==9):
			src_port=int(data['flows'][index]['match']['udp_src'])
			dst_port=int(data['flows'][index]['match']['udp_dst'])
			protocol=int(data['flows'][index]['match']['ip_proto'],0)
			datarate=int(data['flows'][index]['byte_count'])/(int(data['flows'][index]['duration_sec'])*1000)
			k=mlp.predict(np.array([[src_port,dst_port,datarate,0,0,1]]))
			return k
	else:
		return 1





p1=switch1()
p2=switch2()
p3=switch3()
p4=switch4()
p5=switch5()
p6=switch6()
p7=switch7()
p8=switch8()
p9=switch9()
p10=switch10()

all_list=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]

lamda=lamda*(0.01)
#gammasbar=sum(sum(gamma))
r=np.ones([10,20])
for i in range(0,10):
	for j in range(0,20):
		r[i][j]=rate_cal(all_list[i],j)
for i in range(0,10):
	for j in range(0,20):
		if np.isnan(r[i][j]):
			r[i][j]=1

gamma = np.ones([10,20])
for i in range(0,10):
	for j in range(0,20):
		gamma[i][j]=lamda[i][j]*r[i][j]

gammasbar=sum(sum(gamma))

print(lamda)


# while(sum(sum(lamda))<=0.1):
# 	for k in range (0,10):
# 		delta=np.zeros(5)
# 		#gammasbar=gammasbar(all_list)
		
# 		for i in range (0,5):
# 			ravg=np.mean(r[k])
# 			gammas=sum(gamma[k])
# 			delta[i]=((float(ravg)*gammas)/gammasbar)

# 			#delta[j]=
# 		pi=min(delta)
# 		pi1=0.207*pi
# 		#print(delta)
# 		lamda[k]=lamda[k]*(1+(pi1/delta))
# 		#print(lamda)


new_gamma=np.ones([10,20])
for i in range(0,10):
	for j in range(0,20):
		new_gamma[i][j]=lamda[i][j]*r[i][j]

print('load: '+ str(sum(sum(new_gamma))))



















