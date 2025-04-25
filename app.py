import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

st.set_page_config(page_title="Probability Visualizer")

# App Title
st.title("Interactive Probability Distribution Visualizer")

# Dropdown menu to choose distribution
dist_type = st.selectbox("Choose a Distribution:", ["Normal", "Bimodal", "Poisson", "Compare All"])

# Prepare the figure
fig, ax = plt.subplots()


x = np.linspace(-20, 20, 500)

if dist_type == "Normal":
    mu = st.slider("Mean (μ)", -10.0, 10.0, 0.0)
    sigma = st.slider("Standard Deviation (σ)", 0.5, 5.0, 1.0)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
    ax.plot(x, y, color="blue")
    ax.set_title("Normal Distribution")

elif dist_type == "Bimodal":
    mu1 = st.slider("First Peak Mean (μ₁)", -10.0, 0.0, -3.0)
    mu2 = st.slider("Second Peak Mean (μ₂)", 0.0, 10.0, 3.0)
    sigma = st.slider("Standard Deviation (σ)", 0.5, 5.0, 1.0)
    y1 = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu1) ** 2) / (2 * sigma ** 2))
    y2 = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu2) ** 2) / (2 * sigma ** 2))
    y = (y1 + y2) / 2
    ax.plot(x, y, color="green")
    ax.set_title("Bimodal Distribution")

elif dist_type == "Poisson":
    lambda_ = st.slider("Lambda (λ)", 1, 20, 5)
    x_vals = np.arange(0, 30)
    y_vals = poisson.pmf(x_vals, mu=lambda_)
    ax.bar(x_vals, y_vals, color="orange")
    ax.set_xlim(0, 30)
    ax.set_title("Poisson Distribution")
    ax.set_xlabel("Number of Events (k)")

elif dist_type == "Compare All":
    st.markdown("### 🎯 Adjust and Compare All Distributions")

    # Create layout: narrow column for sliders, wide column for graph
    col1, col2 = st.columns([1, 3])  # 1/4 left (sliders), 3/4 right (graph)

    with col1:
        st.markdown("#### 🎛 Parameters")
        mu = st.slider("Normal Mean (μ)", -10.0, 10.0, 0.0)
        sigma = st.slider("Normal Std Dev (σ)", 0.5, 5.0, 1.0)
        mu1 = st.slider("Bimodal Peak 1 (μ₁)", -10.0, 0.0, -3.0)
        mu2 = st.slider("Bimodal Peak 2 (μ₂)", 0.0, 10.0, 3.0)
        lambda_ = st.slider("Poisson Rate (λ)", 1, 20, 5)

    with col2:
        fig_compare, ax_compare = plt.subplots(figsize=(10, 5))  # Wider graph

        # Normal
        y_norm = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
        ax_compare.plot(x, y_norm, label="Normal", color="blue")

        # Bimodal
        sigma_bi = 1.0
        y1 = (1 / (sigma_bi * np.sqrt(2 * np.pi))) * np.exp(-((x - mu1) ** 2) / (2 * sigma_bi ** 2))
        y2 = (1 / (sigma_bi * np.sqrt(2 * np.pi))) * np.exp(-((x - mu2) ** 2) / (2 * sigma_bi ** 2))
        y_bi = (y1 + y2) / 2
        ax_compare.plot(x, y_bi, label="Bimodal", color="green")

        # Poisson
        x_p = np.arange(0, 30)
        y_p = poisson.pmf(x_p, mu=lambda_)
        ax_compare.bar(x_p, y_p, color="orange", alpha=0.5, label="Poisson")

        ax_compare.set_title("Comparison: Normal vs Bimodal vs Poisson")
        ax_compare.set_xlim(-10, 30)
        ax_compare.set_ylabel("Probability")
        ax_compare.grid(True)
        ax_compare.legend()

        st.pyplot(fig_compare)

# Shared styling
ax.set_ylabel("Probability")
ax.grid(True)

# Show the plot
st.pyplot(fig)

# Optional description to help students understand
with st.expander("📘 Learn About This Distribution"):
    if dist_type == "Normal":
        st.markdown("Used for natural measurements like height or test scores. Symmetrical and centered around the mean.")
    elif dist_type == "Bimodal":
        st.markdown("Used when there are two groups in the data. Example: Two different teaching styles in a class.")
    elif dist_type == "Poisson":
        st.markdown("Used for counting how often something happens in a fixed time or space. Example: emails per hour.")

