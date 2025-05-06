````markdown
# ✈️ AI Travel Planner

Welcome to the AI Travel Planner — a full-stack AI-powered travel assistant that generates personalized itineraries based on user preferences, budget, and travel history.

This MVP was built as a one-day sprint using a lean agile approach. It leverages AI (e.g. OpenAI or Ollama), Supabase for backend services, and modern web frameworks for the frontend.

---

## 🚀 Features

- 🌍 **Trip Input Interface**: Define destination, travel dates, style, and budget
- 🧠 **AI Itinerary Generation**: Create personalized day-by-day plans using LLMs
- 🗂️ **Supabase Backend**: Postgres schema for users, trips, and itinerary items
- 🗺️ **Daily View UI**: Itinerary rendered by day, with activity details
- 📦 **Exportable JSON**: Optionally view raw code mode of itinerary
- 🧪 **Seed Data**: Includes demo user and sample trip for testing

---

## 🛠️ Tech Stack

| Layer        | Tool                    |
|--------------|-------------------------|
| Frontend     | React or Next.js        |
| Backend      | FastAPI / Node.js       |
| Database     | Supabase (PostgreSQL)   |
| AI Engine    | OpenAI / Ollama         |
| Deployment   | Vercel / Supabase Edge  |
| Maps         | Google Maps API (future)|
| Styling      | Tailwind CSS            |

---

## 🧾 Data Model (Simplified)

- `users`: User accounts with travel preferences
- `trips`: Each planned trip with destination and dates
- `itinerary_items`: Daily plan items (flights, hotels, activities, etc.)
- `user_preferences`: User-specific category weights (e.g. food, culture)
- `bookings`: Optional integration with booking providers
- `ai_interactions`: Logs AI prompt/response cycles for feedback

---

## ⚙️ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/your-org/ai-travel-planner.git
cd ai-travel-planner
````

2. **Install dependencies**

For frontend:

```bash
cd frontend
npm install
```

For backend (FastAPI example):

```bash
cd backend
pip install -r requirements.txt
```

3. **Configure Supabase**

* Create a project at [https://app.supabase.com/](https://app.supabase.com/)
* Apply schema from `/supabase/schema.sql`
* Set environment variables in `.env`

```env
SUPABASE_URL=...
SUPABASE_KEY=...
OPENAI_API_KEY=...
```

4. **Run locally**

Frontend:

```bash
npm run dev
```

Backend:

```bash
uvicorn main:app --reload
```

---

## 📦 API Endpoints

| Method | Endpoint              | Description                               |
| ------ | --------------------- | ----------------------------------------- |
| POST   | `/generate-itinerary` | Accepts trip data, returns JSON itinerary |
| GET    | `/trip/:id`           | Fetches a saved trip plan                 |

---

## 📸 Screenshots

> *(Add after building UI — wireframes, map view, and itinerary render)*

---

## 🧠 Prompt Format (Sample)

```text
Create a 5-day itinerary for Tokyo under $1500. Traveler prefers food, culture, and nature. Include 3 activities per day, hotel, and basic transport.
```

---

## 📌 Roadmap (Post MVP)

* 🗺️ Map view with drag-and-drop reordering
* 🤝 Collaborative trip planning with friends
* 🔄 Real-time re-planning with weather/API triggers
* 🛎️ Booking integrations: Skyscanner, Booking.com, GetYourGuide
* 📱 Mobile offline access / PWA support

---

## 👥 Team & Credits

* Lead Developer: \[Your Name]
* Design: \[Contributor or Figma link]
* Prompt Engineering: \[Your Name / ChatGPT]
* APIs: Supabase, OpenAI, Google Maps (optional)

---

## 📄 License

This project is private and licensed for internal or demo use only.

```

---

Would you like a public open-source version of this `README` with badges and deploy buttons included?
```
