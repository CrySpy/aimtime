import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, 500)

ticks = np.arange(0,101, 5)


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
vents_coeff = 0            #Base
#vents_coeff = 6            #Category bonus
#vents_coeff = 7.5          #Bounty
#vents_coeff = 8.5          #Bonds
other_crew_coeff = 0       #BiA, Food

acc = 0.38
speed = 1
coeff = 4
aim_time = 2.7
crew_member_level = 0
commander_level = 0
intra_clip = 2.73


def crewbonus(crew=100, commander=100, bonus=0):
    return 0.57 + 0.43 * (crew/100 + commander/1000 + bonus/100 + bonus/1000)

def aimfunc(bloom=1, aimTime=3, accuracy=0.3):
    arr = bloom * np.exp(-t/aimTime)
    result = np.maximum(arr, accuracy)
    return result

def bloomFunc(accuracy=0.3, coeff=0.3):
    return accuracy * np.sqrt(1+coeff**2)


acc =  acc / crewbonus(crew_member_level, commander_level, other_crew_coeff)
coeff = coeff / crewbonus(crew_member_level, commander_level, other_crew_coeff)
aim_time = aim_time / crewbonus(crew_member_level, commander_level, other_crew_coeff)

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

#ax.set_xlim([0,7])
#ax.set_ylim([0.4, 0.6])
ax.set_xlabel('t time[s]')
ax.set_ylabel('y aim circle radius[m]')
ax.set_title('BatChat 0%crew after firing')
ax.grid()
ax.legend()

#plt.show()
plt.savefig('cursed.png', dpi=600, format='png')