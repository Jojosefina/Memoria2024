from catalog.models import (
    Asignaturas,
    TiposMaterial,
    Profesores,
    Semestres
)


def populate_asignaturas():
    asignaturas = [
        {"nombre": "Introducción al Cálculo", "codigo_curso": "MA1001"},
        {"nombre": "Cálculo Diferencial e Integral", "codigo_curso": "MA1002"},
        {"nombre": "Introducción al Álgebra", "codigo_curso": "MA1101"},
        {"nombre": "Álgebra Lineal", "codigo_curso": "MA1102"},
        {"nombre": "Cálculo en Varias Variables", "codigo_curso": "MA2001"},
        {"nombre": "Cálculo Avanzado y Aplicaciones", "codigo_curso": "MA2002"},
        {"nombre": "Ecuaciones Diferenciales Ordinarias", "codigo_curso": "MA2601"},
        {"nombre": "Herramientas Computacionales para Ingeniería y Ciencias",
            "codigo_curso": "CC1000"},
        {"nombre": "Introducción a la Programación", "codigo_curso": "CC1002"},
        {"nombre": "Introducción a la Física Clásica", "codigo_curso": "FI1000"},
        {"nombre": "Introducción a la Física Moderna", "codigo_curso": "FI1100"},
        {"nombre": "Mecánica", "codigo_curso": "FI2001"},
        {"nombre": "Métodos Experimentales", "codigo_curso": "FI2003"},
        {"nombre": "Electromagnetismo", "codigo_curso": "FI2002"},
        {"nombre": "Termodinámica", "codigo_curso": "FI2004"},
        {"nombre": "Aplicaciones de la Biología a la Ingeniería y Ciencias",
            "codigo_curso": "BT1211"},
        {"nombre": "Química", "codigo_curso": "IQ2211"},
        {"nombre": "Termodinámica Química", "codigo_curso": "IQ2212"},
    ]
    for asignatura in asignaturas:
        Asignaturas.objects.create(**asignatura)


def populate_tipos_material():
    tipos_material = [
        {"nombre": "Teórico"},
        {"nombre": "Práctico"},
    ]
    for tipo_material in tipos_material:
        TiposMaterial.objects.create(**tipo_material)


def getAsignaturasId(codigo):
    asignatura = Asignaturas.objects.get(codigo_curso=codigo)
    return asignatura.id_asignatura


def populate_profesores():
    profesores = [
        {"apellido": "Aceituno", "nombre": "Patricio",
            "asignatura": [getAsignaturasId("FI2001")]},
        {"apellido": "Acuña", "nombre": "Vicente", "asignatura": [
            getAsignaturasId("MA1102"), getAsignaturasId("MA1101")]},
        {"apellido": "Aguayo", "nombre": "Jorge", "asignatura": [
            getAsignaturasId("MA2601"), getAsignaturasId("MA1001")]},
        {"apellido": "Araya", "nombre": "Esteban", "asignatura": [
            getAsignaturasId("BT1211"), getAsignaturasId("IQ2211")]},
        {"apellido": "Arenas", "nombre": "Claudio", "asignatura": [getAsignaturasId(
            "FI1000"), getAsignaturasId("FI2002"), getAsignaturasId("FI1100")]},
        {"apellido": "Astromujoff", "nombre": "Natacha",
            "asignatura": [getAsignaturasId("MA1102")]},
        {"apellido": "Baloian", "nombre": "Nelson",
            "asignatura": [getAsignaturasId("CC1000")]},
        {"apellido": "Berlanga", "nombre": "Isadora",
            "asignatura": [getAsignaturasId("IQ2211")]},
        {"apellido": "Bordeu", "nombre": "Ignacio",
            "asignatura": [getAsignaturasId("FI1000")]},
        {"apellido": "Brieva", "nombre": "Francisco",
            "asignatura": [getAsignaturasId("FI2002")]},
        {"apellido": "Bruna", "nombre": "Tamara",
            "asignatura": [getAsignaturasId("IQ2211")]},
        {"apellido": "Casassus", "nombre": "Simón",
            "asignatura": [getAsignaturasId("FI2002")]},
        {"apellido": "Castro", "nombre": "Carmen",
            "asignatura": [getAsignaturasId("IQ2211")]},
        {"apellido": "Clerc", "nombre": "Marcel",
            "asignatura": [getAsignaturasId("FI2002")]},
        {"apellido": "Colet", "nombre": "Melanie", "asignatura": [
            getAsignaturasId("IQ2211"), getAsignaturasId("IQ2212")]},
        {"apellido": "Conca", "nombre": "Carlos",
            "asignatura": [getAsignaturasId("MA2002")]},
        {"apellido": "Correa", "nombre": "Rafael",
            "asignatura": [getAsignaturasId("MA2001")]},
        {"apellido": "Dartnell", "nombre": "Pablo", "asignatura": [
            getAsignaturasId("MA1101"), getAsignaturasId("MA1102")]},
        {"apellido": "Daza", "nombre": "Anamaría",
            "asignatura": [getAsignaturasId("BT1211")]},
        {"apellido": "Dulic", "nombre": "Diana",
            "asignatura": [getAsignaturasId("FI2003")]},
        {"apellido": "Díaz", "nombre": "Gerardo",
            "asignatura": [getAsignaturasId("IQ2212")]},
        {"apellido": "Escala", "nombre": "Andrés",
            "asignatura": [getAsignaturasId("FI2001")]},
        {"apellido": "Falcon", "nombre": "Claudio", "asignatura": [
            getAsignaturasId("FI1000"), getAsignaturasId("FI2004")]},
        {"apellido": "Felmer", "nombre": "Patricio", "asignatura": [
            getAsignaturasId("MA1001"), getAsignaturasId("MA1002")]},
        {"apellido": "Flores", "nombre": "Marcos",
            "asignatura": [getAsignaturasId("FI2003")]},
        {"apellido": "Frank", "nombre": "Alexander", "asignatura": [
            getAsignaturasId("MA1101"), getAsignaturasId("MA1102")]},
        {"apellido": "Fuentes", "nombre": "Alexis", "asignatura": [
            getAsignaturasId("MA2001"), getAsignaturasId("MA1101")]},
        {"apellido": "Fuentes", "nombre": "César",
            "asignatura": [getAsignaturasId("FI2001")]},
        {"apellido": "Fuenzalida", "nombre": "Victor",
            "asignatura": [getAsignaturasId("FI2004")]},
        {"apellido": "Gerdtzen", "nombre": "Ziomara",
            "asignatura": [getAsignaturasId("BT1211")]},
        {"apellido": "Godoy", "nombre": "Eduardo", "asignatura": [
            getAsignaturasId("CC1000"), getAsignaturasId("CC1002")]},
        {"apellido": "González", "nombre": "Valentino",
            "asignatura": [getAsignaturasId("FI1000")]},
        {"apellido": "Guiñez", "nombre": "Flavio",
            "asignatura": [getAsignaturasId("MA1101")]},
        {"apellido": "Gutiérrez", "nombre": "Francisco",
            "asignatura": [getAsignaturasId("CC1002")]},
        {"apellido": "Gutiérrez", "nombre": "Rodolfo",
            "asignatura": [getAsignaturasId("MA1002")]},
        {"apellido": "Guzmán", "nombre": "Diego",
            "asignatura": [getAsignaturasId("FI2003")]},
        {"apellido": "Hermann", "nombre": "Carla",
            "asignatura": [getAsignaturasId("FI2003")]},
        {"apellido": "Hernández", "nombre": "Nicolás",
            "asignatura": [getAsignaturasId("MA1101")]},
        {"apellido": "Hernández", "nombre": "Álvaro",
            "asignatura": [getAsignaturasId("MA1101")]},
        {"apellido": "Inostroza", "nombre": "Patricio",
            "asignatura": [getAsignaturasId("CC1002")]},
        {"apellido": "Jiménez", "nombre": "Natalia",
            "asignatura": [getAsignaturasId("BT1211")]},
        {"apellido": "Kiwi", "nombre": "Marcos",
            "asignatura": [getAsignaturasId("MA1102")]},
        {"apellido": "Kowalczyk", "nombre": "Michal",
            "asignatura": [getAsignaturasId("MA2601")]},
        {"apellido": "Landeta", "nombre": "Catalina",
            "asignatura": [getAsignaturasId("BT1211")]},
        {"apellido": "Lund", "nombre": "Fernando",
            "asignatura": [getAsignaturasId("FI1000")]},
        {"apellido": "López", "nombre": "Sebastián",
            "asignatura": [getAsignaturasId("FI1100")]},
        {"apellido": "Maas", "nombre": "Alejandro",
            "asignatura": [getAsignaturasId("MA1102")]},
        {"apellido": "Manasevich", "nombre": "Raul",
            "asignatura": [getAsignaturasId("MA2601")]},
        {"apellido": "Mardones", "nombre": "Diego",
            "asignatura": [getAsignaturasId("FI1100")]},
        {"apellido": "Martinez", "nombre": "Salome",
            "asignatura": [getAsignaturasId("MA2601")]},
        {"apellido": "Maulen", "nombre": "Juan José", "asignatura": [
            getAsignaturasId("MA1001"), getAsignaturasId("MA1002")]},
        {"apellido": "Max-Moerbeck", "nombre": "Walter",
            "asignatura": [getAsignaturasId("FI1000"), getAsignaturasId("FI2002")]},
        {"apellido": "Mella", "nombre": "José", "asignatura": [
            getAsignaturasId("FI1000"), getAsignaturasId("FI1100")]},
        {"apellido": "Mella", "nombre": "Pablo",
            "asignatura": [getAsignaturasId("IQ2211")]},
        {"apellido": "Mendoza", "nombre": "Gabriel",
            "asignatura": [getAsignaturasId("IQ2211")]},
        {"apellido": "Meza", "nombre": "Andrés",
            "asignatura": [getAsignaturasId("FI1100")]},
        {"apellido": "Muñoz", "nombre": "Claudio",
            "asignatura": [getAsignaturasId("MA2001")]},
        {"apellido": "Muñoz", "nombre": "Macarena", "asignatura": [
            getAsignaturasId("FI1000"), getAsignaturasId("FI1100")]},
        {"apellido": "Muñoz", "nombre": "Ricardo", "asignatura": [
            getAsignaturasId("IQ2211"), getAsignaturasId("FI2001")]},
        {"apellido": "Muñoz", "nombre": "Valentin", "asignatura": [
            getAsignaturasId("CC1000"), getAsignaturasId("CC1002")]},
        {"apellido": "Méndez", "nombre": "René",
            "asignatura": [getAsignaturasId("FI2003")]},
        {"apellido": "Narváez", "nombre": "Diana", "asignatura": [
            getAsignaturasId("MA1001"), getAsignaturasId("MA1002")]},
        {"apellido": "Nornberg", "nombre": "Gabrielle",
            "asignatura": [getAsignaturasId("MA2601")]},
        {"apellido": "Olivera", "nombre": "Álvaro",
            "asignatura": [getAsignaturasId("BT1211")]},
        {"apellido": "Ortega", "nombre": "Francisco",
            "asignatura": [getAsignaturasId("MA2601")]},
        {"apellido": "Ortega", "nombre": "Jaime",
            "asignatura": [getAsignaturasId("MA2002")]},
        {"apellido": "Osses", "nombre": "Axel",
            "asignatura": [getAsignaturasId("MA2601")]},
        {"apellido": "Palma", "nombre": "Gonzalo",
            "asignatura": [getAsignaturasId("FI2001")]},
        {"apellido": "Paredes", "nombre": "Ivan",
            "asignatura": [getAsignaturasId("BT1211")]},
        {"apellido": "Parra", "nombre": "Cristián", "asignatura": [
            getAsignaturasId("CC1000"), getAsignaturasId("CC1002")]},
        {"apellido": "Parra", "nombre": "Nicole",
            "asignatura": [getAsignaturasId("IQ2211")]},
        {"apellido": "Perez", "nombre": "Ariel", "asignatura": [getAsignaturasId(
            "MA2001"), getAsignaturasId("MA2002"), getAsignaturasId("MA2601")]},
        {"apellido": "Pires", "nombre": "Moniellen",
            "asignatura": [getAsignaturasId("FI2004")]},
        {"apellido": "Quero", "nombre": "Franck", "asignatura": [getAsignaturasId(
            "BT1211"), getAsignaturasId("IQ2211"), getAsignaturasId("IQ2212")]},
        {"apellido": "Quiroz", "nombre": "Patricio", "asignatura": [
            getAsignaturasId("MA1101"), getAsignaturasId("MA2601")]},
        {"apellido": "Ramírez", "nombre": "Javier", "asignatura": [getAsignaturasId(
            "MA1001"), getAsignaturasId("MA2001"), getAsignaturasId("MA2002")]},
        {"apellido": "Remenik", "nombre": "Daniel",
            "asignatura": [getAsignaturasId("MA1102")]},
        {"apellido": "Reyes", "nombre": "Cristián", "asignatura": [
            getAsignaturasId("MA1001"), getAsignaturasId("MA1002")]},
        {"apellido": "Riquelme", "nombre": "Simón",
            "asignatura": [getAsignaturasId("FI2002")]},
        {"apellido": "Romero", "nombre": "Claudio", "asignatura": [
            getAsignaturasId("FI2001"), getAsignaturasId("FI2002")]},
        {"apellido": "Rosenkranz", "nombre": "Andreas",
            "asignatura": [getAsignaturasId("IQ2212")]},
        {"apellido": "Ross", "nombre": "Juan",
            "asignatura": [getAsignaturasId("MA1101")]},
        {"apellido": "Ruiz", "nombre": "Natalia",
            "asignatura": [getAsignaturasId("MA1001")]},
        {"apellido": "Salazar", "nombre": "Oriana",
            "asignatura": [getAsignaturasId("BT1211")]},
        {"apellido": "Salgado", "nombre": "J. Cristian",
            "asignatura": [getAsignaturasId("BT1211")]},
        {"apellido": "San Martín", "nombre": "Jaime",
            "asignatura": [getAsignaturasId("MA1102")]},
        {"apellido": "San Martín", "nombre": "Jorge", "asignatura": [
            getAsignaturasId("MA1001"), getAsignaturasId("MA1002")]},
        {"apellido": "Sapone", "nombre": "Domenico",
            "asignatura": [getAsignaturasId("FI2002")]},
        {"apellido": "Sepúlveda", "nombre": "Avelio",
            "asignatura": [getAsignaturasId("MA2002")]},
        {"apellido": "Soler", "nombre": "Mónica",
            "asignatura": [getAsignaturasId("IQ2211")]},
        {"apellido": "Soto", "nombre": "Claudia",
            "asignatura": [getAsignaturasId("MA2001")]},
        {"apellido": "Soto", "nombre": "Rodrigo",
            "asignatura": [getAsignaturasId("FI1000")]},
        {"apellido": "Stein", "nombre": "Maya",
            "asignatura": [getAsignaturasId("MA1101")]},
        {"apellido": "Sánchez", "nombre": "Bruno",
            "asignatura": [getAsignaturasId("IQ2211")]},
        {"apellido": "Sánchez", "nombre": "Leonardo", "asignatura": [
            getAsignaturasId("MA1001"), getAsignaturasId("MA1101")]},
        {"apellido": "Telias", "nombre": "Mauricio", "asignatura": [
            getAsignaturasId("MA1002"), getAsignaturasId("MA1101")]},
        {"apellido": "Torrealba", "nombre": "Matías", "asignatura": [
            getAsignaturasId("CC1000"), getAsignaturasId("CC1002")]},
        {"apellido": "Trujillo", "nombre": "Ana",
            "asignatura": [getAsignaturasId("MA1101")]},
        {"apellido": "Winkler", "nombre": "Maricarmen", "asignatura": [
            getAsignaturasId("FI1000"), getAsignaturasId("FI1100")]},
        {"apellido": "Y.", "nombre": "Yamit",
            "asignatura": [getAsignaturasId("MA1001")]},
        {"apellido": "Álvarez", "nombre": "Juan", "asignatura": [
            getAsignaturasId("CC1000"), getAsignaturasId("CC1002")]},
    ]
    for profesor_data in profesores:
        profesor = Profesores.objects.create(
            apellido=profesor_data["apellido"], nombre=profesor_data["nombre"])
        profesor.save()
        asignaturas = profesor_data["asignatura"]
        for asignatura in asignaturas:
            profesor.asignatura.add(asignatura)


def populate_semestres():
    semestres = [
        {"nombre": "Primer Semestre", "asignatura": [getAsignaturasId("MA1001"), getAsignaturasId("MA1101"), getAsignaturasId(
            "CC1000"), getAsignaturasId("FI1000"), getAsignaturasId("BT1211")]},
        {"nombre": "Segundo Semestre", "asignatura": [getAsignaturasId("MA1002"), getAsignaturasId(
            "MA1102"), getAsignaturasId("CC1002"), getAsignaturasId("FI1100")]},
        {"nombre": "Tercer Semestre", "asignatura": [getAsignaturasId("MA2001"), getAsignaturasId(
            "MA2601"), getAsignaturasId("FI2001"), getAsignaturasId("FI2003"), getAsignaturasId("IQ2211")]},
        {"nombre": "Cuarto Semestre", "asignatura": [getAsignaturasId("MA2002"), getAsignaturasId(
            "FI2002"), getAsignaturasId("FI2004"), getAsignaturasId("IQ2212")]},
    ]
    for semestre_data in semestres:
        semestre = Semestres.objects.create(nombre=semestre_data["nombre"])
        semestre.save()
        asignaturas = semestre_data["asignatura"]
        for asignatura in asignaturas:
            semestre.asignatura.add(asignatura)


def populate():
    populate_asignaturas()
    populate_tipos_material()
    populate_profesores()
    populate_semestres()
    print("Data populated successfully")


if __name__ == "__main__":
    populate()
