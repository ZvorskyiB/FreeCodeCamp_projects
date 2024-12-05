import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('Medical Data Visualizer\\medical_examination.csv', sep=',')

# 2
def ow_b(x):
  BMI=x['weight']/((x['height']/100)**2)
  if BMI<=25:
    return 0
  return 1
df['overweight'] = df.apply(ow_b, axis=1)

# 3
df['cholesterol']=df['cholesterol'].apply(lambda x: 0 if x==1 else 1)
df['gluc']=df['gluc'].apply(lambda x: 0 if x==1 else 1)

# 4
def draw_cat_plot():
    # 5
    df_cat =  df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']) 


    # 6
    df_cat = df_cat=df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size().rename(columns={'size':'total'})
    

    # 7



    # 8
    fig = sns.catplot(df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar').fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
           (df['ap_lo'] <= df['ap_hi']) &
           (df['height'] >= df['height'].quantile(0.025)) &
           (df['height'] <= df['height'].quantile(0.975)) &
           (df['weight'] >= df['weight'].quantile(0.025)) &
           (df['weight'] <= df['weight'].quantile(0.975))
   ]     

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(corr, mask=mask, ax=ax, fmt='.1f', annot=True) 


    # 16
    fig.savefig('heatmap.png')
    return fig 