# views.py

from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.http import JsonResponse


# views.py
from django.shortcuts import render
import requests

# views.py
from django.shortcuts import render
import requests

# views.py
from django.shortcuts import render
import requests

import requests

import requests

from django.shortcuts import render
import requests

# views.py
import json
import requests
from django.http import JsonResponse
from django.shortcuts import render

# views.py
import json
import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render
import requests

from django.shortcuts import render
import requests

import requests
from django.shortcuts import render

import requests
from django.shortcuts import render




from django.shortcuts import render,redirect

def index(request):
     if request.method == 'POST':
        city = request.POST.get('city', '')
        latitude = request.POST.get('latitude', None)
        longitude = request.POST.get('longitude', None)
        print(latitude)
        print(longitude)

        if latitude is not None and longitude is not None:
            # Process live location
            # For example, you can store the live location in the session
            request.session['latitude'] = latitude
            request.session['longitude'] = longitude
            return redirect('search_results')
        else:
            # Process city selection
            # Store the selected city in session
            request.session['selected_city'] = city
            # Redirect to the search results page
            return redirect('search_results')

     return render(request, 'index.html')

from django.shortcuts import render, redirect

def city_search(request):
    if request.method == 'POST':
        genre = request.POST.get('selected_genre', '')
       

            # Process city selection
            # Store the selected city in session
        request.session['selected_destination'] = genre
            # Redirect to the search results page
        return redirect('map')

    return render(request, 'search.html')

def input(request):
   
    start_latitude, start_longitude = get_coordinates(request.session.get('selected_city'))
    
       
    context = {
        'start_latitude': start_latitude,
        'start_longitude':start_longitude,
        'genr':request.session.get('selected_destination'),

        # Add more key-value pairs as needed
    }
    print(request.session.get('selected_destination'))

    return render(request, 'input.html',context)






def get_coordinates(address):
    # HERE Geocoding API endpoint
    url = "https://geocode.search.hereapi.com/v1/geocode"

    # API Key for HERE Geocoding API
    api_key = "FfI5QQOFQUYfxoHtkujlgYPHpUdxFubsDw_affYPZ3A"

    # Parameters for the API request
    params = {
        "q": address,
        "apiKey": api_key
    }

    try:
        # Send GET request to the API
        response = requests.get(url, params=params)
        data = response.json()

        # Extract latitude and longitude from the response
        if data and 'items' in data and data['items']:
            location = data['items'][0]['position']
            latitude = location['lat']
            longitude = location['lng']
            return latitude, longitude
        else:
            return None, None
    except Exception as e:
        # Handle exceptions
        print(f"Error fetching coordinates: {e}")
        return None, None

def get_driving_route(request):
    if request.method == 'POST':
        start_address = request.POST.get('start_address', '')
        print(start_address)

        end_address = request.POST.get('end_address', '')
        print(end_address)

        # Get coordinates for start and end addresses
        start_latitude, start_longitude = get_coordinates(start_address)
        print(start_latitude)
        print(start_longitude)

        end_latitude, end_longitude = get_coordinates(end_address)
        print(end_latitude)

        if start_latitude is None or start_longitude is None or \
           end_latitude is None or end_longitude is None:
            error_message = "Unable to retrieve coordinates for start or end address."
            return render(request, 'error.html', {'error_message': error_message})

        # API endpoint and parameters for finding driving route
        url = "https://trueway-directions2.p.rapidapi.com/FindDrivingRoute"
        querystring = {"stops": f"{start_latitude},{start_longitude};{end_latitude},{end_longitude}"}

        # API headers with RapidAPI key
        headers = {
            "X-RapidAPI-Key": "6dfb7d9827msh67772e560a03016p127156jsnb2f02115e771",
            "X-RapidAPI-Host": "trueway-directions2.p.rapidapi.com"
        }

        try:
            # Make a GET request to the API
            response = requests.get(url, headers=headers, params=querystring)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                route_data = response.json()
                print(route_data)
               

                # Pass the route data to the template for rendering
                return render(request, 'path.html', {'route_data': route_data})
            else:
                # If the request was not successful, return an error message
                error_message = f"Error: {response.status_code} - {response.reason}"
                return render(request, 'error.html', {'error_message': error_message})
        except Exception as e:  
            # Handle exceptions, such as network errors
            error_message = f"Error: {str(e)}"
            return render(request, 'error.html', {'error_message': error_message})
    else:
        return render(request, 'index.html')



# views.py

from django.shortcuts import render
import requests
import json

from django.shortcuts import render
import requests



from django.shortcuts import render
import requests

from django.shortcuts import render
import requests

# views.py
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def happening_places(request):
    url = "https://www.whatshot.in/delhi-ncr"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract relevant information from the webpage
    places = []
    for item in soup.find_all('div', class_='search-title'):
        name = item.find('h3').text.strip()
        address = item.find('div', class_='location').text.strip()
        places.append({'name': name, 'address': address})

    return render(request, 'city_info.html', {'places': places})



import requests
from django.shortcuts import render

def get_route(request):
    # Get latitude and longitude from request parameters
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')

    # Pass latitude and longitude to the HTML template
    context = {
        'latitude': latitude,
        'longitude': longitude,
    }
    
    # Check if latitude and longitude are provided
    if latitude is not None and longitude is not None:
       
        start_latitude, start_longitude = get_coordinates(request.session.get('selected_city'))
        
        
        url = "https://trueway-directions2.p.rapidapi.com/FindDrivingRoute"
        querystring = {"stops": f"{start_latitude},{start_longitude};{latitude},{longitude}"}
        
        # API headers with your RapidAPI key
        headers = {
            "X-RapidAPI-Key": "6dfb7d9827msh67772e560a03016p127156jsnb2f02115e771",
            "X-RapidAPI-Host": "trueway-directions2.p.rapidapi.com"
        }

        try:
            # Make a GET request to the API
            response = requests.get(url, headers=headers, params=querystring)
        
            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                route_data = response.json()

             
                # Pass the route data to the template for rendering
                return render(request, 'path.html', {'route_data': route_data})
                 
            else:
                # If the request was not successful, return an error message
                error_message = f"Error: {response.status_code} - {response.reason}"
                return render(request, 'error.html', {'error_message': error_message})
        except Exception as e:
            # Handle exceptions, such as network errors
            error_message = f"Error: {str(e)}"
            return render(request, 'error.html', {'error_message': error_message})

    # If latitude or longitude is not provided, render the HTML template with context
    return render(request, 'input.html', context)
