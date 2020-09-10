import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import utils

trav_range = np.linspace(0, 60, 500)
angle_range = np.linspace(0, 360, 500)
aim_range = np.linspace(0, 6, 500)
coef_range = np.linspace(0, 1, 500)

aiming_time = 3.26
turr_coeff = 0.15
turr_angle = 90
turr_speed = 39.63

GLD = utils.GLD_BASE_COEFF
BONUS = utils.VSTABS_BASE_COEFF

def turr_time(angle, trav_speed):
    return (0.1 * angle / (1.1 * trav_speed))

def mod_disp(trav_speed, coeff, bonus=1):
    return np.sqrt(1 + (bonus * coeff * trav_speed)**2)

def irm_gld_time(aim_time, trav_speed, coeff):
    return aim_time * (1 - GLD) * np.log(mod_disp(trav_speed, coeff))
    

def irm_vs_time(aim_time, trav_speed, coeff):
    return aim_time * np.log(mod_disp(trav_speed, coeff)/mod_disp(trav_speed, coeff, bonus=BONUS))


fig, ax = plt.subplots()
ax.plot(angle_range, turr_time(angle_range, turr_speed), label='Traverse time delta')
plt.axhline(y=irm_gld_time(aiming_time, turr_speed, turr_coeff), label='GLD IRM time delta', color='orange')
plt.axhline(y=irm_vs_time(aiming_time, turr_speed, turr_coeff), label='VS IRM time delta', color='green')
ax.legend()
ax.set_xlim([0, 360])
#ax.set_ylim([0, 0.2])
ax.set_xlabel('turret angle [deg]')
ax.set_ylabel('t_delta [s]')
ax.set_title('A-44 turret traverse')


def prep_vs(angle):
    return turr_time(angle, turr_speed) - irm_vs_time(aiming_time, turr_speed, turr_coeff)

def prep_gld(angle):
    return turr_time(angle, turr_speed) - irm_gld_time(aiming_time, turr_speed, turr_coeff)

result = optimize.root_scalar(prep_vs, bracket=[0, 360])
print('IRM better than VS at {0} degrees'.format(result.root))
result = optimize.root_scalar(prep_gld, bracket=[0, 360])
print('IRM better than GLD at {0} degrees'.format(result.root))

plt.show()
#plt.savefig('irmgld2.png', dpi=600, format='png')