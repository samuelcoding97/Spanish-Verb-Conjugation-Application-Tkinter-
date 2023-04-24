import random

regular = [
    ('Yo', 'Abrir', 'abro', 'I open'),
    ('Tú', 'Abrir', 'abres', 'You open'),
    ('Él', 'Abrir', 'abre', 'He opens'),
    ('Ella', 'Abrir', 'abre', 'She opens'),
    ('Usted', 'Abrir', 'abre', 'You open'),
    ('Nosotros', 'Abrir', 'abrimos', 'We open'),
    ('Vosotros', 'Abrir', 'abrís', 'You open'),
    ('Ellos', 'Abrir', 'abren', 'They open')
    ]

tuple = random.choice(regular)

print("Infinitive: " + tuple[1])
print("Pronoun: " + tuple[0])