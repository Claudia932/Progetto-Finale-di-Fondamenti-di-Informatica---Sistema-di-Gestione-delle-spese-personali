# Sistema di Gestione delle Spese Personali
Progetto finale del corso di Fondamenti di Informatica, creazione di un programma: Sistema di gestione delle spese personali e del budget
## Informazioni Generali

**Studente:** Claudia Giammarini

**Matricola:** 0082600204

**Corso:** Fondamenti di Informatica

**Università:** Università San Raffaele di Roma (UniRoma5)

**Anno Accademico:** 2026/2027

---

## Obiettivo del Progetto

Il progetto ha come obiettivo la realizzazione di un'applicazione per la gestione delle spese personali mediante il linguaggio Python e l'utilizzo di un database SQLite.

Il sistema permette all'utente di registrare le proprie spese, organizzarle per categoria, definire budget di riferimento e visualizzare report riepilogativi utili al monitoraggio delle uscite economiche.

---

## Funzionalità Implementate

Il programma consente di:

- Creare e gestire categorie di spesa;
- Registrare nuove spese;
- Definire budget associati alle categorie;
- Consultare report riepilogativi;
- Confrontare le spese effettuate con i budget impostati;
- Verificare eventuali superamenti dei limiti di spesa.

---

## Struttura del Repository

Il repository contiene i seguenti file:

| File | Descrizione |
|--------|--------|
| main.py | Programma principale |
| database.sql | Script SQL per la progettazione del database |
| Elaborato.pdf | Relazione completa del progetto |
| video_demo.mp4 | Video dimostrativo del funzionamento |

---

## Tecnologie Utilizzate

- Python
- SQLite
- SQL

---

## Avvio del Programma

Eseguire il file:

```bash
python main.py
```

Una volta avviato il programma sarà possibile accedere alle funzionalità mediante il menu testuale.

---

## Moduli Principali

### Gestione Categorie

Permette l'inserimento e la gestione delle categorie utilizzate per classificare le spese.

### Inserimento Spese

Consente di registrare le spese indicando:

- data;
- importo;
- descrizione;
- categoria.

### Gestione Budget

Permette di associare ad ogni categoria un budget di riferimento.

### Report

Visualizza le spese raggruppate per categoria e confronta i totali con i relativi budget, evidenziando eventuali superamenti.

---

## Video Dimostrativo

Il video mostra:

1. Inserimento delle categorie;
2. Definizione dei budget;
3. Registrazione delle spese;
4. Generazione del report finale;
5. Chiusura dell'applicazione.

---

## Note Finali

Il database viene creato automaticamente all'avvio del programma.

Lo sviluppo è stato effettuato seguendo un approccio modulare, realizzando inizialmente i singoli componenti dell'applicazione e successivamente integrandoli in un'unica soluzione software
