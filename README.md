# BLOGIFY

A simple and elegant blog application built with Django. Users can register, log in, create posts, and leave comments on posts. This project demonstrates fundamental Django concepts, including authentication, form handling, and pagination.

## Features

- **User Authentication**: Users can register, log in, and log out of the application.
- **Post Management**: Users can view posts, create posts, and read individual post details.
- **Commenting System**: Registered users can leave comments on posts.
- **Pagination**: Posts are paginated for easier browsing.
- **User Registration**: New users can sign up with their username and email.
  
## Technologies Used

- **Django 5.1.3**: Web framework for building the app.
- **SQLite**: Database for storing posts and comments (default in Django).
- **HTML/CSS**: Frontend structure and styles.
- **Bootstrap/Tailwind**: For responsive and clean UI (optional).
  
## Setup

### Prerequisites

1. Install Python 3.8+.
2. Install Django: `pip install django`.
3. Install Tailwind (if applicable): `pip install django-tailwind`.

### Installation Steps

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # For MacOS/Linux
    env\Scripts\activate  # For Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser (optional, for admin access):
    ```bash
    python manage.py createsuperuser
    ```

6. Run the server:
    ```bash
    python manage.py runserver
    ```

7. Open the application in your browser at `http://127.0.0.1:8000/`.

### Admin Panel

You can access the Django admin panel at `http://127.0.0.1:8000/admin/`. Log in using the superuser credentials you created.

## URL Endpoints

- `/`: Displays a list of posts.
- `/post/<int:post_id>/`: Displays details of a single post and associated comments.
- `/register/`: User registration page.
- `/login/`: Login page for registered users.
- `/logout/`: Logs out the current user.

## Customization

You can customize the following:

- **Templates**: Modify the HTML files under the `templates/` directory.
- **Styles**: Add custom CSS or use frameworks like Tailwind or Bootstrap.
- **Models**: Extend the `Post` and `Comment` models to include more fields as needed.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Django Framework: [https://www.djangoproject.com/](https://www.djangoproject.com/)
- SQLite: [https://www.sqlite.org/](https://www.sqlite.org/)


