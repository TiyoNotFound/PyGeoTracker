import requests
from tabulate import tabulate
import folium

class IPLocationFinder:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "http://ipinfo.io/"

    def get_location(self, ip_address):
        try:
            response = requests.get(f"{self.api_url}{ip_address}?token={self.api_key}")
            data = response.json()

            if 'error' in data:
                print(f"Error: {data['error']['message']}")
                return None

            location_info = [
                ('IP Address', data['ip']),
                ('City', data['city']),
                ('Region', data['region']),
                ('Country', data['country']),
                ('Latitude', data['loc'].split(',')[0]),
                ('Longitude', data['loc'].split(',')[1]),
                ('ISP', data.get('org', 'N/A')),
                ('Connection Type', data.get('connection', 'N/A')),
            ]
            return location_info

        except Exception as e:
            print(f"Error: {e}")
            return None

def print_formatted_output(location_info):
    if location_info:
        print("\nLocation Information:")
        table = tabulate(location_info, tablefmt="fancy_grid", numalign="left", stralign="right")
        print(table)
    else:
        print("Unable to fetch location information.")

def visualize_location_on_map(latitude, longitude):
    map_center = [float(latitude), float(longitude)]
    location_map = folium.Map(location=map_center, zoom_start=10)
    folium.Marker(location=map_center, popup='Location', icon=folium.Icon(color='blue')).add_to(location_map)
    location_map.save("location_map.html")
    print("Location map saved as location_map.html")

if __name__ == "__main__":
    api_key = "d7dadafb7f7a25"  # Replace with your ipinfo.io API key
    ip_address = input("Enter an IP address: ")

    location_finder = IPLocationFinder(api_key)
    location_info = location_finder.get_location(ip_address)

    print_formatted_output(location_info)

    if location_info:
        latitude = location_info[4][1]
        longitude = location_info[5][1]
        visualize_location_on_map(latitude, longitude)