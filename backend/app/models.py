from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date, DateTime, Text, TypeDecorator, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship
from datetime import datetime
import json
import uuid
import os

Base = declarative_base()

# Check if we're in a testing environment
TESTING = os.environ.get('TESTING', 'False') == 'True'

# Custom type for geography to make it compatible with SQLite during testing
if TESTING:
    # If testing with SQLite, we'll use String instead of GEOGRAPHY
    class GEOGRAPHY(String):
        def __init__(self, geometry_type='POINT', srid=4326):
            super().__init__(250)  # Use a string with a reasonable length
else:
    try:
        # For production with PostgreSQL, use the real GEOGRAPHY type
        from sqlalchemy.dialects.postgresql import GEOGRAPHY
    except ImportError:
        # If GEOGRAPHY is not available, fall back to string
        class GEOGRAPHY(String):
            def __init__(self, geometry_type='POINT', srid=4326):
                super().__init__(250)

# For testing with SQLite, we need to handle PostgreSQL array types
if TESTING:
    # SQLite-compatible ARRAY type for testing
    class ARRAY(TypeDecorator):
        impl = String
        cache_ok = True

        def __init__(self, item_type, *args, **kwargs):
            self.item_type = item_type
            super().__init__(500)  # Use a string length sufficient for serialized arrays

        def process_bind_param(self, value, dialect):
            if value is None:
                return None
            return json.dumps(value)

        def process_result_value(self, value, dialect):
            if value is None:
                return None
            return json.loads(value)
else:
    from sqlalchemy import ARRAY

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    full_name = Column(String)
    language = Column(String, default="en")
    travel_style = Column(String)
    dietary_restrictions = Column(ARRAY(String))
    accessibility_needs = Column(ARRAY(String))
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    preferences = relationship("UserPreference", back_populates="user", cascade="all, delete-orphan")
    trips = relationship("Trip", back_populates="user", cascade="all, delete-orphan")
    feedback = relationship("Feedback", back_populates="user", cascade="all, delete-orphan")
    travel_history = relationship("TravelHistory", back_populates="user", cascade="all, delete-orphan")
    ai_interactions = relationship("AIInteraction", back_populates="user", cascade="all, delete-orphan")


class UserPreference(Base):
    __tablename__ = "user_preferences"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    category = Column(String)
    weight = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Add constraint for weight range
    __table_args__ = (
        CheckConstraint('weight >= 1 AND weight <= 10', name='weight_range'),
    )

    # Relationships
    user = relationship("User", back_populates="preferences")


class Trip(Base):
    __tablename__ = "trips"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String)
    destination = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    total_budget = Column(Float(precision=2))
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="trips")
    itinerary_items = relationship("ItineraryItem", back_populates="trip", cascade="all, delete-orphan")
    collaborators = relationship("TripCollaborator", back_populates="trip", cascade="all, delete-orphan")
    feedback = relationship("Feedback", back_populates="trip", cascade="all, delete-orphan")


class ItineraryItem(Base):
    __tablename__ = "itinerary_items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    trip_id = Column(UUID(as_uuid=True), ForeignKey("trips.id", ondelete="CASCADE"), nullable=False)
    type = Column(String)
    title = Column(String)
    description = Column(Text)
    location = Column(GEOGRAPHY(geometry_type='POINT', srid=4326))
    address = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    cost = Column(Float(precision=2))
    provider_name = Column(String)
    external_link = Column(String)
    booking_status = Column(String, default="unbooked")
    created_at = Column(DateTime, default=datetime.utcnow)

    # Add constraint for item type
    __table_args__ = (
        CheckConstraint("type IN ('flight', 'hotel', 'activity', 'restaurant', 'transport')", name='valid_item_type'),
    )

    # Relationships
    trip = relationship("Trip", back_populates="itinerary_items")
    booking = relationship("Booking", back_populates="itinerary_item", uselist=False, cascade="all, delete-orphan")


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    itinerary_item_id = Column(UUID(as_uuid=True), ForeignKey("itinerary_items.id", ondelete="CASCADE"), nullable=False)
    confirmation_number = Column(String)
    provider = Column(String)
    status = Column(String)
    booked_at = Column(DateTime, default=datetime.utcnow)

    # Add constraint for booking status
    __table_args__ = (
        CheckConstraint("status IN ('pending', 'confirmed', 'cancelled')", name='valid_booking_status'),
    )

    # Relationships
    itinerary_item = relationship("ItineraryItem", back_populates="booking")


class TripCollaborator(Base):
    __tablename__ = "trip_collaborators"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    trip_id = Column(UUID(as_uuid=True), ForeignKey("trips.id", ondelete="CASCADE"), nullable=False)
    collaborator_email = Column(String)
    role = Column(String, default="viewer")
    invited_at = Column(DateTime, default=datetime.utcnow)

    # Add constraint for role type
    __table_args__ = (
        CheckConstraint("role IN ('owner', 'editor', 'viewer')", name='valid_collaborator_role'),
    )

    # Relationships
    trip = relationship("Trip", back_populates="collaborators")


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    trip_id = Column(UUID(as_uuid=True), ForeignKey("trips.id", ondelete="CASCADE"), nullable=False)
    rating = Column(Integer)
    comments = Column(Text)
    flagged_issues = Column(ARRAY(String))
    created_at = Column(DateTime, default=datetime.utcnow)

    # Add constraint for rating range
    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='rating_range'),
    )

    # Relationships
    user = relationship("User", back_populates="feedback")
    trip = relationship("Trip", back_populates="feedback")


class TravelHistory(Base):
    __tablename__ = "travel_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    destination = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    activities = Column(ARRAY(String))
    liked = Column(Boolean, default=True)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="travel_history")


class AIInteraction(Base):
    __tablename__ = "ai_interactions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    input = Column(Text)
    response = Column(Text)
    purpose = Column(String)
    model_used = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="ai_interactions")
