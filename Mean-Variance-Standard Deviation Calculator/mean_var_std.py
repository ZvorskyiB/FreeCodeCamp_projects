import numpy as np

def calculate(list):
  if len(list)!=9:
    raise ValueError('List must contain nine numbers.')
  m=np.array([list[0:3], list[3:6], list[6:9]])

  mean=[np.mean(m, axis=0).tolist(), np.mean(m, axis=1).tolist(), float(np.mean(m))]
  var=[np.var(m, axis=0).tolist(), np.var(m, axis=1).tolist(), float(np.var(m))]
  std=[np.std(m, axis=0).tolist(), np.std(m, axis=1).tolist(), float(np.std(m))]
  max=[np.max(m, axis=0).tolist(), np.max(m, axis=1).tolist(), float(np.max(m))]
  min=[np.min(m, axis=0).tolist(), np.min(m, axis=1).tolist(), float(np.min(m))]
  sum=[np.sum(m, axis=0).tolist(), np.sum(m, axis=1).tolist(), float(np.sum(m))]

  calculations ={'mean': mean,
                 'variance': var,
                 'standard deviation': std,
                 'max': max,
                 'min': min,
                 'sum': sum
                 }
  return calculations