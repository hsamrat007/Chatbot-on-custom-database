
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA


load_dotenv('/Users/harshitsamrat/Documents/python/Anveshak/.env')
os.environ['HUGGINGFACEHUB_API_TOKEN'] = os.getenv("HUGGINGFACEHUB_API_TOKEN")
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['COHERE_API_KEY'] = os.getenv("COHERE_API_KEY")


loader = PyPDFLoader("GHC+2025+R&R+Version+1.0.pdf")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunked = splitter.split_documents(docs)
db = FAISS.from_documents(chunked, CohereEmbeddings())


llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-v0.1",
    task="text-generation",
    max_new_tokens=300,
    do_sample=True,
    temperature=0.7,
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=db.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=True,
)

def get_chatbot_response(user_input):
   
    prompt = f"""Human: {user_input}

Assistant: I will provide a helpful, detailed, and accurate response based on the content of the "GHC+2025+R&R+Version+1.0.pdf" paper. I'll break down the answer step-by-step when appropriate.

"""
    

    result = qa_chain({"query": prompt})
    
  
    answer = result['result']
    sources = [doc.metadata.get('source', 'Unknown') for doc in result['source_documents']]
    
    
    final_response = f"{answer}\n\nSources: {', '.join(sources)}"
    
    return final_response

