-- Table pour l'historique 
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    temperature REAL NOT NULL,
    meteo TEXT NOT NULL,
    time_search TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table pour les villes suivies 
CREATE TABLE IF NOT EXISTS weather_followed (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE, -- UNIQUE pour éviter les doublons de ville
    last_temp REAL,
    last_meteo TEXT
);