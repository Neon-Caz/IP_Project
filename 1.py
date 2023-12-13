from datetime import datetime
import pandas as pd
import numpy as np 

df1={"id":[1,2,3,4,5],"type_name":["Car","Auto","Bus","Bike","Cycle"],"Charge_Per_Hour":[50,30,20,60,10],
     "Charge_per_day":[500,300,200,600,100]}
dframe=pd.DataFrame(df1, index=["r11","r22","r33","r44","r55"])

print(dframe)

print("From the above table, choose the suitable informaton: ")


#how do i even choose the corresponding charge

df2={"r1":{"id":[1],"vehicle_number":"KA06AY7676",
     "vehicle_type_id":1,"in_time":"10:23:23",
     "out_time":"11:20:55","charge":50},
     "r2":{"id":[2],"vehicle_number":"AP07AS3434",
     "vehicle_type_id":2,"in_time":"11:39:56",
     "out_time":"12:30:34","charge":30},
     "r3":{"id":[3],"vehicle_number":"TN65GY6767",
     "vehicle_type_id":1,"in_time":"12:43:56",
     "out_time":"01:45:23","charge":50},
     "r4":{"id":[4],"vehicle_number":[input("Enter your vehicle number:-")],
     "vehicle_type_id":[int(input("Choose your vehicle type"))],"in_time":[input("Enter in time:-")],
     "out_time":[input("Enter exit time:-")],"charge":np.NaN}}

start_time=df2["in_time"]
st="".join(start_time)

end_time=df2["out_time"]
et="".join(end_time)

t1=datetime.strptime(str(st),"%H:%M:%S")
t2=datetime.strptime(str(et),"%H:%M:%S")

tint=t2-t1
tint_secs=tint.total_seconds()
tint_secs2=tint_secs%3600



df1.loc["Charge_Per_Hour"]
if df2.loc["vehicle_type_id"]==df1.loc['id']:
    charge=df1["Charge_Per_Hour"]
    
charge1=charge*tint_secs2

df2.loc["r4","charge"]=charge1

df=pd.DataFrame(df2)
print(df)