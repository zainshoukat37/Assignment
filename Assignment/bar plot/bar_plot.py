import matplotlib.pyplot as plt
import pandas as pd

def generate_bar_chart(data, category_column, total_column):
    # Group the data by the category_column and calculate the sum of total_column within each category
    grouped_data = data.groupby(category_column)[total_column].sum()

    # Create a bar chart
    plt.figure(figsize=(10, 6))

    # Add a label for the legend
    plt.bar(grouped_data.index, grouped_data, color='#000080', label='Total Sales')  # Use navy blue color

    # X-axis label
    plt.xlabel(category_column, fontsize=14)

    # Y-axis label
    plt.ylabel('Total Sales', fontsize=14)

    # Chart title
    plt.title(f'Total Sales by {category_column}', fontsize=16)
    plt.xticks(rotation=45)

    # Add a legend
    plt.legend()

    # Show the chart
    plt.tight_layout()
    plt.show()

# Read the dataset into a DataFrame
df = pd.read_csv("supermarket_sales.csv")

# Call the function to generate the bar chart
generate_bar_chart(df, category_column="Product line", total_column="Total")
generate_bar_chart(df, category_column="City", total_column="Total")
generate_bar_chart(df, category_column="Customer type", total_column="Total")
