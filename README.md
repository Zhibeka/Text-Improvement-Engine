# Text-Improvement-Engine
A tool that analyses a given text and suggests improvements based on the similarity to a list of "standardised" phrases

## Features
- **Data Input**: Provides a method for the user to input the text to be analyzed through a simple UI or via a text file in the CLI. The results are shared as a link to the GitHub project.
- **Standardized Phrases**: The tool is pre-loaded with a list of standardized phrases (e.g., business jargon, scientific terminology, etc.) which serve as the benchmark for text analysis.
- **Text Analysis**: Utilizes a pre-trained language model (not an API) to identify phrases in the input text that are semantically similar to any of the standardized phrases. This is achieved using techniques like cosine similarity with word embeddings.
- **Suggestions**: Provides a list of suggestions to replace phrases in the input text with their more "standard" versions. Each suggestion displays the original phrase, the recommended replacement, and the similarity score.

## Getting Started
1. Clone the repository.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run `python scripts/app.py` to launch the application.

## Usage
The UI comprises three main sections:

- **Standardized Phrases Input**: Load a list of standardized phrases from a CSV or text file by clicking the "Open Standardized Phrases" button or by dragging and dropping the file onto the designated area.
- **Text Input**: Load the text to be analyzed from a text file by clicking the "Open Text" button or by dragging and dropping the file onto the designated area.
- **Result Output**: Click the "Find Similar Phrases" button to run the analysis. The section below will populate with a list of suggestions for phrase replacements.
## Script Structure
- **scripts/app.py**: Contains the code for the UI, file input/output, and triggering the text analysis.
- **scripts/text_analyzer.py**: Contains the `phrase_finder` function which uses a pre-trained language model to compare the input text with the standardized phrases and find similarities.