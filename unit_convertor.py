import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Complete Unit Converter",
    page_icon="⚖",
    layout="centered"
)

# Inject custom CSS for styling
custom_css = """
<style>
    /* Overall page style */
    .stApp {
        background: linear-gradient(135deg, #4f2991, #7dc4ff);
        background-size: cover;
        color: #fff;
        font-family: 'Segoe UI', sans-serif;
    }
    /* Title and author styling */
    .title-header {
        text-align: center;
        font-size: 3em;
        margin-bottom: 0;
    }
    .author {
        text-align: center;
        color: red;
        margin-bottom: 1rem;
        padding-right: 2rem;
    }
    /* Button style */
    div.stButton > button {
        background-color: #7dc4ff;
        color: #fff;
        border: none;
        padding: 0.5em 1em;
        border-radius: 10px;
        font-weight: bold;
    }
    /* Sidebar style */
    .css-1d391kg { 
        background-color: rgba(0, 0, 0, 0.2);
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# App header
st.markdown("<h1 class='title-header'>Complete Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='author'>By Abdul Nabi</h3>", unsafe_allow_html=True)
st.markdown("### Convert Units Easily", unsafe_allow_html=True)

# Conversion type selection
conversion_type = st.selectbox("Select Conversion Type", ["Length", "Mass", "Temperature"])

# Conversion functions
def convert_length(value, from_unit, to_unit):
    # conversion factors relative to meter
    factors = {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Foot": 3.28084,
        "Inch": 39.3701,
    }
    # Convert value to meters then to target unit
    value_in_meters = value / factors[from_unit]
    result = value_in_meters * factors[to_unit]
    return result

def convert_mass(value, from_unit, to_unit):
    # conversion factors relative to kilogram
    factors = {
        "Kilogram": 1,
        "Gram": 1000,
        "Pound": 2.20462,
        "Ounce": 35.274,
    }
    value_in_kg = value / factors[from_unit]
    result = value_in_kg * factors[to_unit]
    return result

def convert_temperature(value, from_unit, to_unit):
    # Temperature conversion formulas
    if from_unit == to_unit:
        return value
    # Convert from unit to Celsius
    if from_unit == "Celsius":
        temp_c = value
    elif from_unit == "Fahrenheit":
        temp_c = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        temp_c = value - 273.15
    # Convert from Celsius to target unit
    if to_unit == "Celsius":
        return temp_c
    elif to_unit == "Fahrenheit":
        return (temp_c * 9/5) + 32
    elif to_unit == "Kelvin":
        return temp_c + 273.15

# Display appropriate inputs based on conversion type
if conversion_type == "Length":
    units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Foot", "Inch"]
    value = st.number_input("Enter value", min_value=0.0, value=1.0, step=0.1)
    from_unit = st.selectbox("From", units, key="length_from")
    to_unit = st.selectbox("To", units, key="length_to")
    if st.button("Convert", key="length_button"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Mass":
    units = ["Kilogram", "Gram", "Pound", "Ounce"]
    value = st.number_input("Enter value", min_value=0.0, value=1.0, key="mass_value", step=0.1)
    from_unit = st.selectbox("From", units, key="mass_from")
    to_unit = st.selectbox("To", units, key="mass_to")
    if st.button("Convert", key="mass_button"):
        result = convert_mass(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    value = st.number_input("Enter value", value=0.0, key="temp_value")
    from_unit = st.selectbox("From", units, key="temp_from")
    to_unit = st.selectbox("To", units, key="temp_to")
    if st.button("Convert", key="temp_button"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

# Save conversion history in session state (simulating a stream list)
if "history" not in st.session_state:
    st.session_state.history = []

# Button to save the latest conversion (if a conversion result is shown)
if st.button("Save Conversion"):
    try:
        if conversion_type == "Length":
            conv_str = f"{value} {from_unit} → {result:.4f} {to_unit}"
        elif conversion_type == "Mass":
            conv_str = f"{value} {from_unit} → {result:.4f} {to_unit}"
        elif conversion_type == "Temperature":
            conv_str = f"{value} {from_unit} → {result:.2f} {to_unit}"
        st.session_state.history.append(conv_str)
        st.success("Conversion saved!")
    except Exception as e:
        st.error("Please perform a conversion first.")

# Display conversion history as a list (stream list)
if st.session_state.history:
    st.markdown("#### Conversion History")
    for item in st.session_state.history:
        st.write("- " + item)
