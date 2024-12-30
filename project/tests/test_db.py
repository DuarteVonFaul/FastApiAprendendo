from api.models import User

def test_user_database_insert(session):
    
    with session:
        user = User(
            username='duarte',
            email='email@mail.com',
            password='secret'
        )

        session.add(user)
        session.commit()
        session.refresh(user)

        ...

    assert user.id == 1
    
    ...