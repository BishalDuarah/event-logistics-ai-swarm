# Event Logistics AI Swarm

**Autonomous Multi-Agent Event Management System**.

This system simulates an **AI organizing committee** capable of managing large-scale technical events such as hackathons.

---

## Problem

Managing technical events involves repetitive tasks:

* Marketing campaigns
* Participant communication
* Scheduling speakers
* Resolving conflicts
* Sending updates

Manual coordination becomes difficult for large events.

---

## Solution

This project implements a **Multi-Agent AI Swarm** where specialized agents collaborate autonomously.

Agents communicate through a central orchestrator and shared memory.

---

# System Architecture
## Content Agent → Analytics Agent → Scheduler Agent → Email Agent

Agents:

* **Content Strategist Agent**

  * Generates promotional campaigns.

* **Analytics Agent**

  * Evaluates engagement insights.

* **Scheduler Agent**

  * Builds event timeline and resolves conflicts.

* **Email Agent**

  * Automates personalized bulk communication.

---

## Features

* Multi-agent orchestration
* AI-generated marketing campaigns
* Dynamic schedule generation
* Automated email distribution
* Conflict detection and resolution
* Human-in-the-loop approval controls
* Interactive dashboard UI

---

## Tech Stack

Frontend

* React
* TailwindCSS

Backend

* FastAPI
* Python

AI

* Gemini API

---

## Demo Flow

1. Organizer enters event parameters
2. AI Swarm executes agents sequentially
3. Marketing campaign generated
4. Event schedule created
5. Emails prepared for participants
6. Disruption simulation triggers schedule recalculation

---

## How to Run

### Backend

```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```
cd frontend
npm install
npm run dev
```

Open:

```
http://localhost:5173
```

---

## Future Improvements

* Social media scheduling automation
* Speaker availability optimization
* Real-time engagement prediction
* Distributed swarm architecture

---

## Author

Bishal Duarah
B.Tech Computer Science
