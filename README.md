# 📄 AI Document Summarizer

> **A modern web application for uploading documents, extracting their content, generating concise summaries, identifying key points, and downloading the results.**

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi\&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-Frontend-E34F26?logo=html5\&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Styling-1572B6?logo=css3\&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Frontend-F7DF1E?logo=javascript\&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🌟 Overview

**AI Document Summarizer** is a web-based document processing application designed to make long documents easier to understand.

Users can upload supported documents and receive:

* 📝 A concise summary
* 📌 Important key points
* 🔢 Word count
* 🔤 Character count
* 📥 A downloadable summary

The application provides a simple interface while using a **FastAPI backend** to handle document uploads and text processing.

> **Current version:** The summarization functionality uses lightweight local text processing and does not require an external AI API key.

---

## ✨ Features

### 📤 Document Upload

Upload documents directly through the web interface.

Supported formats:

| File Type | Supported |
| --------- | :-------: |
| 📕 PDF    |     ✅     |
| 📘 DOCX   |     ✅     |
| 📄 TXT    |     ✅     |

---

### 📝 Automatic Summarization

The application processes the extracted document text and produces a concise summary.

This makes it easier to quickly understand the main content without reading the entire document.

---

### 📌 Key Point Extraction

Important sentences are extracted and presented as easy-to-read bullet points.

This allows users to quickly identify the major information contained in the document.

---

### 📊 Document Statistics

The application displays useful document statistics:

* Total word count
* Total character count
* Uploaded filename

---

### 📥 Download Summary

Users can download the generated summary and key points as a `.txt` file for later use.

---

### 📱 Responsive Interface

The frontend is designed to work across:

* 💻 Desktop
* 💻 Laptop
* 📱 Mobile

---

## 🖥️ Application Preview

### Upload Interface

The application provides a clean upload interface where users can select their document.

```text
┌──────────────────────────────────────────┐
│                                          │
│              📄                          │
│                                          │
│       Upload your document               │
│                                          │
│      PDF • DOCX • TXT                    │
│                                          │
│          [ Choose File ]                 │
│                                          │
└──────────────────────────────────────────┘

          [ Summarize Document ]
```

### Results

After processing:

```text
┌──────────────────────────────────────────┐
│          Document Summary                │
│                                          │
│  Words              Characters           │
│  245                 1,482                │
│                                          │
│  📝 Summary                              │
│  ──────────────────────────────────────  │
│  Concise document summary appears here.  │
│                                          │
│  📌 Key Points                           │
│  • Important point one                   │
│  • Important point two                   │
│  • Important point three                 │
│                                          │
│       [ Download Summary ]               │
└──────────────────────────────────────────┘
```

---

# 🏗️ System Architecture

```text
                    ┌───────────────────┐
                    │       User        │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   Web Frontend    │
                    │ HTML / CSS / JS   │
                    └─────────┬─────────┘
                              │
                              │ HTTP Request
                              ▼
                    ┌───────────────────┐
                    │   FastAPI Server  │
                    │     Backend       │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Document Upload   │
                    │ & Validation      │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │  Text Extraction  │
                    │ PDF / DOCX / TXT  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Text Processing   │
                    └─────────┬─────────┘
                              │
                 ┌────────────┼────────────┐
                 ▼            ▼            ▼
             Summary      Key Points    Statistics
                 │            │            │
                 └────────────┼────────────┘
                              ▼
                    ┌───────────────────┐
                    │   Results Page    │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Download Summary  │
                    └───────────────────┘
```

---

# 🧰 Technology Stack

## Backend

| Technology         | Purpose                     |
| ------------------ | --------------------------- |
| 🐍 Python          | Core programming language   |
| ⚡ FastAPI          | REST API and backend server |
| 📄 PDF processing  | PDF text extraction         |
| 📝 DOCX processing | DOCX text extraction        |

## Frontend

| Technology | Purpose                                |
| ---------- | -------------------------------------- |
| HTML5      | Page structure                         |
| CSS3       | Styling and responsive design          |
| JavaScript | User interaction and API communication |

---

# 📁 Project Structure

```text
ai-document-summarizer/
│
├── backend/
│   │
│   ├── main.py
│   │   ├── FastAPI application
│   │   ├── document upload endpoint
│   │   └── API routes
│   │
│   ├── summarizer.py
│   │   ├── summary generation
│   │   ├── key point extraction
│   │   └── word counting
│   │
│   └── utils.py
│       └── document text extraction
│
├── frontend/
│   │
│   ├── index.html
│   │   └── Application interface
│   │
│   ├── style.css
│   │   └── Responsive styling
│   │
│   └── script.js
│       └── Frontend logic and API communication
│
├── uploads/
│   └── Uploaded documents
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🔄 Application Workflow

The application follows this process:

### 1️⃣ Select Document

The user selects a PDF, DOCX, or TXT document.

### 2️⃣ Upload

The frontend sends the document to the FastAPI `/upload` endpoint.

### 3️⃣ Validate

The backend checks whether the uploaded file has a supported extension.

### 4️⃣ Extract Text

The backend extracts readable text from the uploaded document.

### 5️⃣ Process

The extracted text is processed to generate:

* Summary
* Key points
* Word count
* Character count

### 6️⃣ Display Results

The results are returned to the frontend and displayed in a clean interface.

### 7️⃣ Download

The user can download the summary as a text file.

---

# 🔌 API Endpoints

## `GET /`

Returns the main application interface.

### Response

```text
AI Document Summarizer Web Application
```

---

## `GET /health`

Checks whether the backend is running.

### Example Response

```json
{
    "status": "healthy"
}
```

---

## `POST /upload`

Uploads and processes a document.

### Supported formats

```text
.pdf
.docx
.txt
```

### Example Response

```json
{
    "filename": "example.txt",
    "characters": 1482,
    "word_count": 245,
    "summary": "Document summary...",
    "key_points": [
        "Important point one",
        "Important point two",
        "Important point three"
    ]
}
```

---

# 🚀 Installation

## Prerequisites

Make sure you have:

* Python 3.9 or newer
* Git
* A modern web browser

---

## 1. Clone the Repository

```bash
git clone https://github.com/shashanknagabhushana/ai-document-summarizer.git
```

---

## 2. Enter the Project

```bash
cd ai-document-summarizer
```

---

## 3. Create Virtual Environment

```bash
python3 -m venv venv
```

---

## 4. Activate Virtual Environment

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## 6. Start the Server

```bash
python -m uvicorn backend.main:app --reload
```

---

## 7. Open the Application

Open your browser and visit:

```text
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically generates interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use the Swagger interface to test the API endpoints directly.

---

# 🧪 Testing

The application can be tested using:

### TXT

Create a text file:

```text
test.txt
```

Add sample content and upload it through the application.

### PDF

Upload any text-based PDF document.

### DOCX

Upload a Microsoft Word document containing text.

---

# 🔐 Security Considerations

The application currently performs basic file validation.

It:

* Checks supported file extensions
* Sanitizes uploaded filenames
* Stores uploaded files in the uploads directory
* Rejects unsupported formats
* Handles extraction errors

For production deployment, additional security measures should be implemented, including:

* File size limits
* Malware scanning
* Authentication
* Rate limiting
* Secure temporary storage
* HTTPS
* Stronger file validation

---

# 📈 Future Development

The current version provides the complete document-processing workflow.

Possible future improvements include:

### 🤖 AI Integration

Replace the lightweight local summarization approach with a modern AI model.

### 🎯 Multiple Summary Modes

Allow users to choose:

```text
Short
Medium
Detailed
```

### 🖱️ Drag & Drop

Allow users to drag documents directly into the upload area.

### 📚 Document History

Store previously processed documents and their summaries.

### 👤 Authentication

Add user accounts and private document storage.

### ☁️ Cloud Deployment

Deploy the application to a cloud platform.

### 🗄️ Database

Store document metadata and generated summaries.

### 🌐 Multiple Languages

Support document summarization in multiple languages.

---

# 🎯 Project Goals

This project was developed to demonstrate practical skills in:

* Backend API development
* Frontend development
* File handling
* Document processing
* REST API communication
* Python programming
* Web application architecture
* Git and GitHub workflow

---

# 💡 Why This Project?

Long documents can take significant time to read and understand.

This application provides a simple workflow:

> **Upload → Process → Understand → Download**

The goal is to reduce the time required to identify the most important information in a document.

---

# 👨‍💻 Author

## Shashank P N

Computer Science and Engineering Student

Interested in:

* Software Development
* Artificial Intelligence
* Data Analytics
* Machine Learning
* Cloud Technologies

---

# ⭐ Project Status

**Current Status:** ✅ Completed

The current application supports document uploading, text extraction, local summarization, key-point extraction, document statistics, and summary downloading.

---

## ⭐ If you find this project useful

Consider giving the repository a ⭐ on GitHub.

**Built with Python, FastAPI, HTML, CSS, and JavaScript.**
