# AI-Powered Document Analysis Chatbot

This project is a sophisticated AI-powered chatbot designed for intelligent document analysis and question answering. It combines a Flask backend with a JavaScript frontend to provide a seamless, interactive experience for users seeking information from uploaded documents.

## Features

-**Text File Analysis**: I processed and analyzed text files (like medical textbooks) using advanced NLP techniques.
-**Intelligent Chunking**: I utilized RecursiveCharacterTextSplitter for optimal text segmentation.
-**Advanced Embedding**: I leveraged Hugging Face embeddings to create high-quality text representations.
-*8Efficient Retrieval**: I employed FAISS to ensure fast and accurate information retrieval.
-*8Powerful Language Model**: I integrated Llama-3-8B to generate human-like responses.
-**Interactive Web Interface**: I provided a user-friendly chat interface for seamless interactions.
-**Real-time Communication**: I enabled smooth communication between the frontend and backend for efficient, real-time question answering.

## Technologies Used

### Backend
- Flask
- LangChain
- Hugging Face
- Cohere
- FAISS
- PyPDF
- Python dotenv

### Frontend
- HTML5
- JavaScript (ES6+)
- CSS3

## Project Structure

- `app.py`: Flask application serving as the backend.
- `chatbot.py`: Core logic for document processing and question answering.
- `static/script.js`: Frontend JavaScript for handling user interactions.
- `templates/index.html`: HTML template for the chat interface.

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables in a `.env` file:
   ```
   HUGGINGFACEHUB_API_TOKEN=your_token_here
   LANGCHAIN_API_KEY=your_key_here
   COHERE_API_KEY=your_key_here
   ```

4. Run the Flask application:
   ```
   python app.py
   ```

5. Open a web browser and navigate to `http://localhost:5000` to use the chatbot.

## Usage

1. Upload a PDF document through the web interface.
2. Type your questions in the chat input.
3. Receive detailed answers based on the content of the uploaded document.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


