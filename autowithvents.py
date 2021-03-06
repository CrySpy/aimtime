import matplotlib.pyplot as plt
import numpy as np
from utils import crewbonus, aimfunc, bloomFunc

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

acc = 0.35
coeff = 4
aim_time = 2.5
crew_member_level = 100
commander_level = 100
intra_clip = 2.5



acc =  acc / crewbonus(crew_member_level, commander_level, vents_coeff + other_crew_coeff)
coeff = coeff / crewbonus(crew_member_level, commander_level, vents_coeff + other_crew_coeff)
aim_time = aim_time / crewbonus(crew_member_level, commander_level, vents_coeff + other_crew_coeff)

base_bloom = bloomFunc(acc, coeff)
vstabs_bloom = bloomFunc(acc, vstabs_coeff*coeff)
irm_vstab_bloom = bloomFunc(acc, (irm_coeff*vstabs_coeff)*coeff)
gld_vstab_bloom = bloomFunc(acc, vstabs_coeff*coeff)
iau_vstab_bloom = bloomFunc(iau_coeff*acc, vstabs_coeff*coeff)



fig, ax = plt.subplots()

ax.plot(t, aimfunc(t, base_bloom, aim_time, acc), label='Base', linewidth=1.25)
ax.plot(t, aimfunc(t, vstabs_bloom, aim_time, acc), label='VSTABS', linewidth=1.25)
ax.plot(t, aimfunc(t, irm_vstab_bloom, aim_time, acc), label='IRM + VSTABS', linewidth=1.25)
ax.plot(t, aimfunc(t, gld_vstab_bloom, gld_coeff*aim_time, acc), label='GLD + VSTABS', linewidth=1.25)
ax.plot(t, aimfunc(t, iau_vstab_bloom, aim_time, iau_coeff*acc), label='IAU + VSTABS', linewidth=1.25)

plt.axvline(x=intra_clip)

ax.set_xlim([2,3.5])
ax.set_ylim([0.3, 0.6])
ax.set_xlabel('t time[s]')
ax.set_ylabel('y aim circle radius[m]')
ax.set_title('50B after firing')
ax.grid()
ax.legend()

plt.show()
#plt.savefig('cursed.png', dpi=600, format='png')