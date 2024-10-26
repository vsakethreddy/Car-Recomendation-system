import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset from the specified path
dataset_path = 'static\data.csv'
New_Cars = pd.read_csv(dataset_path)

# Select the desired columns
choosen_columns = ['Make', 'Model', 'Engine Fuel Type', 'MSRP']
New_Cars['features'] = New_Cars[choosen_columns].apply(lambda x: ' '.join(x.astype(str)), axis=1)

french_stop_words = [
    'a', 'à', 'afin', 'alors', 'après', 'au', 'aucun', 'aussi', 'autre', 'avec',
    'avoir', 'avant', 'c', 'ce', 'cela', 'ces', 'ceux', 'chaque', 'ci', 'comme'
]

tfv = TfidfVectorizer(min_df=10, max_features=None,
            strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}',
            ngram_range=(1, 3),
            stop_words=french_stop_words)

tfv_matrix = tfv.fit_transform(New_Cars['features'])
similarity = cosine_similarity(tfv_matrix)

def get_recommendations(name, msrp_range, cosine_similarities=similarity, data=New_Cars, top_n=100):
    # Get the index of the car with the given name and within the specified MSRP range
    idx = data[(data['Vehicle Size'] == name) & (data['MSRP'].between(*msrp_range))].index[0]

    # Get the similarity scores for all cars
    similarity_scores = list(enumerate(cosine_similarities[idx]))

    # Sort the cars based on similarity scores
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Get the top N most similar cars (returning selected columns)
    top_similar_cars = [
        {
            'Make': data.loc[i[0], 'Make'],
            'Model': data.loc[i[0], 'Model'],
            'Vehicle Size': data.loc[i[0], 'Vehicle Size'],
            'Vehicle Style': data.loc[i[0], 'Vehicle Style'],
            'MSRP': data.loc[i[0], 'MSRP'],
            'Engine Fuel Type': data.loc[i[0], 'Engine Fuel Type'],
            'Transmission Type': data.loc[i[0], 'Transmission Type']
        }
        for i in similarity_scores[1:top_n + 1]
    ]

    # Print details of similar cars for debugging
    # print("Query Car:")
    # print(data.loc[idx, ['Make', 'Model', 'Vehicle Size', 'Vehicle Style', 'MSRP', 'Engine Fuel Type', 'Transmission Type']])

    # print("\nRecommended Cars:")
    # for car in top_similar_cars:
    #     print(car)

    return top_similar_cars

# # Example usage with MSRP range
# car_name = 'Compact'
# msrp_range = (30000, 50000)  # Specify the MSRP range you want to consider

# # Use the query vector to get recommendations
# recommended_cars = get_recommendations(car_name, msrp_range)

# # Now, 'recommended_cars' contains a list of dictionaries representing the recommended cars
# # print(recommended_cars)

