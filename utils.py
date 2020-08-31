import numpy as np

VSTABS_BASE_COEFF = 0.8
VSTABS_BOUNTY_COEFF = 0.75
VSTABS_BONDS_COEFF = 0.725
IRM_BASE_COEFF = 0.9
IRM_CATEGORY_COEFF = 0.885
IAU_BASE_COEFF = 0.95
IAU_CATEGORY_COEFF = 0.93
GLD_BASE_COEFF = 0.909
GLD_UBOUNTY_COEFF = 0.91
GLD_CATEGORY_COEFF = 0.897
GLD_BOUNTY_COEFF = 0.89
GLD_BONDS_COEFF = 0.881
VENTS_BASE_COEFF = 0
VENTS_CATEGORY_COEFF = 6
VENTS_BOUNTY_COEFF = 7.5
VENTS_BONDS_COEFF = 8.5
BIA_COEFF = 5
FOOD_COEFF = 10

def crewbonus(crew=100, commander=100, bonus=0):
    return 0.57 + 0.43 * (crew/100 + commander/1000 + bonus/100 + bonus/1000)

def aimfunc(t, bloom=1, aimTime=3, accuracy=0.3,):
    arr = bloom * np.exp(-t/aimTime)
    result = np.maximum(arr, accuracy)
    return result

def bloomFunc(accuracy=0.3, coeff=0.3, speed=1):
    return accuracy * np.sqrt(1+(speed*coeff)**2)

def time(x, y):
    return np.log(np.sqrt(1+(y)**2)) * x