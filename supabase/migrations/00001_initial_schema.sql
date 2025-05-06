-- QTravel database schema
-- Follows the Supabase SQL conventions
-- This will be used to set up the SQL schema in Supabase

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

-- Add RLS (Row Level Security) policies for secure data access
-- These policies ensure users can only access their own data

-- RLS for users table
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
CREATE POLICY users_policy ON users 
  USING (auth.uid() = id);

-- RLS for user_preferences table
ALTER TABLE user_preferences ENABLE ROW LEVEL SECURITY;
CREATE POLICY user_preferences_policy ON user_preferences 
  USING (auth.uid() = user_id);

-- RLS for trips table
ALTER TABLE trips ENABLE ROW LEVEL SECURITY;
CREATE POLICY trips_policy ON trips 
  USING (auth.uid() = user_id);

-- RLS for itinerary_items table (via trips)
ALTER TABLE itinerary_items ENABLE ROW LEVEL SECURITY;
CREATE POLICY itinerary_items_policy ON itinerary_items 
  USING (trip_id IN (SELECT id FROM trips WHERE user_id = auth.uid()));

-- RLS for bookings table (via itinerary_items and trips)
ALTER TABLE bookings ENABLE ROW LEVEL SECURITY;
CREATE POLICY bookings_policy ON bookings 
  USING (itinerary_item_id IN (
    SELECT id FROM itinerary_items WHERE trip_id IN (
      SELECT id FROM trips WHERE user_id = auth.uid()
    )
  ));

-- RLS for trip_collaborators table (for shared trips)
ALTER TABLE trip_collaborators ENABLE ROW LEVEL SECURITY;
CREATE POLICY trip_collaborators_policy ON trip_collaborators 
  USING (trip_id IN (SELECT id FROM trips WHERE user_id = auth.uid()));

-- RLS for feedback table
ALTER TABLE feedback ENABLE ROW LEVEL SECURITY;
CREATE POLICY feedback_policy ON feedback 
  USING (user_id = auth.uid());

-- RLS for travel_history table
ALTER TABLE travel_history ENABLE ROW LEVEL SECURITY;
CREATE POLICY travel_history_policy ON travel_history 
  USING (user_id = auth.uid());

-- RLS for ai_interactions table
ALTER TABLE ai_interactions ENABLE ROW LEVEL SECURITY;
CREATE POLICY ai_interactions_policy ON ai_interactions 
  USING (user_id = auth.uid());
