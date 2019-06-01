from app import app
from app.models import User

# u = User(username='dorian', email='dorian@example.com')
# db.session.add(u)
# db.session.commit()

users = User.query.all()
for user in users:
    print(user)
