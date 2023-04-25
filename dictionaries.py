import random

regular = [
    ('Yo', 'Abrir', 'abro', 'I open'),
    ('Tú', 'Abrir', 'abres', 'You open'),
    ('Él', 'Abrir', 'abre', 'He opens'),
    ('Ella', 'Abrir', 'abre', 'She opens'),
    ('Usted', 'Abrir', 'abre', 'You open'),
    ('Nosotros', 'Abrir', 'abrimos', 'We open'),
    ('Nosotras', 'Abrir', 'abrimos', 'We open'),
    ('Vosotros', 'Abrir', 'abrís', 'You open'),
    ('Vosotras', 'Abrir', 'abrís', 'You open'),
    ('Ellos', 'Abrir', 'abren', 'They open'),
    ('Ellas', 'Abrir', 'abren', 'They open'),
    ('Ustedes', 'Abrir', 'abren', 'They open'),
    ('Yo', 'Beber', 'bebo', 'I drink'),
    ('Tú', 'Beber', 'bebes', 'You drink'),
    ('Él', 'Beber', 'bebe', 'He drinks'),
    ('Ella', 'Beber', 'bebe', 'He drinks'),
    ('Usted', 'Beber', 'bebe', 'He drinks'),
    ('Nosotros', 'Beber', 'bebemos', 'We drink'),
    ('Vosotras', 'Beber', 'bebéis', 'You drink'),
    ('Ellos', 'Beber', 'beben', 'They drink'),
    ('Ellas', 'Beber', 'beben', 'They drink'),
    ('Ustedes', 'Beber', 'beben', 'They drink'),
    ('Yo', 'Correr', 'corro', 'I run'),
    ('Tú', 'Correr', 'corres', 'You run'),
    ('Él', 'Correr', 'corre', 'He runs'),
    ('Ella', 'Correr', 'corre', 'He runs'),
    ('Usted', 'Correr', 'corre', 'He runs'),
    ('Nosotros', 'Correr', 'corremos', 'We run'),
    ('Nosotras', 'Correr', 'corremos', 'We run'),
    ('Vosotros', 'Correr', 'corréis', 'You run'),
    ('Ellos', 'Correr', 'corren', 'They run'),
    ('Ellas', 'Correr', 'corren', 'They run'),
    ('Ustedes', 'Correr', 'corren', 'They run'),
    ('Yo', 'Montar', 'monto', 'I get on'),
    ('Tú', 'Montar', 'montas', 'You get on'),
    ('Él', 'Montar', 'monta', 'He gets on'),
    ('Ella', 'Montar', 'monta', 'He gets on'),
    ('Usted', 'Montar', 'monta', 'He gets on'),
    ('Nosotros', 'Montar', 'montamos', 'We get on'),
    ('Nosotras', 'Montar', 'montamos', 'We get on'),
    ('Vosotros', 'Montar', 'montáis', 'You get on'),
    ('Vosotras', 'Montar', 'montáis', 'You get on'),
    ('Ellos', 'Montar', 'montan', 'They get on'),
    ('Ellas', 'Montar', 'montan', 'They get on'),
    ('Ustedes', 'Montar', 'montan', 'They get on'),
]

tuple = random.choice(regular)

print("Infinitive: " + tuple[1])
print("Pronoun: " + tuple[0])