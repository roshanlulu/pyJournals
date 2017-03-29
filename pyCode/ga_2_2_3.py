import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')

exercise = 2

if exercise == 1:
    titanic = pd.DataFrame.from_csv('/Users/roshanlulu/Documents/GA/pyJournals/pyCode/datasets/titanic_clean.csv')

    print(titanic.describe())

    pclass = titanic.groupby('Pclass')
    print(type(pclass))
    # print(pclass[0]) --> This wont work. Grouped dataframes dont work the smae as lists

    for g in pclass:
        print ('Pclass group:', g[0])
        print ('titanic subset head:', g[1].head())
        print ('------------------------------------------')

    pclass_surv = titanic.groupby(['Pclass','Survived'])
    print(len(pclass_surv))

    print(pclass_surv.mean())
    print(pclass_surv.median())
    print(titanic.groupby('Embarked')['Survived'].mean())
    avg_fare = titanic.groupby(['Embarked','Pclass'])[['Fare','Age']].mean()
    print(avg_fare)

    def rounded_mean(subset):
        subset = subset.mean()
        subset = subset.round()
        return subset


    avg_fare = titanic.groupby(['Embarked','Pclass'])[['Fare','Age']].apply(rounded_mean).reset_index()
    print(avg_fare)

    def top_paying_females(data):
        data = data.sort_values('Fare', ascending=False)
        subset = data[data['Sex'] == 'female']
        return subset.head(5)

    print(top_paying_females(titanic))

    print(titanic.groupby('Survived').apply(top_paying_females))

    class_counts = titanic.groupby('Pclass').size()
    print(class_counts)

    class_counts.plot(kind="bar", color='y', width=0.5)

    titanic.groupby(['Pclass','Sex'])['Fare'].mean().plot(kind='bar', width=0.6)

    # plt.show()

    mean_fare = titanic.groupby(['Pclass','Sex'])['Fare'].mean()
    print(mean_fare)
    print(mean_fare.unstack())
    mean_fare.unstack().plot(kind='bar')

    mean_fare.unstack().plot(kind='bar', stacked=True)
    plt.show()

elif exercise == 2:
    # ufo_dframe = pd.DataFrame.from_csv('/Users/roshanlulu/Documents/GA/pyJournals/pyCode/datasets/ufo.csv')

    ufo_data = pd.read_csv("./datasets/ufo.csv")
    ufo_dframe = pd.DataFrame(ufo_data)

    print(ufo_dframe.head())
    print(ufo_dframe.isnull().sum())
    print(ufo_dframe.shape)
    print(ufo_dframe.groupby('City').apply(len).sort_values(ascending=False).head(10))
    print(ufo_dframe['Shape Reported'].value_counts())

    cities = ['Seattle', 'New York City', 'Phoenix', 'Las Vegas', 'Portland']
    shapes = ['LIGHT', 'TRIANGLE', 'CIRCLE', 'FIREBALL', 'OTHER']
    subset = ufo_dframe[ufo_dframe['City'].isin(cities) & ufo_dframe['Shape Reported'].isin(shapes)]

    print(ufo_dframe.shape)
    print(subset.shape)

    counts = subset.groupby(['City', 'Shape Reported']).size()
    print(counts)

    counts = counts.reset_index()
    counts.columns = ['city', 'shape', 'count']
    counts['percent'] = counts.groupby('city')['count'].apply(lambda x: x / np.sum(x))

    subset.groupby(['City', 'Shape Reported']).size().unstack().plot(kind='bar')
    plt.show()