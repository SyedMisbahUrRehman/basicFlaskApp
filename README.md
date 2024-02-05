# Flask Login App

## Overview
This is a simple Flask web application with basic login functionality. Users can log in with hardcoded credentials, and once logged in, their username is displayed on the homepage.

## Pages

### 1. Home (index.html)
- Displays a welcome message.
- If a user is logged in, it shows the username.

### 2. About (about.html)
- Provides information about the application.

### 3. Contact (contact.html)
- Contact information or form.

### 4. Login (login.html)
- Allows users to log in with hardcoded credentials.

## Technologies Used
- Flask
- HTML
- Jinja2 (for template rendering)

## Installation
1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask app with `python app.py`.

## Usage
1. Open the app in your browser.
2. Navigate to the login page and log in using the hardcoded credentials.
3. Upon successful login, you will be redirected to the homepage, where your username is displayed.

## File Structure
- `app.py`: Flask application main file.
- `templates/`: Folder containing HTML templates.
  - `base.html`: Base template with common elements.
  - `index.html`: Homepage template.
  - `about.html`: About page template.
  - `contact.html`: Contact page template.
  - `login.html`: Login page template.

## Customize
Feel free to customize the templates, add more pages, or enhance the functionality as needed for your project.

## Contributions
Contributions are welcome! Feel free to fork the project and submit pull requests.

## License
Null
