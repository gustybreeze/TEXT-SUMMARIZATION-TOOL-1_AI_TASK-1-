# TEXT-SUMMARIZATION-TOOL-1-AI-TASK-1

*COMPANY*: CODTECH IT SOLUTIONS PVT.LTD

*NAME*: SAMEER KUMAR MISHRA

*INTERN ID*: CT04DZ379

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR


**Task 1: Text Summarization Tool**


**Overview**
Text summarization is a fundamental problem in Natural Language Processing (NLP) that deals with the process of shortening long pieces of text into concise summaries while preserving the original meaning and important information. In this task, I developed a Text Summarization Tool that can automatically generate summaries of large paragraphs, articles, or documents using Python and essential NLP libraries. This tool aims to make reading more efficient and help users grasp the key ideas without reading the entire content.

The project primarily focused on extractive summarization, which involves identifying and extracting the most important sentences from the source text, rather than generating new ones (as done in abstractive summarization). Extractive methods are easier to implement and more reliable for maintaining factual accuracy.


**Objectives**
- To understand and implement the concept of extractive text summarization.

- To build a Python-based application that can take any text input and generate a concise summary.

- To work with various NLP preprocessing techniques like tokenization, stopword removal, sentence scoring, etc.

- To apply scoring mechanisms to rank the importance of each sentence.

- To produce meaningful and readable summaries based on the most informative sentences.


**Tools & Technologies Used**
- Python 3.10+: Main programming language.

- NLTK (Natural Language Toolkit): For natural language processing tasks like tokenization, stopword removal,     and frequency analysis.

- spaCy (optional): Used for more advanced NLP preprocessing and sentence parsing.

- BeautifulSoup4 (optional): For cleaning HTML content if working with web-scraped data.

- Tkinter (optional GUI): For creating a basic interface to input text and show summarized output.


**Working Process**
1. Input Text
The user inputs a long text (either copy-pasted or read from a file). This can be an article, essay, research paper, news story, or blog post.

2. Preprocessing
The input text is preprocessed through the following steps:

- Sentence Tokenization: Breaking the content into individual sentences.

- Word Tokenization: Breaking sentences into words.

- Lowercasing all words for uniformity.

- Removing stopwords (common but uninformative words like “and”, “the”, “is”).

- Removing punctuation and irrelevant symbols.

3. Frequency Analysis
Each word is analyzed for frequency (excluding stopwords). Words occurring more frequently in the text are considered more informative. The frequency of words is normalized to ensure fair comparison.

4. Sentence Scoring
Each sentence is scored based on the cumulative frequency of the important words it contains. This score helps in ranking the sentences by relevance.

5. Summary Generation
Based on the sentence scores, the top N highest-scoring sentences are selected to form the summary. The number N can be user-defined or calculated automatically as a percentage of the original content.

6. Output Display
The final summary is printed in the console or shown through a GUI if implemented. The summary is coherent, grammatically correct, and retains the main points of the original input.


**Outcomes**
- The tool was successfully able to generate short summaries from large input texts.

- It significantly reduced reading time while preserving key information.

- The system showed consistent performance across different types of texts such as academic content, blogs, and   news articles.

- This project enhanced my understanding of fundamental NLP concepts like tokenization, stopword filtering,       frequency-based scoring, and sentence ranking.


**Learnings**

Through this task, I gained practical exposure to real-world NLP workflows. I learned how to preprocess and manipulate text data, extract meaningful insights from natural language, and implement intelligent summarization logic using simple yet effective techniques. This laid the foundation for more advanced NLP projects such as abstractive summarization, question-answering systems, and text classification.


**Output**
<img width="1918" height="862" alt="Image" src="https://github.com/user-attachments/assets/9d4c5987-0690-4edc-9e79-68f3180f7b5f" />

