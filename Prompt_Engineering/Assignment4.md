# Adaptive Recommendation Chatbot with RAG and Vector Database

Objective: 

The goal of this assignment is to develop a domain-specific application that combines the strengths of a Large Language Model (LLM) for understanding and processing natural language queries with the efficiency of a vector database for data storage and retrieval. You have the flexibility to choose between creating a semantic search engine, a responsive chatbot, or a personalized recommendation system, each focusing on a specific domain of your interest.

Assignment Description: 

You are required to develop a chatbot that interacts with users to understand their needs and preferences. The chatbot should generate personalized recommendations using Retrieval-Augmented Generation (RAG). The recommendations should be based solely on user inputs and must be accurate to the user's stated preferences. The system should only return information that is present in the vector store.

Key Requirements:
- User Interaction: The chatbot should allow users to input their preferences and needs through a conversational interface.
- RAG-Based Recommendations: Based on the user’s input, the chatbot should generate recommendations using RAG.
- Intelligent Responses: The chatbot must respond appropriately to user requests and queries, providing relevant information and suggestions. It should ensure that the recommendations are accurate to the user's context and preferences.
- Pre-existing Data: Recommendations should be created only from the existing list of data available in the system. The chatbot should not source plans from the internet.
- Backend Integration: The system backend should utilize LangChain to manage the flow of interactions. The details and descriptions should be stored in a vector database of your choice.
- Data Fetching: The system should fetch the top K (K <= 3) data entries based on the user's description using similarity search in the vector database.
- Prompt Engineering for Mock Data: Use prompt engineering to generate the mock data, which will be stored in the vector database for similarity search.

Tasks: 
1. Domain Selection: Choose a specific domain for your application. Clearly define the scope and type of data your application will handle.
2. Data Collection and Preprocessing: Acquire data relevant to your chosen domain by either webscraping or utilizing dynamic data sources.
  -  The dataset should contain textual data that can be indexed in the vector database.
  -  Preprocess the dataset to clean and prepare the data for indexing.
  -  This includes removing any irrelevant information, handling missing data, and ensuring the text is in a suitable format for the LLM.
  -  Ensure the dataset is large enough to showcase your application's functionality.
4. Vector Database Implementation:
  - Choose a vector database suitable for your application needs (e.g., Milvus, Pinecone, or Weaviate).
  - Store your preprocessed dataset in the vector database, ensuring that data is indexed in a way that supports efficient retrieval based on semantic similarity or other relevant criteria.
5. Application Development:
  - Develop your application with a user interface that allows users to input natural language queries or preferences.
  Implement the backend logic to use the LLM for query processing and the vector database for data retrieval, ensuring the system returns relevant and accurate results or responses.
6. Evaluation and Testing:
  - Test your application thoroughly with various queries or inputs to evaluate its performance and accuracy.

Submission Requirements:
- Functional Chatbot: A fully functional chatbot that meets the specified requirements
- Mock Data Generation: Use prompt engineering to create mock data
- Source Code and Documentation: Provide the source code and documentation explaining the implementation details [GitHub Repo]
- Report: A report detailing the approach taken, challenges faced, and how they were overcome. [PDF]
- Video Demonstration: A short video demonstration of the chatbot in action. [Link to Youtube Video attached in the Readme of GitHub Repo] 

Meeting Requirements (80%):
- Functionality (40%): Ensure the chatbot interacts with users to collect preferences and needs accurately. The chatbot must generate recommendations based on user inputs using Retrieval-Augmented Generation (RAG).
- Pre-existing Data (20%): Recommendations should be created only from the existing list of data stored in the system and not sourced from the internet.
- Backend Integration (20%): The system backend should effectively utilize LangChain. The details and descriptions must be stored in a vector database, and the system should fetch the top K data entries based on the user’s description using similarity search.

Creativity (20%):
- Extended Data Structure (3%): Students are encouraged to extend the current data structure to include more features. Examples of extended features include additional types of data, more detailed user preferences, ratings, and reviews, etc.
- Nuanced Understanding (7%): The chatbot’s ability to understand and process nuanced requirements from the user. This includes recognizing complex preferences and constraints.
- Sensible and accurate responses (10%): The chatbot should provide responses that are sensible in real life based on the constraints provided by the user.

Please review the assignment requirements carefully and begin working on your solutions. If you have any questions or need further clarification, do not hesitate to reach out.

Submission:  Publicly accessible GitHub repo URL that contains the code, Readme, PDF report and link to your YouTube video.

-----------------------------------------------------------------------------------------

Example: Travel Itinerary Recommendation Chatbot

Tasks:

1. Domain Selection:
   Domain:Travel Itinerary
   Scope:Provide personalized travel itineraries, including activities, food options, and accommodation based on user preferences.

2. Data Collection and Preprocessing:
   - Acquire data relevant to travel itineraries from travel blogs, tour guides, and local tourism websites.
   - Preprocess the dataset to clean and prepare the data for indexing. This includes removing irrelevant information, handling missing data, and ensuring the text is in a suitable format for the LLM.
   - Ensure the dataset is large enough to showcase your application's functionality.

3. Vector Database Implementation:
   - Choose a vector database suitable for your application needs (e.g., Milvus, Pinecone, or Weaviate).
   - Store your preprocessed dataset in the vector database, ensuring that data is indexed in a way that supports efficient retrieval based on semantic similarity or other relevant criteria.

4. Application Development:
   - Develop your application with a user interface that allows users to input natural language queries or preferences.
   - Implement the backend logic to use the LLM for query processing and the vector database for data retrieval, ensuring the system returns relevant and accurate results or responses.

5. Evaluation and Testing:
   - Test your application thoroughly with various queries or inputs to evaluate its performance and accuracy.

 

1. Meeting Requirements (80%):
- Functionality (40%): Ensure the chatbot interacts with users to collect travel preferences and needs accurately. The chatbot must generate travel recommendations based on user inputs using RAG.
- Pre-existing Travel Plans (20%): Recommendations should be created only from the existing list of plans stored in the system and not sourced from the internet.
- Backend Integration (20%): The system backend should effectively utilize LangChain. The travel plan details and descriptions must be stored in a vector database, and the system should fetch the top K plan data based on the user’s description using similarity search.

2. Creativity (20%):
- Extended Data Structure (3%): Students are encouraged to extend the current data structure to include more features. Examples of extended features include additional activity types, more detailed user preferences, ratings, and reviews for travel plans, etc.
- Nuanced Understanding (7%): The chatbot’s ability to understand and process nuanced requirements from the user. This includes recognizing complex preferences and constraints, such as specific dietary requirements, exact travel times, or multiple concurrent conditions. Examples include:

Simple Query Examples:
- "I want to visit a museum in the afternoon."
- "I am looking for outdoor activities."
- "I need a place for lunch."
- "I want a travel plan for the weekend."
- "Show me available beach activities."

Nuanced Query Examples:
- "I want to visit a museum in the afternoon, then have lunch at a place that serves vegetarian food, and finish with a walk in a nearby park."
- "I am looking for outdoor activities that are wheelchair accessible and pet-friendly, and I would like to end the day with a seafood dinner."
- "I need a travel plan that includes a morning hike, lunch at a vegan restaurant, and an evening show. The restaurant should have gluten-free options, and the show should be family-friendly."
- "I want a weekend travel plan that includes visiting historical sites on Saturday morning, shopping in the afternoon, and a spa in the evening. On Sunday, I want to explore local cuisine for brunch and attend a concert in the evening."
- "Show me beach activities that can accommodate a group of 10 people, are accessible by public transport, and have nearby restaurants open until late evening."

Sensible and accurate responses (10%): The chatbot should provide responses that are sensible in real life based on the constraints provided by the user. Responses should adhere to constraints like:
- "I only have time for a quick lunch between 1 PM and 2 PM, and it should be within walking distance from the office."
- "I want to find activities suitable for kids, including an afternoon nap time and dinner at a place that serves kid-friendly meals."
- "I need recommendations for a quiet place to relax that also offers yoga classes and has a café with vegan options."
- "Show me evening activities available today, preferably live music events, and a place for a late dinner afterwards."
- "Find a nearby park for a morning walk that has jogging tracks, pet-friendly zones, and a smoothie bar."
