# Sentence Similarity Techniques

## Project Overview

This project explores various methods for calculating sentence similarity. Sentence similarity is a fundamental concept in natural language processing (NLP) and has applications in search engines, recommendation systems, plagiarism detection, and more. The project covers traditional methods for calculating sentence similarity, providing a foundation before diving into more advanced, neural network-based techniques including word embeddings and RAG.

The primary goal of this project is to implement and compare different methods for determining the similarity between sentences and paragraphs. This will help in understanding the strengths and weaknesses of each method and how they can be applied to real-world NLP problems.

## Features

### 1. Text Preprocessing
- **Tokenization**: Splitting sentences into individual words.
- **Stop Words Removal**: Filtering out common words that do not contribute to the meaning (e.g., 'and', 'the', 'is').
- **Punctuation Removal**: Eliminating punctuation marks to focus on the words themselves.

### 2. Similarity Calculation Methods
- **Bag of Words (BoW)**: A simple representation where sentences are converted into vectors of word counts.
- **TF-IDF**: Term Frequency-Inverse Document Frequency, a statistical measure used to evaluate the importance of a word in a document relative to a collection of documents.
- **Jaccard Similarity**: Measures the similarity between two sets by comparing the size of their intersection to the size of their union.
- **Levenshtein Distance (Edit Distance)**: Calculates the minimum number of single-character edits required to change one word into another.
- **Overlap Coefficient**: Measures the overlap between two sets relative to the smaller set.
- **Dice Coefficient**: Measures the similarity between two sets based on the ratio of twice the size of the intersection to the sum of the sizes of the sets.

### 3. Advanced Techniques Using Neural Networks
- **Word Embeddings**: Exploring sentence similarity through vector representations of words. This section includes implementing models like Word2Vec to generate word embeddings and using those embeddings to calculate sentence vectors.
- **Retrieval-Augmented Generation (RAG)**: Combining the strengths of retrieval-based and generative models to enhance sentence similarity assessments. This includes demonstrating how retrieved information can be integrated into a generative process to produce responses that are contextually enriched.

### 4. Example Sentences and Paragraphs
Included examples from different contexts to demonstrate how the methods perform on various types of text.

### 5. Comprehensive Notebook
An interactive Jupyter Notebook that includes explanations, code snippets, and results for each method. The notebook is designed to provide a hands-on learning experience, showing not only how each method works but also how they compare when applied to the same datasets.

## Conclusion

By examining a broad range of techniques from simple statistical methods to sophisticated neural network models, this project provides a comprehensive overview of the approaches available for measuring sentence similarity. The findings and tools developed here can be utilized by practitioners and researchers in the field of NLP to enhance systems that rely on understanding and processing human language.

## Contributing
Feel free to fork the repository and submit pull requests. You can also open an issue if you find any bugs or have suggestions for further improvements.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Authors
- Dhruv Parthasarathy

## Acknowledgments
- Thanks to everyone who has contributed to the open-source packages used in this project.
