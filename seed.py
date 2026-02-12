# seed.py
from sqlalchemy.orm import Session
from database import SessionLocal
from database_model import User, Venue, Event, Artist, Review, EventArtist
from enums import UserRoleEnum, VenuetypeEnum, GenreEnum
# from passlib.context import CryptContext
import uuid
from datetime import date, time, timedelta

# # Password hashing
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def hash_password(password: str) -> str:
#     return pwd_context.hash(password)

def seed_database():
    db = SessionLocal()
    
    try:
        print("🌱 Starting database seeding...")
        
        # ============================================
        # 1. CREATE USERS (10 users)
        # ============================================
        print("\n📝 Creating users...")
        users = []
        
        user_data = [
            ("John Smith", "john@example.com", "+255712345001", UserRoleEnum.ORGANIZER),
            ("Sarah Johnson", "sarah@example.com", "+255712345002", UserRoleEnum.ORGANIZER),
            ("Michael Brown", "michael@example.com", "+255712345003", UserRoleEnum.ORGANIZER),
            ("Emily Davis", "emily@example.com", "+255712345004", UserRoleEnum.USER),
            ("David Wilson", "david@example.com", "+255712345005", UserRoleEnum.USER),
            ("Lisa Anderson", "lisa@example.com", "+255712345006", UserRoleEnum.USER),
            ("James Taylor", "james@example.com", "+255712345007", UserRoleEnum.USER),
            ("Maria Garcia", "maria@example.com", "+255712345008", UserRoleEnum.ADMIN),
            ("Robert Martinez", "robert@example.com", "+255712345009", UserRoleEnum.USER),
            ("Jennifer Lee", "jennifer@example.com", "+255712345010", UserRoleEnum.USER),
        ]
        
        for full_name, email, phone, role in user_data:
            user = User(
                id=uuid.uuid4(),
                full_name=full_name,
                email=email,
                phone=phone,
                password_hash="password123",
                role=role,
                created_at="2026-02-06"
            )
            users.append(user)
            db.add(user)
        
        db.commit()
        print(f"✅ Created {len(users)} users")
        
        # ============================================
        # 2. CREATE VENUES (10 venues)
        # ============================================
        print("\n🏢 Creating venues...")
        venues = []
        
        venue_data = [
            ("Blue Note Jazz Club", VenuetypeEnum.CLUB, "Premier jazz venue in the heart of the city", 
             "123 Jazz Street, Dar es Salaam", "+255712340001", 200, users[0].id),
            ("The Rock Arena", VenuetypeEnum.ARENA, "Large concert venue for big events", 
             "456 Rock Avenue, Dar es Salaam", "+255712340002", 5000, users[1].id),
            ("Sunset Bar & Lounge", VenuetypeEnum.BAR, "Cozy bar with live music every weekend", 
             "789 Beach Road, Dar es Salaam", "+255712340003", 100, users[2].id),
            ("Grand Concert Hall", VenuetypeEnum.HALL, "Elegant hall for classical and contemporary music", 
             "321 Music Lane, Dar es Salaam", "+255712340004", 800, users[0].id),
            ("Urban Club", VenuetypeEnum.CLUB, "Modern club featuring local and international DJs", 
             "654 Night Street, Dar es Salaam", "+255712340005", 300, users[1].id),
            ("Acoustic Cafe", VenuetypeEnum.BAR, "Intimate cafe with acoustic performances", 
             "987 Coffee Road, Dar es Salaam", "+255712340006", 80, users[2].id),
            ("Bongo Stadium", VenuetypeEnum.ARENA, "Massive outdoor stadium", 
             "147 Stadium Way, Dar es Salaam", "+255712340007", 15000, users[0].id),
            ("Jazz Corner", VenuetypeEnum.CLUB, "Traditional jazz club with vintage vibes", 
             "258 Heritage Street, Dar es Salaam", "+255712340008", 150, users[1].id),
            ("The Gospel House", VenuetypeEnum.HALL, "Dedicated venue for gospel and worship events", 
             "369 Faith Avenue, Dar es Salaam", "+255712340009", 500, users[2].id),
            ("Afrobeat Lounge", VenuetypeEnum.CLUB, "Afrobeat and Afro-fusion hotspot", 
             "741 Rhythm Road, Dar es Salaam", "+255712340010", 250, users[0].id),
        ]
        
        for name, vtype, desc, addr, phone, cap, owner_id in venue_data:
            venue = Venue(
                id=uuid.uuid4(),
                name=name,
                type=vtype,
                description=desc,
                address=addr,
                phone=phone,
                capacity=cap,
                rating=round(3.5 + (len(venues) * 0.3), 1),  # Ratings between 3.5-6.2
                reviews_count=len(venues) * 5,
                owner_id=owner_id,
                hours={"Mon-Thu": "6PM - 12AM", "Fri-Sat": "6PM - 2AM", "Sun": "Closed"},
                amenities=["Full Bar", "Food Menu", "Parking", "AC"],
                images=["https://example.com/venue1.jpg", "https://example.com/venue2.jpg"]
            )
            venues.append(venue)
            db.add(venue)
        
        db.commit()
        print(f"✅ Created {len(venues)} venues")
        
        # ============================================
        # 3. CREATE ARTISTS (10 artists)
        # ============================================
        print("\n🎤 Creating artists...")
        artists = []
        
        artist_data = [
            ("Diamond Platnumz", ["BONGOFLEVA", "AFRO"], "2.5M", "Award-winning Bongo Flava artist"),
            ("Sauti Sol", ["AFRO", "POP"], "1.8M", "Kenyan afro-pop band"),
            ("Ali Kiba", ["BONGOFLEVA", "AFRO"], "1.2M", "Popular Tanzanian singer"),
            ("Lady Jaydee", ["BONGOFLEVA", "AFRO_FUSION"], "900K", "Queen of Bongo Flava"),
            ("Juma Nature", ["HIPHOP", "BONGOFLEVA"], "650K", "Pioneer of Tanzanian hip hop"),
            ("Barnaba Classic", ["AFRO", "POP"], "500K", "Contemporary afro artist"),
            ("Christina Shusho", ["GOSPEL"], "1.5M", "Gospel music sensation"),
            ("Vanessa Mdee", ["AFRO", "POP"], "850K", "Afro-pop diva"),
            ("The Jazzy Trio", ["JAZZ"], "120K", "Smooth jazz ensemble"),
            ("Msondo Ngoma", ["TRADITIONAL"], "300K", "Traditional Tanzanian music group"),
        ]
        
        for name, genres, followers, bio in artist_data:
            artist = Artist(
                id=uuid.uuid4(),
                name=name,
                genre=genres,
                followers_count=followers,
                bio=bio,
                long_bio=f"{bio}. Known for electrifying performances and chart-topping hits.",
                images=["https://example.com/artist1.jpg", "https://example.com/artist2.jpg"],
                cover_image="https://example.com/cover.jpg",
                social_links={
                    "instagram": f"https://instagram.com/{name.lower().replace(' ', '')}",
                    "spotify": f"https://spotify.com/artist/{name.lower().replace(' ', '')}",
                    "website": f"https://{name.lower().replace(' ', '')}.com"
                },
                stats={
                    "total_events": len(artists) * 10,
                    "monthly_listeners": f"{len(artists) * 100}K"
                }
            )
            artists.append(artist)
            db.add(artist)
        
        db.commit()
        print(f"✅ Created {len(artists)} artists")
        
        # ============================================
        # 4. CREATE EVENTS (10 events)
        # ============================================
        print("\n🎪 Creating events...")
        events = []
        
        event_data = [
            ("Diamond Live in Concert", "BONGOFLEVA", "An unforgettable night with Diamond Platnumz", 
             date(2026, 3, 15), time(19, 0), time(23, 0), time(18, 30), "18+", False, artists[0].name),
            ("Sauti Sol Extravaganza", "AFRO", "Experience the magic of Sauti Sol live", 
             date(2026, 3, 20), time(20, 0), time(23, 30), time(19, 0), "All Ages", False, artists[1].name),
            ("Jazz Night with The Jazzy Trio", "JAZZ", "Smooth jazz under the stars", 
             date(2026, 3, 10), time(19, 30), time(22, 0), time(19, 0), "21+", False, artists[8].name),
            ("Gospel Fest 2026", "GOSPEL", "Praise and worship with Christina Shusho", 
             date(2026, 4, 5), time(17, 0), time(21, 0), time(16, 30), "All Ages", True, artists[6].name),
            ("Bongo Flava Night", "BONGOFLEVA", "Ali Kiba and friends", 
             date(2026, 3, 25), time(21, 0), time(2, 0), time(20, 0), "18+", False, artists[2].name),
            ("Afrobeat Festival", "AFRO_FUSION", "Celebrating African rhythms", 
             date(2026, 4, 15), time(18, 0), time(23, 0), time(17, 30), "All Ages", False, artists[3].name),
            ("Hip Hop Jam", "HIPHOP", "Juma Nature headline show", 
             date(2026, 3, 30), time(20, 0), time(1, 0), time(19, 30), "18+", False, artists[4].name),
            ("Traditional Music Showcase", "TRADITIONAL", "Msondo Ngoma presents cultural evening", 
             date(2026, 4, 10), time(18, 30), time(21, 30), time(18, 0), "All Ages", True, artists[9].name),
            ("Vanessa Mdee: The Pop Experience", "POP", "Chart-topping hits and new releases", 
             date(2026, 4, 20), time(19, 0), time(22, 30), time(18, 30), "16+", False, artists[7].name),
            ("Acoustic Sunday", "AFRO", "Barnaba Classic unplugged", 
             date(2026, 3, 17), time(15, 0), time(18, 0), time(14, 30), "All Ages", True, artists[5].name),
        ]
        
        for i, (title, genre, desc, evt_date, start, end, door, age, is_free, artist_name) in enumerate(event_data):
            event = Event(
                id=uuid.uuid4(),
                title=title,
                description=desc,
                genre=[genre],
                venue_id=venues[i].id,
                organizer_id=users[i % 3].id,  # Rotate between first 3 organizers
                date=evt_date,
                start_time=start,
                end_time=end,
                door_time=door,
                age_restriction=age,
                is_free_event=is_free,
                ticket_tiers=[
                    {"name": "General Admission", "price": 0 if is_free else 25000},
                    {"name": "VIP", "price": 0 if is_free else 50000}
                ] if not is_free else None,
                poster_image=f"https://example.com/poster{i+1}.jpg",
                artist_name=artist_name,
                artist_bio=f"Special performance by {artist_name}",
                social_links={
                    "instagram": "https://instagram.com/event",
                    "facebook": "https://facebook.com/event"
                },
                is_published=True
            )
            events.append(event)
            db.add(event)
        
        db.commit()
        print(f"✅ Created {len(events)} events")
        
        # ============================================
        # 5. CREATE EVENT-ARTIST RELATIONSHIPS (10)
        # ============================================
        print("\n🔗 Creating event-artist relationships...")
        for i, event in enumerate(events):
            event_artist = EventArtist(
                id=uuid.uuid4(),
                event_id=event.id,
                artist_id=artists[i].id
            )
            db.add(event_artist)
        
        db.commit()
        print(f"✅ Created {len(events)} event-artist relationships")
        
        # ============================================
        # 6. CREATE REVIEWS (10 reviews)
        # ============================================
        print("\n⭐ Creating reviews...")
        reviews = []
        
        review_comments = [
            "Amazing performance! Would definitely attend again.",
            "Great venue and fantastic sound quality.",
            "The artist was incredible, best concert ever!",
            "Good event but could have better organization.",
            "Loved every minute of it!",
            "Excellent atmosphere and wonderful music.",
            "Worth every penny, highly recommended!",
            "Good show but started late.",
            "Phenomenal performance, exceeded expectations!",
            "Great music but venue was too crowded."
        ]
        
        for i in range(10):
            review = Review(
                id=uuid.uuid4(),
                rating=4 + (i % 2),  # Ratings between 4-5
                comment=review_comments[i],
                user_id=users[i].id,
                event_id=events[i].id
            )
            reviews.append(review)
            db.add(review)
        
        db.commit()
        print(f"✅ Created {len(reviews)} reviews")
        
        # ============================================
        # 7. CREATE USER-ARTIST FOLLOWS (some relationships)
        # ============================================
        print("\n👥 Creating user-artist follow relationships...")
        # Users 3-9 follow some artists
        users[3].following_artists.extend([artists[0], artists[1], artists[6]])
        users[4].following_artists.extend([artists[2], artists[7]])
        users[5].following_artists.extend([artists[8], artists[9]])
        users[6].following_artists.extend([artists[0], artists[3], artists[6]])
        users[9].following_artists.extend([artists[1], artists[4]])
        
        db.commit()
        print("✅ Created user-artist follows")
        
        # ============================================
        # 8. CREATE USER-VENUE FOLLOWS (some relationships)
        # ============================================
        print("\n📍 Creating user-venue follow relationships...")
        users[3].following_venues.extend([venues[0], venues[2]])
        users[4].following_venues.extend([venues[1], venues[3]])
        users[5].following_venues.extend([venues[4], venues[5]])
        users[6].following_venues.extend([venues[0], venues[8]])
        users[9].following_venues.extend([venues[2], venues[9]])
        
        db.commit()
        print("✅ Created user-venue follows")
        
        # ============================================
        # SUMMARY
        # ============================================
        print("\n" + "="*50)
        print("🎉 DATABASE SEEDING COMPLETED SUCCESSFULLY!")
        print("="*50)
        print(f"✅ Users: {len(users)}")
        print(f"✅ Venues: {len(venues)}")
        print(f"✅ Artists: {len(artists)}")
        print(f"✅ Events: {len(events)}")
        print(f"✅ Reviews: {len(reviews)}")
        print("="*50)
        
        print("\n📋 Sample Data for Testing:")
        print(f"\n👤 Sample User (Organizer):")
        print(f"   Email: {users[0].email}")
        print(f"   ID: {users[0].id}")
        
        print(f"\n🏢 Sample Venue:")
        print(f"   Name: {venues[0].name}")
        print(f"   ID: {venues[0].id}")
        
        print(f"\n🎤 Sample Artist:")
        print(f"   Name: {artists[0].name}")
        print(f"   ID: {artists[0].id}")
        
        print(f"\n🎪 Sample Event:")
        print(f"   Title: {events[0].title}")
        print(f"   ID: {events[0].id}")
        print("="*50)
        
    except Exception as e:
        print(f"\n❌ Error seeding database: {e}")
        import traceback
        print(traceback.format_exc())
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()