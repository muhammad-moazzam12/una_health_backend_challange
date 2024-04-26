# Glucose Data Management API

This Home Task Django project provides APIs for glucose data, including retrieving, and prepopulating glucose data from CSV files.

## General Information

- **Software Architecture**: The project follows the Django framework. The RESTful API endpoints are implemented using Django's REST Framework.

- **Clean Code Structure**: The project maintains a clean code structure, following Django's recommended directory layout. App within the project i-e api contains its own set of models, serializers, views, and tests, ensuring modularity.

- **Coding Conventions**: The code adheres to Python PEP 8 style guidelines for naming conventions, indentation, and code layout. `.pre-commit-config.yaml` and `pyproject.toml` added for PEP8 style guide and sorting and organizing import statements. Comments are included where necessary to explain complex logic or provide context.

- **Use of Django Generics**: Django's generic views i-e `ListAPIView` and `RetrieveAPIView` are used for implementing `GlucoseDataListView` and `GlucoseDataSingleView` respectively.

- **APIView for Prepopulate Data**: The `PrepopulateGlucoseData` view is implemented using Django's `APIView` class.

## Getting Started

1. Clone the project repository to your local machine:

    ```bash
    git clone https://github.com/rakurai-io/rakurai_backend
    ```

2. Navigate to the project directory:

    ```bash
    cd una_health_backend_challange
    ```

## Running the Project with Docker

### Prerequisites
Make sure you have the following software installed on your machine:

- [Docker](https://www.docker.com/)

### 1. Build the Docker Image

Run the following command to build the Docker image:

```bash
docker build -t <name_of_image> .
```

Replace `name_of_image` with the desired name for your Docker image.

### 2. Run the Docker Container

Now, run the following command to start a Docker container:

```bash
docker run --name <name_of_container> -p 8000:8000 <name_of_image>
```

Replace `name_of_container` with the desired name for your Docker container.

## Endpoints

- **List Glucose Data**: `GET /api/v1/levels/`
  - Retrieves a list of glucose data with optional filtering by user ID, start timestamp, and stop timestamp. Supports pagination and sorting.
- **Retrieve Glucose Data**: `GET /api/v1/levels/<id>/`
  - Retrieves a particular glucose data entry by ID.
- **Prepopulate Glucose Data**: `POST /api/v1/prepopulate-data/`
  - Uploads and prepopulates glucose data from a CSV file.

## API Documentation

To access API Documentation please run the server first and access the following urls
- Swagger UI: [http://localhost:8000/swagger_doc/](http://localhost:8000/swagger_doc/)
- ReDoc: [http://localhost:8000/doc/](http://localhost:8000/doc/)

## Project Structure

- **api**: Contains the Django app for handling API functionality.
  - **models.py**: Defines the database models for Customer, Device, and GlucoseData.
  - **serializers.py**: Contains serializers for converting model instances to JSON and vice versa.
  - **views.py**: Defines API views for listing, retrieving, and prepopulating glucose data.
  - **urls.py**: Contains URL patterns for routing API endpoints.
- **requirements.txt**: Lists project dependencies.
- **README.md**: Documentation for the project.

## Running Tests

Tests for the API endpoints and functionality are located in the `api/tests` directory. To run the tests, use the following command:

```
python manage.py test api
```
