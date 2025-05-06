-- QTravel seed data
-- This seed file follows the project coding standards and includes a demo user with sample trip data

-- Demo User
INSERT INTO users (id, email, full_name, language, travel_style, dietary_restrictions)
VALUES (
  '00000000-0000-0000-0000-000000000001', -- Fixed UUID for testing
  'demo@qtravel.example',
  'Demo Traveler',
  'en',
  'cultural',
  ARRAY['vegetarian']
);

-- User Preferences
INSERT INTO user_preferences (user_id, category, weight)
VALUES 
  ('00000000-0000-0000-0000-000000000001', 'food', 8),
  ('00000000-0000-0000-0000-000000000001', 'art', 7),
  ('00000000-0000-0000-0000-000000000001', 'nature', 9),
  ('00000000-0000-0000-0000-000000000001', 'history', 6);

-- Sample Trip
INSERT INTO trips (id, user_id, title, destination, start_date, end_date, total_budget)
VALUES (
  '00000000-0000-0000-0000-000000000002', -- Fixed UUID for testing
  '00000000-0000-0000-0000-000000000001',
  'Tokyo Adventure',
  'Tokyo, Japan',
  '2025-06-15',
  '2025-06-20',
  1500.00
);

-- Sample Itinerary Items
INSERT INTO itinerary_items (trip_id, type, title, description, address, start_time, end_time, cost)
VALUES
  -- Day 1
  (
    '00000000-0000-0000-0000-000000000002',
    'flight',
    'Flight to Tokyo',
    'International flight to Narita Airport',
    'Narita International Airport',
    '2025-06-15 08:00:00',
    '2025-06-15 12:00:00',
    650.00
  ),
  (
    '00000000-0000-0000-0000-000000000002',
    'transport',
    'Airport to Hotel',
    'Narita Express train to Tokyo Station',
    'Tokyo Station',
    '2025-06-15 13:00:00',
    '2025-06-15 14:00:00',
    30.00
  ),
  (
    '00000000-0000-0000-0000-000000000002',
    'hotel',
    'Hotel Check-in',
    'Boutique hotel in Shinjuku district',
    'Shinjuku, Tokyo',
    '2025-06-15 15:00:00',
    '2025-06-15 16:00:00',
    180.00
  ),
  (
    '00000000-0000-0000-0000-000000000002',
    'activity',
    'Evening walk in Shinjuku',
    'Explore the vibrant neighborhood and enjoy dinner',
    'Shinjuku, Tokyo',
    '2025-06-15 18:00:00',
    '2025-06-15 21:00:00',
    40.00
  ),
  
  -- Day 2
  (
    '00000000-0000-0000-0000-000000000002',
    'activity',
    'Meiji Shrine & Harajuku',
    'Visit the peaceful shrine and trendy Harajuku district',
    'Meiji Shrine, Tokyo',
    '2025-06-16 09:00:00',
    '2025-06-16 12:00:00',
    0.00
  ),
  (
    '00000000-0000-0000-0000-000000000002',
    'restaurant',
    'Lunch at local ramen shop',
    'Authentic vegetarian ramen experience',
    'Harajuku, Tokyo',
    '2025-06-16 12:30:00',
    '2025-06-16 13:30:00',
    15.00
  ),
  (
    '00000000-0000-0000-0000-000000000002',
    'activity',
    'Teamlab Borderless Museum',
    'Immersive digital art experience',
    'Odaiba, Tokyo',
    '2025-06-16 15:00:00',
    '2025-06-16 18:00:00',
    35.00
  ),
  
  -- Day 3
  (
    '00000000-0000-0000-0000-000000000002',
    'activity',
    'Tsukiji Outer Market',
    'Explore the famous food market',
    'Tsukiji, Tokyo',
    '2025-06-17 08:00:00',
    '2025-06-17 10:00:00',
    25.00
  ),
  (
    '00000000-0000-0000-0000-000000000002',
    'activity',
    'Imperial Palace Gardens',
    'Serene gardens in the heart of Tokyo',
    'Chiyoda, Tokyo',
    '2025-06-17 11:00:00',
    '2025-06-17 13:00:00',
    0.00
  ),
  (
    '00000000-0000-0000-0000-000000000002',
    'activity',
    'Tokyo National Museum',
    'Japan\'s oldest and largest museum',
    'Ueno Park, Tokyo',
    '2025-06-17 14:00:00',
    '2025-06-17 17:00:00',
    20.00
  ),
  
  -- Day 4
  (
    '00000000-0000-0000-0000-000000000002',
    'activity',
    'Day trip to Mt. Fuji',
    'Scenic trip to iconic Mount Fuji and Lake Kawaguchi',
    'Kawaguchiko, Japan',
    '2025-06-18 08:00:00',
    '2025-06-18 19:00:00',
    120.00
  ),
  
  -- Day 5
  (
    '00000000-0000-0000-0000-000000000002',
    'activity',
    'Asakusa & Sensoji Temple',
    'Visit Tokyo\'s oldest temple and traditional area',
    'Asakusa, Tokyo',
    '2025-06-19 09:00:00',
    '2025-06-19 12:00:00',
    0.00
  ),
  (
    '00000000-0000-0000-0000-000000000002',
    'activity',
    'Tokyo Skytree',
    'Panoramic views from Tokyo\'s tallest structure',
    'Sumida, Tokyo',
    '2025-06-19 14:00:00',
    '2025-06-19 16:00:00',
    25.00
  ),
  (
    '00000000-0000-0000-0000-000000000002',
    'restaurant',
    'Farewell dinner at vegetarian izakaya',
    'Traditional Japanese pub with vegetarian options',
    'Shibuya, Tokyo',
    '2025-06-19 19:00:00',
    '2025-06-19 21:00:00',
    45.00
  ),
  
  -- Day 6
  (
    '00000000-0000-0000-0000-000000000002',
    'hotel',
    'Hotel Check-out',
    'Check out and prepare for departure',
    'Shinjuku, Tokyo',
    '2025-06-20 10:00:00',
    '2025-06-20 11:00:00',
    0.00
  ),
  (
    '00000000-0000-0000-0000-000000000002',
    'transport',
    'Hotel to Airport',
    'Narita Express train to airport',
    'Narita International Airport',
    '2025-06-20 12:00:00',
    '2025-06-20 13:00:00',
    30.00
  ),
  (
    '00000000-0000-0000-0000-000000000002',
    'flight',
    'Flight from Tokyo',
    'International departure',
    'Narita International Airport',
    '2025-06-20 16:00:00',
    '2025-06-20 20:00:00',
    0.00
  );

-- Sample AI Interaction
INSERT INTO ai_interactions (user_id, input, response, purpose, model_used)
VALUES (
  '00000000-0000-0000-0000-000000000001',
  'Create a 5-day itinerary for Tokyo under $1500. I prefer food, culture, and nature.',
  '{"days":[{"day":1,"activities":[...],"accommodation":"Shinjuku Hotel"},...]}',
  'trip_generation',
  'gpt-4'
);
