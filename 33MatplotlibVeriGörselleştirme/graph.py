import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1,6)
y = np.arange(2,11,2)
fig = plt.figure()



# figure açmak için dosyaya gidip pytohn ile aç anaconda prompt ile

axes = fig.add_axes([0.1,0.2,0.4,0.6]) # ilk soldan içeride başlamalı 2. alttan ne kadar yukarıda 3 grafik ne kadar uzun olacak hepsi 0ile1 arası
# 0.6 uzunluğu boydan belirliyor.


# axes2 = fig.add_axes([0.4,0.5,0.4,0.8])


axes.plot(y,x)
axes.set_xlabel("Outer X")
axes.set_ylabel("Outer y")
axes.set_title("OuterGraph")

plt.show()