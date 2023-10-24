CREATE DATABASE Xbox_GamePass;

USE Xbox_GamePass;

CREATE TABLE GamePass(
	GAME varchar (255) not null,
    RATIO decimal,
    GAMERS varchar (255),
    COMP decimal,
    TIME varchar (255),
    RATING decimal,
    ADDED varchar (255),
    TRUE_ACHIEVEMENT int,
    GAME_SCORE int
);

select * from GamePass;