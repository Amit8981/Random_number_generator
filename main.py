import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, poisson, expon

#Function to generate random numbers
def generate_random_numbers(dist, params):
    if dist == "Normal":
        return norm.rvs(loc=params["mean"], scale=params["std_dev"], size=params["size"])
    elif dist == "Poisson":
        return poisson.rvs(mu=params["lambda"], size=params["size"])
    elif dist == "Exponential":
        return expon.rvs(scale=1/params["lambda"], size=params["size"])

#Function to plot histogram
def plot_histogram(numbers, dist):
    fig, ax = plt.subplots()
    ax.hist(numbers, bins=30, density=True)
    ax.set_title(f"Histogram of {dist} Distribution")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    return fig

#Main app
st.title("Random Number Generator")

dist = st.selectbox("Select Distribution", ["Normal", "Poisson", "Exponential"])

if dist == "Normal":
    mean = st.number_input("Mean", value=0.0)
    std_dev = st.number_input("Standard Deviation", value=1.0)
    params = {"mean": mean, "std_dev": std_dev}
elif dist == "Poisson":
    lambda_ = st.number_input("Lambda", value=1.0)
    params = {"lambda": lambda_}
elif dist == "Exponential":
    lambda_ = st.number_input("Lambda", value=1.0)
    params = {"lambda": lambda_}

size = st.number_input("Size", value=1000)

if st.button("Generate"):
    params["size"] = size
    numbers = generate_random_numbers(dist, params)
    st.write(f"Mean : {round(np.mean(numbers),2)}")
    st.write(f"Median : {round(np.median(numbers),2)}")
    st.write(f"SD : {round(np.std(numbers),2)}")
    st.write(f"Min : {round(np.min(numbers),2)}")
    st.write(f"Max : {round(np.max(numbers),2)}")
    fig = plot_histogram(numbers, dist)
    st.pyplot(fig)
