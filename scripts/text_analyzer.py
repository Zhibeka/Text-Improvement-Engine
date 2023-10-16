from sentence_transformers import SentenceTransformer, util

def phrase_finder(text, phrases):
    # Load a pre-trained SBERT model
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    
    # Split the text into sentences
    text_sentences = text.split('.')
    
    # Compute embeddings for the phrases and sentences
    phrases_embeddings = model.encode(phrases)
    text_sentences_embeddings = model.encode(text_sentences)
    
    # Compute similarities between the embeddings
    similarities = util.pytorch_cos_sim(phrases_embeddings, text_sentences_embeddings)
    similar_words = []
    # Iterate over the similarities to find matches or similar phrases
    for i in range(len(phrases)):
        for j in range(len(text_sentences)):
            if similarities[i][j] > 0.40:  # You can adjust this threshold
                similar_words.append([phrases[i], text_sentences[j]])
                print(f'Phrase "{phrases[i]}" is similar to sentence "{text_sentences[j]}"')
    return similar_words

if __name__ == "__main__":
    phrase_finder(text, words_list)
