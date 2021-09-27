import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['savefig.dpi']=300


a=[666618,588597,443497,269913,197146,195835,139682,134647,130100,125753]
for i in range(len(a)):
    a[i]=a[i]/10000

data={'country':['美国','巴西','印度','墨西哥','秘鲁','俄罗斯','印度尼西亚','英国','意大利','哥伦比亚'],
      'deadnum':a}

pdat=pd.DataFrame(data)
l=pdat['deadnum']
N=pdat.shape[0]
width=2*np.pi/N
rad=np.cumsum([width]*N)

colors=['red','darkred','maroon','firebrick','brown','indianred','lightcoral','salmon','rosybrown','mistyrose']

plt.figure(figsize=(15,20))#创建画布
ax=plt.subplot(projection='polar')#创建极坐标
ax.set_ylim(0,np.ceil(l).max()+1)
ax.set_theta_zero_location('N')#极坐标起点
ax.grid(False)#不显示极轴
ax.spines['polar'].set_visible(False)#不显示最外的圆形
ax.set_yticks([])#不显示坐标间隔
ax.set_thetagrids([])#不显示极轴坐标

ax.bar(rad,l,width=width,color=colors,alpha=1)
ax.bar(rad,5,width=width,color='white',alpha=1)
ax.bar(rad,10,width=width,color='white',alpha=0.2)

for i in np.arange(N):
    ax.text(rad[i],l[i]-4,data['country'][i],rotation=rad[i]*180/np.pi,
            rotation_mode='anchor',alpha=1,fontweight='bold',size=12,color='white')
    ax.text(rad[i], l[i] - 7, data['deadnum'][i], rotation=rad[i] * 180 / np.pi,
            rotation_mode='anchor', alpha=1, fontweight='bold', size=12,color='white')

plt.savefig('2.png',bbox_inches='tight')

plt.show()










