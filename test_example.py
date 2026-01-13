"""
Example script to test the video generation pipeline.
"""

import requests
import json

# Example request data
example_data = {
    "title": "Introduction to Photosynthesis",
    "slides": [
        {
            "text": "Photosynthesis is the process by which plants make food.",
            "image_prompt": "green plants under sunlight"
        },
        {
            "text": "It uses sunlight, carbon dioxide, and water.",
            "image_prompt": "diagram of photosynthesis process"
        },
        {
            "text": "The process produces glucose and oxygen as byproducts.",
            "image_prompt": "chemical equation of photosynthesis"
        }
    ]
}

def test_api():
    """Test the API endpoint."""
    url = "http://localhost:8000/generate-video"
    
    print("Sending request to API...")
    print(f"Title: {example_data['title']}")
    print(f"Number of slides: {len(example_data['slides'])}")
    
    try:
        response = requests.post(url, json=example_data)
        response.raise_for_status()
        
        result = response.json()
        print("\n✅ Success!")
        print(f"Status: {result['status']}")
        print(f"Video path: {result['video_path']}")
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to API. Make sure the server is running:")
        print("   python main.py")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_api()

