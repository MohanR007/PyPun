import requests
from bs4 import BeautifulSoup

# Flipkart product URL
url = "https://www.flipkart.com/alienware-intel-core-i9-10th-gen-10980hk-32-gb-1-tb-ssd-windows-10-home-8-gb-graphics-nvidia-geforce-rtx-2080-max-q-m15r3-gaming-laptop/p/itm026c3f18c350d?pid=COMFTC4YG3ZD5PXA"

# Headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# Send request
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract product name
    product_name = soup.find("span", class_="B_NuCI")
    product_name = product_name.text if product_name else "Not found"

    # Extract price
    price = soup.find("div", class_="_30jeq3 _16Jk6d")
    price = price.text if price else "Not found"

    # Extract rating
    rating = soup.find("div", class_="_3LWZlK _1BLPMq")
    rating = rating.text if rating else "No rating available"

    # Extract specifications
    specs = soup.find_all("li", class_="rgWa7D")
    specifications = [spec.text for spec in specs]

    # Extract image URL
    image = soup.find("img", class_="_396cs4 _3exPp9")
    image_url = image["src"] if image else "No image found"

    # Print results
    print(f"Product Name: {product_name}")
    print(f"Price: {price}")
    print(f"Rating: {rating}")
    print(f"Specifications:")
    for spec in specifications:
        print(f"  - {spec}")
    print(f"Image URL: {image_url}")

else:
    print("Failed to retrieve the webpage. Flipkart might be blocking the request.")
