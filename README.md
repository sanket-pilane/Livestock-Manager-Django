# Livestock Manager 🐄

A Django-based web application for managing livestock records. This application allows users to register, log in, and manage a database of livestock, including adding, updating, and deleting animal records.

## ✨ Features

*   **User Authentication:** Secure user registration and login system.
*   **Livestock Management:** CRUD (Create, Read, Update, Delete) functionality for livestock records.
*   **Owner Management:** Ability to create and assign owners to livestock.
*   **Responsive UI:** A clean and modern user interface built with Tailwind CSS.

## 🛠️ Tech Stack

*   **Backend:** Python, Django
*   **Frontend:** HTML, Tailwind CSS
*   **Database:** SQLite 3

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### 1. Prerequisites

Make sure you have Python 3 installed on your system.

### 2. Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone <repository-url>
cd <project-directory>
```

### 3. Set Up the Environment

This project uses a Python virtual environment to manage dependencies.

**Create and activate the virtual environment:**

*   **Linux/macOS:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
*   **Windows:**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

### 4. Install Dependencies

Install all the required packages using pip. The `requirements.txt` file is located in the `livestock_manager` directory.

```bash
pip install -r livestock_manager/requirements.txt
```

### 5. Database Setup

This project uses SQLite as its database. The following command will create the database and apply the necessary migrations.

```bash
python livestock_manager/manage.py migrate
```

### 6. Create a Superuser

To access the Django admin panel, you need to create a superuser. A superuser with the following credentials has already been created for you:

*   **Username:** `admin`
*   **Password:** `AdminPass123!`

If you need to create another superuser, you can run:
```bash
python livestock_manager/manage.py createsuperuser
```
And follow the prompts.

### 7. Run the Development Server

Now, you can start the Django development server:

```bash
./devserver.sh
```

The application will be running at the URL provided in the terminal, and you should see a live preview in your IDE.

## 🔑 Admin Panel

You can access the admin panel at `/admin` (e.g., `http://127.0.0.1:8000/admin`).

Log in with the superuser credentials to manage users, owners, and livestock directly from the admin interface.

---

Happy coding! 💻
