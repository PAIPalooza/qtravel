# 🗃️ Supabase SQL Data Model for AI Travel Planner

```sql
-- 1. Users Table
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT UNIQUE NOT NULL,
  full_name TEXT,
  language TEXT DEFAULT 'en',
  travel_style TEXT, -- e.g., luxury, backpacking, cultural
  dietary_restrictions TEXT[],
  accessibility_needs TEXT[],
  created_at TIMESTAMP DEFAULT now()
);

-- 2. Preferences Table (Tag-weight pairs)
CREATE TABLE user_preferences (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  category TEXT, -- e.g., "art", "nature", "food"
  weight INT CHECK (weight BETWEEN 1 AND 10), -- user weight for preference
  created_at TIMESTAMP DEFAULT now()
);

-- 3. Trip Table
CREATE TABLE trips (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  title TEXT,
  destination TEXT,
  start_date DATE,
  end_date DATE,
  total_budget NUMERIC(10,2),
  created_at TIMESTAMP DEFAULT now()
);

-- 4. Itinerary Items Table
CREATE TABLE itinerary_items (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  trip_id UUID REFERENCES trips(id) ON DELETE CASCADE,
  type TEXT CHECK (type IN ('flight', 'hotel', 'activity', 'restaurant', 'transport')),
  title TEXT,
  description TEXT,
  location GEOGRAPHY(Point, 4326),
  address TEXT,
  start_time TIMESTAMP,
  end_time TIMESTAMP,
  cost NUMERIC(10,2),
  provider_name TEXT,
  external_link TEXT,
  booking_status TEXT DEFAULT 'unbooked', -- unbooked, booked, cancelled
  created_at TIMESTAMP DEFAULT now()
);

-- 5. Bookings Table
CREATE TABLE bookings (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  itinerary_item_id UUID REFERENCES itinerary_items(id) ON DELETE CASCADE,
  confirmation_number TEXT,
  provider TEXT,
  status TEXT CHECK (status IN ('pending', 'confirmed', 'cancelled')),
  booked_at TIMESTAMP DEFAULT now()
);

-- 6. Trip Collaborators Table
CREATE TABLE trip_collaborators (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  trip_id UUID REFERENCES trips(id) ON DELETE CASCADE,
  collaborator_email TEXT,
  role TEXT CHECK (role IN ('owner', 'editor', 'viewer')) DEFAULT 'viewer',
  invited_at TIMESTAMP DEFAULT now()
);

-- 7. Reviews / Feedback Table
CREATE TABLE feedback (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  trip_id UUID REFERENCES trips(id) ON DELETE CASCADE,
  rating INT CHECK (rating BETWEEN 1 AND 5),
  comments TEXT,
  flagged_issues TEXT[],
  created_at TIMESTAMP DEFAULT now()
);

-- 8. Travel History Table (for AI personalization)
CREATE TABLE travel_history (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  destination TEXT,
  start_date DATE,
  end_date DATE,
  activities TEXT[],
  liked BOOLEAN DEFAULT true,
  notes TEXT,
  created_at TIMESTAMP DEFAULT now()
);

-- 9. System Prompts & Logs (AI interactions)
CREATE TABLE ai_interactions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  input TEXT,
  response TEXT,
  purpose TEXT, -- e.g. 'trip_generation', 'replanning'
  model_used TEXT,
  created_at TIMESTAMP DEFAULT now()
);
```

---

# 🔄 Relationships Diagram (ERD Summary)

* `users` → `trips` (1\:M)
* `users` → `user_preferences` (1\:M)
* `users` → `feedback` (1\:M)
* `trips` → `itinerary_items` (1\:M)
* `itinerary_items` → `bookings` (1:1)
* `trips` → `trip_collaborators` (1\:M)
* `users` → `travel_history` (1\:M)

---

# 🧠 AI Features Supported

* **`user_preferences`** + **`travel_history`** → used for preference embedding & trip scoring
* **`ai_interactions`** → audit trail and feedback loop for LLM improvement
* **`feedback`** → fine-tunes future suggestions per user and contributes to ratings of destinations/activities
* **`bookings`** → track user commitment and offer better filters

---

