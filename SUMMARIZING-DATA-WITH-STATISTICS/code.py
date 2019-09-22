# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

#Code starts here 

data = pd.read_csv(path)
data['Gender'].replace('-','Agender', inplace= True)
gender_count = data.Gender.value_counts()
gender_count.plot(kind ='bar')


# --------------
#Code starts here
alignment = data.Alignment.value_counts()
alignment.plot(kind='pie')


# --------------
#Code starts here
sc_df = data[['Strength','Combat']]
sc_covariance = sc_df.cov().iloc[0,1]
print('Covariance : ',sc_covariance)
sc_strength = sc_df.Strength.std()
sc_combat = sc_df.Combat.std()
print('Strenght std deviation :',sc_strength)
print('Combat Std deviation :',sc_combat)
sc_pearson = sc_covariance/(sc_combat * sc_strength)
print('Pearson: ',sc_pearson)

ic_df = data[['Intelligence','Combat']]
ic_covariance = ic_df.cov().iloc[0,1]
print('Covariance : ',ic_covariance)
ic_intelligence = ic_df.Intelligence.std()
ic_combat = ic_df.Combat.std()
print('Strenght std deviation :',ic_intelligence)
print('Combat Std deviation :',ic_combat)
ic_pearson = ic_covariance/(ic_combat * ic_intelligence)
print('Pearson: ',ic_pearson)


# --------------
#Code starts here
total_high = data.Total.quantile(q=0.99)
super_best = data[data['Total']>total_high]
super_best_names = list(super_best['Name'])
super_best_names


# --------------
#Code starts here
#Code starts here

#Setting up the subplots
fig, (ax_1, ax_2,ax_3) = plt.subplots(1,3, figsize=(20,8))

#Plotting box plot
ax_1.boxplot(super_best['Intelligence'])

#Setting the subplot axis title
ax_1.set(title='Intelligence')


#Plotting box plot
ax_2.boxplot(super_best['Speed'])

#Setting the subplot axis title
ax_2.set(title='Speed')


#Plotting box plot
ax_3.boxplot(super_best['Power'])

#Setting the subplot axis title
ax_3.set(title='Power')

#Code ends here   


