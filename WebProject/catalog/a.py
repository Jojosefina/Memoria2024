from pprint import pprint
elementos = [
    "Diana Narváez", "Jorge Aguayo", "Javier Ramírez", "Jorge San Martín", "Leonardo Sánchez",
    "Yamit Y.", "Juan José Maulen", "Natalia Ruiz", "Cristián Reyes", "Patricio Felmer",
    "Juan José Maulen", "Jorge San Martín", "Cristián Reyes", "Patricio Felmer", "Mauricio Telias",
    "Rodolfo Gutiérrez", "Diana Narváez", "Martín Matamala", "Ana Trujillo", "Patricio Quiroz",
    "Maya Stein", "Vicente Acuña", "Nicolás Hernández", "Mauricio Telias", "Juan Ross",
    "Flavio Guiñez", "Leonardo Sánchez", "Pablo Dartnell", "Alexis Fuentes", "Álvaro Hernández",
    "Alexander Frank", "Jaime San Martín", "Pablo Dartnell", "Daniel Remenik", "Martín Matamala",
    "Alexander Frank", "Alejandro Maas", "Vicente Acuña", "Natacha Astromujoff", "Marcos Kiwi",
    "Alexis Fuentes", "Javier Ramírez", "Rafael Correa", "Ariel Perez", "Claudia Soto",
    "Claudio Muñoz", "Javier Ramírez", "Jaime Ortega", "Carlos Conca", "Avelio Sepúlveda",
    "Ariel Perez", "Michal Kowalczyk", "Gabrielle Nornberg", "Patricio Quiroz", "Salome Martinez",
    "Jorge Aguayo", "Raul Manasevich", "Francisco Ortega", "Axel Osses", "Ariel Perez",
    "Nelson Baloian", "Eduardo Godoy", "Juan Álvarez", "Cristian Parra", "Matías Torrealba",
    "Valentín Muñoz", "Juan Álvarez", "Juan Álvarez", "Francisco Gutiérrez", "Valentin Muñoz",
    "Matías Torrealba", "Eduardo Godoy", "Patricio Inostroza", "Cristián Parra", "Ignacio Bordeu",
    "Fernando Lund", "Maricarmen Winkler", "Walter Max-Moerbeck", "Valentino González",
    "Claudio Arenas", "José Mella", "Macarena Muñoz", "Claudio Falcon", "Rodrigo Soto",
    "Claudio Arenas", "Diego Mardones", "José Mella", "Macarena Muñoz", "Andrés Meza",
    "Sebastián López", "Maricarmen Winkler", "Claudio Romero", "Andrés Escala", "Gonzalo Palma",
    "Patricio Aceituno", "Ricardo Muñoz", "César Fuentes", "Diana Dulic", "Marcos Flores",
    "Diego Guzmán", "Carla Hermann", "René Méndez", "Simón Casassus", "Claudio Romero",
    "Domenico Sapone", "Simón Riquelme", "Francisco Brieva", "Claudio Arenas", "Walter Max-Moerbeck",
    "Marcel Clerc", "Claudio Falcón", "Victor Fuenzalida", "Moniellen Pires", "Ivan Paredes",
    "Oriana Salazar", "Catalina Landeta", "Franck Quero", "Natalia Jiménez", "Esteban Araya",
    "Ziomara Gerdtzen", "J. Cristian Salgado", "Álvaro Olivera", "Anamaría Daza", "Melanie Colet",
    "Nicole Parra", "Isadora Berlanga", "Tamara Bruna", "Gabriel Mendoza", "Ricardo Muñoz",
    "Mónica Soler", "Franck Quero", "Nicole Parra", "Pablo Mella", "Bruno Sánchez", "Esteban Araya",
    "Carmen Castro", "Tamara Bruna", "Gerardo Díaz", "Andreas Rosenkranz", "Franck Quero",
    "Andreas Rosenkranz", "Melanie Colet"
]

print(len(elementos))
# eliminar elementos repetidos de la lista elementos
elementos2 = list(set(elementos))
print(len(elementos2))

profesores = ['Marcel Clerc', 'Oriana Salazar', 'Eduardo Godoy', 'Diana Dulic', 'Simón Riquelme', 'Juan José Maulen', 'Juan Álvarez', 'Gonzalo Palma', 'Mauricio Telias', 'Rafael Correa', 'Gabriel Mendoza', 'Ricardo Muñoz', 'Andrés Escala', 'Claudio Arenas', 'Nicolás Hernández', 'Alexis Fuentes', 'Cristián Reyes', 'Ana Trujillo', 'Carla Hermann', 'Jorge Aguayo', 'Anamaría Daza', 'Javier Ramírez', 'Diego Guzmán', 'Claudia Soto', 'Marcos Kiwi', 'Moniellen Pires', 'Carlos Conca', 'Salome Martinez', 'Alejandro Maas', 'Flavio Guiñez', 'Diana Narváez', 'Ariel Perez', 'Francisco Gutiérrez', 'Pablo Mella', 'Rodrigo Soto', 'J. Cristian Salgado', 'Daniel Remenik', 'Patricio Aceituno', 'Ignacio Bordeu', 'Catalina Landeta', 'Carmen Castro', 'Alexander Frank', 'Ivan Paredes', 'Claudio Romero', 'René Méndez', 'Esteban Araya', 'Francisco Brieva', 'Mónica Soler', 'Patricio Inostroza', 'Bruno Sánchez',
              'Maya Stein', 'Simón Casassus', 'Valentin Muñoz', 'Gerardo Díaz', 'Raul Manasevich', 'Macarena Muñoz', 'Tamara Bruna', 'Álvaro Olivera', 'Jaime San Martín', 'Marcos Flores', 'Francisco Ortega', 'Claudio Falcon', 'Victor Fuenzalida', 'Patricio FelmJosé Mella', 'Andrés Meza', 'Leonardo Sánchez', 'Maricarmen Winkler', 'Andreas Rosenkranz', 'Avelio Sepúlveda', 'Jorge San Martín', 'Michal Kowalczyk', 'Natalia Ruiz', 'Cristián Parra', 'Vicente Acuña', 'Claudio Muñoz', 'Sebastián López', 'Natacha Astromujoff', 'Nelson Baloian', 'Ziomara Gerdtzen', 'Domenico Sapone', 'Álvaro Hernández', 'Natalia Jiménez', 'Nicole Parra', 'Axel Osses', 'Gabrielle Nornberg', 'Diego Mardones', 'Rodolfo Gutiérrez', 'Juan Ross', 'Patricio Quiroz', 'Fernando Lund', 'Walter Max-Moerbeck', 'Jaime Ortega', 'Franck Quero', 'César Fuentes', 'Matías Torrealba', 'Yamit Y.', 'Pablo Dartnell', 'Melanie Colet', 'Isadora Berlanga', 'Valentino González']

profesores_problematicos = []
profesores_clean = []
for profesor in profesores:
    nombres = profesor.split(' ')
    if len(nombres) > 2:
        profesores_problematicos.append(profesor)
        continue
    nombre = nombres[0]
    apellido = nombres[-1]
    profesores_clean.append({
        "nombre": nombre,
        "apellido": apellido
    })
print(profesores_problematicos)
profesores_clean.sort(key=lambda p: (p["apellido"], p["nombre"]))
pprint(profesores_clean)
