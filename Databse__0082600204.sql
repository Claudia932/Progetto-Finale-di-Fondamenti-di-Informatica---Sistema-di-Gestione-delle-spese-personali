
-- =====================================
-- CREAZIONE TABELLA CATEGORIE
-- =====================================
CREATE TABLE categorie (
    id_categoria INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);
-- =====================================
-- CREAZIONE TABELLA SPESE
-- =====================================
CREATE TABLE spese (
    id_spesa INTEGER PRIMARY KEY,
    data_spesa TEXT NOT NULL,
    importo REAL NOT NULL CHECK(importo > 0),
    descrizione TEXT,
    id_categoria INTEGER NOT NULL,
    FOREIGN KEY (id_categoria)
        REFERENCES categorie(id_categoria)
);
-- =====================================
-- CREAZIONE TABELLA BUDGET
-- =====================================
CREATE TABLE budget (
    id_budget INTEGER PRIMARY KEY,
    mese TEXT NOT NULL,
    importo_budget REAL NOT NULL CHECK(importo_budget > 0),
    id_categoria INTEGER NOT NULL,
    FOREIGN KEY (id_categoria)
        REFERENCES categorie(id_categoria)
);


