import requests
import math


# -----------------------------
# Distance Calculator
# -----------------------------
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 2)


# -----------------------------
# Overpass Request (Safe)
# -----------------------------
def fetch_overpass(query):

    overpass_urls = [
        "https://overpass-api.de/api/interpreter",
        "https://lz4.overpass-api.de/api/interpreter"
    ]

    for url in overpass_urls:
        try:
            response = requests.post(url, data=query, timeout=25)

            if response.status_code != 200:
                continue

            if not response.text.strip():
                continue

            return response.json()

        except Exception:
            continue

    return None


# -----------------------------
# Main Function
# -----------------------------
def get_nearby_places(user_lat, user_lng, radius_km=10, hospital_type="all"):

    radius_meters = radius_km * 1000

    if hospital_type == "hospital":
        tag_filter = '["amenity"="hospital"]'
    elif hospital_type == "clinic":
        tag_filter = '["amenity"="clinic"]'
    else:
        tag_filter = '["amenity"~"hospital|clinic"]'

    query = f"""
    [out:json][timeout:25];
    (
      node{tag_filter}(around:{radius_meters},{user_lat},{user_lng});
      way{tag_filter}(around:{radius_meters},{user_lat},{user_lng});
      relation{tag_filter}(around:{radius_meters},{user_lat},{user_lng});
    );
    out center;
    """

    data = fetch_overpass(query)

    if not data:
        return []

    hospitals = []

    for element in data.get("elements", []):

        if element.get("lat"):
            lat = element["lat"]
            lng = element["lon"]
        else:
            center = element.get("center")
            if not center:
                continue
            lat = center.get("lat")
            lng = center.get("lon")

        if not lat or not lng:
            continue

        distance = calculate_distance(user_lat, user_lng, lat, lng)

        hospitals.append({
            "name": element.get("tags", {}).get("name", "Unnamed Healthcare Center"),
            "latitude": lat,
            "longitude": lng,
            "distance": distance
        })

    hospitals.sort(key=lambda x: x["distance"])

    return hospitals[:20]