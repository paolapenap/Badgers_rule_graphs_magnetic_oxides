#GRAPHS OF Frequency of the Ag(1) against electronegativity and V-O_t distance

import numpy as np
from numpy import *
from scipy import odr
from pylab import *

import matplotlib.pyplot as plt

import matplotlib as mpl
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from matplotlib import rc, rcParams
rc('text',usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern']})
mpl.rcParams['legend.fontsize']= 20 # tamanho de las letras en la leyenda
mpl.rcParams['xtick.labelsize']=20 # tamanho los numeros en el eje x
mpl.rcParams['ytick.labelsize']= 20 # tamanho los numeros en el eje y

Ent=[1.55, 1.88, 1.91, 1.65]# electronegativity
V_Ot=array([1.47, 1.76, 1.64, 1.77])# interatomic distance V-O_t
Delta_V=[10.7, 4.3, 7, 15]
Z=[25, 27, 28, 30]
labelsX = ['Mn', "Co", "Ni", "Zn"]

Ag_freq=np.array([864, 850, 859, 906]) # frequency of the Ag(1) mode


figure()
plt.plot(Ent, Ag_freq, 'o')
plt.plot(1.31, 915.7, 'd')
plt.show()


##### BAdger's rule prove

Badger_Ag_freq = Ag_freq**(2.0/3) 
Badger_VOt= 1/V_Ot

#print Badger_VOt
#ax=plt.subplot(1,1,1)
#x_test=np.arange(0.57, 0.68, 0.01)
#def f_test(m,x):
#    return  m[0]+(m[1]*x)

#m0=[1, 1]
#linear = odr.Model(f_test)
#mydata = odr.Data(Badger_VOt[0:3], Badger_Ag_freq[0:3])                   
#myodr  = odr.ODR(mydata, linear, beta0=m0)         
#myoutput = myodr.run()

#plsq      = myoutput.beta                                 # parameters fited
#y_test=f_test(plsq,x_test)

#ax.plot(Badger_VOt[0:3], Badger_Ag_freq[0:3],  'o', ms=10)
#ax.plot(Badger_VOt[3::], Badger_Ag_freq[3::], 'D', ms=10)
#ax.plot(0.591, 94.2979, 'd', ms=10)
#ax.plot(x_test, y_test, '-')

#text(0.677, 90.3, r'Mn', fontsize=17)
#text(0.567, 89.9, r'Co', fontsize=17)
#text(0.61, 90.46, r'Ni', fontsize=17)
#text(0.569, 93.4, r'Zn', fontsize=17)
#text(0.594, 94.1, r'Mg*', fontsize=17) ### Data for Mg from Tang et. al. Chin. Phys. B Vol. 22, No. 6 (2013) 066202
#ax.xaxis.set_major_locator(MultipleLocator(0.02))### Major ticks on x axis separated by 0.02 from each other
#ax.xaxis.set_minor_locator(MultipleLocator(0.01))### Minor ticks on x separated by 0.01 from each other

#ax.set_ylabel(r'$\bar{\omega}^{2/3}$ (cm$^{-2/3}$)',fontsize=20)
#ax.set_xlabel(r'$1/d_{\textrm{V-O}_t}$ (1/\AA)', fontsize=20)
#plt.show()





###### Wavenumber of Ag(1) mode vs distortion index of VO6 octahedra


##figure()
ax=plt.subplot(1,1,1)
x_test=np.arange(4.3, 11, 0.5)
def f_test(m,x):
    return  m[0]+(m[1]*x)

m0=[7, 850]
linear = odr.Model(f_test)
mydata = odr.Data(Delta_V[0:3], Ag_freq[0:3])                   
myodr  = odr.ODR(mydata, linear, beta0=m0)         
myoutput = myodr.run()

plsq      = myoutput.beta                                 # parameters fited
plsq_err  = myoutput.sd_beta                              # error parameters fited

#print plsq, plsq_err

y_test=f_test(plsq,x_test)
ax.plot(Delta_V, Ag_freq, 'o', ms=10)
ax.plot(x_test, y_test, '--')
plot(8.867, 915.7, 'd', ms=10) ### Data for Mg from Tang et. al. Chin. Phys. B Vol. 22, No. 6 (2013) 066202
text(4.3, 852, r'Co', fontsize=17)
text(7, 861, r'Ni', fontsize=17)
text(11, 864, r'Mn', fontsize=17)
text(14.6, 900, r'Zn', fontsize=17)
text(9, 910, r'Mg$^\ast$', fontsize=17)
ax.set_ylim(845, 920)
ax.yaxis.set_minor_locator(MultipleLocator(10))
ax.set_ylabel(r'$\bar{\omega}$ (cm$^{-1}$)',fontsize=20)
ax.set_xlabel(r'$\Delta_\textrm{V}$ ($10^{-3}$)', fontsize=20)
plt.show()


###### Wavenumber of Ag(1) mode (red) and electronegativity (blue) vs. atomic number Z 

#fig, ax1 = plt.subplots()

#color='tab:red'
#ax1.set_ylabel(r'Wavenumber (cm$^{-1}$)',fontsize=20, color=color)
#ax1.plot(Z, Ag_freq, 'o', ms=10, color=color)
#ax1.plot(Z[0:3], Ag_freq[0:3], '--', color=color)
#ax1.plot(Z[2::], Ag_freq[2::], ':', color=color)
#ax1.tick_params(axis='y', labelcolor=color)
#ax1.set_ylim(845,920)
#ax1.annotate("", xy=(26,850), xytext=(27, 850), arrowprops=dict(arrowstyle="->", color=color))
#ax1.tick_params(axis='y', labelcolor=color)

#ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

#color = 'tab:blue'
#ax2.set_ylabel(r'Electronegativity', fontsize=20, color=color)  # we already handled the x-label with ax1
#ax2.plot(Z, Ent, '^', ms=10, color=color)
#ax2.plot(Z[0:3], Ent[0:3], '--',  color=color)
#ax2.plot(Z[2::], Ent[2::], ':',  color=color)
#ax2.tick_params(axis='y', labelcolor=color)
#ax2.annotate("", xy=(28,1.88), xytext=(27, 1.88), arrowprops=dict(arrowstyle="->", color=color))

#xticks(Z, labelsX, fontsize=20, )
#fig.tight_layout()  # otherwise the right y-label is slightly clipped
#plt.show()




###### Wavenumber of Ag(1) mode (red) and Interatomic V-Ot distance (green) vs. atomic number Z  

#fig, ax1 = plt.subplots()

#color='tab:red'
#ax1.set_ylabel(r'Wavenumber (cm$^{-1}$)',fontsize=20, color=color)
#ax1.plot(Z, Ag_freq, 'o', ms=10, color=color)
#ax1.plot(Z[0:3], Ag_freq[0:3], '--', color=color)
#ax1.plot(Z[2::], Ag_freq[2::], ':', color=color)
#ax1.tick_params(axis='y', labelcolor=color)
#ax1.set_ylim(845,920)
#ax1.annotate("", xy=(26,850), xytext=(27, 850), arrowprops=dict(arrowstyle="->", color=color))

#ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

#color = 'tab:green'
#ax2.set_ylabel(r'$d_{\textrm{V-O}_t}$ (\AA)', fontsize=20, color=color)  # we already handled the x-label with ax1
#ax2.plot(Z, V_Ot, 'D', ms=10, color=color)
#ax2.plot(Z[0:3], V_Ot[0:3], '--',  color=color)
#ax2.plot(Z[2::], V_Ot[2::], ':', color=color)
#ax2.tick_params(axis='y', labelcolor=color)
#ax2.annotate("", xy=(28,1.76), xytext=(27, 1.76), arrowprops=dict(arrowstyle="->",  color=color))


#xticks(Z, labelsX, fontsize=20, )
#fig.tight_layout()  # otherwise the right y-label is slightly clipped
#plt.show()

