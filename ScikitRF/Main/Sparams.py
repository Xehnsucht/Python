import skrf as rf
import matplotlib as mlp
rf.stylely()
from pylab import *

# Load data
pathToSparams = r'D:/Work/Meas/Instr/PetlaiAntenna/'
probe = rf.Network(pathToSparams + 'Antenna_TEM_cell_20dBm.s2p')


s11 = probe.s11
s21 = probe.s21
#  time-gate the first largest reflection

# plot frequency and time-domain s-parameters
figure(figsize=(8, 4))
subplot(221)
s11.plot_s_db()
title('Frequency Domain')

subplot(222)
s11.plot_s_db_time()
title('Time Domain')

subplot(223)
s21.plot_s_db()

subplot(224)
s21.plot_s_smith()
tight_layout()
plt.show()