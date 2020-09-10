import matplotlib.pyplot as plt
import numpy as np
from utils import crewbonus, aimfunc, bloomFunc

t = np.linspace(0, 1, 1000)

ticks = np.arange(0,101, 5)

vstabs_coeff = 0.8         #Base
#vstabs_coeff = 0.75        #Bounty
#vstabs_coeff = 0.725       #Bonds
#irm_coeff = 0.9            #Base
irm_coeff = 0.885          #Category bonus       
iau_coeff = 0.95           #Base
#iau_coeff = 0.93           #Category bonus
gld_coeff = 0.909          #Base
#gld_coeff = 0.91           #Unupgraded bounty           
#gld_coeff = 0.897          #Category bonus
#gld_coeff = 0.89           #Bounty
#gld_coeff = 0.881          #Bonds
#vents_coeff = 5            #Base
vents_coeff = 6            #Category bonus
#vents_coeff = 7.5          #Bounty
#vents_coeff = 8.5          #Bonds
other_crew_coeff = 0        #BiA, Food          

acc = 0.36
speed = 16
coeff = 0.05
aim_time = 2.1
crew_member_level = 100
commander_level = 100



acc100 =  acc / crewbonus(crew_member_level, commander_level, other_crew_coeff)
coeff100 = coeff / crewbonus(crew_member_level, commander_level, other_crew_coeff)
aim_time100 = aim_time / crewbonus(crew_member_level, commander_level, other_crew_coeff)

vents =  crewbonus(crew_member_level, commander_level, vents_coeff + other_crew_coeff)

base_bloom = bloomFunc(acc100, coeff100, speed)
vstabs_bloom = bloomFunc(acc100, vstabs_coeff*coeff100, speed)
irm_bloom = bloomFunc(acc100, irm_coeff*coeff100, speed)
gld_bloom = bloomFunc(acc100, coeff100, speed)
iau_bloom = bloomFunc(iau_coeff*acc100, coeff100, speed)
vents_bloom = bloomFunc(acc/vents, coeff/vents, speed)


fig, ax = plt.subplots()

ax.plot(t, aimfunc(t, base_bloom, aim_time100, acc100), label='Base', linewidth=1.25)
ax.plot(t, aimfunc(t, vstabs_bloom, aim_time100, acc100), label='VS', linewidth=1.25)
ax.plot(t, aimfunc(t, irm_bloom, aim_time100, acc100), label='IRM', linewidth=1.25)
ax.plot(t, aimfunc(t, gld_bloom, gld_coeff*aim_time100, acc100), label='GLD', linewidth=1.25)
ax.plot(t, aimfunc(t, iau_bloom, aim_time100, iau_coeff*acc100), label='IAU', linewidth=1.25)
ax.plot(t, aimfunc(t, vents_bloom, aim_time/vents, acc/vents), label='Vents', linewidth=1.25)


ax.set_xlim([0, 0.5])
#ax.set_xlim([5, 6.5])
#ax.set_ylim([0.3, 0.5])
ax.set_xlabel('t time[s]')
ax.set_ylabel('y aim circle radius[m]')
ax.set_title('Maus turret traverse')
ax.grid(which='major', color='#666666', linestyle='-')
ax.grid(which='minor', color='#ccccff', linestyle='-')
plt.minorticks_on()
ax.legend()

plt.show()
#plt.savefig('withvents.png', dpi=600, format='png')