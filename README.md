# Drone-image-classification
This project sets up a FastAPI server with a YOLOv8 model for  object detection. 
The API accepts image upload, performs predictions and returns the results in a structured format.

## Project Structure



## Setup and Installation

### Prerequisites

- Docker
- Docker Compose

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd drone-image-classification

2. **Build and Run the Docker Container**

    ```bash
    docker compose up --build
This command builds the Docker image and starts the FastAPI server.

**API Documentation with Swagger**

FastAPI automatically generates interactive API documentation using Swagger UI. Once the server is running, you can access the documentation at:

Swagger UI: http://localhost:5000/docs

This UI allows you to interact with the API endpoints and view detailed information about request parameters and responses.

**API Endpoints**

Instead of sending the path, it is better for API to accept the image file itself. This is a more common approach and ensures that the image is accessible to the  container.

**POST** 

    /predict/upload_image

    accepts: File upload 

    /predict

    In case u want to use the image path make sure you upload the image inside the app/test_images folder and give the path as below


```bash

    curl --request POST 'http://localhost:5000/predict'
        --data-raw '{"image_path": "test_images/image_name.jpg"}'
