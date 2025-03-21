import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_huggingface import HuggingFaceEndpoint

from langchain_huggingface import HuggingFaceEmbeddings  
from langchain_community.vectorstores import FAISS


load_dotenv('/Volumes/Sam t7/Projects/custom_chatbot/Chatbot-on-custom-database/.env')


loader = PyPDFLoader("/Volumes/Sam t7/Projects/custom_chatbot/Chatbot-on-custom-database/400-Finance-Questions.pdf")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=384,
    chunk_overlap=96,
    separators=["\n\n", "\n", ". ", " ", ""]
)
chunked_docs = text_splitter.split_documents(docs)


# 
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'},  # Required parameter [7]
    encode_kwargs={'normalize_embeddings': True}  # Optional but recommended
)
db = FAISS.from_documents(
    documents=chunked_docs,
    embedding=embeddings
)
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.1",
    task="text-generation",
    max_new_tokens=512,
    temperature=0.7,
    top_p=0.95,
    repetition_penalty=1.15
)
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    output_key='answer'
)
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=db.as_retriever(search_kwargs={"k": 4}),
    memory=memory,
    return_source_documents=True,
    get_chat_history=lambda h: h,
    verbose=False
)
def get_chatbot_response(user_input):
    # Format prompt with document context instructions
    formatted_prompt = f"""You are a very smart document reader your task is to answer all the queries which user asks and answer should be from the document i provide if you are not sure of answer just tell it i am not sure about it and tell "have a good day",dont asnwer anything other than the pdf dont use your general llm knowledge.
    
    Question: {user_input}
    
    Helpful Answer:"""
    
    # Execute the chain
    response = qa_chain({"question": formatted_prompt})
    
    # Process sources
    sources = list(set(
        f"Page {doc.metadata['page']+1}"  # Convert 0-index to 1-index
        for doc in response['source_documents']
    ))
    
    return f"{response['answer']}\n\nSources: {', '.join(sources)}"