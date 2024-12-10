import matplotlib.pyplot as plt
import numpy as np

# 数据：fable, fairytale, science, history, folklore, movie
i_blip2 = [70.0, 58.1, 65.0, 58.8, 71.2, 64.3]
i_llava = [68.8, 53.5, 67.5, 75.0, 63.6, 65.6]
i_GPT4V = [78.8, 73.3, 82.5, 80.0, 84.8, 79.6]
i_human = [97.4, 96.4, 93.5, 93.1, 95.8, 95.2]

# 标签
labels=np.array(["fable", "fairytale", "science", "history", "folklore", "movie"])
num_vars = len(labels)

# 角度
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# 数据闭环
i_blip2 = np.concatenate((i_blip2, [i_blip2[0]]))
i_llava = np.concatenate((i_llava, [i_llava[0]]))
i_GPT4V = np.concatenate((i_GPT4V, [i_GPT4V[0]]))
i_human = np.concatenate((i_human, [i_human[0]]))

# 角度闭环
angles += angles[:1]

# 初始化图表
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# 绘制每个数据集的雷达图
ax.fill(angles, i_blip2, color='salmon', alpha=0.3)
ax.fill(angles, i_llava, color='lightblue', alpha=0.3)
ax.fill(angles, i_GPT4V, color='lightgreen', alpha=0.3)
ax.fill(angles, i_human, color='violet', alpha=0.3)


# 设置图例
ax.legend(['BLIP-2', 'LLaVA', 'GPT-4V', 'Human'], loc='upper right', bbox_to_anchor=(0.1, 0.1))

ax.plot(angles, i_blip2, color='darkred', linewidth=1.5)
ax.plot(angles, i_llava, color='darkblue', linewidth=1.5)
ax.plot(angles, i_GPT4V, color='darkgreen', linewidth=1.5)
ax.plot(angles, i_human, color='rebeccapurple', linewidth=1.5)

# 设置标签
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

plt.savefig('ide.png', bbox_inches='tight', dpi=300)
plt.show()



# e_blip2 = [12.5, 10.9, 7.5, 7.5, 16.1, 10.7]
# e_llava = [60.0, 58.7, 70.0, 75.0, 41.9, 61.9]
# e_GPT4V = [80.0, 84.8, 95.0, 82.5, 83.9, 85.3]
# e_human = [98.1, 97.7, 95.5, 96.3, 95.5, 96.6]

# # 标签
# labels=np.array(["fable", "fairytale", "science", "history", "folklore", "movie"])
# num_vars = len(labels)

# # 角度
# angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# # 数据闭环
# e_blip2 = np.concatenate((e_blip2, [e_blip2[0]]))
# e_llava = np.concatenate((e_llava, [e_llava[0]]))
# e_GPT4V = np.concatenate((e_GPT4V, [e_GPT4V[0]]))
# e_human = np.concatenate((e_human, [e_human[0]]))

# # 角度闭环
# angles += angles[:1]

# # 初始化图表
# fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# # 绘制每个数据集的雷达图
# ax.fill(angles, e_blip2, color='salmon', alpha=0.3)
# ax.fill(angles, e_llava, color='lightblue', alpha=0.3)
# ax.fill(angles, e_GPT4V, color='lightgreen', alpha=0.3)
# ax.fill(angles, e_human, color='violet', alpha=0.3)


# # 设置图例
# ax.legend(['BLIP-2', 'LLaVA', 'GPT-4V', 'Human'], loc='upper right', bbox_to_anchor=(0.1, 0.1))

# ax.plot(angles, e_blip2, color='darkred', linewidth=1.5)
# ax.plot(angles, e_llava, color='darkblue', linewidth=1.5)
# ax.plot(angles, e_GPT4V, color='darkgreen', linewidth=1.5)
# ax.plot(angles, e_human, color='rebeccapurple', linewidth=1.5)

# # 设置标签
# ax.set_xticks(angles[:-1])
# ax.set_xticklabels(labels)

# plt.savefig('ela.png', bbox_inches='tight', dpi=300)
# plt.show()
