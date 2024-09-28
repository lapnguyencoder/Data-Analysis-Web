import geopandas as gpd
import matplotlib.pyplot as plt

usa = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

massachusetts = usa[(usa['name'] == 'United States') & (usa['iso_a2'] == 'US')]
fig, ax = plt.subplots(figsize=(8, 8))
massachusetts.plot(ax=ax, color='lightblue')

ax.set_title('Bản đồ Tiểu bang Massachusetts', fontsize=15)
ax.set_xlabel('Kinh độ')
ax.set_ylabel('Vĩ độ')

plt.show()
