from datetime import datetime
import pandas as pd
import numpy as np 

df1={"id":[1,2,3,4,5],"type_name":["Car","Auto","Bus","Bike","Cycle"],"Charge_Per_Hour":[50,30,20,60,10],
     "Charge_per_day":[500,300,200,600,100]}
dframe=pd.DataFrame(df1)

print(dframe)

print("From the above table, choose the suitable informaton:-")

df2={"id":[1],"vehicle_number":[input("Enter your vehicle number:-")],
     "vehicle_type_id":[int(input("Choose your vehicle type"))],"in_time":[input("Enter in time:-")],
     "out_time":[input("Enter exit time:-")]}

start_time=df2[("in_time")]
st="".join(start_time)

end_time=df2["out_time"]
et="".join(end_time)

t1=datetime.strptime(str(st),"%H:%M:%S")
t2=datetime.strptime(str(et),"%H:%M:%S")

tint=t2-t1
tint_secs=tint.total_seconds()
tint_secs2=tint_secs%3600

charge_int=int()

charge=tint_secs2*charge_int
df2["charge"]=charge
df=pd.DataFrame(df2)
print(df)