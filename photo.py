import requests
from PIL import Image
from io import BytesIO
data = ['https://t4.ftcdn.net/jpg/05/72/82/85/360_F_572828530_ofzCYowQVnlOwkcoBJnZqT36klbJzWdn.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLj-lKqnaX9ulY0qLcGdzaELG-39w21Y5PIQ&s']
# URL of the image you want to download
def image(data):
    count = 0
    for link in data:
        count +=1
        image_url = link
        
        # Send a GET request to the image URL
        response = requests.get(image_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Open the image from the response content
            image = Image.open(BytesIO(response.content))
            
            # Save the image to a file
            image.save(f"{count}_downloaded_image.jpg")
            print("Image downloaded and saved as downloaded_image.jpg")
        else:
            print("Failed to retrieve the image")

image(data)