import pandas as pd
import matplotlib.pyplot as plt

def create_pie_plot(gender_beravages, gender):
    # Filter the gender_beravages for the specified gender
    gender_data = gender_beravages[gender_beravages['Gender'] == gender]

    # Count the occurrences of each favorite beverage
    beverage_counts = gender_data['Favorite Beverage'].value_counts()

    # Create a pie plot
    plt.figure(figsize=(8, 4))
    plt.pie(beverage_counts, labels=beverage_counts.index, autopct='%1.1f%%', startangle=140)

    # Set the title based on the gender
    if gender == 'M':
        plt.title('Favorite Beverages Distribution for Males')
    elif gender == 'F':
        plt.title('Favorite Beverages Distribution for Females')

    plt.axis('equal')
    # Equal aspect ratio ensures that the pie chart is circular
    plt.show()

# Load the dataset with the specified encoding
gender_beravages = pd.read_csv("Transformed Data Set - Sheet1.csv")

# Create two pie plots for males
create_pie_plot(gender_beravages, gender='M')
create_pie_plot(gender_beravages, gender='F')