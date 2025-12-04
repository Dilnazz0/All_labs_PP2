import psycopg2
import csv


connection = psycopg2.connect(
    host="localhost",
    database="lab10bd",
    user="postgres",
    password="123456"
)

cursor = connection.cursor()
print("Connected!")


cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
);
""")
connection.commit()
print("Table 'contacts' created!")


cursor.execute("""
CREATE OR REPLACE FUNCTION fn_search_contacts(pattern TEXT)
RETURNS TABLE (
    id INT,
    name VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.phone
    FROM contacts c
    WHERE c.name ILIKE '%' || pattern || '%'
       OR c.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

""")

connection.commit()


cursor.execute("""
CREATE OR REPLACE PROCEDURE sp_add_or_update_user(p_name VARCHAR, p_phone VARCHAR)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;
""")
connection.commit()


cursor.execute("""
DROP PROCEDURE IF EXISTS sp_insert_many_users(text[], text[]);

CREATE OR REPLACE PROCEDURE sp_insert_many_users(
    IN p_names TEXT[],
    IN p_phones TEXT[]
)
AS $$
DECLARE
    i INT := 1;
BEGIN
    WHILE i <= array_length(p_names, 1) LOOP
        -- вставляем только корректные телефоны (только цифры, длина 5-15)
        IF p_phones[i] ~ '^[0-9]{5,15}$' THEN
            INSERT INTO contacts(name, phone)
            VALUES (p_names[i], p_phones[i]);
        END IF;
        i := i + 1;
    END LOOP;
END;
$$ LANGUAGE plpgsql;
""")
connection.commit()


cursor.execute("""
CREATE OR REPLACE FUNCTION fn_get_contacts_page(p_limit INT, p_offset INT)
RETURNS TABLE (
    id INT,
    name VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.phone
    FROM contacts c
    ORDER BY c.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

""")
connection.commit()


cursor.execute("""
CREATE OR REPLACE PROCEDURE sp_delete_contact(p_value TEXT)
AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_value OR phone = p_value;
END;
$$ LANGUAGE plpgsql;
""")
connection.commit()

print("All SQL objects created successfully!")


def add_or_update():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cursor.execute("CALL sp_add_or_update_user(%s, %s)", (name, phone))
    connection.commit()
    print("Done!")

def insert_many_from_csv():
    path = input("Enter CSV file name: ")
    names = []
    phones = []

    try:
        with open(path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                names.append(row["name"])
                phones.append(row["phone"])

        cursor.execute("CALL sp_insert_many_users(%s, %s)", (names, phones))
        connection.commit()
        print("Inserted! (invalid phones skipped)")

    except Exception as e:
        print("Error:", e)

def search():
    pattern = input("Enter search pattern: ")
    cursor.execute("SELECT * FROM fn_search_contacts(%s)", (pattern,))
    rows = cursor.fetchall()
    print("\nResults:")
    for row in rows:
        print(row)

def pagination():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))
    cursor.execute("SELECT * FROM fn_get_contacts_page(%s, %s)", (limit, offset))
    rows = cursor.fetchall()
    print("\nPage results:")
    for row in rows:
        print(row)

def delete_contact():
    value = input("Enter name or phone to delete: ")
    cursor.execute("CALL sp_delete_contact(%s)", (value,))
    connection.commit()
    print("Deleted!")

while True:
    print("\n===== PhoneBook Menu =====")
    print("1. Add or update user")
    print("2. Insert many users (CSV)")
    print("3. Search by pattern")
    print("4. Show with pagination")
    print("5. Delete by name/phone")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_or_update()
    elif choice == "2":
        insert_many_from_csv()
    elif choice == "3":
        search()
    elif choice == "4":
        pagination()
    elif choice == "5":
        delete_contact()
    elif choice == "0":
        break
    else:
        print("Wrong option!")

cursor.close()
connection.close()
print("Bye!")
