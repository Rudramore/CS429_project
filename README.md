# Web Crawling and Search Engine Project

## Abstract:

The primary objective of this project is to develop a web-based search engine capable of crawling, indexing, and retrieving relevant information from websites. The core functionalities include web crawling using Scrapy, indexing and ranking documents based on TF-IDF and cosine similarity calculations using scikit-learn, and handling user queries through a Flask-based interface.

The project focuses on building a search engine type application that utilizes the Flask backend processor as a method to communicate between the user and the documents available on the engine that serve the users needs. A spider class is implemented through the scrapy library to scrape webpages from a set of allowed links and domains eligible for scraping and stores the data in an inverted index along with its Tf-idf values deduced from once it is cleaned through a pipeline module.
  
The search engine aims to provide users with a seamless experience by offering features such as query validation, error-checking, and top-k ranked results. Optional enhancements include concurrent and distributed crawling, vector embedding representations, semantic search using kNN similarity, query spelling correction, and query expansion.

The anticipated outcome is a fully operational search engine that can efficiently crawl, index, and retrieve relevant information from websites based on user queries. Future development steps include performance optimizations, integration with additional data sources, and exploration of advanced techniques in natural language processing and information retrieval.

## Overview:

The proposed system is a web-based search engine designed to retrieve relevant information from websites based on user queries. The search engine consists of three main components: a web crawler, an indexer, and a query processor. The web crawler, implemented using Scrapy, is responsible for retrieving web documents from specified seed URLs and domains. The indexer, built with scikit-learn, processes the retrieved documents, calculates TF-IDF scores, and constructs an inverted index for efficient retrieval. The query processor, developed using Flask, handles user queries, performs necessary preprocessing and validation, and returns top-k ranked results based on cosine similarity scores.
The development of this search engine is inspired by existing web search engines and information retrieval systems, which have proven to be invaluable tools for navigating and accessing the vast amount of information available on the internet. The proposed system aims to leverage established techniques in web crawling, indexing, and natural language processing to provide users with a reliable and efficient search experience.

## Features

<li> Web Crawling: Automated spiders to crawl specified domains and collect documents.</li>
<li>Document Indexing: Utilizes TF-IDF scoring for indexing documents, enabling efficient search and relevance scoring.</li>
<li>Search Interface: A Flask-based web application allowing users to input queries and receive ranked search results.</li>
<l>Respect for robots.txt: Ensures ethical crawling by adhering to website-specific crawling restrictions.</l>

## Design:

The search engine should meet the following functional requirements:

1. Web Crawling: The system should be capable of crawling websites based on provided seed URLs and domains, with the ability to specify maximum pages and crawling depth.
2. Indexing: Retrieved web documents should be processed, and an inverted index should be constructed to facilitate efficient retrieval. The indexing process should incorporate techniques such as TF-IDF and cosine similarity calculations.
3.	Query Processing: Users should be able to submit free-text queries through a web interface. The system should validate and preprocess the queries, perform necessary error-checking, and return top-k ranked results based on relevance scores.
4.	User Interface: The search engine should provide a user-friendly interface for submitting queries and displaying search results.
5.	Optional Features: Depending on the project's scope, additional features such as concurrent and distributed crawling, vector embedding representations, semantic search using kNN similarity, query spelling correction, and query expansion could be implemented.

The integration of the crawler, indexer, and query processor components is crucial for the overall functionality of the search engine. The web crawler will retrieve web documents, which will be processed and indexed by the indexer. The query processor will then utilize the constructed index to retrieve and rank relevant results based on user queries.

## Architecture:

The search engine's software architecture consists of the following main components:

1.	Web Crawler (Scrapy): This component is responsible for crawling websites and retrieving web documents based on the provided seed URLs and domains. It handles the initialization, crawling logic, and data extraction from the crawled pages.
2.	Indexer (scikit-learn): The indexer processes the retrieved web documents, performs text preprocessing (e.g., stopword removal, lemmatization), calculates TF-IDF scores, and constructs an inverted index for efficient retrieval. It also handles the storage and retrieval of the index and associated metadata. An inverted index is a data structure used in information retrieval to facilitate fast full-text searches. It's called an "inverted" index because it inverts the process of indexing, which is typically done by creating a forward index that maps documents to the terms they contain. In an inverted index, each term is associated with a list of documents that contain that term.Scikit-learn is a popular machine learning library for Python that includes a variety of tools for text analysis, including a TfidfVectorizer for converting text into a matrix of TF-IDF features. Here's an example of how to use TfidfVectorizer to create an inverted index:
3.	Query Processor (Flask): This component handles user queries submitted through a web interface. It validates and preprocesses the queries, performs error-checking, and interacts with the indexer to retrieve and rank relevant results based on cosine similarity scores. It also manages the presentation of search results to the user.

The web crawler and indexer components interact by exchanging the retrieved web documents and associated metadata. The query processor interacts with the indexer to retrieve and rank relevant results based on user queries. Additionally, the query processor interacts with the web interface to receive user input and display search results.

The items.py file in the provided codebase serves as a container to store the extracted data from web pages efficiently, making it easier to process and use in the inverted index construction.

In the Scrapy framework, items.py defines the data structure for the scraped data, similar to a Python class with attributes corresponding to the desired fields. This approach allows for a structured and organized way of storing and accessing the scraped data.
In the given items.py file, the HtmlscraperItem class is defined, which inherits from the scrapy.Item class. It has three fields:
- url: Stores the URL of the crawled web page.
- text: Stores the extracted text content from the web page.
- title: Stores the title of the web page.

These fields act as containers to store the corresponding data extracted by the spider during the crawling process. In the testspider.py file, the spider yields instances of HtmlscraperItem with the extracted data, which are then processed by the HtmlscraperPipeline in the pipelines.py file.

In the HtmlscraperPipeline, the process_item method receives the HtmlscraperItem instances and stores the url, text, and title data in separate lists (self.url, self.text, and self.title, respectively). These lists are then used to construct the inverted index, where the url and text fields are essential for mapping the URLs to their corresponding text content and calculating the TF-IDF scores.

By using the HtmlscraperItem class as a container, the scraped data is organized and can be easily accessed and processed during the indexing stage. This approach promotes code reusability, modularity, and maintainability, as the data structure can be extended or modified without affecting the core functionality of the spider or the pipeline.

The pickle format is helpful in constructing an inverted index because it allows you to serialize and deserialize Python objects, which can be useful for storing and retrieving data structures like inverted indices. An example of how you might use pickle to create an inverted index as a dictionary. We then iterate over each file, tokenize the contents of the file, and add each token to the inverted index with a list of the file numbers where it appears. Finally, we serialize the inverted index to a pickle file using pickle.dump().

Based on the implementation of the Articlespider class, bThe provided code demonstrates how different websites require different selectors and paths to access HTML content due to their varying structures and pagination mechanisms. Here's an explanation of how the code handles this:

1. Handling Different Domains:
- The parse method in the ArticleSpider class checks the domain of the current URL being processed using urlparse(response.url).netloc. Based on the domain, it calls a specific parsing function tailored for that website. For example, if the domain is 'arxiv.org', it calls the arxiv method, and if it's 'proceedings.neurips.cc' or 'papers.neurips.cc', it calls the neurips method.

2. Using Different CSS/XPath Selectors:
- Each parsing function (e.g., arxiv, neurips, coursera, ruder, robotreport) uses CSS or XPath selectors specific to the website's HTML structure to extract the desired information, such as the title, text content, and URL. For instance, the arxiv method uses response.css('h1.title.mathjax::text') to extract the title, while the neurips method uses response.css('h4::text').

3. Handling Pagination:
- The commented-out section in the parse method demonstrates how to handle pagination for websites like therobotreport.com. - It checks if the current page number is within the max_depth_count limit, constructs the next page URL, and yields a new request to the parse method with the next page URL.

4. Extracting Different Content:
- Some websites may have different structures or formats for presenting the desired content. For example, the arxiv method extracts the title and abstract paragraph, while the neurips method extracts the title, authors, and abstract text. The code adjusts the selectors and processing logic accordingly to handle these variations.
- By implementing separate parsing functions for different domains and using tailored CSS/XPath selectors, the code can effectively handle the diverse HTML structures and content formats across various websites. Additionally, the code demonstrates how to handle pagination by constructing and following the next page URLs when applicable.
- It's important to note that as websites evolve and change their HTML structures, the selectors and parsing logic may need to be updated to ensure the crawler continues to work correctly. Robust error handling and regular maintenance are essential for web crawlers to adapt to changes in the target websites.
- The internal workings of each component involve various techniques and algorithms specific to their respective domains. For example, the web crawler may utilize techniques for URL extraction, politeness policies, and parallelization. The indexer may employ text preprocessing, feature extraction, and indexing algorithms. The query processor may involve query parsing, tokenization, and ranking algorithms.

## Operation:

To set up and operate the search engine, follow these steps:
1.	Install the required software dependencies listed in the requirements.txt file using a package manager like pip.
2.	Clone or download the source code from the provided repository.
3.	Configure the system by specifying the seed URLs, domains, and other relevant parameters (e.g., maximum pages, crawling depth) in the appropriate configuration files or scripts.
4.	Run the web crawler component to initiate the crawling process and retrieve web documents.
5.	Execute the indexer component to process the retrieved documents and construct the inverted index.
6.	Start the Flask-based query processor component, which will expose a web interface for submitting queries and displaying search results.
7.	Access the web interface through a web browser and interact with the search engine by entering queries and browsing the search results.

## Getting Started

### Prerequisites

<li>Python 3x</li>
<li>Pip and virtualenv</li>

### Installation

#### 1. Clone the Repository

```
git clone https://github.com/yourusername/yourprojectname.git
cd yourprojectname
```
#### 2. Set Up a Virtual Environment

```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

#### 3. Set Up a Virtual Environment

```
pip install -r requirements.txt
```

#### Running the Project

1. **Start the Crawling Process**: Navigate to the Scrapy project directory and start the crawling process.
```
cd scrapy_project
scrapy crawl yourspidername
```

2. **Run the Flask Application**: After crawling and processing, start the Flask application to serve search queries.
```
cd ../flask_app
flask run
```

### Usage

Running the base python module controlling renders of created html templates for different queries is vital to running the app smoothly.

### License

Distributed under the MIT License. See LICENSE for more information.

## Conclusion:

The search engine project aims to develop a fully functional system capable of crawling websites, indexing retrieved documents, and providing relevant search results based on user queries. The anticipated outcome is a web-based application that can efficiently retrieve and rank information from websites, enhancing the user experience in accessing and navigating online content.
- The major breakthroughs in the project included:
1. Backend and Frontend Synchronization:
+ The project excelled in integrating the backend processes with the user interface. This synchronization ensures that user queries are processed efficiently, and results are displayed in a clear and concise manner, enhancing user experience.
2. Stable Search Capabilities:
+ Even though navigation through hyperlinks was limited, the engine successfully indexed and searched static content. This core functionality was tested thoroughly and performed well under the constraints of the current system architecture.
3. Scalable Architecture:
+ The design and implementation of the system were carried out with scalability in mind. Although some advanced features are yet to be perfected, the existing framework supports easy integration and expansion. Future versions can build on this to include more complex functionalities such as dynamic hyperlink navigation and page count adjustments.
4. Educational Value:
+The project served as an excellent educational tool, providing practical experience in integrating various software engineering principles from web crawling to frontend development. This experience is invaluable for academic and professional growth.

- Challenges and Opportunities for Improvement
While the project succeeded in establishing a robust foundation for a search engine, there were notable challenges in fully implementing some of the more advanced functionalities, which provide clear directions for future development:

1. Hyperlink Traversal:
+ The system was designed to crawl through multiple pages by following hyperlinks. However, implementing a robust mechanism to automatically detect and navigate through pagination links (e.g., "Next Page") proved challenging. The crawler often missed these navigational cues, which limited the depth and breadth of content that could be indexed.
2. Dynamic Content Handling:
+ The crawler struggled with dynamically generated content and links, which are increasingly common in modern web applications. These elements often require interaction or trigger JavaScript execution, which were not fully accounted for in the initial crawler design.

3. Vector Embedding Implementation:
+ The integration of vector embeddings such as Word2Vec for enhancing semantic understanding of texts was initiated but not completed. While basic semantic grouping was implemented, providing a superficial layer of context recognition, the full potential of embedding complex semantic relationships in the search algorithm remains untapped.
Semantic Search Capability:
+ The project aimed to incorporate semantic search functionalities to enhance the relevance of search results by understanding the deeper meanings behind queries. However, this was only partially achieved. The current system can group documents that are contextually similar at a basic level but lacks the ability to fully interpret and match based on the nuanced meanings of the query terms.
4. Query Expansion Techniques:
+ Another area where the project faced challenges was in the implementation of query expansion using tools like WordNet. The intention was to broaden the search results by including synonyms and related terms, enhancing the engine's ability to handle diverse queries. This feature was only partially developed, and its integration is crucial for improving the search engine's comprehensiveness and accuracy.
+ While the core functionalities of web crawling, indexing, and query processing have been implemented, there may be limitations in terms of scalability, performance, and the breadth of features offered. Future improvements could include optimizing the system for large-scale deployments, incorporating advanced natural language processing techniques for query understanding and result ranking, and integrating with additional data sources or specialized domains.
+ It is important to note that the success of the project will be evaluated based on thorough testing and benchmarking against predefined test cases and performance metrics. Additionally, potential ethical considerations, such as privacy and data protection, should be addressed to ensure responsible and ethical use of the search engine.

- Recommendations for Future Enhancements
* Implement Advanced Crawling Techniques: To better handle dynamic content and complex web architectures.
* Optimize System Performance: Through code optimization and better resource allocation to handle increased load.
* Enhance Security Measures: To protect against web vulnerabilities and ensure data integrity and user safety.
* Upgrade Ranking Algorithms: To incorporate more sophisticated metrics and potentially integrate machine learning techniques for better accuracy.

## Data Sources:

During the development and testing phases of the project, the following data sources were utilized:

- ArXiv.org - An open-access archive for scientific papers in various fields, including computer science, physics, and mathematics.
- Proceedings.neurips.cc - A collection of papers presented at the Neural Information Processing Systems (NeurIPS) conference.
- Papers.neurips.cc - Another repository of NeurIPS conference papers.
- Coursera.org - An online learning platform offering courses and educational materials.
-  Ruder.io - A blog focused on natural language processing and machine learning.
- TheRobotReport.com - A news website covering the latest developments in robotics and automation.

These data sources were chosen to provide a diverse set of web documents for testing the search engine's crawling, indexing, and retrieval capabilities across different domains and content types.
* Test Cases
- The search engine was thoroughly tested using a comprehensive testing framework and various test scenarios. The testing process aimed to validate the functionality and performance of each component, as well as the integration between components.
  
* The testing framework included the following components:

- Unit Tests: Individual components, such as the web crawler, indexer, and query processor, were subjected to unit testing to verify their correct behavior and functionality.
Integration Tests: The interactions and data flow between the different components were tested to ensure proper integration and end-to-end functionality.
- Performance Tests: The system was benchmarked under various load conditions and with different data volumes to evaluate its performance characteristics, such as crawling speed, indexing time, and query response times.
- User Acceptance Tests: A set of test cases was designed to simulate real-world usage scenarios, including various types of queries, edge cases, and error conditions, to validate the search engine's usability and robustness.

The test cases covered a wide range of scenarios, including but not limited to:

1. Crawling websites with different structures and content types
2. Indexing documents with varying lengths and complexities
3. Processing queries with different levels of complexity and ambiguity
4. Handling edge cases, such as empty or malformed queries
5. Evaluating the relevance and ranking of search results
6. Measuring the system's performance and scalability under different load conditions

## Test cases:

Given that the search focuses mainly on natural language processing papers and articles, machine learning and robotics articles, the inputs are given as follows

### Input 1:


### Output 1:


Extends further but more links and scores 
Additional home button to restart the search for a specific topic

### Input 2:


### Output 2:



Default value of 10 documents so that the user can increase more later

### Input 3:



Basic use of topic without adding top documents generally bringing out highest grossing articles matching the topic but can be more specific although focused more on the research side 










## Bibliography:


-   Olston, Christopher, and Marc Najork. "Web Crawling." Foundations and Trends® in Information Retrieval 4, no. 3 (2010): 175-246. https://doi.org/10.1561/1500000017. 
- Desikan, Purnesh, and Justin Heinonen. "Inverted Indices for Phrase-Based Information Retrieval." In Proceedings of the 21st ACM International Conference on Information and Knowledge Management, 2012. https://doi.org/10.1145/2396761.2396786. 
- Manning, Christopher D., Prabhakar Raghavan, and Hinrich Schütze. Introduction to Information Retrieval. Cambridge University Press, 2008. https://nlp.stanford.edu/IR-book/. 
- Baeza-Yates, Ricardo, and Berthier Ribeiro-Neto. Modern Information Retrieval. 2nd ed. Addison-Wesley, 2011. 
-  Zhai, ChengXiang, and Sean Massung. "Text Data Management and Analysis: A Practical Introduction to Information Retrieval and Text Mining." ACM SIGMOD Record 45, no. 2 (2016): 3-11. https://doi.org/10.1145/2980742.2980746. 
- Koopman, Ben, and Guido Zampieri. "Pragmatic Neural Retrieval." In Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, 2020. https://doi.org/10.1145/3394486.3403113. 
- Gormley, Clinton, and Zachary Tong. Elasticsearch: The Definitive Guide. O'Reilly Media, Inc., 2015. 
-  Salton, Gerard, and Michael J. McGill. Introduction to Modern Information Retrieval. McGraw-Hill, Inc., 1986. 
-  Blanco, Roi, and Christina Lioma. "Estimating Term Relevance Scores via TF-IDF Alternatives and Its Relationship with Information Retrieval Scale Transitions." Information Retrieval Journal 23, no. 1 (2020): 109-139. https://doi.org/10.1007/s10791-019-09364-5. 
  Schütze, Hinrich, Christopher D. Manning, and Prabhakar Raghavan. Introduction to Information Retrieval. Vol. 39. Cambridge University Press, 2008.

- Python Software Foundation. "pickle - Python object serialization." Accessed April 19, 2024. https://docs.python.org/3/library/pickle.html.

- Machine Learning Plus. "Creating Inverted Index with Python." Accessed April 19, 2024. https://www.machinelearningplus.com/python/inverted-index-python/.

- Python Software Foundation. "string - Operations on strings." Accessed April 18, 2024. https://docs.python.org/3/library/string.html#string.punctuation.

- Python Software Foundation. "Input and Output." Accessed April 18, 2024. https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files.

- Python Software Foundation. "Data Structures." Accessed April 19, 2024. https://docs.python.org/3/tutorial/datastructures.html.

- Python Software Foundation. "Dictionaries." Accessed April 18, 2024. https://docs.python.org/3/tutorial/datastructures.html#dictionaries.

- Python Software Foundation. "More on Lists." Accessed April 18, 2024. https://docs.python.org/3/tutorial/datastructures.html#more-on-lists.

- Python Software Foundation. "Tuples and Sequences." Accessed April 19, 2024. https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences.

- Python Software Foundation. "Sets." Accessed April 18, 2024. https://docs.python.org/3/tutorial/datastructures.html#sets.

- Python Software Foundation. "String Methods." Accessed April 19, 2024. https://docs.python.org/3/library/stdtypes.html#string-methods.

- Python Software Foundation. "TextIOWrapper Object." Accessed April 18, 2024. https://docs.python.org/3/library/io.html#io.TextIOWrapper.read.

- Python Software Foundation. "Pickle Protocols." Accessed April 18, 2024. https://docs.python.org/3/library/pickle.html#pickle-protocols.

- Python Software Foundation. "Pickle Security." Accessed April 18, 2024. https://docs.python.org/3/library/pickle.html#pickle-security.

- Python Software Foundation. "Pickle Performance." Accessed April 19, 2024. https://docs.python.org/3/library/pickle.html#pickle-performance.

- Python Software Foundation. "Pickle Examples." Accessed April 19, 2024. https://docs.python.org/3/library/pickle.html#pickle-example.

- Python Software Foundation. "Pickle Out-of-Band Buffers." Accessed April 19, 2024. https://docs.python.org/3/library/pickle.html#pickle-out-of-band.

- Real Python. (2021). Web Scraping using Python. Retrieved from https://realpython.com/python-web-scraping-practical-introduction/

- DataCamp. (2021). Web Scraping with Beautiful Soup and Scrapy. Retrieved from https://www.datacamp.com/community/tutorials/web-scraping-using-python-r

- W3Schools. (2021). Web Scraping using Python. Retrieved from https://www.w3schools.com/python/python_web_scraping.asp

- Scrapy. (2021). Handling Different Domains in Scrapy. Retrieved from https://docs.scrapy.org/en/latest/topics/media-pipeline.html#handling-different-domains

- W3Schools. (2021). CSS Selectors. Retrieved from https://www.w3schools.com/cssref/css_selectors.asp

- W3Schools. (2021). XPath Selectors. Retrieved from https://www.w3schools.com/xml/xpath_intro.asp
- ScrapingBee. (2021). CSS Selectors vs XPath Selectors. Retrieved from https://www.scrapingbee.com/blog/css-selectors-vs-xpath/
- Scrapy. (2021). Handling Pagination in Scrapy. Retrieved from https://docs.scrapy.org/en/latest/topics/practices.html#handling-pagination
- GeeksforGeeks. (2021). Handling Pagination using Python. Retrieved from https://www.geeksforgeeks.org/web-scraping-pagination-using-python/


















