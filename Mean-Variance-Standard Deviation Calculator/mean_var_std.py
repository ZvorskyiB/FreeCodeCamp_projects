import numpy as np

def calculate(list):
  if len(list)!=9:
    raise ValueError("List must contain nine numbers.")
  else:
    m=np.array([list[0:3],list[3:6],list[6:9]])

    l_mean=[]
    l_mean.append([])
    for i in m.mean(axis=0):
      l_mean[0].append(float(i))
    l_mean.append([])
    for i in m.mean(axis=1):
      l_mean[1].append(float(i))
    l_mean.append(float(m.mean()))

    l_var=[]
    l_var.append([])
    for i in m.var(axis=0):
      l_var[0].append(float(i))
    l_var.append([])
    for i in m.var(axis=1):
      l_var[1].append(float(i))
    l_var.append(float(m.var()))


   
    l_std=[]
    l_std.append([])
    for i in m.std(axis=0):
      l_std[0].append(float(i))
    l_std.append([])
    for i in m.std(axis=1):
      l_std[1].append(float(i))
    l_std.append(float(m.std()))

    l_max=[]
    l_max.append([])
    for i in m.max(axis=0):
      l_max[0].append(int(i))
    l_max.append([])
    for i in m.max(axis=1):
      l_max[1].append(int(i))
    l_max.append(int(m.max()))

    l_min=[]
    l_min.append([])
    for i in m.min(axis=0):
      l_min[0].append(int(i))
    l_min.append([])
    for i in m.min(axis=1):
      l_min[1].append(int(i))
    l_min.append(int(m.min()))

    l_sum=[]
    l_sum.append([])
    for i in m.sum(axis=0):
      l_sum[0].append(int(i))
    l_sum.append([])
    for i in m.sum(axis=1):
      l_sum[1].append(int(i))
    l_sum.append(int(m.sum()))

    calculations={'mean': l_mean,'variance': l_var,'standard deviation': l_std,'max': l_max,'min': l_min,'sum': l_sum}
    return calculations