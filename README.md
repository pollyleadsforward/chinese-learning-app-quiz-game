# Chinese Learning App 🇨🇳

A mobile-first Chinese vocabulary quiz app designed for reviewing technical vocabulary used in Product Management, Core Banking, IT, Testing, Deployment, and AI-related work.

Created by **pollyleadsforward** 🌸

---

## Overview

This application was built as a personal Chinese vocabulary review tool.

The goal is to make technical Chinese vocabulary easier to remember through:

- Multiple-choice quizzes
- Immediate feedback
- Repeated review of incorrectly answered words
- Vocabulary grouping by topic
- Mobile-friendly UI
- Pastel visual design

The application currently contains more than **500 vocabulary items across 5 learning sets**.

---

## Vocabulary Sets

### 1. CBS — Core Banking System
Core banking and digital lending vocabulary.

Examples:

- 系统 — System
- 数据库 — Database
- 接口 — Interface
- 数据源 — Data Source
- 根本原因 — Root Cause
- 回滚 — Rollback

### 2. System & API
System architecture, API, parameters, data transmission, access, and integration vocabulary.

### 3. Incident & Operations
Incident management, monitoring, troubleshooting, operations, risk, and corrective action vocabulary.

### 4. AI / LLM / Platform
Vocabulary related to AI, Large Language Models, RAG, embeddings, model evaluation, monitoring, cost, and platform operations.

### 5. Testing / UAT / Deployment
Testing, UAT, regression testing, environments, deployment, migration, release, and production vocabulary.

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
- Separate score tracking for each vocabulary set
- Correct / Answered / Score dashboard
- 5 selectable vocabulary categories
- Responsive mobile-first interface
- Pastel rainbow visual theme
- Android PWA support
- Custom app icon

---

## Technology

Built with:

- Python
- Streamlit
- HTML / CSS
- GitHub
- Streamlit Community Cloud
- GitHub Pages
- Progressive Web App (PWA)

---

## Run Locally

Install the required packages:

```bash
pip install -r requirements.txt
