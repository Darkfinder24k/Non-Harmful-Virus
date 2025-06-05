import streamlit as st
import geocoder
import time
import os
import re
import random
import threading
from PIL import Image

# --- Streamlit Page Settings ---
st.set_page_config(page_title="Hi! There", layout="centered")
st.title("🌐 Welcome to Stimulate")

# --- Fetch IP and Location Info ---
g = geocoder.ip('me')
location_data = g.geojson['features'][0]['properties'] if g and g.ok else {}
ip_address = g.ip if g and g.ok else None

# --- First Innocent Message ---
st.markdown("## 😎 Welcome! Nothing special here...")
st.markdown("### 🧐 Scroll down to see something crazy... 👀")
st.markdown("<br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)

# --- Surprise Section (IP and Location) ---
st.subheader("🎯 Surprise! Here's What We Found:")

if ip_address:
    st.success(f"**Your IP Address is:** `{ip_address}`")
else:
    st.error("❌ Could not retrieve your IP address.")

if location_data:
    st.write(f"**City:** {location_data.get('city', 'Unknown')}")
    st.write(f"**Region:** {location_data.get('region', 'Unknown')}")
    st.write(f"**Country:** {location_data.get('country', 'Unknown')}")
    st.write(f"**Latitude:** {location_data.get('lat', 'Unknown')}")
    st.write(f"**Longitude:** {location_data.get('lng', 'Unknown')}")
else:
    st.warning("Location details not available.")

# --- More Scroll Down Space ---
st.markdown("<br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
st.markdown("### 📡 Scroll down to also see your Wi-Fi History...")

# --- Wi-Fi History Section ---
st.subheader("🔍 Your Wi-Fi History:")
try:
    st.warning("Wi-Fi information cannot be accessed in this cloud environment.")
except Exception as e:
    st.error(f"❌ An error occurred: {e}")

# --- Scroll More ---
st.markdown("<br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
st.markdown("### 🔥 Scroll down even more for the final surprise!")

# --- Final Shock Button ---
if st.button("👻 Click Here for the Final Shock!", key="final_shock_button"):
    st.subheader("🔐 Saved Wi-Fi Profiles & Passwords:")
    st.warning("This feature is disabled in the cloud version for security reasons.")
    
    # --- Ghost Flicker Placeholder ---
    try:
        st.markdown("### 👁️ Screen glitch initiated...")
        for i in range(3):
            st.markdown(f"👻 Flicker {i+1}")
            time.sleep(1.2)
    except Exception as e:
        st.error(f"💀 Visual effect failed: {e}")

    # --- Mouse Movement Prank Placeholder ---
    try:
        st.markdown("### 🖱️ Your mouse would be possessed here... if this weren't running in the cloud 😈")
    except Exception as e:
        st.error(f"❌ Prank failed: {e}")
