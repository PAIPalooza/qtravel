"""
Tests for the Supabase database schema for the QTravel application.
Following BDD testing strategy as specified in the QTravel coding standards.
"""
import sys
import os
import unittest
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

# Add the parent directory to the path so we can import the models
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.models import Base, User, UserPreference, Trip, ItineraryItem, Booking

class TestDatabaseSchema(unittest.TestCase):
    """Test suite to validate the Supabase database schema"""
    
    def setUp(self):
        """Set up an in-memory SQLite database for testing"""
        # For real tests, we would use a test Supabase instance
        # But for schema validation, we can use SQLite in-memory
        self.engine = create_engine('sqlite:///:memory:', echo=False)
        Base.metadata.create_all(self.engine)
        
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    
    def tearDown(self):
        """Clean up after tests"""
        Base.metadata.drop_all(self.engine)
        self.session.close()
    
    def test_users_table_exists(self):
        """Test that the users table is created with correct columns"""
        inspector = inspect(self.engine)
        self.assertIn('users', inspector.get_table_names())
        
        columns = [column['name'] for column in inspector.get_columns('users')]
        expected_columns = ['id', 'email', 'full_name', 'language', 
                           'travel_style', 'dietary_restrictions', 
                           'accessibility_needs', 'created_at']
        for column in expected_columns:
            self.assertIn(column, columns)
    
    def test_user_preferences_table_exists(self):
        """Test that the user_preferences table is created with correct columns"""
        inspector = inspect(self.engine)
        self.assertIn('user_preferences', inspector.get_table_names())
        
        columns = [column['name'] for column in inspector.get_columns('user_preferences')]
        expected_columns = ['id', 'user_id', 'category', 'weight', 'created_at']
        for column in expected_columns:
            self.assertIn(column, columns)
    
    def test_trips_table_exists(self):
        """Test that the trips table is created with correct columns"""
        inspector = inspect(self.engine)
        self.assertIn('trips', inspector.get_table_names())
        
        columns = [column['name'] for column in inspector.get_columns('trips')]
        expected_columns = ['id', 'user_id', 'title', 'destination', 
                           'start_date', 'end_date', 'total_budget', 'created_at']
        for column in expected_columns:
            self.assertIn(column, columns)
    
    def test_itinerary_items_table_exists(self):
        """Test that the itinerary_items table is created with correct columns"""
        inspector = inspect(self.engine)
        self.assertIn('itinerary_items', inspector.get_table_names())
        
        columns = [column['name'] for column in inspector.get_columns('itinerary_items')]
        expected_columns = ['id', 'trip_id', 'type', 'title', 'description',
                           'address', 'start_time', 'end_time', 'cost',
                           'provider_name', 'external_link', 'booking_status', 'created_at']
        for column in expected_columns:
            self.assertIn(column, columns, f"Column {column} not found in itinerary_items")
    
    def test_can_create_user(self):
        """Test that we can create a user in the database"""
        user = User(
            email="test@example.com",
            full_name="Test User",
            language="en",
            travel_style="adventure",
            dietary_restrictions=["vegetarian"],
            accessibility_needs=[]
        )
        self.session.add(user)
        self.session.commit()
        
        # Query the user back from the database
        user_from_db = self.session.query(User).filter(User.email == "test@example.com").first()
        self.assertEqual(user_from_db.email, "test@example.com")
        self.assertEqual(user_from_db.full_name, "Test User")
    
    def test_user_trip_relationship(self):
        """Test the relationship between users and trips"""
        # Create a user
        user = User(
            email="trip_test@example.com",
            full_name="Trip Test User"
        )
        self.session.add(user)
        self.session.commit()
        
        # Create a trip for the user
        trip = Trip(
            user_id=user.id,
            title="Test Trip",
            destination="Test Destination",
            total_budget=1000.00
        )
        self.session.add(trip)
        self.session.commit()
        
        # Query the user and check their trips
        user_from_db = self.session.query(User).filter(User.email == "trip_test@example.com").first()
        self.assertEqual(len(user_from_db.trips), 1)
        self.assertEqual(user_from_db.trips[0].title, "Test Trip")
        
        # Query the trip and check the user
        trip_from_db = self.session.query(Trip).filter(Trip.title == "Test Trip").first()
        self.assertEqual(trip_from_db.user.email, "trip_test@example.com")
    
    def test_trip_itinerary_item_relationship(self):
        """Test the relationship between trips and itinerary items"""
        # Create a user
        user = User(email="itinerary_test@example.com")
        self.session.add(user)
        self.session.commit()
        
        # Create a trip
        trip = Trip(
            user_id=user.id,
            title="Itinerary Test Trip"
        )
        self.session.add(trip)
        self.session.commit()
        
        # Create itinerary items for the trip
        item1 = ItineraryItem(
            trip_id=trip.id,
            type="activity",
            title="Test Activity",
            cost=50.00
        )
        item2 = ItineraryItem(
            trip_id=trip.id,
            type="hotel",
            title="Test Hotel",
            cost=200.00
        )
        self.session.add_all([item1, item2])
        self.session.commit()
        
        # Query the trip and check its itinerary items
        trip_from_db = self.session.query(Trip).filter(Trip.title == "Itinerary Test Trip").first()
        self.assertEqual(len(trip_from_db.itinerary_items), 2)
        
        # Check that costs are correct
        total_cost = sum(item.cost for item in trip_from_db.itinerary_items if item.cost is not None)
        self.assertEqual(total_cost, 250.00)
    
    def test_booking_relationship(self):
        """Test the relationship between itinerary items and bookings"""
        # Create the necessary objects
        user = User(email="booking_test@example.com")
        self.session.add(user)
        self.session.commit()
        
        trip = Trip(user_id=user.id, title="Booking Test Trip")
        self.session.add(trip)
        self.session.commit()
        
        item = ItineraryItem(
            trip_id=trip.id,
            type="flight",
            title="Test Flight"
        )
        self.session.add(item)
        self.session.commit()
        
        # Create a booking for the itinerary item
        booking = Booking(
            itinerary_item_id=item.id,
            confirmation_number="ABC123",
            provider="Test Airline",
            status="confirmed"
        )
        self.session.add(booking)
        self.session.commit()
        
        # Query the item and check its booking
        item_from_db = self.session.query(ItineraryItem).filter(ItineraryItem.title == "Test Flight").first()
        self.assertIsNotNone(item_from_db.booking)
        self.assertEqual(item_from_db.booking.confirmation_number, "ABC123")
        self.assertEqual(item_from_db.booking.status, "confirmed")

if __name__ == '__main__':
    unittest.main()
