from datetime import datetime
import numpy as np



def getSensorData():
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    
    
    
    #runtime_factor = float(np.random.uniform(0.5, 1.5)) 
    machines =['machine_1','machine_2','machine_3','machine_4'] 
        
    machine_data = {
        "DATETIME": dt_string,
        'machine_num':str(np.random.choice(machines, 1)[0]),
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
    return machine_data

if __name__ == "__main__":
    print(getSensorData())
