
# Movie Recommendation System

This repository contains the code for a Movie Recommendation System developed as a 6th semester college project. The system utilizes K-Nearest Neighbors (KNN) Algorithm, cosine similarity, and content-based filtering to recommend movies based on various features.

## Key Components
- 🔄 **Data Preparation:** Merging movie and credit datasets, extracting relevant features.
- 🛠️ **Feature Engineering:** Converting genres, keywords, cast, and crew into a usable format.
- ✂️ **Text Processing:** Utilizing stemming and CountVectorizer to create feature vectors.
- 📏 **Similarity Computation:** Applying cosine similarity to measure the closeness of movies.
- 🎯 **Recommendation Algorithm:** Generating movie recommendations based on calculated similarities.

## Evaluation Metrics
To ensure the effectiveness of the recommendation system, we employed various evaluation metrics:
- **Precision@k**
- **Recall@k**
- **Mean Squared Error**
- **Classification Report**
- **Confusion Matrix**

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Natural Language Processing (NLP)

## How to Use
1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/movie-recommendation-system.git
    cd movie-recommendation-system
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Download the datasets:
    - [tmdb_5000_movies.csv](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)
    - [tmdb_5000_credits.csv](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_credits.csv)    

4. Downlod this file since it is bigger file so it cannot push in Github.
    -https://drive.google.com/file/d/1C3MUxSPGP3xM1HVwVSFWi_2ZQ9t2TFH7/view?usp=drive_link


    *** Download the datasets & file and place it in directory.

5. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

Hope you guys liked it !!!!!!