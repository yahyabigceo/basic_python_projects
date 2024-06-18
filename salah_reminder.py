#salah reminder
import os
import time
from win10toast import ToastNotifier
t=(time.strftime('%H:%M:%S'))
hour=int(time.strftime('%H'))
minute=int(time.strftime('%M'))
seconds=int(time.strftime('%S'))

toast=ToastNotifier()
if hour== 5 and minute==15 :
    toast.show_toast("salah reminder!","its fajr time!!",None,10,True)  
elif hour== 1 and minute==15 :
    toast.show_toast("salah reminder!","its dhuhr time!!",None,10,True)   
elif hour== 17 and minute==25 :
    toast.show_toast("salah reminder!","its Asr time!!",None,10,True)   
elif hour== 19 and minute==10 :
    toast.show_toast("salah reminder!","its Maghrib time!!",None,10,True)  
elif hour== 20 and minute==55 :
    toast.show_toast("salah reminder!","its Isha time!!",None,10,True)   
    
else:
    pass
print(t)
print(hour)  
print(minute)  
print(seconds)  
time.sleep(30)
