import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title("Interactive Normal Distribution")

# Sliders for mean and standard deviation
mean = st.slider("Select the Mean (μ)", -10.0, 10.0, 0.0)
std_dev = st.slider("Select the Standard Deviation (σ)", 0.5, 5.0, 1.0)

# Generate data
x = np.linspace(-20, 20, 400)
y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-((x - mean)**2) / (2 * std_dev**2))

# Plotting
fig, ax = plt.subplots()
ax.plot(x, y, color='blue')
ax.set_title("Normal Distribution Curve")
ax.set_xlabel("x")
ax.set_ylabel("Probability Density")
ax.grid(True)

# Show plot
st.pyplot(fig)
