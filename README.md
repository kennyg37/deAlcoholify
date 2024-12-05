

# deAlcoholify app

Welcome to the deAlcoholify App! This project aims to educate and inform users about the risks of alcohol use through data visualization and analysis. By using powerful statistical tools, we help individuals make informed decisions and contribute to a healthier community.

## 🚀 Deployed App

You can access the live version of the app [here](https://dealcoholify.onrender.com).

## 🎥 Video Demo

Check out the demo video of how the app works:  
[Watch the Demo](https://drive.google.com/drive/folders/1QdDYwiG8SCY5D7xOZjWGfk63MQ80pQ0d?usp=drive_link)

## 🛠 Project Setup - Local Installation

To run this project locally, follow the steps below:

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
 git clone https://github.com/kennyg37/deAlcoholify.git
cd deAlcoholify
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
PORT= 3000
```

> **Note:** Replace with your prefered port.


### 5. Run the App Locally

To run the app locally, use the following command:

```bash
python app.py
```

Now, open your browser and navigate to `http://127.0.0.1:3000` to view the app.

**Note:** Replace the url with the port you chose

## 💻 Project Structure

```
/deAlcoholify
    /assets                # Static files (images, styles, etc.)
    /components             # Pages and other components
    /models                # machine learning models and notebooks that created them
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
