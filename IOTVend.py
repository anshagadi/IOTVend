import streamlit as st

# Initialize session state for button presses and cart management
if 'buy_pressed' not in st.session_state:
    st.session_state.buy_pressed = {"Ultrasonic Sensor": False, "IR Sensor": False, "PIR Sensor": False}
if 'sell_pressed' not in st.session_state:
    st.session_state.sell_pressed = {"Ultrasonic Sensor": False, "IR Sensor": False, "PIR Sensor": False}
if 'cart' not in st.session_state:
    st.session_state.cart = {"Ultrasonic Sensor": 0, "IR Sensor": 0, "PIR Sensor": 0}
if 'points' not in st.session_state:
    st.session_state.points = 0

# Set the title of the application
st.title("IOTVend")

# Sensor specifications
sensors = {
    "Ultrasonic Sensor": {
        "specs": "Range: 2cm - 400cm, Accuracy: ±3mm",
        "image": "https://raw.githubusercontent.com/pranshu131004/IOTVend/master/ultrasonic_sensor_image.jpg"  # Update with the actual image path
    },
    "IR Sensor": {
        "specs": "Range: 2cm - 30cm, Detection Angle: 35°",
        "image": "https://raw.githubusercontent.com/pranshu131004/IOTVend/master/pir_sensor_image.jpg"  # Update with the actual image path
    },
    "PIR Sensor": {
        "specs": "Range: 3m - 7m, Detection Angle: 120°",
        "image": "E:/WebD/IOTVend/pir_sensor_image.jpg"  # Update with the actual image path
    }
}

# Helper function to create sensor sections
def create_sensor_section(sensor_name, sensor_details, col):
    with col.expander(sensor_name, expanded=True):
        st.subheader(sensor_name)
        st.write(sensor_details["specs"])
        
        # Placeholder for sensor image
        st.image(sensor_details["image"], width=150)
        
        # Display Buy and Sell buttons
        if st.button(f"Buy {sensor_name}", key=f"buy_{sensor_name}"):
            st.session_state.buy_pressed[sensor_name] = True
            st.session_state.sell_pressed[sensor_name] = False
        
        if st.button(f"Sell {sensor_name}", key=f"sell_{sensor_name}"):
            st.session_state.sell_pressed[sensor_name] = True
            st.session_state.buy_pressed[sensor_name] = False
        
        if st.session_state.buy_pressed[sensor_name] or st.session_state.sell_pressed[sensor_name]:
            if st.button(f"Vend {sensor_name}", key=f"vend_{sensor_name}"):
                st.success(f"The {sensor_name} has been vended.")
                st.session_state.cart[sensor_name] += 1
                st.session_state.buy_pressed[sensor_name] = False
                st.session_state.sell_pressed[sensor_name] = False
            
            if st.button(f"ReVend {sensor_name}", key=f"revend_{sensor_name}"):
                st.success(f"The {sensor_name} has been revend.")
                st.session_state.cart[sensor_name] += 1
                st.session_state.buy_pressed[sensor_name] = False
                st.session_state.sell_pressed[sensor_name] = False

# Create three columns
col1, col2, col3 = st.columns(3)

# Create sections for each sensor in separate columns
create_sensor_section("Ultrasonic Sensor", sensors["Ultrasonic Sensor"], col1)
create_sensor_section("IR Sensor", sensors["IR Sensor"], col2)
create_sensor_section("PIR Sensor", sensors["PIR Sensor"], col3)

# Sidebar for cart and points management
st.sidebar.header("Cart")
for sensor, quantity in st.session_state.cart.items():
    st.sidebar.write(f"{sensor}: {quantity}")

if st.sidebar.button("Add to Cart"):
    total_points = 0
    for sensor, quantity in st.session_state.cart.items():
        if quantity > 0:
            st.sidebar.write(f"{sensor}: {quantity}")
            total_points += 50 * quantity  # Assuming all sensors work for simplicity
            # Reset the cart after adding to cart
            st.session_state.cart[sensor] = 0
    st.sidebar.write(f"Total Points: {total_points}")
    st.session_state.points += total_points

# Display total points
st.sidebar.markdown("---")
st.sidebar.write(f"Total Points: {st.session_state.points}")

# Footer
st.markdown("---")
st.write("IOTVend © 2024")
