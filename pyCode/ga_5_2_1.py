import numpy as np
import scipy
from scipy.interpolate import interp1d
import seaborn as sns
import pandas as pd

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score

import matplotlib
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

days = np.arange(1,85,1)
print(days)

weekpoints = [1, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84]
moralepoints = [20, 30, 35, 18, 6, 3, 12, 35, 44, 53, 62, 73, 80]

morale_func = interp1d(weekpoints, moralepoints, kind='cubic')
morale_true = morale_func(days)

# Function to plot morale
fig = plt.figure(figsize=(8,5))
ax = fig.gca()

ax.plot(days, morale_true, lw=7., c='gold', alpha=0.5, label='true function')

ax.set_xlabel('days', fontsize=16)
ax.set_ylabel('morale', fontsize=16)
ax.set_title('Morale over time\n', fontsize=20)

plt.legend(loc='upper left')

plt.show()

# Create student data
def make_students(f, days, size=12):
    students = {}
    for student in ['A', 'B', 'C', 'D']:
        daysamp = np.random.choice(days, replace=False, size=size)
        morales = f(daysamp) + np.random.normal(0, 13, size=size)
        students[student] = {'days': daysamp, 'morale': morales}
    return students

students = make_students(morale_func, days, size=12)

print(students)

# Plot student morales
fig = plt.figure(figsize=(8,5))
ax = fig.gca()

ax.plot(days, morale_true, lw=7., c='gold', alpha=0.3, label='true function')
ax.scatter(students['A']['days'], students['A']['morale'],
           s=70, c='darkred', label='student A', alpha=0.7)

ax.set_xlabel('days', fontsize=16)
ax.set_ylabel('morale', fontsize=16)
ax.set_title('Morale over time\n', fontsize=20)
ax.set_xlim([0, 85])

plt.legend(loc='upper left')

plt.show()

# Build a model for days predicting morale using student A data
studA_days = students['A']['days']
studA_mor = students['A']['morale']

Amod = LinearRegression()
Amod.fit(studA_days[:, np.newaxis], studA_mor)

# Plot the modeled relation between days and morale
fig = plt.figure(figsize=(8,5))
ax = fig.gca()

ax.plot(days, morale_true, lw=7., c='gold', alpha=0.5, label='true function')

ax.plot(days, Amod.predict(days[:, np.newaxis]), lw=7., c='darkred', alpha=0.5, label='model')

ax.scatter(students['A']['days'], students['A']['morale'],
           s=70, c='darkred', label='student A', alpha=0.7)

ax.set_xlabel('days', fontsize=16)
ax.set_ylabel('morale', fontsize=16)
ax.set_title('Morale over time\n', fontsize=20)
ax.set_xlim([0, 85])

plt.legend(loc='upper left')

plt.show()

# Get the total error = Bias + variance + Irreducible error

fig = plt.figure(figsize=(9,6))
ax = fig.gca()

ax.plot(days, morale_true, lw=7., c='gold', alpha=0.5, label='true function')

predictions = Amod.predict(days[:, np.newaxis])
ax.plot(days, predictions, lw=7., c='darkred', alpha=0.5, label='model')

ax.scatter(students['A']['days'], students['A']['morale'],
           s=70, c='darkred', label='student A', alpha=0.7)

for d in students['A']['days']:
    p = Amod.predict(d)
    ax.plot([d, d], [p, morale_func(d)], c='black', lw=3.)

ax.set_xlabel('days', fontsize=16)
ax.set_ylabel('morale', fontsize=16)
ax.set_title('Morale over time (difference from true function)\n', fontsize=20)
ax.set_xlim([0, 85])

plt.legend(loc='upper left')

plt.show()

# Plot new students data
fig = plt.figure(figsize=(8,5))
ax = fig.gca()

ax.plot(days, morale_true, lw=7., c='gold', alpha=0.5, label='true function')

ax.scatter(students['A']['days'], students['A']['morale'],
           s=70, c='darkred', label='student A', alpha=0.7)

ax.scatter(students['B']['days'], students['B']['morale'],
           s=70, c='steelblue', label='student B', alpha=0.7)

ax.set_xlabel('days', fontsize=16)
ax.set_ylabel('morale', fontsize=16)
ax.set_title('Morale over time\n', fontsize=20)
ax.set_xlim([0, 85])

plt.legend(loc='upper left')

plt.show()

# Model to fit the new data
# Fit student b's model
studB_days = students['B']['days']
studB_mor = students['B']['morale']

Bmod = LinearRegression()
Bmod.fit(studB_days[:, np.newaxis], studB_mor)

# Plot the difference between predictions of students A and B

fig = plt.figure(figsize=(8,5))
ax = fig.gca()

ax.plot(days, morale_true, lw=7., c='gold', alpha=0.5, label='true function')

Apred = Amod.predict(days[:, np.newaxis])
ax.plot(days, Apred, lw=7., c='darkred', alpha=0.5, label='A model')

Bpred = Bmod.predict(days[:, np.newaxis])
ax.plot(days, Bpred, lw=7., c='steelblue', alpha=0.5, label='B model')

ax.scatter(students['A']['days'], students['A']['morale'],
           s=70, c='darkred', label='student A', alpha=0.7)

ax.scatter(students['B']['days'], students['B']['morale'],
           s=70, c='steelblue', label='student B', alpha=0.7)

ax.fill_between(days, Apred, Bpred, color='grey', hatch='//', edgecolor=None)

ax.set_xlabel('days', fontsize=16)
ax.set_ylabel('morale', fontsize=16)
ax.set_title('Morale over time (difference between estimates)\n', fontsize=20)
ax.set_xlim([0, 85])

plt.legend(loc='upper left')

plt.show()

# Plot data for 3 student data

fig = plt.figure(figsize=(8,5))
ax = fig.gca()

ax.plot(days, morale_true, lw=7., c='gold', alpha=0.5, label='true function')

ax.scatter(students['A']['days'], students['A']['morale'],
           s=70, c='darkred', label='student A', alpha=0.7)

ax.scatter(students['B']['days'], students['B']['morale'],
           s=70, c='steelblue', label='student B', alpha=0.7)

ax.scatter(students['C']['days'], students['C']['morale'],
           s=70, c='darkgreen', label='student C', alpha=0.7)

ax.set_xlabel('days', fontsize=16)
ax.set_ylabel('morale', fontsize=16)
ax.set_title('Morale over time\n', fontsize=20)
ax.set_xlim([0, 85])

plt.legend(loc='upper left')

plt.show()

# Fit model for 3rd student data

# Fit student C's model
studC_days = students['C']['days']
studC_mor = students['C']['morale']

Cmod = LinearRegression()
Cmod.fit(studC_days[:, np.newaxis], studC_mor)

# Plot the models for all 3 students
fig = plt.figure(figsize=(9,6))
ax = fig.gca()

ax.plot(days, morale_true, lw=7., c='gold', alpha=0.5, label='true function')


Apred = Amod.predict(days[:, np.newaxis])
ax.plot(days, Apred, lw=5., c='darkred', alpha=0.5, label='A model')

Bpred = Bmod.predict(days[:, np.newaxis])
ax.plot(days, Bpred, lw=5., c='steelblue', alpha=0.5, label='B model')

Cpred = Cmod.predict(days[:, np.newaxis])
ax.plot(days, Cpred, lw=5., c='darkgreen', alpha=0.5, label='C model')

ax.scatter(students['A']['days'], students['A']['morale'],
           s=70, c='darkred', label='student A', alpha=0.7)

ax.scatter(students['B']['days'], students['B']['morale'],
           s=70, c='steelblue', label='student B', alpha=0.7)

ax.scatter(students['C']['days'], students['C']['morale'],
           s=70, c='darkgreen', label='student C', alpha=0.7)

ax.set_xlabel('days', fontsize=16)
ax.set_ylabel('morale', fontsize=16)
ax.set_title('Morale over time\n', fontsize=20)
ax.set_xlim([0, 85])

plt.legend(loc='upper left')

plt.show()

# Increase the complexity of ur model to match the true function which is curvy
def polynomial_modeler(X, y, degrees):
    polynomial_features = PolynomialFeatures(degree=degrees,
                                             include_bias=False)
    linear_regression = LinearRegression()
    pipeline = Pipeline([("polynomial_features", polynomial_features),
                         ("linear_regression", linear_regression)])
    pipeline.fit(X[:, np.newaxis], y)
    return pipeline


def plot_polyfit(X, y, truefunc, degrees=[1, 4, 9, 32],
                 student_color='darkred', name='A'):
    # set the plot size
    plt.subplots(figsize=(18, 7))

    # create a plot for each polynomial degree plotted
    for i in range(len(degrees)):
        ax = plt.subplot(1, len(degrees), i + 1)

        poly_model = polynomial_modeler(X, y, degrees[i])

        X_test = np.linspace(1, 84, 200)
        plt.plot(X_test, poly_model.predict(X_test[:, np.newaxis]), lw=5.,
                 c=student_color, label="model", alpha=0.6)
        plt.plot(X_test, truefunc(X_test), lw=5., c='gold', alpha=0.6, label='true function')
        plt.scatter(X, y, label="Student observations", c=student_color, s=40)
        plt.xlabel("days")
        plt.ylabel("morale")
        plt.xlim((0, 85))
        plt.ylim((-20, 100))
        plt.legend(loc="best")

        plt.title('Student ' + name + " (degree {})".format(degrees[i]))


plot_polyfit(students['A']['days'], students['A']['morale'], morale_func,
             student_color='darkred', name='A')

plot_polyfit(students['B']['days'], students['B']['morale'], morale_func,
             student_color='steelblue', name='B')

plot_polyfit(students['C']['days'], students['C']['morale'], morale_func,
             student_color='darkgreen', name='C')
plt.show()

fig = plt.figure(figsize=(9,6))
ax = fig.gca()

ax.plot(days, morale_true, lw=7., c='gold', alpha=0.5, label='true function')

Amod_complex = polynomial_modeler(students['A']['days'], students['A']['morale'], 32)
Bmod_complex = polynomial_modeler(students['B']['days'], students['B']['morale'], 32)


Apred = Amod_complex.predict(days[:, np.newaxis])
ax.plot(days, Apred, lw=7., c='darkred', alpha=0.5, label='A model')

Bpred = Bmod_complex.predict(days[:, np.newaxis])
ax.plot(days, Bpred, lw=7., c='steelblue', alpha=0.5, label='B model')

ax.scatter(students['A']['days'], students['A']['morale'],
           s=70, c='darkred', label='student A', alpha=0.7)

ax.scatter(students['B']['days'], students['B']['morale'],
           s=70, c='steelblue', label='student B', alpha=0.7)

ax.fill_between(days, Apred, Bpred, color='grey', hatch='//', edgecolor=None)

ax.set_xlabel('days', fontsize=16)
ax.set_ylabel('morale', fontsize=16)
ax.set_title('Morale over time (16th polynomial)\n', fontsize=20)
ax.set_xlim([0, 85])
ax.set_ylim([-2000,2000])

plt.legend(loc='upper left')

plt.show()


# Bias is the difference betweent he models attained for each student
# Variance is the difference between student a  data points and their corresponding models.
