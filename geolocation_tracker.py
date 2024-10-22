import requests
import folium
import webbrowser
import re

# Function to validate IP address
def is_valid_ip(ip):
    # Regular expression for validating an IP address
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return pattern.match(ip) is not None


# Function to get geolocation data for a given IP address
def get_geolocation(ip_address=None):
    try:
        # If no IP is provided, use the public IP of the user
        url = (
            f"https://ipinfo.io/{ip_address}/json"
            if ip_address
            else "https://ipinfo.io/json"
        )

        # Request geolocation data from the API
        response = requests.get(url)
        data = response.json()

        # Extracting location data
        location = data["loc"]  # Latitude and Longitude
        city = data.get("city", "N/A")
        country = data.get("country", "N/A")
        return location, city, country
    except Exception as e:
        print(f"Error fetching geolocation data: {e}")
        return None, None, None  # Ensures it returns three values


# Function to display the location on a map
def display_map(location, city, country):
    # Split the location into latitude and longitude
    lat, lon = map(float, location.split(","))

    # Create a map centered around the given location
    user_map = folium.Map(location=[lat, lon], zoom_start=12)

    # Add a marker to the map at the location
    folium.Marker([lat, lon], popup=f"{city}, {country}").add_to(user_map)

    # Save the map to an HTML file
    file_path = "user_location_map.html"
    user_map.save(file_path)

    # Inform the user that the map is being opened
    print("Map generated! Opening in your browser...")

    # Automatically open the file in the browser
    webbrowser.open(file_path)


# Main execution loop
while True:
    ip_address = input(
        "Enter an IP address (or leave blank to use your current public IP): "
    )

    if ip_address and not is_valid_ip(ip_address):
        print(
            "The format of the IP address entered is invalid. Please ensure it follows the format '134.xxx.xxx.215' and try again."
        )
        continue  # Prompt for a new IP address

    location, city, country = get_geolocation(ip_address)

    if location:
        # Show geolocation info in the console
        print(f"Location: {location}, City: {city}, Country: {country}")

        # Display the map
        display_map(location, city, country)
        break  # Exit the loop after successful execution
    else:
        print("Unable to retrieve geolocation data. Please try again.")