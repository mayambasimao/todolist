from dataclasses import asdict

from sqlalchemy import select

from todolist.models import Todo, User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(username='alice', password='secret', email='test@test')
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert asdict(user) == {
        'id': 1,
        'username': 'alice',
        'password': 'secret',
        'email': 'test@test',
        'todos': [],
        'created_at': time,
        'updated_at': time,
    }


def test_create_todo(session, user: User):
    todo = Todo(
        title='Test Todo',
        description='Test Desc',
        state='draft',
        user_id=user.id,
    )

    session.add(todo)
    session.commit()
    session.refresh(todo)

    user = session.scalar(select(User).where(User.id == user.id))

    assert todo in user.todos
