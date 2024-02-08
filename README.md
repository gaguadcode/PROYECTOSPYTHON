# Movie Recommendation App
![Alt text](Screenshot 2024-02-05 at 17.25.34)
This project aims to provide movie recommendations based on user preferences using two different language models: BERT and GPT-4. The BERT model, introduced in 2019, is known for its lightweight architecture. In contrast, GPT-4, unveiled in 2023, stands out as a more densely structured model. The application utilizes movie overviews and embeddings to calculate similarity scores and suggests the top N similar films. 

## Overview

The project consists of two main components:

1. **BERT Model:**
   - Utilizes the Sentence Transformers library to create embeddings for movie overviews.
   - Calculates similarity scores between user input and the movie overviews using cosine similarity.
   - Displays the top N similar films based on BERT embeddings.

2. **GPT-4 Model:**
   - Employs the AstraDB for vector storage and retrieval, connecting with the LangChain library and OpenAI for embeddings.
   - Extracts vector embeddings for movie overviews and retrieves similar movies using the AstraDB collection.
   - Displays the top N similar films based on GPT-4 embeddings.

## Usage

To run the Movie Recommendation App, follow these steps:

1. Ensure all required libraries are installed using `pip install -r requirements.txt`.

2. Set up the necessary environment variables in a `.env` file:
   - `ASTRA_DB_APPLICATION_TOKEN`: AstraDB application token.
   - `ASTRA_DB_API_ENDPOINT`: AstraDB API endpoint.
   - `OPENAI_API_KEY`: OpenAI API key.
   - `OMDB_API_KEY`: API key for the Open Movie Database (OMDb).

3. Create the Astrapy database, based in the file embeddings_store_datastax.ipynb, and the dataset: titleoverview_comb

4. Execute the script, and the Gradio interface will launch.

## Dependencies

- pandas
- sentence_transformers
- astrapy
- langchain
- langchain_openai
- gradio
- dotenv
- matplotlib
- requests
- Pillow
- tkinter

## Gradio Interface

The Gradio interface allows users to input the last movie they liked, choose the model for embeddings (BERT or GPT4), and select the number of recommended movies (N). The interface then displays the movie posters of the top N recommended films.

## Note

Ensure that you have a stable internet connection as the application relies on external APIs for movie information and posters.

Feel free to explore and discover new movies based on your preferences!
