#!/usr/bin/env python3
"""Batch 16 - themes: relationships, communication, change, growth, reflection."""
import json

ADDITIONS16 = {
    "infancia": [
        ("¿Cuándo fue la primera vez que entendiste que alguien que admirabas era humano e imperfecto?", 1),
        ("¿Cuál fue el personaje de un libro o película que más quisiste ser de chico?", 1),
        ("¿Cuándo fue la primera vez que alguien te regaló algo hecho a mano?", 1),
        ("¿Cuándo fue la primera vez que te quedaste sin palabras de alegría?", 1),
        ("¿Cuándo fue la primera vez que te emocionaste viendo a alguien que querías triunfar?", 1),
        ("¿Cuándo fue la primera vez que perdiste algo que importaba y tuviste que seguir igual?", 1),
        ("¿Tenías algún amigo imaginario o compañero de juego inventado?", 1),
        ("¿Cuándo fue la primera vez que hiciste algo que sabías que estaba mal pero lo hiciste igual?", 1),
        ("¿Cuándo fue la primera vez que alguien te demostró que confiaba en vos?", 1),
        ("¿Cuándo fue la primera vez que viste a alguien llorar y no supiste qué hacer?", 1),
        ("¿Cuándo fue la primera vez que alguien te dio algo sin pedir nada a cambio?", 2),
        ("¿Cuándo fue la primera vez que te diste cuenta de que tus amigos podían equivocarse?", 2),
        ("¿Cuándo fue la primera vez que tuviste que elegir entre lo que querías y lo que era correcto?", 2),
        ("¿Cuándo fue la primera vez que alguien te ayudó cuando no podías pedirlo?", 2),
        ("¿Cuándo fue la primera vez que sentiste que podías confiar más en vos que en lo que te decían?", 2),
        ("¿Cuándo fue la primera vez que perdiste a alguien que amabas y cómo lo procesaste?", 3),
        ("¿Cuándo fue la primera vez que elegiste ser honesto aunque fuera costoso?", 3),
        ("¿Cuál fue el momento de tu infancia que más explica tu relación con la confianza hoy?", 3),
    ],

    "futuro": [
        ("¿Cuál es la ciudad del mundo en la que más te imaginas viviendo?", 1),
        ("¿Cuándo te imaginas que vas a estar en la mejor forma física de tu vida?", 1),
        ("¿Cuándo te imaginas que vas a aprender el idioma que querés aprender?", 1),
        ("¿Cuándo te imaginas que vas a tener la vida que describís como ideal?", 1),
        ("¿Cuándo te imaginas que vas a haber hecho el viaje de tu vida?", 1),
        ("¿Cuándo te imaginas que vas a sentirte más en paz con quien sos?", 1),
        ("¿Cuándo te imaginas que vas a completar el proyecto personal más importante?", 1),
        ("¿Cuándo te imaginas que vas a tener la relación que más querés?", 1),
        ("¿Cuándo te imaginas que vas a sentirte financieramente libre?", 1),
        ("¿Cuándo te imaginas que vas a hacer algo que hoy parece imposible?", 1),
        ("¿Cuándo fue la última vez que te imaginaste fallando en algo grande y seguiste igual?", 2),
        ("¿Cuándo fue la última vez que revisaste si las metas que tenés siguen siendo tuyas?", 2),
        ("¿Cuándo fue la última vez que redefiniste lo que para vos significa el éxito?", 2),
        ("¿Cuándo fue la última vez que el futuro te pareció más una posibilidad que una amenaza?", 2),
        ("¿Cuándo fue la última vez que algo del presente te hizo sentir que el futuro podía ser bueno?", 2),
        ("¿Cuándo fue la última vez que el futuro te generó más curiosidad que ansiedad?", 3),
        ("¿Cuándo fue la última vez que elegiste no planear algo y confiar?", 3),
        ("¿Cuándo fue la última vez que el futuro te pareció exactamente lo que querías?", 3),
    ],

    "amor": [
        ("¿Cuándo fue la última vez que te enamoraste de la manera en que alguien hablaba?", 1),
        ("¿Cuándo fue la última vez que te gustó alguien por algo completamente inesperado?", 1),
        ("¿Cuándo fue la última vez que alguien te sorprendió con algo pequeño que importó mucho?", 1),
        ("¿Cuándo fue la última vez que te gustó tanto alguien que no pudiste concentrarte?", 1),
        ("¿Cuándo fue la última vez que escribiste algo a alguien que te gustaba y te arrepentiste de enviarlo?", 1),
        ("¿Cuándo fue la última vez que alguien te gustó tanto que te puso nervioso solo de pensar?", 1),
        ("¿Cuándo fue la última vez que te gustó alguien sin que hubiera ninguna razón racional?", 1),
        ("¿Cuándo fue la última vez que algo que alguien dijo te cambió completamente la percepción?", 1),
        ("¿Cuándo fue la última vez que el amor fue más liviano que pesado?", 1),
        ("¿Cuándo fue la última vez que el amor te hizo actuar de una manera que te sorprendió?", 1),
        ("¿Cuándo fue la última vez que el amor te enseñó algo que ninguna lección te enseñó?", 2),
        ("¿Cuándo fue la última vez que el amor te mostró una parte de vos que no conocías?", 2),
        ("¿Cuándo fue la última vez que el amor fue lo único que importaba en un momento?", 2),
        ("¿Cuándo fue la última vez que el amor te hizo sentir completamente bien siendo vos?", 2),
        ("¿Cuándo fue la última vez que el amor fue exactamente lo que necesitabas cuando más lo necesitabas?", 2),
        ("¿Cuándo fue la última vez que te animaste a amar sabiendo el riesgo completo?", 3),
        ("¿Cuándo fue la última vez que el amor te transformó de adentro hacia afuera?", 3),
        ("¿Cuándo fue la última vez que amar a alguien fue la decisión más valiente que tomaste?", 3),
    ],

    "familia": [
        ("¿Cuándo fue la última vez que alguien de tu familia hizo algo que te hizo sentir que estabas en el lugar correcto?", 1),
        ("¿Cuándo fue la última vez que tu familia demostró algo de vos que vos mismo no habías notado?", 1),
        ("¿Cuándo fue la última vez que tu familia te hizo sentir que pertenecías?", 1),
        ("¿Cuándo fue la última vez que alguien de tu familia te dijo algo que tardaste años en entender?", 1),
        ("¿Cuándo fue la última vez que tu familia celebró algo tuyo aunque no lo entendiera del todo?", 1),
        ("¿Cuándo fue la última vez que tu familia te acompañó en algo sin pedir explicaciones?", 1),
        ("¿Cuándo fue la última vez que alguien de tu familia te llamó en el momento exacto en que lo necesitabas?", 1),
        ("¿Cuándo fue la última vez que tu familia cambió algo para adaptarse a vos?", 1),
        ("¿Cuándo fue la última vez que la distancia con tu familia no importó porque estaban cerca igual?", 1),
        ("¿Cuándo fue la última vez que alguien de tu familia fue exactamente lo que necesitabas?", 1),
        ("¿Cuándo fue la última vez que tu familia demostró que te conocía mejor de lo que pensabas?", 2),
        ("¿Cuándo fue la última vez que alguien de tu familia te abrió algo que tenías cerrado?", 2),
        ("¿Cuándo fue la última vez que tu familia fue la razón por la que seguiste?", 2),
        ("¿Cuándo fue la última vez que tu familia fue honesta con vos aunque te costara escucharlo?", 2),
        ("¿Cuándo fue la última vez que tu familia fue más grande de lo que esperabas?", 2),
        ("¿Cuándo fue la última vez que elegiste honrar algo de tu familia aunque te costara?", 3),
        ("¿Cuándo fue la última vez que tu familia te liberó de algo que creías que debías ser?", 3),
        ("¿Cuándo fue la última vez que sentiste que tu familia fue la base desde la que podías hacer cualquier cosa?", 3),
    ],

    "amistades": [
        ("¿Cuándo fue la última vez que algo que dijo un amigo te cambió la semana?", 1),
        ("¿Cuándo fue la última vez que un amigo te hizo sentir que estabas haciendo algo importante?", 1),
        ("¿Cuándo fue la última vez que un amigo estuvo en el momento más equivocado pero de la manera más correcta?", 1),
        ("¿Cuándo fue la última vez que la risa con un amigo fue exactamente lo que necesitabas?", 1),
        ("¿Cuándo fue la última vez que un amigo te dijo la verdad cuando todos los demás callaban?", 1),
        ("¿Cuándo fue la última vez que un amigo te acompañó en algo sin entender del todo?", 1),
        ("¿Cuándo fue la última vez que algo que un amigo te enseñó lo usaste en un momento clave?", 1),
        ("¿Cuándo fue la última vez que un amigo te hizo sentir que todo iba a estar bien?", 1),
        ("¿Cuándo fue la última vez que un amigo te devolvió algo que habías perdido de vos mismo?", 1),
        ("¿Cuándo fue la última vez que un amigo hizo algo que te hizo sentir orgulloso de conocerlo?", 1),
        ("¿Cuándo fue la última vez que una amistad te hizo más valiente?", 2),
        ("¿Cuándo fue la última vez que un amigo te hizo ver algo que ningún espejo te mostraría?", 2),
        ("¿Cuándo fue la última vez que una amistad te dio exactamente lo que la familia no podía?", 2),
        ("¿Cuándo fue la última vez que una amistad te liberó de algo?", 2),
        ("¿Cuándo fue la última vez que gracias a un amigo dejaste de ser quien no querías ser?", 2),
        ("¿Cuándo fue la última vez que una amistad fue el lugar más seguro que tenías?", 3),
        ("¿Cuándo fue la última vez que una amistad fue la razón por la que seguiste intentándolo?", 3),
        ("¿Cuándo fue la última vez que una amistad te recordó quién eras cuando lo olvidabas?", 3),
    ],

    "exs": [
        ("¿Cuándo fue la última vez que algo del pasado amoroso te ayudó en el presente?", 1),
        ("¿Cuándo fue la primera vez que alguien del pasado te mostró algo de vos que no podías ver?", 1),
        ("¿Cuándo fue la primera vez que una relación te hizo sentir que el mundo era más grande?", 1),
        ("¿Cuándo fue la primera vez que le diste la bienvenida a alguien nuevo después de una ruptura?", 1),
        ("¿Cuándo fue la primera vez que sentiste que estabas listo para algo nuevo?", 1),
        ("¿Cuándo fue la primera vez que saliste de una relación sintiéndote más vos?", 1),
        ("¿Cuándo fue la primera vez que una relación terminó en el momento exacto en que debía?", 1),
        ("¿Cuándo fue la última vez que una relación pasada te hizo sentir agradecido por el presente?", 1),
        ("¿Cuándo fue la última vez que algo que aprendiste de un ex lo usaste en algo importante?", 1),
        ("¿Cuándo fue la última vez que cerraste algo del pasado amoroso de manera limpia?", 1),
        ("¿Cuándo fue la última vez que te diste cuenta de que el pasado amoroso te hizo crecer?", 2),
        ("¿Cuándo fue la última vez que el pasado amoroso fue una fortaleza en vez de un peso?", 2),
        ("¿Cuándo fue la última vez que algo que viviste en el amor te dio herramientas para otras áreas?", 2),
        ("¿Cuándo fue la última vez que perdonar algo del pasado te liberó completamente?", 2),
        ("¿Cuándo fue la última vez que una relación pasada te ayudó a saber qué no querías más?", 2),
        ("¿Cuándo fue la última vez que el amor del pasado te dio fuerza para el presente?", 3),
        ("¿Cuándo fue la última vez que agradeciste algo de una relación pasada que entonces no podías?", 3),
        ("¿Cuándo fue la última vez que el pasado amoroso fue la razón por la que amás mejor ahora?", 3),
    ],

    "personalidad": [
        ("¿Cuándo fue la última vez que alguien te vio de una manera que te costó pero necesitabas?", 1),
        ("¿Cuándo fue la última vez que cambió algo en cómo te relacionabas con vos mismo?", 1),
        ("¿Cuándo fue la última vez que te perdonaste algo que creías imperdonable?", 1),
        ("¿Cuándo fue la última vez que algo externo te mostró algo interno?", 1),
        ("¿Cuándo fue la última vez que te sorprendiste siendo más capaz de lo que esperabas?", 1),
        ("¿Cuándo fue la última vez que elegiste la autenticidad sobre la comodidad?", 1),
        ("¿Cuándo fue la última vez que algo te enseñó más sobre vos que sobre el mundo?", 1),
        ("¿Cuándo fue la última vez que alguien te conoció mejor que vos mismo?", 1),
        ("¿Cuándo fue la última vez que elegiste la bondad cuando nadie te obligaba?", 1),
        ("¿Cuándo fue la última vez que decidiste ser honesto aunque te costara más?", 1),
        ("¿Cuándo fue la última vez que algo te obligó a crecer de manera que no esperabas?", 2),
        ("¿Cuándo fue la última vez que algo cambió tu manera de estar en el mundo?", 2),
        ("¿Cuándo fue la última vez que elegiste soltar algo que te definía pero ya no te servía?", 2),
        ("¿Cuándo fue la última vez que tu mejor versión apareció sin que lo planeaste?", 2),
        ("¿Cuándo fue la última vez que elegiste cambiar algo de vos por razones completamente propias?", 2),
        ("¿Cuándo fue la última vez que te elegiste a vos mismo de manera incondicional?", 3),
        ("¿Cuándo fue la última vez que fuiste completamente fiel a quien sos aunque costara?", 3),
        ("¿Cuándo fue la última vez que sentiste que todo lo que sos tiene sentido?", 3),
    ],

    "miedos": [
        ("¿Cuándo fue la última vez que el miedo te mostró exactamente lo que valorás?", 1),
        ("¿Cuándo fue la última vez que hablaste de un miedo y se hizo más pequeño?", 1),
        ("¿Cuándo fue la última vez que el miedo fue más pequeño de lo que parecía?", 1),
        ("¿Cuándo fue la última vez que el miedo te hizo más curioso que paralizado?", 1),
        ("¿Cuándo fue la última vez que superaste un miedo y sentiste que todo cambiaba?", 1),
        ("¿Cuándo fue la última vez que el miedo se convirtió en algo útil?", 1),
        ("¿Cuándo fue la última vez que el miedo te unió a alguien que sentía lo mismo?", 1),
        ("¿Cuándo fue la última vez que el miedo te obligó a elegir con más cuidado?", 1),
        ("¿Cuándo fue la última vez que el miedo te enseñó a valorar algo que dabas por sentado?", 1),
        ("¿Cuándo fue la última vez que algo que temías resultó ser la mejor decisión?", 1),
        ("¿Cuándo fue la última vez que el miedo fue la señal de que algo importaba?", 2),
        ("¿Cuándo fue la última vez que el miedo al fracaso te hizo prepararte mejor?", 2),
        ("¿Cuándo fue la última vez que el miedo te enseñó algo que el éxito nunca pudo?", 2),
        ("¿Cuándo fue la última vez que el miedo fue más honesto que cualquier razón lógica?", 2),
        ("¿Cuándo fue la última vez que el miedo te llevó exactamente adonde necesitabas ir?", 2),
        ("¿Cuándo fue la última vez que superaste algo que creías que nunca superarías?", 3),
        ("¿Cuándo fue la última vez que el miedo fue el camino hacia algo que realmente querías?", 3),
        ("¿Cuándo fue la última vez que la valentía fue más grande que el miedo?", 3),
    ],

    "logros": [
        ("¿Cuándo fue la última vez que algo que lograste fue más para otros que para vos?", 1),
        ("¿Cuándo fue la última vez que un logro te conectó con gente que no esperabas?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue el resultado de escuchar mejor?", 1),
        ("¿Cuándo fue la última vez que lograste algo que antes era el techo para vos?", 1),
        ("¿Cuándo fue la última vez que algo que hiciste generó un efecto mayor del que esperabas?", 1),
        ("¿Cuándo fue la última vez que tu perseverancia fue la única diferencia?", 1),
        ("¿Cuándo fue la última vez que algo que creaste fue más bueno que lo que planeaste?", 1),
        ("¿Cuándo fue la última vez que un logro fue la consecuencia directa de haber fallado antes?", 1),
        ("¿Cuándo fue la última vez que lograste algo y le dio más sentido a todo lo anterior?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue completamente inesperado?", 1),
        ("¿Cuándo fue la última vez que un logro te hizo más humilde que orgulloso?", 2),
        ("¿Cuándo fue la última vez que algo que lograste cambió cómo te ves en el futuro?", 2),
        ("¿Cuándo fue la última vez que un logro tuyo dio lugar a algo que no esperabas?", 2),
        ("¿Cuándo fue la última vez que un fracaso fue el camino hacia algo mejor?", 2),
        ("¿Cuándo fue la última vez que algo que lograste te cambió profundamente como persona?", 2),
        ("¿Cuándo fue la última vez que un logro fue la respuesta a años de esfuerzo silencioso?", 3),
        ("¿Cuándo fue la última vez que lograste algo que cambió quién sos para siempre?", 3),
        ("¿Cuándo fue la última vez que lo que lograste fue exactamente lo que el mundo necesitaba de vos?", 3),
    ],

    "sinFiltro": [
        ("¿Cuántas veces por semana hacés algo sabiendo que después te vas a arrepentir?", 1),
        ("¿Cuántas veces revisaste si alguien vio tu estado sin haberle escrito?", 1),
        ("¿Cuántas veces por mes dejás tareas para mañana que acaban siendo para la semana que viene?", 1),
        ("¿Cuántas conversaciones incómodas evitaste con mensajes de 'sí, claro'?", 1),
        ("¿Cuántas veces al mes comprás algo con envío porque no querés salir a buscarlo?", 1),
        ("¿Cuántas veces diste like a algo por pura cortesía y no por convicción?", 1),
        ("¿Cuántas veces al mes te quedás dormido con el celular en la mano?", 1),
        ("¿Cuántas veces por semana tenés ganas de no responder absolutamente nada de nadie?", 1),
        ("¿Cuántas veces guardaste un numero sin intención de llamar?", 1),
        ("¿Cuántas veces prometiste devolver algo que todavía no devolviste?", 1),
        ("¿Cuándo fue la última vez que hiciste algo que definitivamente no era para vos pero lo hiciste igual por presión?", 2),
        ("¿Cuándo fue la última vez que te creaste una versión de los hechos que era conveniente para vos?", 2),
        ("¿Cuándo fue la última vez que hiciste algo cuestionable y lo justificaste perfectamente?", 2),
        ("¿Cuándo fue la última vez que actuaste desde el rencor y tardaste en reconocerlo?", 2),
        ("¿Cuándo fue la última vez que usaste la 'honestidad' para decir algo cruel?", 2),
        ("¿Cuándo fue la última vez que hiciste algo que nadie esperaría de vos y que no contarías?", 3),
        ("¿Cuál es la cosa que más miedo te daría que este grupo supiera de vos?", 3),
        ("¿Cuándo fue la última vez que actuaste de una manera que contradecía todo lo que mostrás?", 3),
    ],
}

def get_prefix(cat_id):
    return {
        "infancia": "inf", "futuro": "fut", "amor": "am", "familia": "fam",
        "amistades": "ami", "exs": "ex", "personalidad": "per",
        "miedos": "mie", "logros": "log", "sinFiltro": "sf",
    }[cat_id]

def main():
    with open("data/questions.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for cat in data["categories"]:
        cat_id = cat["id"]
        if cat_id not in ADDITIONS16:
            continue

        prefix = get_prefix(cat_id)
        max_idx = {1: 0, 2: 0, 3: 0}
        for q in cat["questions"]:
            parts = q["id"].split("_")
            level = int(parts[1])
            idx = int(parts[2])
            if idx > max_idx[level]:
                max_idx[level] = idx

        level_counters = dict(max_idx)
        new_qs = []

        for (text, level) in ADDITIONS16[cat_id]:
            level_counters[level] += 1
            q_id = f"{prefix}_{level}_{level_counters[level]:03d}"
            new_qs.append({"id": q_id, "text": text, "level": level})

        cat["questions"].extend(new_qs)
        print(f"{cat_id}: {len(cat['questions']) - len(new_qs)} → {len(cat['questions'])} (+{len(new_qs)})")

    with open("data/questions.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    total = sum(len(c["questions"]) for c in data["categories"])
    print(f"\nTotal questions: {total}")

if __name__ == "__main__":
    main()
