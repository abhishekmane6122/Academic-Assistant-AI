# 🎓 Subject-Specific Academic Assistant

Welcome to the **Academic Expert System** – an all-in-one canvas solution designed to help you quickly get precise answers for your subject-specific questions by simply uploading your question papers and notes PDFs! 🚀

---

## 🌟 Overview

This repository contains a **Streamlit** application that integrates advanced AI models with state-of-the-art document retrieval. The tool is specifically tailored for subjects like **Natural Language Processing**, **Advanced Computer Vision**, **Data Engineering**, **Blockchain Technology**, and **Time Series Forecasting**. It leverages Google’s Gemini-1.5-flash model alongside a FAISS-based vector database, providing an interactive, fast, and reliable way to extract the right answer from your uploaded materials. 


## 🔍 Key Features

- **Subject-Specific Analysis:**  
  Each subject has its custom prompt template tailored to provide detailed expert analysis with linguistic breakdowns, architecture diagrams, code snippets, mathematical notations, and research references.
  
- **Seamless PDF Upload & Processing:**  
  Easily upload your **question papers** and **notes PDFs**. The system processes these files by splitting them into manageable document chunks for effective retrieval.
  
- **Advanced Retrieval-Based QA System:**  
  Utilizes FAISS for vector-based retrieval combined with a MultiQuery Retriever. This ensures that you get the most relevant sections from your documents with minimal hassle.
  
- **Google Generative AI Integration:**  
  Powered by the Gemini-1.5-flash model, the system generates context-aware and accurate responses tailored to your academic needs.
  
- **All-In-One Canvas Layout:**  
  The interactive, canvas-style layout in Streamlit organizes each subject’s portal neatly, allowing you to switch effortlessly between subjects and review detailed responses alongside reference materials. 🎨

---

## 🔄 How It Works

1. **Upload Your PDFs:**  
   Simply drag and drop your question papers and class notes into the app interface. 📂

2. **Document Processing:**  
   The tool processes the PDFs by splitting them into chunks, ensuring efficient and precise retrieval.  
   ➡️ **Behind the Scenes:** Uses `PyPDFLoader` and `RecursiveCharacterTextSplitter` to prepare the content.

3. **Enter Your Question:**  
   Type your subject-specific question in the input field provided in each subject tab. ❓

4. **Retrieve & Answer:**  
   The system retrieves the most relevant document chunks using a vector database (FAISS) and generates a detailed answer via the Gemini-1.5-flash model. 🧠

5. **Review References:**  
   The output includes source document references so you can easily verify or dive deeper into the material. 🔎

---

# Academic Expert System 🎓

**A Smart Solution for Academic Q&A Using Your Course Materials**  
*Powered by Gemini AI + LangChain + Streamlit*

![Demo](https://via.placeholder.com/800x400?text=Academic+QA+System+Demo)  
*Replace with actual demo GIF*

## 📖 Problem Statement: Why I Built This
As a student, I constantly face these challenges:
1. **Manual Cross-Checking**: When solving question papers, I need to:
   - Type questions into ChatGPT
   - Search same questions on Google
   - Verify answers against multiple PDF notes
2. **PDF Navigation Issues**:
   - Teachers' notes often contain redundant text
   - Hard to find exact answers in lengthy PDFs
   - Page numbers don't always match between materials

This multi-step process can be overwhelming, especially when your class notes contain extra, unnecessary text that doesn't directly contribute to the exam answer. With this tool, you can simply **upload your question paper and your notes PDF** and get a consolidated, accurate answer quickly! ⚡

Imagine if you already have your class notes provided by your subject teacher, yet you still need to sift through the PDF to extract just the relevant answers for your exam. This tool helps you cut through the noise and fetch only what you need. No more redundant text – just the essential, exam-ready answer! 🎯


**Solution**: This tool lets you:
- 📤 Upload question papers + reference PDFs
- ❓ Ask subject-specific questions
- 🚀 Get instant answers verified against **your materials**
- 🔍 See exact PDF sources with page numbers

## ✨ Key Features
| Feature | Description |
|---------|-------------|
| 📚 Multi-Subject Support | NLP, Computer Vision, Data Engineering, Blockchain, Time Series Analysis |
| 🔄 PDF Intelligence | Processes notes to create subject-specific knowledge base |
| 🧠 Context-Aware AI | Combines Gemini's NLP with your materials' context |
| 📊 Technical Response Formatting | Matrices, equations, code snippets, research references |
| 🛡️ Safety-First AI | Content filtering for educational integrity |

## 🛠️ Tech Stack
**Core Components**:
- `Google Gemini 1.5 Flash` - AI reasoning engine
- `LangChain` - Document processing & retrieval
- `FAISS` - Vector similarity search
- `Streamlit` - Web interface

**Supporting Libraries**:
```python
PyPDFLoader, RecursiveCharacterTextSplitter, MultiQueryRetriever, GoogleGenerativeAIEmbeddings
