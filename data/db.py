from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class nbaDB:
    def __init__(self, user, password):
        self.engine = create_engine(
            f"postgresql://{user}:{password}@localhost:5432/nba_stats", echo=False
        )
        Sess = sessionmaker(bind=self.engine)
        self.session = Sess()

    def query():
        pass

    def get_player_stats():
        pass

    def get_game_stats():
        pass

    