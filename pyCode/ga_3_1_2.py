# data modules
import numpy as np
import scipy.stats as stats
import pandas as pd

# plotting modules
import matplotlib.pyplot as plt
import seaborn as sns


inverted_questions = ['usually_dont_laugh',
                      'tease_others_mistakes',
                      'let_others_laugh_at_me',
                      'rarely_make_laugh_stories',
                      'use_self_deprecation',
                      'tease_disliked_people',
                      'cant_think_witty_things',
                      'allow_others_tease_me',
                      'harshly_self_deprecate',
                      'dont_often_joke',
                      'if_sad_cant_laugh',
                      'dont_like_telling_jokes',
                      'dont_care_impact_jokes',
                      'self_deprecate_to_befriend',
                      'friends_often_tease_me',
                      'joke_when_inappropriate']

column_change = {
    'Q1':'usually_dont_laugh',
    'Q2':'if_depressed_use_humor',
    'Q3':'tease_others_mistakes',
    'Q4':'let_others_laugh_at_me',
    'Q5':'make_others_laugh_easy',
    'Q6':'when_alone_amused',
    'Q7':'my_humor_never_offensive',
    'Q8':'use_self_deprecation',
    'Q9':'rarely_make_laugh_stories',
    'Q10':'if_upset_use_humor',
    'Q11':'dont_care_impact_jokes',
    'Q12':'self_deprecate_to_befriend',
    'Q13':'laugh_alot_with_friends',
    'Q14':'humorous_outlook_improves_mood',
    'Q15':'dislike_mean_humor',
    'Q16':'dont_self_deprecate',
    'Q17':'dont_like_telling_jokes',
    'Q18':'when_alone_try_laugh',
    'Q19':'joke_when_inappropriate',
    'Q20':'harshly_self_deprecate',
    'Q21':'enjoy_making_others_laugh',
    'Q22':'if_sad_cant_laugh',
    'Q23':'never_use_mean_humor',
    'Q24':'friends_often_tease_me',
    'Q25':'dont_often_joke',
    'Q26':'humor_coping_mechanism',
    'Q27':'tease_disliked_people',
    'Q28':'hide_unhappiness_humor',
    'Q29':'cant_think_witty_things',
    'Q30':'dont_need_others_amused',
    'Q31':'if_mean_wont_laugh',
    'Q32':'allow_others_tease_me'
}


# Function to print the header , shape and head of a given dataframe
def print_header(df):
    print('Header\n', df.columns)
    print('Shape\n', df.shape)
    print('Data description\n', df.describe())
    print('Data head\n', df.head())
    return df.columns


# Section C - Loading and examining data

hsq = pd.read_csv('./datasets/hsq_data.csv')
# # hsq_columns = print_header(hsq)
# hsq.rename(columns = {'agressive':'aggressive'}, inplace = True)
# print('Header\n', hsq.columns)
#
# print('Max age that is entered', hsq.max()['age'])
# print(hsq.std())

# # Plot the distribution for Q 15 and plot for aggressive
#
# sns.distplot(hsq.Q15, kde=False)
# sns.distplot(hsq.aggressive, kde=False)
# plt.show()

# Section D


# Rename  columns from QNumber to the ones in column_change
hsq.rename(columns = column_change, inplace = True)
print(hsq.columns)

# Add a subject ID
subject_ids = np.arange(1, hsq.shape[0] + 1)
print(subject_ids.shape, hsq.shape)
print(subject_ids[0:10])
hsq['subject_id'] = subject_ids
print(hsq.shape)

# Transform data to long format

style_columns = ['affiliative','selfenhancing','aggressive','selfdefeating']
question_columns = list(column_change.values())
to_value_variable_columns = style_columns + question_columns + ['accuracy']

header_list = hsq.columns.values.tolist()
val_vars = [c for c in header_list if c != 'age' and c != 'gender' and c != 'hsq_id']

id_columns = ['subject_id','age','gender']

hsq_long = pd.melt(hsq, id_vars = id_columns,
                   value_vars=to_value_variable_columns,
                   var_name='variable',
                   value_name='value')

# print_header(hsq_long)
print(hsq_long.variable.unique())
#
# # Print subset of df with subject id = 10
print((hsq_long[hsq_long.subject_id == 10]))

# Order index by Subject_ id
hsq_long.sort_values('subject_id', inplace=True)
print(hsq_long.shape)

# Reset the index
hsq_long.reset_index(drop=True, inplace=True)
print(hsq_long.head())

# Section E
def convert_gender(x):
    if x == 1:
        return 'male'
    elif x == 2:
        return 'female'
    elif x == 3:
        return 'other'

# update gender to text value in the dataframe
hsq_long['gender'] = hsq_long.gender.map(convert_gender)
print(hsq_long.head())

# Remove subjects from dataset
unresponded = hsq_long[hsq_long.value == -1]
print(unresponded.shape)

incomplete_subs = unresponded.subject_id.unique()
print(incomplete_subs.shape)
print(incomplete_subs)

# Remove all rows from datasets corresponding to bad users
print(hsq_long.shape)
hsq_long = hsq_long[~hsq_long.subject_id.isin(incomplete_subs)]
print(hsq_long.shape)

# Remove subjects who entered 0 for accuracy
request_exclusion = hsq_long[(hsq_long.variable == 'accuracy') & (hsq_long.value == 0)]
print(request_exclusion.shape)

# Find subjects who reported age over 100
lying_subjects = hsq_long[hsq_long.age > 100].subject_id.unique()
print(lying_subjects, lying_subjects.shape)

hsq_long = hsq_long[~hsq_long.subject_id.isin(lying_subjects)]
print(hsq_long.shape)

# Define a score inverter
def score_inverter(question_score):
    if question_score == 5:
        return 1
    elif question_score == 4:
        return 2
    elif question_score == 3:
        return 3
    elif question_score == 2:
        return 4
    elif question_score == 1:
        return 5


row_mask = hsq_long.variable.isin(inverted_questions)
print(row_mask[0:10])

hsq_long.ix[row_mask, 'value'] = hsq_long.value[row_mask].apply(score_inverter)
print(hsq_long.head())


# Transform dataset back to wide dataset

