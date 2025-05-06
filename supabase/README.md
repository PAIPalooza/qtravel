# QTravel Supabase Schema Setup

This directory contains the SQL migration scripts for setting up the QTravel database schema in Supabase.

## Database Schema

The database schema includes the following tables:

1. `users` - User accounts with travel preferences
2. `user_preferences` - User-specific category weights (e.g., food, culture)
3. `trips` - Each planned trip with destination and dates
4. `itinerary_items` - Daily plan items (flights, hotels, activities, etc.)
5. `bookings` - Integration with booking providers
6. `trip_collaborators` - Collaborative trip planning with friends
7. `feedback` - User ratings and comments on trips
8. `travel_history` - Past travels for AI personalization
9. `ai_interactions` - Logs AI prompt/response cycles for feedback

## Implementation

The schema follows the specifications in the datamodel.md file and implements:

- UUID primary keys for all tables
- Proper foreign key relationships with cascade delete
- Check constraints for data validation
- Row-Level Security (RLS) policies for secure data access
- Default timestamps for auditing

## Files

- `migrations/00001_initial_schema.sql` - Creates all tables with constraints and RLS policies
- `migrations/00002_seed_data.sql` - Inserts demo user and sample trip data for testing

## How to Apply

### Option 1: Supabase Web Interface

1. Go to your Supabase project dashboard
2. Navigate to the SQL Editor
3. Paste the contents of each SQL file and execute them in order

### Option 2: Supabase CLI

1. Install the Supabase CLI
2. Link to your project: `supabase link --project-ref your-project-ref`
3. Push the migrations: `supabase db push`

## Testing

The schema can be tested using the SQLAlchemy models and tests in the `backend` directory:

```bash
cd backend
pip install -r requirements.txt
python -m unittest tests/test_schema.py
```

## Database Relationships

- `users` → `trips` (1:M)
- `users` → `user_preferences` (1:M)
- `users` → `feedback` (1:M)
- `trips` → `itinerary_items` (1:M)
- `itinerary_items` → `bookings` (1:1)
- `trips` → `trip_collaborators` (1:M)
- `users` → `travel_history` (1:M)
