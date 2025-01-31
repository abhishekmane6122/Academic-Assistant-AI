import streamlit as st
import tempfile
import os
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from google.generativeai.types.safety_types import HarmBlockThreshold, HarmCategory

# Safety configuration
safety_config = {
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
}

# Model initialization
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=st.secrets["GOOGLE_API_KEY"],
    temperature=0.2,
    safety_settings=safety_config
)

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=st.secrets["GOOGLE_API_KEY"],
    task_type="retrieval_document"
)

# Properly escaped prompt templates
PROMPTS = {
    "Natural Language Processing": PromptTemplate(
        template="""**NLP Expert Analysis**
Context: {context}
Question: {question}

Respond with:
1. Linguistic concept breakdown
2. Relevant architecture diagrams
3. Mathematical notation (e.g., $$e^{{i\\theta}} = \\cos{{\\theta}} + i\\sin{{\\theta}}$$)
4. Framework code snippets
5. Research references (Author, Year)
Answer:""",
        input_variables=["context", "question"]
    ),
    "Advance Computer Vision": PromptTemplate(
        template="""**CV Specialist Response**
Context: {context}
Question: {question}

Include:
1. Image processing steps
2. Matrix operations (e.g., $$K = \\begin{{bmatrix}}f & 0 & c_x\\\\ 0 & f & c_y\\\\ 0 & 0 & 1\\end{{bmatrix}}$$)
3. CNN architecture
4. Vision library code
5. Conference references
Answer:""",
        input_variables=["context", "question"]
    ),
    "Data Engineering": PromptTemplate(
        template="""**Data Engineering Solution**
Context: {context}
Question: {question}

Structure:
1. ETL pipeline design
2. Spark/Airflow implementation
3. SQL optimization
4. Data modeling
5. Scalability analysis
Answer:""",
        input_variables=["context", "question"]
    ),
    "Block Chain Technology": PromptTemplate(
        template="""**Blockchain Analysis**
Context: {context}
Question: {question}

Must contain:
1. Cryptographic explanations
2. Smart contract code
3. Consensus comparisons
4. Validation steps
5. Whitepaper references
Answer:""",
        input_variables=["context", "question"]
    ),
    "Time Series Forcasting": PromptTemplate(
        template="""**Time Series Report**
Context: {context}
Question: {question}

Include:
1. Model equations (e.g., $$ARIMA(p,d,q)$$)
2. Decomposition analysis
3. LSTM structure
4. Evaluation metrics
5. Implementation code
Answer:""",
        input_variables=["context", "question"]
    )
}

def process_uploaded_file(uploaded_file):
    """Process PDF files into document chunks"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getbuffer())
        tmp_path = tmp_file.name
    
    loader = PyPDFLoader(tmp_path)
    raw_docs = loader.load()
    os.unlink(tmp_path)
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=200,
        separators=["\\n\\n", "\\n", "(?<=\. )", " ", ""]
    )
    return splitter.split_documents(raw_docs)

def initialize_qa_system(docs, subject):
    """Create vector store and QA chain for a subject"""
    vector_db = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=f"/tmp/chroma_db/{subject.replace(' ', '_')}"  # Use /tmp directory
    )
    vector_db.persist()
    
    retriever = MultiQueryRetriever.from_llm(
        retriever=vector_db.as_retriever(search_kwargs={"k": 5}),
        llm=llm
    )
    
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": PROMPTS[subject]},
        return_source_documents=True
    )

def main():
    """Streamlit application interface"""
    st.set_page_config(page_title="Academic Expert System", layout="wide" , page_icon="🎓")
    st.title("Subject-Specific Academic Assistant")
    
    # Create subject tabs
    tabs = st.tabs(list(PROMPTS.keys()))
    
    for idx, subject in enumerate(PROMPTS.keys()):
        with tabs[idx]:
            st.header(f"{subject} Portal")
            
            # File upload section
            uploaded_file = st.file_uploader(
                f"Upload {subject} Materials (PDF only)",
                type=["pdf"],
                key=f"{subject}_upload"
            )
            
            if uploaded_file:
                # Process documents on first upload
                doc_key = f"{subject}_processed"
                if doc_key not in st.session_state:
                    with st.spinner(f"Processing {subject} materials..."):
                        st.session_state[doc_key] = process_uploaded_file(uploaded_file)
                
                # Question input
                query = st.text_input(
                    f"Enter your {subject} question:",
                    key=f"{subject}_query"
                )
                
                if query:
                    # Initialize QA system on first query
                    qa_key = f"{subject}_qa"
                    if qa_key not in st.session_state:
                        st.session_state[qa_key] = initialize_qa_system(
                            st.session_state[doc_key],
                            subject
                        )
                    
                    # Get and display response
                    result = st.session_state[qa_key]({"query": query})
                    
                    # Structured output
                    with st.container():
                        st.subheader("Expert Analysis")
                        st.markdown(result["result"])
                        
                        # Source documents
                        with st.expander("Reference Materials"):
                            for i, doc in enumerate(result["source_documents"], 1):
                                st.markdown(f"**Document {i} (Page {doc.metadata['page']+1})**")
                                st.caption(doc.page_content[:500] + "...")
                    
                    # Subject-specific status
                    st.markdown(f"*{subject} analysis complete*")

if __name__ == "__main__":
    main()
