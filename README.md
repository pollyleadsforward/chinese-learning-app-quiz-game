# Chinese Learning App 🇨🇳

A mobile-first Chinese vocabulary quiz app designed for reviewing technical vocabulary used in Product Management, Core Banking, System Integration, Testing, Deployment, Incident Management, and AI-related work.

Created by **pollyleadsforward** 🌸

---

## Overview

This application was built as a personal Chinese vocabulary review tool.

The goal is to make technical Chinese vocabulary easier to remember through:

- Multiple-choice quizzes
- Immediate feedback
- Repeated review of incorrectly answered words
- Vocabulary grouping by topic
- Separate progress tracking for each vocabulary set
- Mobile-first responsive design
- Pastel visual theme

The application contains more than **500 vocabulary items across 5 learning sets**.

---

## Vocabulary Sets

### 1. CBS — Core Banking System

Core banking and digital lending vocabulary.

Examples:

- 系统 — System
- 数据库 — Database
- 数据源 — Data Source
- 接口 — Interface
- 根本原因 — Root Cause
- 回滚 — Rollback

### 2. System & API

Vocabulary related to:

- System architecture
- APIs
- Parameters
- Requests and responses
- Data transmission
- Authentication
- Authorization
- Integration

### 3. Incident & Operations

Vocabulary related to:

- Incident management
- Troubleshooting
- Monitoring
- Risk
- Operations
- Corrective actions
- Root cause analysis

### 4. AI / LLM / Platform

Vocabulary related to:

- Artificial Intelligence
- Large Language Models
- RAG
- Embeddings
- Model evaluation
- Hallucination
- Prompt engineering
- Monitoring
- Platform operations

### 5. Testing / UAT / Deployment

Vocabulary related to:

- Test cases
- Integration testing
- UAT
- Regression testing
- Performance testing
- Test environments
- Production environments
- Deployment
- Migration
- Release

---

## Learning Logic

The application uses a simple spaced-review mechanism.

If the learner answers incorrectly:

1. The correct answer is displayed.
2. The same word returns after **5 other questions**.
3. The word is reviewed again after another **10 questions**.

This helps reinforce vocabulary that is harder to remember.

---

## Features

- 🇨🇳 Chinese vocabulary quiz
- 3 multiple-choice answers
- Automatic next question
- Incorrect-answer review queue
- Separate progress for each vocabulary category
- Correct / Answered / Score dashboard
- 5 selectable vocabulary sets
- Mobile-first interface
- Pastel rainbow visual theme
- Custom rabbit illustrations
- Android PWA support
- Custom application icon

---

## Technology

Built with:

- Python
- Streamlit
- HTML
- CSS
- GitHub
- Streamlit Community Cloud
- GitHub Pages
- Progressive Web App (PWA)

---

## Live App

The application is deployed on **Streamlit Community Cloud** and can be accessed on desktop and mobile.

For Android, the application can also be installed as a **Progressive Web App (PWA)** with a custom app icon.

---

## Architecture

```text
Android / Mobile
      ↓
GitHub Pages PWA
      ↓
Streamlit Community Cloud
      ↓
GitHub app.py
