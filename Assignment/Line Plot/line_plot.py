import pandas as pd
import matplotlib.pyplot as plt

def covid_analysis(covid_data, Country_data):
    """
    This function takes two arguments, monthly Covid data and a selected state.
    And visualizes the Covid state-wise data analysis with the help of a line plot for the 3rd month.

    Parameters
    ----------
    covid_data : pd.DataFrame
        Monthly covid data read through pandas.
    Country_data : str
        Name of the state to be analyzed with data.

    Returns
    -------
    None.
    """

    # Declaring Country_title variable to use it in the title() function
    Country_title = str(Country_data)

    # Segregating data for a selected state
    Country_data = covid_data[covid_data['Country'] == Country_data]

    # Convert the 'Date' column to datetime
    Country_data['Date'] = pd.to_datetime(Country_data['Date'])

    # Filter data for the 3rd month (March)
    Country_data = Country_data[Country_data['Date'].dt.month == 4]

    # Extract day and month from the 'Date' column
    Country_data['DayMonth'] = Country_data['Date'].dt.strftime('%d-%m')

    # Adjusting the figure size to 10x7 inches
    plt.figure(figsize=(10, 7))

    # Plotting the data for Total Cases, Total Recovery cases, Total Death Cases during 4th month
    plt.plot(Country_data['DayMonth'], Country_data['Total Case'], label="Total Cases", marker='o')
    plt.plot(Country_data['DayMonth'], Country_data['Total Recovery'], label="Total Recovery Cases", marker='o')
    plt.plot(Country_data['DayMonth'], Country_data['Total Death'], label="Total Deaths", marker='o')

    # Setting the x-axis label to "Day-Month"
    plt.xlabel("Day-Month")

    # Rotating the x-axis tick labels by 45 degrees for better readability
    plt.xticks(rotation=45)

    # Setting the y-axis label to "Number of Covid Cases"
    plt.ylabel("Number of Covid Cases")

    # Adding a title to the plot based on the input selected Country
    plt.title(f'Covid Analysis of {Country_title} in April 2019')

    # Adding a legend to the plot to display labels
    plt.legend()

    # To show the plot
    plt.show()


# Read the dataset into a DataFrame
covid_data = pd.read_excel('COVID-19_Data_Europe.xlsx')

# Call the covid_analysis function for the 4th month for the states of Malta and Italy
covid_analysis(covid_data, 'United Kingdom')
covid_analysis(covid_data, 'Albania')
