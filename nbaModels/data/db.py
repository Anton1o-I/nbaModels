from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import pandas as pd
from datetime import date

import nbaModels.data.queries as q

USER = os.environ["dbName"]
PASSWORD = os.environ["dbPass"]


class nbaDB:
    def __init__(self, user: str = USER, password: str = PASSWORD):
        self.engine = create_engine(
            f"postgresql://{user}:{password}@localhost:5432/nba_stats", echo=False
        )
        Sess = sessionmaker(bind=self.engine)
        self.session = Sess()

    def query():
        pass

    def _query_logic(
        self, query, start: date = None, end: date = None, team: str = None
    ) -> pd.DataFrame:
        res = self.session.execute(query)
        df = pd.DataFrame(res.fetchall(), columns=res.keys())
        if start is not None:
            df = df[df["date"] >= start]
        if end is not None:
            df = df[df["date"] <= end]
        if team is not None:
            df = df[(df["home_team"] == team) | (df["away_team"] == team)]
        return df

    def query_player_stats(
        self, start: date = None, end: date = None, team: str = None
    ) -> pd.DataFrame:
        return self._query_logic(q.get_player_stats())

    def query_game_data_combined(
        self, start: date = None, end: date = None, team: str = None
    ) -> pd.DataFrame:
        return self._query_logic(q.get_games_combined())

    def query_game_data_by_team(
        self, start: date = None, end: date = None, team: str = None
    ) -> pd.DataFrame:
        return self._query_logic(q.get_games_by_team())
