
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

4.  Download this file since it is a bigger file and cannot be pushed to Github:
    -https://drive.google.com/file/d/1C3MUxSPGP3xM1HVwVSFWi_2ZQ9t2TFH7/view?usp=drive_link


    *** Download the datasets & file and place it in directory.

5. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```


*** Here are some outputs from our Movie Recommendation System: ***



![HomeRecommendation](https://github.com/user-attachments/assets/f36ec8de-623e-435f-867d-5b2b2807d3a6)
![home1](https://github.com/user-attachments/assets/f2b210d2-99fa-4b52-8fa6-329d29b60752)
![Details](https://github.com/user-attachments/assets/81a454d1-bb71-490a-a1c5-897925d23ba6)
![Director and Cast](https://github.com/user-attachments/assets/7c1f0d27-b145-4ac0-8637-f4747ad8c860)
![BroseGenre](https://github.com/user-attachments/assets/007bc1c7-ab73-4aa2-8e41-466061c5934a)
![Fiter Searchh](https://github.com/user-attachments/assets/d9638514-0445-4b11-95cd-ca4257737f34)
![SearchByActor](https://github.com/user-attachments/assets/d14327cb-03b3-405d-9cc9-20a77860fe77)
