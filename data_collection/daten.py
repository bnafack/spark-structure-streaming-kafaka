import numpy as np
from datetime import datetime




from datetime import datetime
import numpy as np


machines_prod=['machine_1','machine_2','machine_3','machine_4']

def GetSensorDataSnapshot():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    return {
        "DATETIME": dt_string,
        'machines_ids':str(np.random.choice(machines_prod, 1)[0]),
        "param1": float(np.random.uniform(0, 20)),
        "param2": float(np.random.uniform(-10, 100)),
        "param3": float(np.random.uniform(0, 200)), 
        "param4": float(np.random.uniform(0, 200)),
        "param5": float(np.random.uniform(-10, 150)), 
        "param6": float(np.random.uniform(0, 300)),
        "param7": float(np.random.uniform(0, 2000)), 
        "param8": float(np.random.uniform(1000, 5000)),
        "param9": float(np.random.uniform(0, 10000))
    }

# Tester la fonction
if __name__ == "__main__":
    print(GetSensorDataSnapshot())



# def GetSensorDataSnapshot():

#     now = datetime.now()
#     dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    
#     return {
#         "DATETIME": dt_string,
#         "param1": float(np.random.uniform(0, 20)),
#         "param2": float(np.random.uniform(-10, 100)),
#         "param3": float(np.random.uniform(0, 200)),
#         "param4": float(np.random.uniform(0, 200)),
#         "param5": float(np.random.uniform(-10, 150)),
#         "param6": float(np.random.uniform(0, 300)),
#         "param7": float(np.random.uniform(0, 2000)),
#         "param8": float(np.random.uniform(1000, 5000)),
#         "param9": float(np.random.uniform(0, 10000))
#     }



# if __name__ == "__main__":
#     print(GetSensorDataSnapshot)
    
