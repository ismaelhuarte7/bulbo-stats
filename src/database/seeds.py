from src.database.database import db
from src.core.models.team import Team
from src.core.models.player import Player
from src.core.models.match import Match
from src.core.models.court import Court
from src.core.models.goal import Goal
from datetime import datetime

from datetime import datetime
from src.database.database import db

def run():
    # Crear una cancha
    court = Court.create(name="Estadio Central", address="Av. Principal 123")

    # Crear jugadores
    player1 = Player.create(
        name="Juan", surname="Pérez", email="juan@example.com", user_name="juanp", password="password123", birth_date=datetime(1990, 5, 10)
    )
    player2 = Player.create(
        name="Carlos", surname="López", email="carlos@example.com", user_name="carlosl", password="password123", birth_date=datetime(1992, 7, 15)
    )
    player3 = Player.create(
        name="Luis", surname="González", email="luis@example.com", user_name="luisg", password="password123", birth_date=datetime(1989, 11, 20)
    )
    player4 = Player.create(
        name="Miguel", surname="Rodríguez", email="miguel@example.com", user_name="miguelr", password="password123", birth_date=datetime(1995, 2, 8)
    )

    # Crear un partido
    match = Match.create(
        date=datetime(2024, 11, 15, 18, 30), 
        result="2-1", 
        court_id=court.id
    )

    # Crear equipos
    team1 = Team.create(name="Equipo A", description="Equipo muy competitivo",id_match=match.id)
    team2 = Team.create(name="Equipo B", description="Equipo de amigos",id_match=match.id)

    # Asociar jugadores con los equipos
    team1.players.append(player1)
    team1.players.append(player2)
    team2.players.append(player3)
    team2.players.append(player4)
    db.session.commit()


    # Asociar jugadores con el partido
    match.players.append(player1)
    match.players.append(player2)
    match.players.append(player3)
    match.players.append(player4)
    db.session.commit()

    # Registrar goles
    goal1 = Goal.create(player_id=player1.id, match_id=match.id)  # Gol de Juan
    goal2 = Goal.create(player_id=player2.id, match_id=match.id)  # Gol de Carlos
    goal3 = Goal.create(player_id=player3.id, match_id=match.id)  # Gol de Luis

        
    print("Datos sembrados con éxito")

