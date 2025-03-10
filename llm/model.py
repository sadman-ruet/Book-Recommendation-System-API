import os
import json
from langchain_community.document_loaders import CSVLoader
from llm import config
# LangChain & Pinecone Imports
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain_pinecone import PineconeVectorStore


# Set environment variables
os.environ['PINECONE_API_KEY'] = config.PINECONE_API_KEY
os.environ["GOOGLE_API_KEY"] = config.GOOGLE_API_KEY

# Load CSV
loader = CSVLoader(file_path="dataset/book_updated.csv")
data = loader.load()

# Text Splitter
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(data)

# Embeddings Model (Can be Local LLM)
embeddings = GoogleGenerativeAIEmbeddings(model=config.EMBEDDINGS_MODEL)
llm = ChatGoogleGenerativeAI(
    model=config.LLM_MODEL,
    temperature=config.LLM_TEMPERATURE,
    max_tokens=config.LLM_MAX_TOKENS
)

# Vector Database (Pinecone)
docsearch = PineconeVectorStore.from_documents(texts, embeddings, index_name=config.INDEX_NAME)

# Prompt Template
template = """You are a book recommender system that helps users find books matching their preferences. 
Use the following pieces of context to answer the question at the end. 
For each question, suggest three books with a short description of the plot and why the user might like them.
If you don't know the answer, just say that you don't know—don't make up an answer.
{context}

Question: {question}
Your response:"""

# Recommendation Function
def recommendation(query: str, llm: ChatGoogleGenerativeAI = llm, docsearch: PineconeVectorStore = docsearch, template: str = template):
    prompt = PromptTemplate(template=template, input_variables=["context", "question"])
    
    # Initialize RetrievalQA Chain
    qa = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff", 
        retriever=docsearch.as_retriever(),
        return_source_documents=True, 
        chain_type_kwargs={"prompt": prompt}
    )
    response = qa.invoke({"query": query})
    return response