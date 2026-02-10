import streamlit as st

st.set_page_config(page_title="Airport Wi-Fi Security Awareness", layout="centered")

st.title("✈️ Airport Wi-Fi Security Awareness Tool")
st.write("Educational simulation of public Wi-Fi risks")

scenario = st.selectbox(
    "Choose a scenario",
    [
        "Evil Twin Wi-Fi",
        "Credential Harvesting",
        "Man-in-the-Middle Attack"
    ]
)

if scenario == "Evil Twin Wi-Fi":
    st.write("⚠️ Fake Wi-Fi hotspots imitate legitimate airport networks.")
    st.code("airbase-ng -e Free_Airport_WiFi wlan0mon", language="bash")

elif scenario == "Credential Harvesting":
    st.write("⚠️ Attackers trick users into fake login portals.")
    st.code("setoolkit", language="bash")

elif scenario == "Man-in-the-Middle Attack":
    st.write("⚠️ Traffic interception on unsecured networks.")
    st.code("ettercap -T -q -i wlan0 -M arp:remote", language="bash")

st.success("Defensive Tip: Always use VPNs and HTTPS on public Wi-Fi.")
