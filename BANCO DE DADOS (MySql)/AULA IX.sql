-- Crie o banco de dados
CREATE DATABASE Epic_Games_Store;

-- Use o banco de dados
USE Epic_Games_Store;

-- Crie a tabela Developers para armazenar informações sobre desenvolvedores de jogos
CREATE TABLE Developers (
    developer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    headquarters_location VARCHAR(255),
    website_url VARCHAR(255)
);

-- Crie a tabela Games para armazenar informações sobre jogos
CREATE TABLE Games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    release_date DATE,
    price DECIMAL(10, 2),
    developer_id INT,
    CONSTRAINT FK_GamesDevelopers FOREIGN KEY (developer_id) REFERENCES Developers(developer_id)
);

-- Crie a tabela Purchases para armazenar informações sobre compras de jogos
CREATE TABLE Purchases (
    purchase_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT,
    purchase_date DATE,
    user_name VARCHAR(255) NOT NULL,
    CONSTRAINT FK_PurchasesGames FOREIGN KEY (game_id) REFERENCES Games(game_id)
);

-- Inserir dados na tabela Developers
INSERT INTO Developers (name, headquarters_location, website_url)
VALUES
    ('Epic Games', 'Cary, North Carolina, USA', 'https://www.epicgames.com'),
    ('Ubisoft', 'Montreuil, France', 'https://www.ubisoft.com'),
    ('Electronic Arts', 'Redwood City, California, USA', 'https://www.ea.com'),
    ('Rockstar Games', 'New York City, New York, USA', 'https://www.rockstargames.com'),
    ('CD Projekt', 'Warsaw, Poland', 'https://www.cdprojekt.com'),
    ('Valve Corporation', 'Bellevue, Washington, USA', 'https://www.valvesoftware.com'),
    ('Square Enix', 'Tokyo, Japan', 'https://www.square-enix.com'),
    ('Capcom', 'Osaka, Japan', 'https://www.capcom.com'),
    ('Bethesda Softworks', 'Rockville, Maryland, USA', 'https://bethesda.net'),
    ('Konami', 'Tokyo, Japan', 'https://www.konami.com'),
    ('Bandai Namco Entertainment', 'Tokyo, Japan', 'https://www.bandainamcoent.com'),
    ('Sega', 'Tokyo, Japan', 'https://www.sega.com'),
    ('Blizzard Entertainment', 'Irvine, California, USA', 'https://www.blizzard.com'),
    ('343 Industries', 'Redmond, Washington, USA', 'https://www.343industries.com'),
    ('Bungie', 'Bellevue, Washington, USA', 'https://www.bungie.net'),
    ('BioWare', 'Edmonton, Alberta, Canada', 'https://www.bioware.com'),
    ('Eidos-Montreal', 'Montreal, Quebec, Canada', 'https://www.eidosmontreal.com'),
    ('Respawn Entertainment', 'Los Angeles, California, USA', 'https://www.respawn.com'),
    ('Gearbox Software', 'Frisco, Texas, USA', 'https://www.gearboxsoftware.com'),
    ('NetherRealm Studios', 'Chicago, Illinois, USA', 'https://www.netherrealm.com'),
    ('Remedy Entertainment', 'Espoo, Finland', 'https://www.remedygames.com'),
    ('Treyarch', 'Santa Monica, California, USA', 'https://www.treyarch.com'),
    ('Insomniac Games', 'Burbank, California, USA', 'https://www.insomniacgames.com'),
    ('Obsidian Entertainment', 'Irvine, California, USA', 'https://www.obsidian.net'),
    ('Square Enix Montreal', 'Montreal, Quebec, Canada', 'https://www.square-enix-montreal.com'),
    ('Riot Games', 'Los Angeles, California, USA', 'https://www.riotgames.com'),
    ('Creative Assembly', 'Horsham, West Sussex, UK', 'https://www.creative-assembly.com'),
    ('Double Fine Productions', 'San Francisco, California, USA', 'https://www.doublefine.com'),
    ('Guerrilla Games', 'Amsterdam, Netherlands', 'https://www.guerrilla-games.com'),
    ('Larian Studios', 'Ghent, Belgium', 'https://www.larian.com'),
    ('Mediatonic', 'London, UK', 'https://www.mediatonicgames.com'),
    ('Monolith Productions', 'Kirkland, Washington, USA', 'https://www.lith.com'),
    ('Playdead', 'Copenhagen, Denmark', 'https://www.playdead.com'),
    ('Playtonic Games', 'Burton-on-Trent, UK', 'https://www.playtonicgames.com'),
    ('Quantic Dream', 'Paris, France', 'https://www.quanticdream.com'),
    ('Red Barrels', 'Montreal, Quebec, Canada', 'https://www.redbarrelsgames.com'),
    ('Respawn Entertainment', 'Los Angeles, California, USA', 'https://www.respawn.com'),
    ('Riot Forge', 'Los Angeles, California, USA', 'https://www.riotforgegames.com'),
    ('Splash Damage', 'London, UK', 'https://www.splashdamage.com'),
    ('Studio Wildcard', 'Gainesville, Florida, USA', 'https://www.studiowildcard.com'),
    ('Techland', 'Wroclaw, Poland', 'https://www.techland.net'),
    ('The Coalition', 'Vancouver, British Columbia, Canada', 'https://www.thecoalitionstudio.com'),
    ('Turtle Rock Studios', 'Lake Forest, California, USA', 'https://www.turtlerockstudios.com'),
    ('Undead Labs', 'Seattle, Washington, USA', 'https://www.undeadlabs.com'),
    ('Vicarious Visions', 'Albany, New York, USA', 'https://www.vvisions.com'),
    ('Yager Development', 'Berlin, Germany', 'https://www.yager.de'),
    ('Zenimax Online Studios', 'Hunt Valley, Maryland, USA', 'https://www.zenimaxonline.com'),
    ('ZeniMax Media', 'Rockville, Maryland, USA', 'https://www.zenimax.com'),
    ('Squanch Games', ' Burbank, California, USA', 'https://squanchgames.com'),
    ('The Astronauts', 'Varsóvia, Polônia', 'https://www.theastronauts.com/');

select name,headquarters_location from Developers where headquarters_location like '%USA';
select * from Games where ;
select * from Purchases where ;


-- Inserir dados na tabela Games
INSERT INTO Games (title, release_date, price, developer_id)
VALUES
    ('Fortnite', '2017-07-25', 0.00, 1), -- Epic Games
    ('Assassin\'s Creed Valhalla', '2020-11-10', 59.99, 2), -- Ubisoft
    ('FIFA 22', '2021-10-01', 59.99, 3), -- Electronic Arts
    ('Grand Theft Auto V', '2013-09-17', 29.99, 4), -- Rockstar Games
    ('Cyberpunk 2077', '2020-12-10', 49.99, 5), -- CD Projekt
    ('Portal 2', '2011-04-18', 19.99, 6), -- Valve Corporation
    ('Final Fantasy VII Remake', '2020-04-10', 59.99, 7), -- Square Enix
    ('Resident Evil Village', '2021-05-07', 49.99, 8), -- Capcom
    ('The Elder Scrolls V: Skyrim', '2011-11-11', 19.99, 9), -- Bethesda Softworks
    ('Metal Gear Solid V: The Phantom Pain', '2015-09-01', 29.99, 10), -- Konami
    ('Tekken 7', '2017-06-02', 39.99, 11), -- Bandai Namco Entertainment
    ('Sonic Mania', '2017-08-15', 19.99, 12), -- Sega
    ('Diablo III', '2012-05-15', 19.99, 13), -- Blizzard Entertainment
    ('Halo Infinite', '2021-12-08', 59.99, 14), -- 343 Industries
    ('Destiny 2', '2017-10-24', 0.00, 15), -- Bungie
    ('Mass Effect Legendary Edition', '2021-05-14', 59.99, 16), -- BioWare
    ('Deus Ex: Mankind Divided', '2016-08-23', 29.99, 17), -- Eidos-Montreal
    ('Apex Legends', '2019-02-04', 0.00, 18), -- Respawn Entertainment
    ('Borderlands 3', '2019-09-13', 59.99, 19), -- Gearbox Software
    ('Mortal Kombat 11', '2019-04-23', 49.99, 20), -- NetherRealm Studios
    ('Control', '2019-08-27', 29.99, 21), -- Remedy Entertainment
    ('Call of Duty: Black Ops Cold War', '2020-11-13', 59.99, 22), -- Treyarch
    ('Spider-Man: Miles Morales', '2020-11-12', 49.99, 23), -- Insomniac Games
    ('The Outer Worlds', '2019-10-25', 29.99, 24), -- Obsidian Entertainment
    ('Hitman 3', '2021-01-20', 59.99, 25), -- Square Enix Montreal
    ('League of Legends', '2009-10-27', 0.00, 26), -- Riot Games
    ('Total War: Three Kingdoms', '2019-05-23', 59.99, 27), -- Creative Assembly
    ('Psychonauts 2', '2021-08-25', 29.99, 28), -- Double Fine Productions
    ('Horizon Zero Dawn', '2020-08-07', 49.99, 29), -- Guerrilla Games
    ('Divinity: Original Sin 2', '2017-09-14', 39.99, 30), -- Larian Studios
    ('Fall Guys: Ultimate Knockout', '2020-08-04', 19.99, 31), -- Mediatonic
    ('Middle-earth: Shadow of War', '2017-10-10', 29.99, 32), -- Monolith Productions
    ('Inside', '2016-07-07', 19.99, 33), -- Playdead
    ('Yooka-Laylee', '2017-04-11', 19.99, 34), -- Playtonic Games
    ('Detroit: Become Human', '2019-12-12', 39.99, 35), -- Quantic Dream
    ('Outlast', '2013-09-04', 19.99, 36), -- Red Barrels
    ('Titanfall 2', '2016-10-28', 29.99, 37), -- Respawn Entertainment
    ('Ruined King: A League of Legends Story', '2021-11-16', 29.99, 38), -- Riot Forge
    ('Gears 5', '2019-09-06', 39.99, 39), -- Splash Damage
    ('ARK: Survival Evolved', '2015-08-27', 49.99, 40), -- Studio Wildcard
    ('Dying Light', '2015-01-27', 29.99, 41), -- Techland
    ('Gears of War 5', '2019-09-10', 59.99, 42), -- The Coalition
    ('Back 4 Blood', '2021-10-12', 59.99, 43), -- Turtle Rock Studios
    ('State of Decay 2', '2018-05-22', 29.99, 44), -- Undead Labs
    ('Crash Bandicoot 4: It\'s About Time', '2020-10-02', 59.99, 45), -- Vicarious Visions
    ('Spec Ops: The Line', '2012-06-26', 19.99, 46), -- Yager Development
    ('The Elder Scrolls Online', '2014-04-04', 29.99, 47), -- Zenimax Online Studios
    ('Doom Eternal', '2020-03-20', 59.99, 48), -- Zenimax Media
    ('High On Life', '2022-12-13', 107.99, 49), -- Squanch Games
    ('Witchfire', '2023-09-20', 107.99, 50);


-- Inserir dados fictícios na tabela Purchases
INSERT INTO Purchases (game_id, purchase_date, user_name)
VALUES
  (1, '2023-01-05', 'GrrrlPowa'),
  (2, '2020-03-20', 'Leon'),
  (3, '2022-02-15', 'Polly Rocket'),
  (4, '2015-04-10', 'Painkiller '),
  (5, '2021-05-22', 'ValsinhaVeneno'),
  (6, '2012-06-12', 'CRMessi'),
  (7, '2021-03-28', 'Sara Sahara'),
  (8, '2023-04-05', 'Whiskey'),
  (9, '2012-01-14', 'MoçaTaDiferente'),
  (10, '2016-02-01', 'Rocks'),
  (11, '2018-02-25', 'Cover Girl'),
  (12, '2018-01-17', 'Coyote'),
  (13, '2013-03-05', 'Girllirla'),
  (14, '2022-03-30', 'Napoleon'),
  (15, '2020-04-18', 'NinjaKawai'),
  (16, '2023-05-02', 'Zombie'),
  (17, '2017-06-08', 'ByancaNoir'),
  (18, '2020-01-28', 'Prodigy'),
  (19, '2020-02-10', 'Aguja'),
  (20, '2020-05-16', 'Falcão'),
  (21, '2020-04-22', 'Mika'),
  (22, '2022-06-30', 'Cobra'),
  (23, '2022-05-08', 'Nathy'),
  (24, '2023-04-02', 'Mcgregor'),
  (25, '2023-02-12', 'BeClare'),
  (26, '2022-02-19', 'Scorpion'),
  (27, '2023-01-24', 'Maya'),
  (28, '2023-03-15', 'Satoshi'),
  (29, '2023-06-05', 'Ostarha'),
  (30, '2023-01-29', 'Hazzard'),
  (31, '2023-04-14', 'Labirinto de Pandora'),
  (32, '2020-06-25', 'Torpedo'),
  (33, '2023-05-12', 'PinaColada'),
  (34, '2023-03-10', 'Jaguar'),
  (35, '2022-02-06', 'Tempestade de Amor'),
  (36, '2023-03-25', 'RockyBalboa'),
  (37, '2014-05-18', 'Sniper do Lar'),
  (38, '2022-02-22', 'Sniper'),
  (39, '2023-01-10', 'Girassol'),
  (40, '2022-01-22', 'Naoki'),
  (41, '2023-04-01', 'Cheetara'),
  (42, '2016-06-20', 'Overtaker'),
  (43, '2018-05-29', 'Sheera'),
  (44, '2022-03-12', 'Exterminator'),
  (45, '2023-01-08', 'Dona Flor'),
  (46, '2019-06-02', 'Maximus'),
  (47, '2023-04-16', 'PanificadoraOmega'),
  (48, '2013-05-05', 'Thor'),
  (49, '2016-02-03', 'Caramelo'),
  (50, '2023-01-19', 'Akinori');
  
  
