import matplotlib as mpl
import matplotlib.pyplot as plt  

years = list(map(str, range(1980,2014)))

df_canada.loc['Haiti', years].plot(kind='line')
plt.title('Immi')
plt.ylabel('Number')
plt.xlabel('Years')

plt.show()
