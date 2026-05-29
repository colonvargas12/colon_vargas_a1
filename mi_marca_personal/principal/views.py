from django.shortcuts import render

def inicio(request):
    datos = {
        "nombre": "Colon Vargas",
        "marca": "Colon Vargas | Marca Personal",
        "descripcion": "Estudiante interesado en desarrollo de software, inteligencia artificial y creación de páginas web.",
        "habilidades": ["Python", "Django", "HTML", "CSS", "JavaScript", "Bases de datos"],
        "proyectos": [
            "Landing page de marca personal",
            "Sistemas web con registro de usuarios",
            "Asistentes educativos con inteligencia artificial"
        ]
    }
    return render(request, 'principal/index.html', datos)
