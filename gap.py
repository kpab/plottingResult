import seaborn as sns
import japanize_matplotlib
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import numpy as np
from result_morning import *


# ヒートマップの差の出力
def GappingHeatmap(results, walls, fig_name):
    global normal
    normal = np.array(normal)
    results = np.array(results)
    
    gap = results - normal

    fig2, ax2 = plt.subplots(figsize=(12.0, 8.0),
                           facecolor="gainsboro")
    
    ax2.set_xlim(0, 500)
    ax2.set_ylim(0, 500)

    ax2.set_title("~ヒートマップの差~")
    ax2 = sns.heatmap(gap, cmap='bwr',cbar=False, annot=True, fmt='d', annot_kws={'fontsize':4.0}, vmax=8000, vmin=-8000)
    for wall in walls:
            ax2.add_patch(Rectangle((wall[0]/10, wall[1]/10), (wall[2]-wall[0])/10, (wall[3]-wall[1])/10))
    ax2.invert_yaxis()
    plt.show()
    fig2.savefig(f"{fig_name}_gap.png", dpi=300)




GappingHeatmap(aw06, walls, "aw06")

