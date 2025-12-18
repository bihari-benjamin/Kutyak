import sqlite3

def adatbazis_letrehozas():

    conn = sqlite3.connect('kutyak.db')
    cursor = conn.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS kutyak (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nev TEXT NOT NULL,
            fajta TEXT NOT NULL,
            kor INTEGER,
            gazda_neve TEXT
        )
    ''')


    alap_kutyak = [
        ('Bodri', 'Puli', 5, 'Kovács János'),
        ('Mancs', 'Német juhász', 3, 'Szabó Edit'),
        ('Bella', 'Golden Retriever', 2, 'Nagy Péter'),
        ('Rex', 'Tacskó', 8, 'Tóth Gábor'),
        ('Luna', 'Husky', 4, 'Horváth Anna'),
        ('Buksi', 'Keverék', 10, 'Molnár Béla'),
        ('Daisy', 'Beagle', 1, 'Kiss Dóra'),
        ('Morzsa', 'Kuvasz', 6, 'Varga Lajos'),
        ('Cooper', 'Border Collie', 3, 'Fekete Zita'),
        ('Zsemle', 'Labrador', 7, 'Papp Miklós')
    ]


    cursor.execute('SELECT COUNT(*) FROM kutyak')
    if cursor.fetchone()[0] == 0:
        cursor.executemany('''
            INSERT INTO kutyak (nev, fajta, kor, gazda_neve) 
            VALUES (?, ?, ?, ?)
        ''', alap_kutyak)
        print("Adatok sikeresen hozzáadva!")

    conn.commit()
    return conn

def kutyak_lekerdezese(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM kutyak')
    
    rows = cursor.fetchall()
    
    print("\n--- Kutyanyilvántartás ---")
    print(f"{'ID':<3} | {'Név':<10} | {'Fajta':<18} | {'Kor':<4} | {'Gazda neve'}")
    print("-" * 60)
    
    for row in rows:
        print(f"{row[0]:<3} | {row[1]:<10} | {row[2]:<18} | {row[3]:<4} | {row[4]}")


if __name__ == "__main__":
    kapcsolat = adatbazis_letrehozas()
    kutyak_lekerdezese(kapcsolat)
    kapcsolat.close()