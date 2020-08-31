import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 7, 1000)

ticks = np.arange(0,101, 5)

#vstabs_coeff = 0.8         #Base
#vstabs_coeff = 0.75        #Bounty
vstabs_coeff = 0.725       #Bonds
#irm_coeff = 0.9            #Base
irm_coeff = 0.885          #Category bonus       
iau_coeff = 0.95           #Base
#iau_coeff = 0.93           #Category bonus
#gld_coeff = 0.909          #Base
#gld_coeff = 0.91           #Unupgraded bounty           
#gld_coeff = 0.897          #Category bonus
#gld_coeff = 0.89           #Bounty
gld_coeff = 0.881          #Bonds
#vents_coeff = 5            #Base
#vents_coeff = 6            #Category bonus
#vents_coeff = 7.5          #Bounty
vents_coeff = 8.5          #Bonds
other_crew_coeff = 15        #BiA, Food          

acc = 0.38
speed = 1
coeff = 4
aim_time = 2.7
crew_member_level = 100
commander_level = 100



def crewbonus(crew=100, commander=100, bonus=0):
    return 0.57 + 0.43 * (crew/100 + commander/1000 + bonus/100 + bonus/1000)

def aimfunc(bloom=1, aimTime=3, accuracy=0.3):
    arr = bloom * np.exp(-t/aimTime)
    result = np.maximum(arr, accuracy)
    return result

def bloomFunc(accuracy=0.3, coeff=0.3):
    return accuracy * np.sqrt(1+(coeff*speed)**2)

acc100 =  acc / crewbonus(crew_member_level, commander_level, other_crew_coeff)
coeff100 = coeff / crewbonus(crew_member_level, commander_level, other_crew_coeff)
aim_time100 = aim_time / crewbonus(crew_member_level, commander_level, other_crew_coeff)


base_bloom = bloomFunc(acc100, coeff100)
vstabs_bloom = bloomFunc(acc100, vstabs_coeff*coeff100)
irm_bloom = bloomFunc(acc100, irm_coeff*coeff100)
gld_bloom = bloomFunc(acc100, coeff100)
iau_bloom = bloomFunc(iau_coeff*acc100, coeff100)
vents_bloom = bloomFunc(acc/crewbonus(crew_member_level, commander_level, vents_coeff + other_crew_coeff), coeff/crewbonus(crew_member_level, commander_level, vents_coeff + other_crew_coeff))


fig, ax = plt.subplots()

ax.plot(t, aimfunc(base_bloom, aim_time100, acc100), label='Base', linewidth=1.25)
ax.plot(t, aimfunc(vstabs_bloom, aim_time100, acc100), label='VS', linewidth=1.25)
ax.plot(t, aimfunc(irm_bloom, aim_time100, acc100), label='IRM', linewidth=1.25)
ax.plot(t, aimfunc(gld_bloom, gld_coeff*aim_time100, acc100), label='GLD', linewidth=1.25)
ax.plot(t, aimfunc(iau_bloom, aim_time100, iau_coeff*acc100), label='IAU', linewidth=1.25)
ax.plot(t, aimfunc(vents_bloom, aim_time/crewbonus(crew_member_level, commander_level, vents_coeff), acc/crewbonus(crew_member_level, commander_level, vents_coeff)), label='Vents', linewidth=1.25)


#ax.set_xlim([0, 6.5])
ax.set_xlim([5, 6.5])
ax.set_ylim([0.3, 0.5])
ax.set_xlabel('t time[s]')
ax.set_ylabel('y aim circle radius[m]')
ax.set_title('BatChat full speed')
ax.grid(which='major', color='#666666', linestyle='-')
ax.grid(which='minor', color='#ccccff', linestyle='-')
plt.minorticks_on()
ax.legend()

#plt.show()
plt.savefig('withvents.png', dpi=600, format='png')