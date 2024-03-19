from sqlalchemy import Integer, Column, String, Boolean, Float
from joke import db, app


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class Joke(BaseModel):

    content = Column(String(1000), nullable=False)
    status = Column(Boolean, default=0)
    ratio = Column(Float, default=0.0)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
         db.create_all()
         j = Joke(content="I am devoting the rest of my life to turning my griping into gratitude, my murmuring into melody. I want to spend my days not bellyaching but singing the praises of God. Unfortunately, too many of us are stalled at the test of gratitude. A double dose of holy humor can cure that malady")
         j1 = Joke(content="Holy hilarity, a sanctified sense of humor, is strong medicine. A merry heart doeth good like a medicine: but a broken spirit drieth the bones (Prov. 17:22 KJV). A merry heart keeps us from taking ourselves too seriously.")
         j2 = Joke(content="One of the signs of a healthy mind is the ability to smile at ourselves and see the humorous side of everything we do.")
         j3 = Joke(content="The medicine of a merry heart not only cures us from an exaggerated sense of self-importance, it tends to put space between us and the traumatic experiences in our lives. It acts as a buffer zone to absorb some of their bad vibrations. There's nothing like a merry heart to medicate you from the remorse and regrets of the woulda-coulda-shoulda syndrome.")
         j4 = Joke(content="One hundred and forty-seven daily portions of mirth--from jokes to rib-tickling stories, from tall tales to true accounts, from hilarious things kids say to funny things that happen in church--these drops of holy hilarity will lighten any heart.")
         db.session.add_all([j, j1, j2, j3, j4])
         db.session.commit()