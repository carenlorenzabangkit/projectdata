# Import necessary libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned data
day_data_cleaned = pd.read_csv('Bike-sharing-dataset/day.csv')

# Set the title of the dashboard
st.title("Bike Rental Analysis Dashboard")

# Section 1: Weather Conditions Impact
st.header("1. Impact of Weather Conditions on Bike Rentals")

# Average rentals by weather condition
weather_rental_analysis = day_data_cleaned.groupby('weathersit')['cnt'].mean().reset_index()
weather_rental_analysis.columns = ['Weather Condition', 'Average Rentals']

# Bar Plot for Average Rentals by Weather Condition
st.subheader("Average Rentals by Weather Condition")
fig1, ax1 = plt.subplots()
sns.barplot(x='Weather Condition', y='Average Rentals', data=weather_rental_analysis, ax=ax1)
ax1.set_xticklabels(['Clear', 'Misty', 'Light Rain/Snow', 'Heavy Rain/Fog'])
ax1.set_title('Average Bike Rentals by Weather Condition')
ax1.set_xlabel('Weather Condition')
ax1.set_ylabel('Average Rentals')
st.pyplot(fig1)

# Display Insight
st.write("""
**Insight**: The analysis reveals a clear correlation between weather conditions and bike rentals. 
Favorable weather leads to a significant increase in rentals, while adverse conditions result in lower counts. 
Promoting usage during pleasant weather is essential for rental services.
""")

# Section 2: Effect of Holidays and Weekends
st.header("2. Effect of Holidays and Weekends on Bike Rental Patterns")

# Average rentals by holiday
holiday_rental_analysis = day_data_cleaned.groupby('holiday')['cnt'].mean().reset_index()
holiday_rental_analysis.columns = ['Holiday', 'Average Rentals']

# Bar Plot for Average Rentals by Holiday
st.subheader("Average Rentals on Holidays vs Non-Holidays")
fig2, ax2 = plt.subplots()
sns.barplot(x='Holiday', y='Average Rentals', data=holiday_rental_analysis, ax=ax2)
ax2.set_xticklabels(['Non-Holiday', 'Holiday'])
ax2.set_title('Average Bike Rentals on Holidays vs Non-Holidays')
ax2.set_xlabel('Holiday')
ax2.set_ylabel('Average Rentals')
st.pyplot(fig2)

# Display Insight
st.write("""
**Insight**: The findings demonstrate that bike rentals are notably higher during holidays compared to non-holidays. 
This suggests a need for rental services to target marketing efforts during these times to boost revenue.
""")

# Average rentals by working day
workingday_rental_analysis = day_data_cleaned.groupby('workingday')['cnt'].mean().reset_index()
workingday_rental_analysis.columns = ['Working Day', 'Average Rentals']

# Bar Plot for Average Rentals by Working Day
st.subheader("Average Rentals on Working Days vs Weekends")
fig3, ax3 = plt.subplots()
sns.barplot(x='Working Day', y='Average Rentals', data=workingday_rental_analysis, ax=ax3)
ax3.set_xticklabels(['Weekend', 'Working Day'])
ax3.set_title('Average Bike Rentals on Working Days vs Weekends')
ax3.set_xlabel('Working Day')
ax3.set_ylabel('Average Rentals')
st.pyplot(fig3)

# Display Insight
st.write("""
**Insight**: The analysis shows that bike rentals are significantly higher on weekends compared to working days. 
This highlights the importance of optimizing bike availability during weekends to maximize usage.
""")
