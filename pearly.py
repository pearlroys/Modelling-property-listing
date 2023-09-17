import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Your DataFrame and sorting logic
# df = ...

# Create a figure and axis
fig, ax = plt.subplots()
fig.set_tight_layout(True)

# Define the update function for the animation
def update(year):
    ax.clear()
    ax.set_title(f'Year: {year}')
    
    # Filter data for the current year
    data = df[df['Year'] == year]
    
    # Plot lines for each country
    for country, group in data.groupby('Country'):
        ax.plot(group['Year'], group['Life expectancy '], label=country)
    
    ax.set_xlabel('Year')
    ax.set_ylabel('Life Expectancy')
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Create the animation
ani = FuncAnimation(fig, update, frames=df['Year'].unique(), repeat=False)

# Display the animation
plt.show()
