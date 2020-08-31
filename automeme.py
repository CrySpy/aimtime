import matplotlib.pyplot as plt
import numpy as np

path = 'C:\\Users\\Christoffer\\Documents\\Aimtime tings'

t = np.linspace(0, 3.5, 500)

acc = 0.44
#speed = 65
coeff = 3.84
aim_time = 2.88
intra_clip = 3

vstabs_coeff = 0.8         #Base
#vstabs_coeff = 0.75        #Bounty
#vstabs_coeff = 0.725       #Bonds
irm_coeff = 0.9            #Base
#irm_coeff = 0.885          #Category bonus       
iau_coeff = 0.95           #Base
#iau_coeff = 0.93           #Category bonus
gld_coeff = 0.909          #Base
#gld_coeff = 0.91           #Unupgraded bounty           
#gld_coeff = 0.897          #Category bonus
#gld_coeff = 0.89           #Bounty
#gld_coeff = 0.881          #Bonds


def aimfunc(bloom=1, aimTime=3, accuracy=0.3):
    arr = bloom * np.exp(-t/aimTime)
    result = np.maximum(arr, accuracy)
    return result

def bloomFunc(accuracy=0.3, coeff=0.3):
    return accuracy * np.sqrt(1+coeff**2)

base_bloom = bloomFunc(acc, coeff)
vstabs_bloom = bloomFunc(acc, vstabs_coeff*coeff)
irm_vstab_bloom = bloomFunc(acc, (irm_coeff*vstabs_coeff)*coeff)
gld_vstab_bloom = bloomFunc(acc, vstabs_coeff*coeff)
iau_vstab_bloom = bloomFunc(iau_coeff*acc, vstabs_coeff*coeff)


fig, ax = plt.subplots()

ax.plot(t, aimfunc(base_bloom, aim_time, acc), label='Base', linewidth=1.25)
ax.plot(t, aimfunc(vstabs_bloom, aim_time, acc), label='VSTABS', linewidth=1.25)
ax.plot(t, aimfunc(irm_vstab_bloom, aim_time, acc), label='IRM + VSTABS', linewidth=1.25)
ax.plot(t, aimfunc(gld_vstab_bloom, gld_coeff*aim_time, acc), label='GLD + VSTABS', linewidth=1.25)
ax.plot(t, aimfunc(iau_vstab_bloom, aim_time, iau_coeff*acc), label='IAU + VSTABS', linewidth=1.25)
plt.axvline(x=intra_clip)

ax.set_xlim([2.5,3.5])
ax.set_ylim([0.4, 0.6])
ax.set_xlabel('t time[s]')
ax.set_ylabel('y aim circle radius[m]')
ax.set_title('IS-3A after firing')
ax.grid()
ax.legend()

plt.show()
#plt.savefig('big2.png', dpi=600, format='png')