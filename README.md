**Geolocation Tracker**

**Overview**
The Geolocation Tracker is a Python script that fetches geolocation information based on an IP address. It provides users with the option to enter a specific IP address or use their own public IP. The location is displayed on a map generated using the Folium library.

**Features**
Fetches geolocation data for a given IP address or the user's public IP.
Displays the location on an interactive map.
Validates the IP address format to ensure accurate results.
Opens the generated map automatically in the user's web browser.

**Technologies Used**
Python
Requests library for making HTTP requests
Folium for creating interactive maps
Regular expressions for IP address validation

**Installation**
To run the Geolocation Tracker, follow these steps:

Clone the repository: git clone https://github.com/abdul-kareem-2410/CodeAlpha_GeolocationTracker.git

Navigate to the project directory: cd CodeAlpha_GeolocationTracker

Install the required libraries: You can install the required libraries using pip: pip install requests folium

**Usage**
Run the script: python geolocation_tracker.py

Enter an IP address when prompted (or leave blank to use your current public IP).

The program will fetch the geolocation data and display it on a map, which will open automatically in your default web browser.

**Example**
When you enter a valid IP address, the output will display the location, city, and country, along with a map showing the exact location.

Location: 33.7215, 73.0433, City: Islamabad, Country: PK

**License**
This project is licensed under the MIT License. See the LICENSE file for details.

**Author**
Abdul Kareem 
abdulkareemp.2410@gmail.com
