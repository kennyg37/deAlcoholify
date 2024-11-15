

# deAlcoholify app

Welcome to the deAlcoholify App! This project aims to educate and inform users about the risks of alcohol use through data visualization and analysis. By using powerful statistical tools, we help individuals make informed decisions and contribute to a healthier community.

## 🚀 Deployed App

You can access the live version of the app [here](https://your-deployed-app-link.com).

## 🎥 Video Demo

Check out the demo video of how the app works:  
[Watch the Demo](https://link-to-video-demo.com)

## 🛠 Project Setup - Local Installation

To run this project locally, follow the steps below:

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/your-username/alcohol-awareness-app.git
cd alcohol-awareness-app
```

### 2. Create a Virtual Environment

It is recommended to create a virtual environment for the project:

```bash
python3 -m venv venv
```

Activate the virtual environment:
- **Windows:**

```bash
venv\Scripts\activate
```

- **Mac/Linux:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

Install all the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory of the project. Add the following environment variables:

```bash
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
```

> **Note:** Make sure to replace the values with your actual database URL and secret key.

### 5. Database Setup

If the project uses a database, you'll need to run the migrations to set up the database:

```bash
flask db upgrade
```

### 6. Run the App Locally

To run the app locally, use the following command:

```bash
flask run
```

Now, open your browser and navigate to `http://127.0.0.1:5000` to view the app.

## 💻 Project Structure

```
/alcohol-awareness-app
    /assets                # Static files (images, styles, etc.)
    /templates             # HTML templates
    /src                   # Source code
    /models                # Database models (if applicable)
    app.py                 # Main app entry point
    requirements.txt       # List of dependencies
    .env                   # Environment variables
    README.md              # Project documentation
```

## 👥 Contributing

We would like to thank everyone who contributed to the project! Here's a list of the amazing people involved:

- **Ken Ganza** - Full-stack Engineer/ALU
- **Kwihangana Dimitri** - Machine Learning Engineer/ALU
- **Kwizera Alain Bertrand** - Data Analyst/AUCA

## 🔧 License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.
