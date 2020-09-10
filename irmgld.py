import numpy as np
import matplotlib.pyplot as plt
import utils

trav_range = np.linspace(0, 60, 500)
angle_range = np.linspace(0, 180, 500)
aim_range = np.linspace(0, 6, 500)
coef_range = np.linspace(0, 1, 500)

aiming_time = 2.1
turr_coeff = 0.08
turr_angle = 180
turr_speed = 30

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
ax.plot(trav_range, turr_time(turr_angle, trav_range), label='Traverse time delta')
ax.plot(trav_range, irm_gld_time(aiming_time, trav_range, turr_coeff), label='GLD IRM time delta')
ax.plot(trav_range, irm_vs_time(aiming_time, trav_range, turr_coeff), label='VS IRM time delta')
ax.legend()
ax.set_xlim([0, 60])
ax.set_ylim([0, 1])
ax.set_xlabel('turret traverse [deg/s]')
ax.set_ylabel('t_delta [s]')
ax.set_title('E50M {0} turret traverse'.format(turr_angle))
plt.show()
#plt.savefig('irmgld.png', dpi=600, format='png')

