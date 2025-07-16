
# Confession App

Welcome to the Confession App, a Django-based platform for users to post and view anonymous confessions. This project utilizes Django for the backend and a simple, clean interface for the user experience.

## ✨ Features

-   **Anonymous Confessions:** Users can post confessions without revealing their identity.
-   **View Confessions:** A public feed to view all submitted confessions.
-   **User Authentication:** Secure login and registration system for users (though confessions remain anonymous).
-   **Simple & Clean UI:** A straightforward and easy-to-navigate user interface.

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have Python and pip installed on your system.

-   [Python](https://www.python.org/downloads/) (Version 3.8 or higher recommended)
-   [pip](https://pip.pypa.io/en/stable/installation/)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone <your-repository-url>
    cd sample_project_1
    ```

2.  **Create and activate a virtual environment:**
    -   **Linux/macOS:**
        ```sh
        python3 -m venv .venv
        source .venv/bin/activate
        ```
    -   **Windows:**
        ```sh
        python -m venv .venv
        .venv\Scripts\activate
        ```

3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up the database:**
    This project uses SQLite, so no external database server is needed. Simply run the migrations to create the database file and schema.
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

## 🛠️ Technologies Used

-   **Backend:**
    -   [Django](https://www.djangoproject.com/): The web framework used.
    -   [Django REST Framework](https://www.django-rest-framework.org/): For creating a powerful Web API.
-   **Database:**
    -   [SQLite](https://www.sqlite.org/index.html): For local development.
-   **Frontend:**
    -   HTML5
    -   CSS3 (with Bootstrap for styling)

## 📂 Project Structure

The project is organized into the following main components:

-   `my_site/`: The main Django project directory.
    -   `settings.py`: Contains the project's settings.
    -   `urls.py`: The main URL configuration.
-   `confession_app/`: The core application for handling confessions.
    -   `models.py`: Defines the database models.
    -   `views.py`: Contains the application logic.
    -   `urls.py`: The app-specific URL configuration.
    -   `templates/`: Contains the HTML templates for the UI.
-   `manage.py`: A command-line utility for interacting with the Django project.
-   `requirements.txt`: A list of all Python dependencies.
-   `db.sqlite3`: The SQLite database file.

---
