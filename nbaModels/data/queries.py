def get_team_stats(start: str = None, end: str = None, team: str = None):
    return """
    SELECT * FROM team_stats;
    """


def get_games_combined(start: str = None, end: str = None):
    return """ 
    SELECT
        game.date,
        game.season,
        game.home_wins as home_wins,
        game.home_losses as home_losses,
        game.away_wins as away_wins,
        game.away_losses as away_losses,
        tsh.team_abbr as team_home,
        tsh.fgm as fgm_home,
        tsh.fga as fga_home,
        tsh.fg_per as fg_per_home,
        tsh.x3pa as x3pa_home,
        tsh.x3pm as x3pm_home,
        tsh.x3p_per as x3p_per_home,
        tsh.fta as fta_home,
        tsh.ftm as ftm_home,
        tsh.ft_per as ft_per_home,
        tsh.orebs as orebs_home,
        tsh.drebs as drebs_home,
        tsh.rebounds as rebounds_home,
        tsh.assists as assists_home,
        tsh.steals as steals_home,
        tsh.blocks as blocks_home,
        tsh.turnovers as turnovers_home, 
        tsh.fouls as fouls_home,
        tsh.points as points_home,
        tsh.x1q_pts as x1q_pts_home,
        tsh.x2q_pts as x2q_pts_home,
        tsh.x3q_pts as x3q_pts_home,
        tsh.x4q_pts as x4q_pts_home,
        tsh.ot_pts as ot_pts_home,
        tsh.pace as pace_home,
        tsh.efg_per as efg_per_home,
        tsh.ft_per_fga as ft_per_fga_home,
        tsh.ts_per as ts_per_home,
        tsh.x3p_ar as x3p_ar_home,
        tsh.ft_ar as ft_ar_home,
        tsh.oreb_per as oreb_per_home,
        tsh.dreb_per as dreb_per_home,
        tsh.reb_per as reb_per_home,
        tsh.ast_per as ast_per_home,
        tsh.stl_per as stl_per_home,
        tsh.blk_per as blk_per_home,
        tsh.tov_per as tov_per_home,
        tsh.usg_per as usg_per_home,
        tsh.off_rating as off_rating_home,
        tsh.def_rating as def_rating_home,
        tsa.team_abbr as team_away,
        tsa.fgm as fgm_away,
        tsa.fga as fga_away,
        tsa.fg_per as fg_per_away,
        tsa.x3pa as x3pa_away,
        tsa.x3pm as x3pm_away,
        tsa.x3p_per as x3p_per_away,
        tsa.fta as fta_away,
        tsa.ftm as ftm_away,
        tsa.ft_per as ft_per_away,
        tsa.orebs as orebs_away,
        tsa.drebs as drebs_away,
        tsa.rebounds as rebounds_away,
        tsa.assists as assists_away,
        tsa.steals as steals_away,
        tsa.blocks as blocks_away,
        tsa.turnovers as turnovers_away, 
        tsa.fouls as fouls_away,
        tsa.points as points_away,
        tsa.x1q_pts as x1q_pts_away,
        tsa.x2q_pts as x2q_pts_away,
        tsa.x3q_pts as x3q_pts_away,
        tsa.x4q_pts as x4q_pts_away,
        tsa.ot_pts as ot_pts_away,
        tsa.pace as pace_away,
        tsa.efg_per as efg_per_away,
        tsa.ft_per_fga as ft_per_fga_away,
        tsa.ts_per as ts_per_away,
        tsa.x3p_ar as x3p_ar_away,
        tsa.ft_ar as ft_ar_away,
        tsa.oreb_per as oreb_per_away,
        tsa.dreb_per as dreb_per_away,
        tsa.reb_per as reb_per_away,
        tsa.ast_per as ast_per_away,
        tsa.stl_per as stl_per_away,
        tsa.blk_per as blk_per_away,
        tsa.tov_per as tov_per_away,
        tsa.usg_per as usg_per_away,
        tsa.off_rating as off_rating_away,
        tsa.def_rating as def_rating_away
    FROM team_stats as tsh
    LEFT JOIN 
        (SELECT * from team_stats) as tsa
        ON tsa.game_id = tsh.game_id
    LEFT JOIN
        (SELECT * FROM games) as game
        ON tsh.game_id = game.id
    WHERE tsh.home = true and tsa.home = false;
    """

def get_games_by_team():
    return """
        SELECT
        game.date,
        game.season,
        ts.team_abbr as team,
        ts.fgm as fgm,
        ts.fga as fga,
        ts.fg_per as fg_per,
        ts.x3pa as x3pa,
        ts.x3pm as x3pm,
        ts.x3p_per as x3p_per,
        ts.fta as fta,
        ts.ftm as ftm,
        ts.ft_per as ft_per,
        ts.orebs as orebs,
        ts.drebs as drebs,
        ts.rebounds as rebounds,
        ts.assists as assists,
        ts.steals as steals,
        ts.blocks as blocks,
        ts.turnovers as turnovers, 
        ts.fouls as fouls,
        ts.points as points,
        ts.x1q_pts as x1q_pts,
        ts.x2q_pts as x2q_pts,
        ts.x3q_pts as x3q_pts,
        ts.x4q_pts as x4q_pts,
        ts.ot_pts as ot_pts,
        ts.pace as pace,
        ts.efg_per as efg_per,
        ts.ft_per_fga as ft_per_fga,
        ts.ts_per as ts_per,
        ts.x3p_ar as x3p_ar,
        ts.ft_ar as ft_ar,
        ts.oreb_per as oreb_per,
        ts.dreb_per as dreb_per,
        ts.reb_per as reb_per,
        ts.ast_per as ast_per,
        ts.stl_per as stl_per,
        ts.blk_per as blk_per,
        ts.tov_per as tov_per,
        ts.usg_per as usg_per,
        ts.off_rating as off_rating,
        ts.def_rating as def_rating,
		CASE 
		 	WHEN ts.home = TRUE THEN game.home_wins
		 	ELSE game.away_wins
		END AS wins,
		CASE 
		 	WHEN ts.home = TRUE THEN game.home_losses
		 	ELSE game.away_losses
		END as losses
    FROM team_stats as ts
    LEFT JOIN
        (SELECT * FROM games) as game
        ON ts.game_id = game.id
    ;
    """

def get_player_stats():
    return """
    SELECT
        game.date,
        game.season,
        player.last_name,
        player.first_name,
        ps.team_abbr as team,
        ps.minutes,
        ps.points,
        ps.drebs,
        ps.orebs,
        ps.rebounds,
        ps.assists,
        ps.turnovers,
        ps.fgm,
        ps.fga,
        ps.fg_per,
        ps.ftm,
        ps.fta,
        ps.ft_per,
        ps.x3pa,
        ps.x3pm,
        ps.x3p_per,
        ps.blocks,
        ps.steals,
        ps.fouls,
        ps.plus_minus,
        ps.ts_per,
        ps.efg_per,
        ps.x3p_ar,
        ps.ft_ar,
        ps.oreb_per,
        ps.dreb_per,
        ps.reb_per,
        ps.ast_per,
        ps.stl_per,
        ps.blk_per,
        ps.tov_per,
        ps.usg_per,
        ps.off_rating,
        ps.def_rating,
        ps.bpm,
        ps.obpm,
        ps.dbpm,
        ps.vorp
    FROM player_stats as ps
    LEFT JOIN
        (SELECT * FROM games) as game
        ON game.id = ps.game_id
    LEFT JOIN
        (SELECT * FROM players) as player
        ON player.id = ps.player_id;
	"""
