# Smart Resume & Job Matching System

## 1. Project Overview

Smart Resume & Job Matching System is a command-line application that analyzes a candidate's resume against a job description.

The system extracts information from a resume PDF, identifies relevant skills, compares them with the skills required by a job description, analyzes education and experience requirements, calculates text similarity using TF-IDF and cosine similarity, and generates a final matching report.

The project is designed to help users understand how closely a resume matches a particular job description and identify skills that may need improvement.

---

## 2. Problem Statement

Recruiters and job seekers often need to compare resumes with job descriptions containing multiple technical and educational requirements.

Manually identifying matching skills, missing skills, education requirements, and relevant experience can be time-consuming.

This project provides a structured automated approach for analyzing a resume against a job description and presenting the results through a command-line interface.

---

## 3. Objectives

- Extract text from resume PDF files.
- Identify technical skills present in the resume.
- Identify skills required by a job description.
- Calculate the percentage of matched skills.
- Identify missing skills.
- Calculate resume-job text similarity using TF-IDF and cosine similarity.
- Analyze education requirements.
- Analyze experience requirements.
- Detect important resume sections.
- Generate recommendations based on missing skills.
- Provide a consolidated final matching report.

---

## 4. Major Features

### Resume PDF Parsing
Extracts textual content from a PDF resume using PyMuPDF.

### Skill Detection
Identifies skills from the resume and job description using a configurable skills database.

### Skill Matching
Compares the candidate's skills with the skills required by the job.

### Text Similarity
Uses TF-IDF vectorization and cosine similarity to calculate similarity between the resume and job description.

### Resume Analysis
Detects sections such as:

- Skills
- Education
- Experience
- Projects

### Education Analysis
Checks education-related requirements mentioned in the job description against the resume.

### Experience Analysis
Checks experience-related requirements against information available in the resume.

### Recommendations
Generates recommendations based on skills missing from the resume.

### Error Handling
Validates required input files and handles file and input errors without exposing unnecessary application tracebacks.

---

## 5. Technologies Used

- Python
- PyMuPDF
- Scikit-learn
- TF-IDF
- Cosine Similarity
- Regular Expressions
- Python unittest
- Command Line Interface

---

## 6. Project Structure

```text
SmartResumeMatcher/
│
├── main.py
├── parser.py
├── skills.py
├── matcher.py
├── analyzer.py
├── reporter.py
├── utils.py
├── requirements.txt
├── .gitignore
│
├── data/
│   └── skills.txt
│
├── samples/
│   ├── resume.pdf
│   └── job.txt
│
└── tests/
    ├── __init__.py
    ├── test_parser.py
    ├── test_skills.py
    ├── test_matcher.py
    └── test_analyzer.py

    ---

## 7. Module Description

| Module | Responsibility |
|---|---|
| `main.py` | Controls the complete application workflow |
| `parser.py` | Extracts text from resume PDF |
| `skills.py` | Loads and detects skills |
| `matcher.py` | Calculates skill match and text similarity |
| `analyzer.py` | Performs resume, education and experience analysis |
| `reporter.py` | Generates and displays the final report |
| `utils.py` | Provides file and input validation utilities |

---

## 8. Installation

### Prerequisites

- Python 3.x
- Internet connection for installing dependencies

### Install Dependencies

Open a terminal in the project directory and run:

```bash
pip install -r requirements.txt