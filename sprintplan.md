# ✈️ AI Travel Planner — One-Day Sprint Plan 🏃‍♂️

### 🗓️ Sprint Duration:

**1 day (8–12 hours)** — Designed for rapid prototyping

---

## 🎯 Sprint Goal

Deliver a working MVP that allows a user to:

1. Create a profile and input trip parameters
2. Generate an AI-powered itinerary
3. View the results in a simple day-by-day format

---

## ✅ Sprint Deliverables

| Feature                   | Description                                                     |
| ------------------------- | --------------------------------------------------------------- |
| 🚀 Basic UI               | Trip input form, profile preferences form                       |
| 🧠 AI Itinerary Generator | Prompt-based LLM call using OpenAI or Ollama                    |
| 🗂️ Supabase Schema       | Deploy SQL schema for users, trips, itinerary\_items            |
| 🌐 API Routes             | Backend endpoints for creating trips and fetching itineraries   |
| 🗺️ Itinerary View        | Basic UI to display daily plan items                            |
| 🧪 Test Prompt            | Working test of one trip generation using fake or real LLM call |
| 📥 Seed Data Script       | Insert demo user and sample trip                                |

---

## ⏱️ Sprint Timeline (Sample Schedule)

| Time        | Task                                                         |
| ----------- | ------------------------------------------------------------ |
| 9:00–10:00  | Set up Supabase schema and seed data                         |
| 10:00–11:00 | Build trip creation form (React/Next.js or simple HTML)      |
| 11:00–12:00 | Implement `/generate-itinerary` API route (FastAPI/Node.js)  |
| 12:00–1:00  | Lunch + Stretch break                                        |
| 1:00–2:00   | Call OpenAI API or mock LLM to generate trip data            |
| 2:00–3:00   | Render itinerary on frontend using grouped day view          |
| 3:00–4:00   | UX polish: Add loading state, error handling, preview toggle |
| 4:00–5:00   | Internal test & feedback loop; improve results; prep demo    |

---

## 🧩 Backlog (Day-1 MVP Only)

```json
[
  { "title": "Setup Supabase schema", "priority": "P0" },
  { "title": "Create user and trip input form", "priority": "P0" },
  { "title": "Implement itinerary generator API (POST /generate)", "priority": "P0" },
  { "title": "Connect OpenAI API and craft initial travel prompt", "priority": "P0" },
  { "title": "Render itinerary results by day on frontend", "priority": "P0" },
  { "title": "Add loading + error states", "priority": "P1" },
  { "title": "Build demo user seed script", "priority": "P1" },
  { "title": "Enable map pins for items with geo data", "priority": "P2" },
  { "title": "Enable itinerary editing (drag/drop)", "priority": "P2" }
]
```

---

## 🧪 Demo Acceptance Criteria

* [ ] User can input destination, duration, and travel style
* [ ] System generates a day-by-day itinerary with 2–3 items/day
* [ ] Output is visible on a clean UI grouped by day
* [ ] No major errors or blockers
* [ ] MVP works with mocked or real LLM integration

---

## 🛠️ Optional Tools / Stack

* **Frontend**: React or Next.js
* **Backend**: FastAPI or Express
* **DB**: Supabase (PostgreSQL)
* **AI**: OpenAI (gpt-4 or gpt-3.5), or local Ollama model
* **Deployment**: Vercel or Supabase Edge Functions for demo

---

