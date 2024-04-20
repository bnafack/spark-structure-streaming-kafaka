#from faker import Faker
import numpy as np
from datetime import datetime



# def GetSellArticle():
#     produc =['Alcool125','Alcool250','vitamine','compress', 'savon','gant','coton','thermon']
#     # datetime object containing current date and time
#     now = datetime.now()

#     # dd/mm/YY H:M:S
#     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#     return {
#     'DateTime': dt_string,
#     'article':str(np.random.choice(produc, 1)[0]),
#     'quantite':float(np.random.choice(20, 1)[0]),
#     'prix unitaire':float(np.random.choice(200000, 1)[0]),
#      }


# if __name__ == "__main__":
#     print(GetSellArticle())


from datetime import datetime
import numpy as np


product=['Alcool125','Alcool250','vitamine','compress', 'savon','gant','coton','thermon']

def GetSellArticle():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    return {
        'datetime': dt_string,
        'article': str(np.random.choice(product, 1)[0]),
        'quantite': int(np.random.randint(1, 21)),
        'prix_unitaire': float(np.random.randint(100, 200001))
    }

# Tester la fonction
if __name__ == "__main__":
    print(GetSellArticle())