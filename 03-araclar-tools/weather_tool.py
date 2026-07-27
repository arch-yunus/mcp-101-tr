def get_weather(location: str) -> dict:
    """Basit bir hava durumu aracı örneği."""
    data = {
        "location": location,
        "temperature_celsius": 24,
        "condition": "Güneşli",
        "advice": "Dışarı çıkmak için güzel bir gün!"
    }
    return data

if __name__ == "__main__":
    sample_location = "İstanbul"
    print(f"{sample_location} için örnek hava durumu: \n{get_weather(sample_location)}")
