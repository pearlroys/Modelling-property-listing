# Sort the DataFrame by 'Year' for animation
df_sorted = df.sort_values(by='Year')

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(df_sorted['Year'].min(), df_sorted['Year'].max())
ax.set_ylim(df_sorted['Life expectancy '].min(), df_sorted['Life expectancy '].max())
line, = ax.plot([], [], lw=2)

# Define the initialization function
def init():
    line.set_data([], [])
    return line,

# Define the update function for the animation
def update(frame):
    data = df_sorted[df_sorted['Year'] == frame]
    x = data['Year']
    y = data['Life expectancy ']
    line.set_data(x, y)
    ax.set_title(f'Year: {frame}')
    return line,

# Create the animation
anim = FuncAnimation(fig, update, frames=df_sorted['Year'].unique(), init_func=init, blit=True)

# Display the animation
plt.show()