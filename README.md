# 📄 AI Document Summarizer
open: http://127.0.0.1:8000

<p align="center">
  <strong>Upload documents. Extract important information. Get a concise summary.</strong>
</p>

<p align="center">
  A web-based document processing application built with Python, FastAPI, HTML, CSS, and JavaScript.
</p>

---

## 🚀 Overview

**AI Document Summarizer** is a web application that helps users quickly understand the contents of documents.

Users can upload **PDF, DOCX, or TXT** files. The application extracts the text, processes the content, generates a concise summary, identifies key points, displays document statistics, and allows the user to download the results.

The current version uses a **lightweight local text-processing approach**, so **no external AI API key is required**.

---

## ✨ Features

| Feature            | Description                          |
| ------------------ | ------------------------------------ |
| 📤 Document Upload | Upload PDF, DOCX, and TXT files      |
| 📄 Text Extraction | Extract readable text from documents |
| 📝 Summarization   | Generate a concise summary           |
| 📌 Key Points      | Extract important sentences          |
| 🔢 Word Count      | Display total number of words        |
| 🔤 Character Count | Display total number of characters   |
| 📥 Download        | Download the generated summary       |
| 📱 Responsive UI   | Works on desktop and mobile screens  |
| ⚡ FastAPI Backend  | Fast and lightweight Python backend  |
| 🔒 File Validation | Validate supported document formats  |

---

## 🖥️ Application Workflow

```text
             ┌──────────────────┐
             │      User        │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Upload Document  │
             │ PDF / DOCX / TXT │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │   FastAPI API    │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │  Text Extraction │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Text Processing  │
             └────────┬─────────┘
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
      Summary    Key Points   Statistics
          │           │           │
          └───────────┼───────────┘
                      ▼
             ┌──────────────────┐
             │ Display Results  │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Download Summary │
             └──────────────────┘
```

---

## 📁 Supported Documents

| Format  | Support |
| ------- | :-----: |
| 📕 PDF  |    ✅    |
| 📘 DOCX |    ✅    |
| 📄 TXT  |    ✅    |

---

## 🛠️ Technology Stack

### Backend

* **Python** — Core programming language
* **FastAPI** — Backend API framework
* **Uvicorn** — ASGI server
* **PDF/DOCX processing libraries** — Document text extraction

### Frontend

* **HTML5** — Application structure
* **CSS3** — Styling and responsive design
* **JavaScript** — Frontend logic and API communication

### Development Tools

* **Git**
* **GitHub**
* **Virtual Environment**

---

## 📂 Project Structure

```text
ai-document-summarizer/
│
├── backend/
│   ├── main.py
│   ├── summarizer.py
│   └── utils.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── uploads/
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

### Backend

`main.py`

Handles:

* FastAPI application
* API routes
* File uploads
* File validation
* Serving the frontend

`utils.py`

Handles document text extraction.

`summarizer.py`

Handles:

* Text summarization
* Key-point extraction
* Word counting

### Frontend

`index.html`

Provides the application interface.

`style.css`

Provides the visual design and responsive layout.

`script.js`

Handles:

* File selection
* API requests
* Displaying results
* Downloading summaries

---

# 🔄 How It Works

### 1. Select a document

The user selects a PDF, DOCX, or TXT file.

### 2. Upload the document

The frontend sends the selected document to the FastAPI backend.

### 3. Validate the file

The backend checks whether the document format is supported.

### 4. Extract the text

The application extracts readable text from the uploaded document.

### 5. Process the text

The extracted content is processed to generate:

* Summary
* Key points
* Word count
* Character count

### 6. Display the results

The processed information is returned to the frontend and displayed to the user.

### 7. Download

The user can download the summary and key points as a text file.

---

# 🔌 API Endpoints

## `GET /`

Returns the main web application.

---

## `GET /health`

Checks whether the backend is running.

### Example response

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

### Example response

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

# 📊 Results

After processing a document, the application displays:

### 📝 Summary

A concise version of the document's content.

### 📌 Key Points

Important sentences extracted from the document.

### 📈 Statistics

* Word count
* Character count
* Original filename

### 📥 Download

The generated summary and key points can be downloaded as a `.txt` file.

---

# ⚙️ Installation

## Prerequisites

Make sure you have:

* Python 3.9 or newer
* Git
* A modern web browser

---

## 1. Clone the repository

```bash
git clone https://github.com/shashanknagabhushana/ai-document-summarizer.git
```

## 2. Enter the project

```bash
cd ai-document-summarizer
```

## 3. Create a virtual environment

```bash
python3 -m venv venv
```

## 4. Activate the virtual environment

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## 6. Start the application

```bash
python -m uvicorn backend.main:app --reload
```

## 7. Open the application

Visit:

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

The Swagger interface can be used to test the API directly.

---

# 🧪 Testing

You can test the application with:

### TXT

Create a `.txt` file containing sample text and upload it.

### PDF

Upload a text-based PDF document.

### DOCX

Upload a Word document containing readable text.

The application should return the document summary, key points, and statistics.

---

# 🔐 Security

The application currently includes basic file validation and filename sanitization.

It:

* Validates supported extensions
* Prevents unsafe file paths
* Handles extraction errors
* Rejects unsupported file formats

For production deployment, additional security should be implemented, including:

* File-size limits
* Malware scanning
* Authentication
* Rate limiting
* HTTPS
* Secure file storage
* Stronger file-content validation

---

# 📈 Future Improvements

The current version provides a complete local document-processing workflow.

Possible future improvements include:

### 🤖 AI-Powered Summarization

Integrate a modern AI model to generate more natural and context-aware summaries.

### 🎚️ Summary Length

Allow users to select:

```text
Short
Medium
Detailed
```

### 🖱️ Drag and Drop

Allow users to drag documents directly into the upload area.

### 📚 Document History

Store previously processed documents and their summaries.

### 👤 User Authentication

Allow users to create accounts and securely access their documents.

### 🗄️ Database Integration

Store document metadata and generated summaries.

### ☁️ Cloud Deployment

Deploy the application for public access.

### 🌐 Multi-Language Support

Support documents written in multiple languages.

---

# 🎯 Learning Objectives

This project demonstrates practical experience with:

* Python programming
* FastAPI development
* REST API design
* Frontend development
* JavaScript API integration
* File handling
* Document processing
* Text processing
* Error handling
* Git and GitHub
* Virtual environments
* Basic web application architecture

---

# 💡 Project Motivation

Reading long documents can take significant time, especially when users only need the most important information.

This project aims to simplify that process through a straightforward workflow:

```text
Upload
   ↓
Extract
   ↓
Process
   ↓
Summarize
   ↓
Understand
   ↓
Download
```

The application focuses on keeping the user experience simple while providing useful document insights.

---

# 📌 Current Status

### ✅ Completed

The current version includes:

* [x] PDF upload
* [x] DOCX upload
* [x] TXT upload
* [x] Text extraction
* [x] Local summarization
* [x] Key-point extraction
* [x] Word count
* [x] Character count
* [x] Summary download
* [x] Responsive frontend
* [x] FastAPI backend
* [x] GitHub project setup

### 🚧 Planned

* [ ] AI-powered summarization
* [ ] Drag-and-drop upload
* [ ] Summary length selection
* [ ] Document history
* [ ] Authentication
* [ ] Database
* [ ] Cloud deployment

---

# 👨‍💻 Author

## Shashank P N

**Computer Science and Engineering Student**

### Interests

* Software Development
* Artificial Intelligence
* Machine Learning
* Data Analytics
* Cloud Technologies

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

<p align="center">
  <strong>Built with Python, FastAPI, HTML, CSS, and JavaScript.</strong>
</p>
