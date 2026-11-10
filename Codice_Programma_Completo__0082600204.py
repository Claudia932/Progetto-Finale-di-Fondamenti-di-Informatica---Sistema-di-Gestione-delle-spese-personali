import sqlite3

# ==========================
# CONNESSIONE DATABASE
# ==========================

conn = sqlite3.connect("spese.db")
cursor = conn.cursor()

# ==========================
# TABELLE
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS categorie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS spese (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    importo REAL NOT NULL,
    descrizione TEXT,
    categoria TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS budget (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria TEXT NOT NULL,
    importo_budget REAL NOT NULL
)
""")

conn.commit()

# ==========================
# MENU PRINCIPALE
# ==========================

while True:

    print("\n=================================")
    print("GESTIONE SPESE PERSONALI")
    print("=================================")

    print("1. Gestione categorie")
    print("2. Inserimento spese")
    print("3. Gestione budget")
    print("4. Report")
    print("5. Esci")

    scelta = input("\nSeleziona un'opzione: ")

    # ==========================
    # CATEGORIE
    # ==========================

    if scelta == "1":

        categoria = input(
            "Inserisci il nome della categoria: "
        )

        try:

            cursor.execute(
                "INSERT INTO categorie (nome) VALUES (?)",
                (categoria,)
            )

            conn.commit()

            print("Categoria salvata correttamente.")

        except Exception:

            print("La categoria esiste già.")

    # ==========================
    # SPESE
    # ==========================

    elif scelta == "2":

        data = input(
            "Data spesa (gg/mm/aaaa): "
        )

        importo = float(
            input("Importo: ")
        )

        descrizione = input(
            "Descrizione: "
        )

        categoria = input(
            "Categoria: "
        )

        cursor.execute("""
        INSERT INTO spese
        (data, importo, descrizione, categoria)
        VALUES (?, ?, ?, ?)
        """, (
            data,
            importo,
            descrizione,
            categoria
        ))

        conn.commit()

        print("Spesa registrata correttamente.")

    # ==========================
    # BUDGET
    # ==========================

    elif scelta == "3":

        categoria = input(
            "Categoria: "
        )

        importo_budget = float(
            input("Importo budget: ")
        )

        cursor.execute("""
        INSERT INTO budget
        (categoria, importo_budget)
        VALUES (?, ?)
        """, (
            categoria,
            importo_budget
        ))

        conn.commit()

        print("Budget registrato correttamente.")

    # ==========================
    # REPORT
    # ==========================

    elif scelta == "4":

        print("\n=================================")
        print("REPORT SPESE")
        print("=================================")

        cursor.execute(
            "SELECT nome FROM categorie"
        )

        categorie = cursor.fetchall()

        if len(categorie) == 0:

            print("Nessuna categoria presente.")

        else:

            for categoria in categorie:

                nome_categoria = categoria[0]

                print(
                    f"\nCATEGORIA: {nome_categoria}"
                )

                cursor.execute("""
                SELECT descrizione, importo
                FROM spese
                WHERE categoria = ?
                """, (
                    nome_categoria,
                ))

                spese_categoria = cursor.fetchall()

                totale_spese = 0

                if len(spese_categoria) == 0:

                    print(
                        "Nessuna spesa registrata."
                    )

                else:

                    for spesa in spese_categoria:

                        print(
                            f"{spesa[0]} - {spesa[1]} €"
                        )

                        totale_spese += spesa[1]

                cursor.execute("""
                SELECT importo_budget
                FROM budget
                WHERE categoria = ?
                """, (
                    nome_categoria,
                ))

                budget = cursor.fetchone()

                print(
                    f"Totale Spese: {totale_spese} €"
                )

                if budget:

                    valore_budget = budget[0]

                    print(
                        f"Budget: {valore_budget} €"
                    )

                    if totale_spese <= valore_budget:

                        print(
                            "STATO: Budget rispettato"
                        )

                    else:

                        differenza = (
                            totale_spese -
                            valore_budget
                        )

                        print(
                            f"STATO: Budget superato di {differenza} €"
                        )

                else:

                    print(
                        "Budget non impostato."
                    )

    # ==========================
    # USCITA
    # ==========================

    elif scelta == "5":

        print("Chiusura programma...")
        break

    else:

        print("Scelta non valida.")

conn.close()
