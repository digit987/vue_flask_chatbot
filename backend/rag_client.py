import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from openai import OpenAI

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def extract_files():
    documents = []
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset")
    files = os.listdir(directory)
    pdf_files = [file for file in files if file.endswith('.pdf')]
    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory, pdf_file)
        loader = PyPDFLoader(pdf_path)
        documents.extend(loader.load_and_split())
    return documents

def store_documents():
    documents = extract_files()
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)
    retriever = db.as_retriever()
    return retriever

def build_rag_chain():
    retriever = store_documents()

    template = """
    You are an assistant for question-answering tasks related to children. While answering, you also have to strictly include the
    knowledge base provided to you. This includes child development, there food recommendations etc. See the context and question and answer.
    Question: {question}
    Context: {context}
    Answer:
    """

    prompt = ChatPromptTemplate.from_template(template)

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    rag_chain = (
        {"context": retriever,  "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain

def invoke_rag_chain(query):
    rag_chain = build_rag_chain()
    response = rag_chain.invoke(query)
    return response