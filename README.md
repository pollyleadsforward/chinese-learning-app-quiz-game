# Chinese Learning App 🇨🇳

A mobile-first Chinese vocabulary quiz designed for practical technical vocabulary used in Product Management, Core Banking, System Integration, Testing, Deployment, Incident Management, and AI-related work.

Created by **pollyleadsforward** 🌸

---

## Overview

This project was built as a personal Chinese vocabulary review application, combining language learning with technical vocabulary used in real-world product and technology environments.

The application includes:

- Multiple-choice vocabulary quizzes
- Immediate feedback
- Spaced review for incorrectly answered words
- Separate progress tracking by category
- Mobile-first responsive design
- Android PWA support
- Custom pastel interface and app icon

The app contains more than **500 vocabulary items across 5 learning categories**.

---

## Vocabulary Categories

| Category | Focus |
|---|---|
| **CBS — Core Banking System** | Core banking and digital lending |
| **System & API** | Systems, APIs, integration and data |
| **Incident & Operations** | Incidents, monitoring and operations |
| **AI / LLM / Platform** | AI, LLM, RAG and platform concepts |
| **Testing / UAT / Deployment** | Testing, UAT, release and deployment |

---

## Learning Logic

The app uses a simple spaced-review mechanism.

When a vocabulary question is answered incorrectly:

**Wrong answer → Review after 5 other questions → Review again after another 10 questions**

Each vocabulary category maintains its own score and review progress.

---

## Technology

**Python · Streamlit · HTML/CSS · GitHub · Streamlit Community Cloud · GitHub Pages · PWA**

---

## Mobile Architecture

```text
Android / Mobile
        ↓
GitHub Pages PWA
        ↓
Streamlit Community Cloud
        ↓
GitHub / app.py
