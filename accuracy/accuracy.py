import matplotlib.pyplot as plt

# Data: Model names and their accuracy percentages
models = ['Basic Validation', 'Supervised Learning', 'Deep Image Recognition', 'Overall Accuracy']
accuracy = [98,92,85,91]  # You can replace these values with your actual accuracy percentages

# Create a bar graph
plt.figure(figsize=(10, 6))
plt.bar(models, accuracy, color=['orange', 'blue', 'green', 'red'])

# Add titles and labels
plt.title('Accuracy of GIF Malware Detection System', fontsize=14)
plt.xlabel('Models/Stages', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)
plt.ylim(80, 100)  # Set y-axis limit to focus on the accuracy range

# Display the accuracy values on top of the bars
for i, v in enumerate(accuracy):
    plt.text(i, v + 1, str(v) + '%', ha='center', fontsize=12)

# Show the plot
plt.show()
