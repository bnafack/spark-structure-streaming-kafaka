from faker import Faker
import numpy as np
from datetime import datetime



def GetSellArticle():
    produc =['Alcool125','Alcool250','vitamine','compress', 'savon','gant','coton','thermon']
    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return {'article':str(np.random.choice(produc, 1)[0]),
    'quantite':str(np.random.choice(20, 1)[0]),
    'prix unitaire':str(np.random.choice(200000, 1)[0]),
    'DateTime': dt_string
     }


if __name__ == "__main__":
    print(GetSellArticle())