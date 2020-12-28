import requests

def get_letters():
    response = requests.get("http://localhost:8666/letters/freq")
    return response.json()

def get_clusters():
    response = requests.get("http://localhost:8666/clusters")