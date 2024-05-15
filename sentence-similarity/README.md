# Sentence Similarity Techniques

## Project Overview

This project explores various methods for calculating sentence similarity. Sentence similarity is a fundamental concept in natural language processing (NLP) and has applications in search engines, recommendation systems, plagiarism detection, and more. The project covers traditional methods for calculating sentence similarity, providing a foundation before diving into more advanced, neural network-based techniques.

The primary goal of this project is to implement and compare different methods for determining the similarity between sentences and paragraphs. This will help in understanding the strengths and weaknesses of each method and how they can be applied to real-world NLP problems.


## Features

1. Text Preprocessing
- Tokenization: Splitting sentences into individual words.
- Stop Words Removal: Filtering out common words that do not contribute to the meaning (e.g., 'and', 'the', 'is').
- Punctuation Removal: Eliminating punctuation marks to focus on the words themselves.

2. Similarity Calculation Methods
- Bag of Words (BoW): A simple representation where sentences are converted into vectors of word counts.
- TF-IDF: Term Frequency-Inverse Document Frequency, a statistical measure used to evaluate the importance of a word in a document relative to a collection of documents.
- Jaccard Similarity: Measures the similarity between two sets by comparing the size of their intersection to the size of their union.
- Levenshtein Distance (Edit Distance): Calculates the minimum number of single-character edits required to change one word into another.
- Overlap Coefficient: Measures the overlap between two sets relative to the smaller set.
- Dice Coefficient: Measures the similarity between two sets based on the ratio of twice the size of the intersection to the sum of the sizes of the sets.

3. Example Sentences and Paragraphs
Included examples from different contexts to demonstrate how the methods perform on various types of text.

4. Comprehensive Notebook
An interactive Jupyter Notebook that includes explanations, code snippets, and results for each method.

## Getting Started

### Prerequisites
- Docker
- Docker Compose
- Git (optional, for cloning the repository)

### Installation
1. **Clone the repository (optional):**
   ```bash
   git clone https://github.com/parthasarathydNU/gen-ai-coursework.git
   cd gen-ai-coursework/sentence-similarity
   ```

2. **Install jupyter and start a jupyter server:**
   ```bash
   jupyter lab
   ```

3. **Running the notebook:**
   - Once the jupyter notebook is up you can access it through `http://localhost:8888` on your browser. Navigate to the `notebooks` dir.
   - Run -> Run all cells


### File Structure
- `scripts/`: Contains Python scripts for data analysis.
- `results/`: Contains outputs from the scripts, including CSV files and plots.
- `Dockerfile`: Defines the Docker container setup.
- `docker-compose.yml`: Configures services, networks, and volumes for Docker.
- `requirements.txt`: Lists Python package dependencies.

## Usage
With Docker Compose, your application will be built and started by running the command mentioned in the Installation section. This will execute the scripts as configured in `docker-compose.yml`. You can edit this file to change which scripts are run or to adjust other settings such as port mapping and volume mounting.

## Contributing
Feel free to fork the repository and submit pull requests. You can also open an issue if you find any bugs or have suggestions for further improvements.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Authors
- Dhruv Parthasarathy

## Acknowledgments
- Thanks to everyone who has contributed to the open-source packages used in this project.
