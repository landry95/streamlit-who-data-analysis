import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import streamlit as st
import os

import matplotlib.pylab as plts
plts.style.use('fivethirtyeight')
import seaborn as sns
sns.set(style="ticks")
sns.set(rc={'figure.figsize':(15,10)})
from IPython.display import display, HTML
from numpy import median
from numpy import sum
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
from PIL import Image
#------------------------------------------

#------------------------------------------
st.set_option('deprecation.showPyplotGlobalUse', False)


st.markdown('<h2><b><font color=‘#5bc0de’>For <i><u>Project : </u></i> Web-App for data visualization !</font></b></h2>', unsafe_allow_html=True)
st.sidebar.markdown('<h2 style="text-align: center; font-family: cursive; color: rgb(255, 127, 39)"><b>WELCOME</b></h3>', unsafe_allow_html=True)
# image = Image.open("logo.PNG")
# st.sidebar.image(image, use_column_width=True)

dataset_name = st.sidebar.selectbox('Select The data you want to analyse', ('about', 'Suside Statistics', 'Suicide Statistics over years',  'Survey on Mental Health in the Tech Workplace'))
# st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)
# st.sidebar.markdown('<ul style="background-color: red"><li>zerfg</li><li>22222222222</li><li>33333333333</li></ul>', unsafe_allow_html=True)
def get_dataset(name):
	wh = None


	if name == 'Suside Statistics':
		st.markdown('<p style="margin-top: 30px">Here, we are analyzing the <b> Horld Health Organization </b> (<i><b>WHO</b></i>) dataset on the suicide statistics in the world.</p><p style="margin-bottom: 30px">We can therefore visualize the data and identify the inequal repartition of this phenomene in countries and also, we can understand the differences depending on the age of the victims and through years</p><hr style="border:1px solid black">', unsafe_allow_html=True)
		wh = pd.read_csv('data/who_suicide_statistics.csv')
		"\n\n"
		wh
		# st.sidebar.write("Check any option to visualize the related data")
		st.sidebar.markdown('<h2 style="text-align: center; color: #f0ad4e"><b>Check any option to visualize the related data</b></h2>', unsafe_allow_html=True)
		st.sidebar.markdown("<br>", unsafe_allow_html=True)

		if st.sidebar.checkbox('Show Description for suside dataset'):
			st.markdown('<h2 style="text-align: center; color: #d9534f"><b>Here is a Description of the data Series.</b></h2>', unsafe_allow_html=True)
			st.write(wh.describe(include="all").T)

		if st.sidebar.checkbox('Show global sucides on years'):
			st.markdown('<h2 style="text-align: center; color: #d9534f; margin-top: 30px"><b>Global sucides through years.</b></h2>', unsafe_allow_html=True)
			st.set_option('deprecation.showPyplotGlobalUse', False)
			sns.set(style="darkgrid")
			sns.set(rc={'figure.figsize':(15,10)})
			ax=sns.regplot(data=wh, x='year', y='suicides_no', x_jitter=0.2, order=4)
			ax.set_yscale('log')
			st.pyplot()

		if st.sidebar.checkbox('Show Suside number by age and country'):
			st.markdown('<h2 style="text-align: center; color: #d9534f; margin-top: 30px"><b>Suside number by age and country.</b></h2>', unsafe_allow_html=True)
			wh.groupby(['country','age']).suicides_no.sum().nlargest(10).plot(kind='barh')
			st.pyplot()

		if st.sidebar.checkbox('Show Suside number by age and sex'):
			st.markdown('<h2 style="text-align: center; color: #d9534f; margin-top: 30px"><b>Suside number by age and sex.</b></h2>', unsafe_allow_html=True)
			ax = sns.catplot(x="sex", y="suicides_no",col='age', data=wh, estimator=median,height=4, aspect=.7,kind='bar')
			st.pyplot()

		if st.sidebar.checkbox('Show Suside number by age interval and sex'):
			st.markdown('<h2 style="text-align: center; color: #d9534f; margin-top: 30px"><b>Suside number by age interval and sex.</b></h2>', unsafe_allow_html=True)
			wh['age'] = wh.age.astype(pd.api.types.CategoricalDtype(categories = ['5-14 years','15-24 years','25-34 years','35-54 years','55-74 years','75+ years']))
			wh.pivot_table(index='age',columns='sex',values='suicides_no', aggfunc='sum').plot(kind='barh')
			st.pyplot()

		# if st.sidebar.checkbox('Show Suside number by age, sex and for each year from 1979 to 2016s'):
		# 	st.markdown('<h4 style="text-align: center; color: #d9534f; margin-top: 30px"><b>Suside number by age, sex and for each year from 1979 to 2016.</b></h4>', unsafe_allow_html=True)
		# 	df = wh.groupby(['year','age']).suicides_no.sum().reset_index()
		# 	df['age'] = df.age.astype(pd.api.types.CategoricalDtype(categories = ['5-14 years','15-24 years','25-34 years','35-54 years','55-74 years','75+ years']))
		# 	sns.set(rc={'figure.figsize':(15,10)})
		# 	st.pyplot()

		if st.sidebar.checkbox('Show Suside number by age, sex and for each year from 1979 to 2016'):
			st.markdown('<h4 style="text-align: center; color: #d9534f; margin-top: 30px"><b>Suside number by age, sex and for each year from 1979 to 2016.</b></h4>', unsafe_allow_html=True)
			sns.catplot('age','suicides_no',hue='sex',col='year',data=wh,kind='bar',col_wrap=3,estimator=sum)
			st.pyplot()

		if st.sidebar.checkbox('Show Evolution of Suside number by sex '):
			st.markdown('<h2 style="text-align: center; color: #d9534f; margin-top: 30px"><b>Evolution of Suside number by sex.</b></h2>', unsafe_allow_html=True)
			sns.set(style="darkgrid")
			g = sns.FacetGrid(wh, row="sex", col="age", margin_titles=True)
			g.map(plt.scatter, "suicides_no","population", edgecolor="w")
			st.pyplot()




	# elif name == 'Nutrition and Population Statistics':
	# 	# health = pd.read_csv('data/data.csv')
	# 	# st.write(health.head())
	# 	# health
	# 	"# aaaaaaaaaaaaa"

	elif name == 'Survey on Mental Health in the Tech Workplace':
		st.sidebar.markdown('<h5 style="margin-top: 30px; margin-bottom: 30px; text-align: center; color: #d9534f; font-family: cursive"><b>Pick an option to make the diagram display</b></h5>', unsafe_allow_html=True)
		st.markdown('<h3 style="margin-top: 20px; color: #fbe25d"><b><u><i>Survey on Mental Health in the Tech Workplace</i></u></b></h3>', unsafe_allow_html=True)
		st.markdown('	<p style="margin-top: 0px">Here, we are analyzing the <b> Horld Health Organization </b> (<u><b>WHO</b></u>) dataset mental health statistics in the world.</p><p style="margin-bottom: 30px">We will then be able to visualize data Comming from thousands of peple all around the world and we will classify them depending on some criterias.</p><ul><li>Their employment status</li><li>Their gender</li><li>Their Anonymity</li><li>Their care options</li><li>Their treatement, if they are ill</li></ul>', unsafe_allow_html=True)
		mtech = pd.read_csv('data/survey.csv')
		st.markdown('<h3 style="margin-top: 20px; color: #d9534f; font-family: cursive"><b>DATASET</b></h3>', unsafe_allow_html=True)
		mtech
		"\n"
		st.markdown('<h3 style="margin-top: 20px; color: #d9534f; font-family: cursive"><b>Description of the data Serie.</b></h3>', unsafe_allow_html=True)
		# "### Description of the data Serie."
		st.write(mtech.describe(include='all'))

		if st.sidebar.checkbox('Diagram depending on the occupation'):
			st.markdown('<h3 style="margin-top: 30px; color: #d9534f; font-family: cursive"><b>Diagram depending on the occupation</b></h3>', unsafe_allow_html=True)
			st.markdown('<p style="margin-top: 10px">Here, we cas visualize the mental health survey depending on if the people are employed or self employed, onsite werkers or remote workers, work for tech company or non tech company</p>', unsafe_allow_html=True)
			sns.catplot(x='self_employed', hue='remote_work', col='tech_company', kind='count', data=mtech)
			st.pyplot()

		if st.sidebar.checkbox('Diagram depending on the occupatio'):
			st.markdown('<h3 style="margin-top: 30px; color: #d9534f; font-family: cursive"><b>anonymity around mental illness</b></h3>', unsafe_allow_html=True)
			st.markdown('<p style="margin-top: 10px">The folowing wisualization show the answers from the question </p><ul><li>if the worker\'s anonymity will be protected if they choose to take advantage of mental health or substance abuse treatment resources</li><li>If they Would be willing to discuss a mental health issue with your coworkers</li><li>If they Would be willing to discuss a mental health issue with your direct supervisor(s)</li></ul><br>The answers are not really positive', unsafe_allow_html=True)
			sns.catplot(x='anonymity', hue='leave', col='supervisor', row='coworkers', kind='count', data=mtech)
			st.pyplot()

		if st.sidebar.checkbox('Consequences of mental illness subject'):
			st.markdown('<h3 style="margin-top: 30px; color: #d9534f; font-family: cursive"><b>Diagram depending on the occupation</b></h3>', unsafe_allow_html=True)
			st.markdown('<p style="margin-top: 10px">The folowing wisualization show the answers from the question: </p><ul><li> Does your employer provide resources to learn more about mental health issues and how to seek help?</li><li>Do you think that discussing a mental health issue with your employer would have negative consequences?</li><li>If they have a family history of mental illness?</li><li>If they Have sought treatment for a mental health condition?</li></ul><br>The answers are not really positive, It show that the subject of mental ilness is still a real taboo in the society', unsafe_allow_html=True)
			sns.catplot(x='seek_help', hue='mental_health_consequence', col='treatment', row='family_history', kind='count', data=mtech)
			st.pyplot()
			

		if st.sidebar.checkbox('Care options and Consequences'):
			st.markdown('<h3 style="margin-top: 30px; color: #d9534f; font-family: cursive"><b>Diagram showing the Care options and Consequences</b></h3>', unsafe_allow_html=True)		
			sns.catplot(x='benefits', hue='treatment', col='wellness_program', row='care_options',kind='count', data=mtech)
			st.pyplot()


	elif name == 'Suicide Statistics over years':
		data = pd.read_csv("data/who_suicide_statistics.csv")
		numeric_columns = data.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns

		# checkbox widget
		checkbox = st.sidebar.checkbox("Reveal data.")

		if checkbox:
		    # st.write(data)
		    st.dataframe(data=data)

		# create jointplot
		st.sidebar.markdown('<br>', unsafe_allow_html=True)
		st.sidebar.markdown('<h3><font color=‘#5cb85c>Joint plot</font></h3>', unsafe_allow_html=True)
		select_box3 = st.sidebar.selectbox(label='x', options=numeric_columns)
		select_box4 = st.sidebar.selectbox(label="y", options=numeric_columns)
		sns.jointplot(x=select_box3, y=select_box4, data=data)
		st.pyplot()


		# create histograms
		# st.sidebar.subheader("Histogram")
		st.sidebar.markdown('<br>', unsafe_allow_html=True)
		st.sidebar.markdown('<h3><font color=‘#5cb85c>Histogram</font></h3>', unsafe_allow_html=True)
		select_box3 = st.sidebar.selectbox(label="Feature", options=numeric_columns)
		histogram_slider = st.sidebar.slider(label="Number of Bins",min_value=5, max_value=100, value=30)
		sns.distplot(data[select_box3], bins=histogram_slider)
		st.pyplot()


		# create scatterplots
		# st.sidebar.subheader("Scatter plot setup")
		st.sidebar.markdown('<br>', unsafe_allow_html=True)
		st.sidebar.markdown('<h3><font color=‘#5cb85c>Scatter plot setup</font></h3>', unsafe_allow_html=True)
		# add select widget
		select_box1 = st.sidebar.selectbox(label='X axis', options=numeric_columns)
		select_box2 = st.sidebar.selectbox(label="Y axis", options=numeric_columns)
		sns.relplot(x=select_box1, y=select_box2, data=data)
		st.pyplot()

		


	else:
		st.balloons()
		"### About the application"
	x = wh
	# return x

get_dataset(dataset_name)

# st.write(wh.columns) displays columns


# wh.groupby(by=['age','sex'])['suicides_no'].sum().unstack().plot(kind='bar',stacked=True)
# a=wh.groupby(by=['age','sex'])['suicides_no'].sum().unstack().reset_index().melt(id_vars='age')
# sns.lineplot('year','suicides_no',hue='age',style='age',data=df,hue_norm=LogNorm(),palette="ch:2.5,.25",sort=False)
# st.pyplot()

