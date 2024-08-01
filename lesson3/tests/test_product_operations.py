from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import unittest

from excercise.models import User, Base


class TestUserOperations(unittest.TestCase):
    def setUp(self):
        # Connect to the in-memory SQLite database
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)  # Create tables
        session = sessionmaker(bind=self.engine)
        self.session = session()

        # Add a sample user for testing
        test_user = User(name='Test User', email='test@example.com')
        self.session.add(test_user)
        self.session.commit()

    def tearDown(self):
        # Drop all tables and close session
        Base.metadata.drop_all(self.engine)
        self.session.close()

    def test_user_retrieval(self):
        # Fetch the test user
        user = self.session.query(User).filter_by(name='Test User').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'test@example.com')

    def test_user_deletion(self):
        # Delete the test user
        self.session.query(User).filter_by(name='Test User').delete()
        self.session.commit()

        # Verify user is deleted
        user = self.session.query(User).filter_by(name='Test User').first()
        self.assertIsNone(user)


if __name__ == '__main__':
    unittest.main()
