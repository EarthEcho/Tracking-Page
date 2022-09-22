#Importing needed libraries
import colorama
import streamlit as st
import time
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('seaborn')
from colorama import Style, Fore, Back #might need to pip install colorama
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv("carbon_footprint.csv")

def main():
    st.title("Welcome To Our Tracking Page")
    st.header("This Page provides live analysis of various individual actions that contributes to carbon emmission")
    st.text("Switch to the fullscreen mode by clicking the three small lines on the top right and selecting settings")

    st.write(f"**Total Visits:** {len(data)}")

    plt.subplot(221)
    data['age_group'].value_counts().plot(kind = 'bar', title = 'Age distribution of visitors', figsize = (20, 12))
    plt.xticks(rotation = 360)
    plt.subplot(222)
    data['work_stat'].value_counts().plot(kind = 'bar', title = 'Work Division Of Visitors')
    plt.xticks(rotation = 360)
    plt.subplot(223)
    data['travel_type'].value_counts().plot(kind = 'pie', title = 'Means of transportation', autopct='%1.1f%%', label = '')
    plt.subplot(224)
    data['travel_time'].value_counts().plot(kind = 'bar', title = 'Time spent on travel')
    plt.xticks(rotation = 360)
    st.pyplot()

    st.text("From the age of 15, the carbon footprint grows in all categories (home, transport, food, and living expenses), peaking between the ages of 45 and 64.")
    st.text("The transport sector is responsible for emitting more greenhouse gases than any other")
    
    plt.subplot(221)
    data['how_engaged'].value_counts().plot(kind = 'pie', title = 'Engagement with the issue of climate change', figsize = (15, 12), label='', autopct='%1.1f%%')
    plt.subplot(222)
    data['carbon_measure'].value_counts().plot(kind = 'bar', title = 'Individual measurement of carbon footprint(Personal opinion)')
    plt.xticks(rotation = 360)
    plt.subplot(223)
    data['change_habit'].value_counts().plot(kind = 'bar', title = 'Possibility of changing habits with more information climate change')
    plt.xticks(rotation = 360)
    plt.subplot(224)
    data['carbon_reduction'].value_counts().plot(kind = 'pie', title = 'Individual careful state on maintaining a good carbon footprint', autopct='%1.1f%%', label = '')
    st.pyplot()

    st.write('**Some Individual motivation to reducing carbon footprint are:**')
    st.write(str(data['motivation'].unique()[:10]))


    plt.subplot(221)
    data['encourage_others'].value_counts().plot(kind = 'bar', title = 'Encourage others to reduce their carbon footprint?', figsize = (15, 12))
    plt.xticks(rotation = 360)
    plt.subplot(222)
    data['location'].value_counts()[:10].plot(kind = 'bar', title = 'Top location with highest visitors')
    plt.xticks(rotation = 360)
    plt.subplot(223)
    highest_travel_type = str(data['travel_type'].value_counts()[[0]]).split()[0]
    data[data['travel_type'] == highest_travel_type]['location'].value_counts().plot(
    kind = 'bar', title = f'Distribution of people that use the highest travel type ({highest_travel_type}) in each locations(Top 10)')
    plt.xticks(rotation = 360)
    plt.subplot(224)
    data[data['how_engaged'] == 'Excellently Engaged']['location'].value_counts()[:10].plot(kind = 'bar', title = f'Distribution of locations that are Excellently engaged in the issue of climate change')
    plt.xticks(rotation = 360)
    st.pyplot()

    st.text("The activities of people living in a particurly environment can contribute largely to their carbon footprint. Some locations might engage in practices that other environment don't practices")

    plt.subplot(221)
    data[data['how_engaged'] == 'Moderately Engaged']['location'].value_counts()[:10].plot(
    kind = 'bar', title = f'Distribution of locations that are Moderately engaged in the issue of climate change', figsize = (15, 12))
    plt.xticks(rotation = 360)
    plt.subplot(222)
    data[data['how_engaged'] == 'Poorly Engaged']['location'].value_counts()[:10].plot(
    kind = 'bar', title = f'Distribution of locations that are poorly engaged in the issue of climate change')
    plt.xticks(rotation = 360)
    plt.subplot(223)
    data['info_source'].value_counts()[:10].plot(
    kind = 'bar', title = 'Information source on carbon reduction')
    plt.xticks(rotation = 360)
    plt.subplot(224)
    data[data['carbon_measure'] == 'Very Low']['location'].value_counts()[:10].plot(
    kind = 'bar', title = f'Distribution of locations that have very low carbon footprint', figsize = (15, 12))
    plt.xticks(rotation = 360)
    st.pyplot()

    st.text("The validity of the sources providing the carbon reduction information and source of measurement matters alot in tackling carbon emmission ")

    if st.button("See More"):
      st.write('**Some Individual difficulty in reducing carbon footprint**\n')
      st.write(str(data['difficulty'].unique()[:10]))

      plt.subplot(221)
      data[data['carbon_measure'] == 'Moderate']['location'].value_counts()[:10].plot(
      kind = 'bar', title = f'Distribution of locations that have Moderate carbon footprint', figsize = (15, 12))
      plt.xticks(rotation = 360)
      plt.subplot(222)
      data[data['carbon_measure'] == 'Very High']['location'].value_counts()[:10].plot(
      kind = 'bar', title = f'Distribution of locations that have very high carbon footprint')
      plt.xticks(rotation = 360)
      plt.subplot(223)
      data[data['carbon_reduction'] == 'Not Careful']['location'].value_counts()[:10].plot(
      kind = 'bar', title = f'Distribution of locations that are not bothered about carbon footprint reduction', figsize = (15, 12))
      plt.xticks(rotation = 360)
      plt.subplot(224)
      data[data['carbon_reduction'] == 'Careful']['location'].value_counts()[:10].plot(
      kind = 'bar', title = f'Distribution of locations that are moderately bothered about carbon footprint reduction', figsize = (15, 12))
      plt.xticks(rotation = 360)
      st.pyplot()

      st.text("""Individuals that are concern about climate change and carbon emmission can easily change their livestyle to reduce their carbon footprint. 
While proper enlightenment can be done in areas with little or no concern for carbon emmission """)
  
      plt.subplot(221)
      data[data['carbon_reduction'] == 'Very Careful']['location'].value_counts()[:10].plot(
      kind = 'bar', title = f'Distribution of locations that are highly bothered about carbon footprint reduction', figsize = (15, 12))
      plt.xticks(rotation = 360)
      plt.subplot(222)
      data[data['carbon_measure'] == 'Very Low']['week_day'].value_counts()[:10].plot(
      kind = 'bar', title = f'Distribution of week day in which there is ver low carbon measurement', figsize = (15, 12))
      plt.xticks(rotation = 360)
      plt.subplot(223)
      data[data['carbon_measure'] == 'Moderate']['week_day'].value_counts()[:10].plot(
      kind = 'bar', title = f'Distribution of week day in which there is Moderate carbon measurement', figsize = (15, 12))
      plt.xticks(rotation = 360)
      plt.subplot(224)
      data[data['carbon_measure'] == 'Very High']['week_day'].value_counts()[:10].plot(
      kind = 'bar', title = f'Distribution of week day in which there is high carbon measurement', figsize = (15, 12))
      plt.xticks(rotation = 360)
      st.pyplot()

      st.text("Knowing the week day and month in which there is high carbon emmission can easily allow for rules, restrictions and cautios on those days and months")

      plt.subplot(221)
      data[data['carbon_measure'] == 'Very Low']['month'].value_counts()[:10].plot(
      kind = 'bar', title = f'Distribution of month in which there is very low carbon measurement', figsize = (15, 12))
      plt.xticks(rotation = 360)
      plt.subplot(222)
      data[data['carbon_measure'] == 'Very High']['month'].value_counts()[:10].plot(
      kind = 'bar', title = f'Distribution of month in which there is high carbon measurement', figsize = (15, 12))
      plt.xticks(rotation = 360)
      st.pyplot()

      st.write("**Always keep your carbon footprint on the low. Thanks for using our service**")


if __name__ == '__main__':
  main()