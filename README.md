
# PyGeoTracker

PyGeoTracker is a Python-based IP geolocation tool that enables users to track the location of an IP address, visualize it on a map, and log the information in separate text files based on the city name.

## Features

1. **Enter IP Address:**
   - Users can input an IP address to get detailed information about its geolocation.

2. **Visualize on Map:**
   - PyGeoTracker generates an interactive map showing the location of the specified IP address.

3. **City-based Logs:**
   - Information about each IP address is logged in separate text files named after the city.

4. **File Logs:**
   - View a list of files created along with options to read the content of specific files.

## Getting Started

### Prerequisites

- Python 3.x

### Install Required Packages

```bash
pip install -r requirements.txt
```

### Get API Key

1. Visit [ipinfo.io](https://ipinfo.io/signup) and sign up for a free account.
2. Obtain your API key from the account dashboard.

### Replace the API Key

To use PyGeoTracker with your own API key, follow these steps:

1. Open the `pygeotracker.py` file in a text editor of your choice.

2. Locate the `api_key` variable at the beginning of the script:

    ```python
    api_key = "d7dadafb7f7a25"  # Replace with your actual API key
    ```

3. Replace the placeholder value (`"d7dadafb7f7a25"`) with your ipinfo.io API key.

    ```python
    api_key = "your_actual_api_key"
    ```

4. Save the file.

Now, PyGeoTracker will use your own API key for fetching IP geolocation information.

**Note:** Keep your API key confidential and avoid sharing it publicly.

### Usage

```bash
python pygeotracker.py
```

Follow the on-screen prompts to use the PyGeoTracker features.

## Advantages

- **City-based Logging:**
  - Organized logs based on city names for easy retrieval and analysis.

- **Interactive Maps:**
  - Visualize geolocation on an interactive map using the Folium library.

- **Flexible and Extendable:**
  - Open-source project that can be customized or extended to suit specific requirements.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
```

Make sure to update the sections with your actual details and any additional information that might be relevant to users.
