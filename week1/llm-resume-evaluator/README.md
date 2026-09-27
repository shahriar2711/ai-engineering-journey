# LLM Resume Evaluator

An LLM-powered resume evaluation system that compares candidate resumes
against a given job description and generates a structured match score
and reasoning.

## Features

- Accepts a job description as text input
- Parses PDF resumes automatically
- Parses DOCX resumes automatically
- Converts resumes into text
- Uses an LLM to extract structured job information
- Uses Pydantic models for structured data
- Extracts structured information from resumes
- Compares resumes against job requirements
- Generates a match score and reasoning
- Supports batch processing of multiple resumes

## Tech Stack

- Python
- Groq API
- GPT-OSS 120B
- Pydantic
- PyPDF
- python-docx
- python-dotenv
- uv

## How It Works

```text
Job Description
       ↓
LLM Job Extraction
       ↓
Structured Job Data
       ↓
PDF / DOCX Resume
       ↓
Text Extraction
       ↓
LLM Resume Parsing
       ↓
Structured Resume Data
       ↓
Resume-JD Matching
       ↓
Match Score + Reasoning