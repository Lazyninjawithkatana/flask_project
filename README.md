# flask_project
 This Flask application is a simple user registration and login system that uses a PostgreSQL database for storing user information.

Database Setup: The database.py file creates a PostgreSQL database named test_123 and a users table within it. The users table has columns for a unique user ID, a unique username, and a password.

User Registration: The /register route handles new user creation. It takes a username and a password, hashes the password using generate_password_hash for security, and stores the username and hashed password in the users table. It also includes basic validation to ensure all fields are filled and that the password and confirm password fields match.

User Login: The / (index) route handles user logins. It checks if a submitted username exists in the database and verifies the provided password against the stored hashed password using check_password_hash. If the credentials are correct, the user's ID and username are stored in a session, and the user is redirected to the /user_page route.

User Page: The /user_page route is an authenticated page that displays a personalized greeting to the logged-in user by rendering user_page.html with their username from the session. Access is restricted, and users who are not logged in are redirected to the login page.

Logout: The /logout route clears the user session, effectively logging the user out and redirecting them to the login page.

HTML Templates: The application uses HTML templates for its front-end. The provided user_page.html is a simple example that greets the logged-in user and provides a link to log out. Other templates, like index.html and register.html, would contain the forms for logging in and registering, respectively.
