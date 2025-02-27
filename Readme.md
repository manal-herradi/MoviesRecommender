# **Movie Recommender System**

## **Context**
This project is a **Personalized Movie Recommender System** built using **collaborative filtering**. The data used in this project is sourced from the **MovieLens 100K dataset**, which contains **user ratings** for movies. The recommender system suggests movies based on users' ratings and provides personalized recommendations by leveraging collaborative filtering techniques.

### **Features:**
- **Collaborative Filtering** for personalized movie recommendations.
- A simple **Flask web app** as the front-end, with an interactive form where users can input their **user ID** to get movie recommendations.
- **HTML**, **CSS** are used for the front-end to create a user-friendly interface.

---

## **Technologies Used**
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, Surprise, Pandas, NumPy
- **Database**: CSV for simplicity
- **Frontend**: HTML, CSS
- **Deployment**: Heroku/Render (optional)

---

## **Project Structure**

```
movie-recommender/
│── app.py  # Flask application that runs the web 
│── requirements.txt  # Python dependencies
├── Readme.md
│── raw_data/
│   ├── u.item # Movie metadata
│   ├── u.data  # User ratings
│── templates/
│   ├── index.html  # Front-end HTML
│── static/
│   ├── style.css  # Custom CSS for styling the web 
|__ modules/
    ├──converter.py
    ├──recommender.py
```

---

## **How to Run the Project Locally**

### **Step 1: Clone the Repository**

To get started, **clone** this repository from GitHub:

```bash
git clone https://github.com/manal-herradi/MoviesRecommender.git
cd MoviesRecommender
```

### **Step 2: Install the Requirements**

Use the **`requirements.txt`** to install all the necessary dependencies. Run the following command:

```bash
pip install -r requirements.txt
```

### **Step 3: Convert `raw-files` Files to `.csv` Format**

This project contains raw data files (`u.data` and `u.item`) in a format that needs to be converted to CSV format for further processing. Run the following script **"converter.py"** to convert these files to **CSV**, and don't forget to create a folder named **data**, to store the new files.

The source of the files is from the [MovieLens 100k dataset](https://grouplens.org/datasets/movielens/100k/).

### **Step 4: Run the Flask App**

After the dependencies are installed, you can run the Flask web app with the following command:

```bash
python app.py
```

By default, the app will be hosted at **http://127.0.0.1:5000/**. Open this URL in your browser to access the recommender system.

### **Step 5: Enter a User ID to Get Recommendations**

Once the web app is running, go to the homepage, enter a **user ID** (you can try different IDs), and click on **"Get Recommendations"**. The system will display a list of movie recommendations based on that user’s ratings.

---

## **Project Files and Description**

### **1. `app.py`** – Flask Web Application

This file contains the Flask app that serves the web interface. It takes the **user ID** input from the user and provides movie recommendations.

### **2. `recommender.py`** – Recommender System Logic

This file contains the logic for the **Collaborative Filtering** algorithm that recommends movies to the user. It uses the **Surprise** library to implement the SVD algorithm and generate movie recommendations.

### **3. `index.html`** – Front-End HTML

This is the main user interface of the web app, which contains a form for entering a **user ID** and displaying movie recommendations.

### **4. `style.css`** – Custom Styling

This file provides basic **CSS styling** for the website

---

## **How the Recommender System Works**

1. **User Input**: The user enters a **user ID** in the input form.
2. **Movie Data**: The movie data (movies.csv) and user ratings (ratings.csv) are loaded into the system.
3. **Collaborative Filtering**: The system uses **Surprise**'s **SVD (Singular Value Decomposition)** algorithm to predict the ratings for movies the user hasn't rated yet.
4. **Recommendations**: The app sorts the predicted ratings and displays the top recommendations.

---

## **Deployment Options**

### **1. Deploy on Heroku**
If you want to deploy this app to **Heroku**, follow these steps:
1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
2. Create a **Procfile** in your project root:
   ```
   web: gunicorn app:app
   ```
3. Log in to Heroku using the CLI:
   ```bash
   heroku login
   ```
4. Create a new Heroku app:
   ```bash
   heroku create movie-recommender
   ```
5. Deploy your app:
   ```bash
   git push heroku main
   ```

### **2. Deploy on Render**
Alternatively, you can deploy this project on **Render** by following their [deployment guide](https://render.com/docs/deploy-flask).