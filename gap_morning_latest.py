import seaborn as sns
import japanize_matplotlib
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import numpy as np
import copy
import numpy as np
from walls import addwalls
from result_morning_latest import *

type = "result_morning"

now_string = "normal"
kabe = False

s_now_string = "s_" + now_string

now = rrr[s_now_string]
keys = ["全部", "AtoK", "BtoK", "CtoK", "KtoA", "KtoB", "KtoC", "S_AtoK", "S_BtoK", "S_CtoK", "S_KtoA", "S_KtoB", "S_KtoC"]
speeds = ["S_AtoK", "S_BtoK", "S_CtoK", "S_KtoA", "S_KtoB", "S_KtoC"]


def HeatmappingNumber(now_agents_positions, walls, fig_name):    
    for key in keys:
        
        fig2, ax2 = plt.subplots(figsize=(12.0, 8.0),
                            facecolor="gainsboro")
        
        ax2.set_xlim(0, 500)
        ax2.set_ylim(0, 500)

        ax2.set_title(f"ヒートマップ: {key}")
        now = now_agents_positions[key]
        fmt = 'd'
        if key in speeds:
            now = [[float(element) for element in row] for row in now]
            fmt = '.3f'

        ax2 = sns.heatmap(now, cmap='Greens',cbar=False, annot=True, fmt=fmt, annot_kws={'fontsize':4.5})
        for wall in walls:
                ax2.add_patch(Rectangle((wall[0]/10, wall[1]/10), (wall[2]-wall[0])/10, (wall[3]-wall[1])/10))
        ax2.invert_yaxis()

        if kabe:
            ax2.add_patch(Rectangle((addwalls[now_string][0]/10, addwalls[now_string][1]/10), (addwalls[now_string][2]-addwalls[now_string][0])/10, (addwalls[now_string][3]-addwalls[now_string][1])/10))

        # plt.show()
        fig2.savefig(f"{type}/{fig_name}/heatmap_{key}.png", dpi=300)
        plt.close(fig2)


# ヒートマップの差の出力
def GappingHeatmap(results, walls, fig_name):
    global normal
    no = copy.deepcopy(normal)
    no = np.array(no)
    results = np.array(results)
    
    gap = results - no

    fig2, ax2 = plt.subplots(figsize=(12.0, 8.0),
                           facecolor="gainsboro")
    
    ax2.set_xlim(0, 500)
    ax2.set_ylim(0, 500)

    ax2.set_title("~ヒートマップの差~")
    ax2 = sns.heatmap(gap, cmap='bwr',cbar=False, annot=True, fmt='d', annot_kws={'fontsize':4.0}, vmax=8000, vmin=-8000)
    for wall in walls:
            ax2.add_patch(Rectangle((wall[0]/10, wall[1]/10), (wall[2]-wall[0])/10, (wall[3]-wall[1])/10))
    ax2.invert_yaxis()
    # -- 壁ある時 --
    if kabe:
        ax2.add_patch(Rectangle((addwalls[now_string][0]/10, addwalls[now_string][1]/10), (addwalls[now_string][2]-addwalls[now_string][0])/10, (addwalls[now_string][3]-addwalls[now_string][1])/10))
    
    fig2.savefig(f"{type}/{fig_name}/gap.png", dpi=300)
    plt.close(fig2)


# 箱ひげ図
def GappingHakohigeHazure(results, fig_name):
    global normal
    no = copy.deepcopy(normal)
      # 二次元を一次元に変換
    results = sum(results, [])
    # 0を除去
    results = list(filter(lambda x: x!=0, results))
    results = np.array(results) # numpy配列に変換
    no = np.array(no)

    no = no.flatten()
    no = list(filter(lambda x: x!=0, no))
  
    data = (no, results)
    # 箱ひげ図のプロット
    fig, ax = plt.subplots()
    ax.boxplot(data, vert=False, showmeans=True, whis=1.4, widths=0.8)  # 横向き, 外れ値表記
    ax.set_title('箱ひげ図(外れ値あり)')
    ax.set_xlabel('通過人数')
    # ax.set_ylabel()
    ax.set_yticklabels(["normal", fig_name])
    plt.grid()
    fig.savefig(f"{type}/{fig_name}/hakogap.png")
    plt.close(fig)


def CountZero(now):
    # 一次変換
    now = sum(now, [])
    zero_wall = 1611
    zero_points = len(now) - np.count_nonzero(np.array(now)) - zero_wall
    print(f"{now_string}のゼロ人数通過地点: {zero_points}")



HeatmappingNumber(now, walls, now_string)

