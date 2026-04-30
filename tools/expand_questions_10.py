#!/usr/bin/env python3
"""Batch 10 - themes: ethics, beauty, time, memory, wildcard."""
import json

ADDITIONS10 = {
    "infancia": [
        ("¿Cuándo fue la primera vez que te pusiste en el lugar de alguien que sufría?", 1),
        ("¿Tenías algún super poder favorito que querías tener?", 1),
        ("¿Cuál fue el primer trabajo que le viste hacer a tu papá o mamá?", 1),
        ("¿Cuándo fue la primera vez que elegiste a quién querías ser como amigo?", 1),
        ("¿Cuándo fue la primera vez que te pusiste el despertador solo?", 1),
        ("¿Cuándo fue la primera vez que cuidaste a alguien menor que vos?", 1),
        ("¿Qué pregunta le hacías a tus padres que nunca pudieron responder bien?", 1),
        ("¿Cuándo fue la primera vez que dormiste sin luz?", 1),
        ("¿Qué hacías cuando te aburrías en casa sin tecnología?", 1),
        ("¿Cuándo fue la primera vez que hiciste algo que tus padres te habían prohibido?", 1),
        ("¿Cuándo fue la primera vez que alguien fue cruel contigo sin razón?", 2),
        ("¿Cuándo fue la primera vez que sentiste que tus padres estaban equivocados sobre algo importante?", 2),
        ("¿Cuándo fue la primera vez que elegiste a un amigo sobre tu familia?", 2),
        ("¿Cuándo fue la primera vez que entendiste que el tiempo no vuelve?", 2),
        ("¿Cuándo fue la primera vez que alguien te enseñó algo que nadie más te enseñó?", 2),
        ("¿Cuándo fue la primera vez que sentiste que tenías que protegerte a vos mismo?", 2),
        ("¿Cuándo fue la primera vez que lloraste sin saber por qué?", 2),
        ("¿Cuándo fue la primera vez que creíste más en vos que en lo que te decían?", 3),
        ("¿Hay algo de tu infancia que nunca le contaste a nadie y que cambió algo en vos?", 3),
        ("¿Cuándo fue la primera vez que elegiste vos mismo sobre lo que los demás querían?", 3),
    ],

    "futuro": [
        ("¿Si pudieras eliminar una cosa del mundo, qué eliminarías?", 1),
        ("¿Si pudieras agregar algo al mundo que no existe, qué agregarías?", 1),
        ("¿Cuándo te imaginás que el mundo va a estar mejor que ahora?", 1),
        ("¿Cuál es el invento que más querés que exista en el futuro?", 1),
        ("¿Cuándo te imaginas que vas a estar más en paz con quien sos?", 1),
        ("¿Cuál es la cosa del pasado que querés que vuelva en el futuro?", 1),
        ("¿Qué tipo de persona querés ser dentro de 20 años?", 1),
        ("¿Cuál es la aventura más grande que aún no te animaste a planear?", 1),
        ("¿Cuándo te imaginas que vas a vivir el mejor año de tu vida?", 1),
        ("¿Cuánto querés que haya cambiado tu economía en 10 años?", 1),
        ("¿Cuándo fue la última vez que te imaginaste en un futuro completamente diferente y te gustó?", 2),
        ("¿Qué sabés que tenés que hacer ahora para que tu futuro sea mejor?", 2),
        ("¿Cuánto de tu futuro está limitado por decisiones que ya tomaste?", 2),
        ("¿Cuándo fue la última vez que imaginaste algo grande para vos y te lo creíste?", 2),
        ("¿Cuánto de tu futuro soñado es alcanzable si empezás hoy?", 2),
        ("¿Cuándo fue la última vez que soltaste un plan del futuro y te alivió?", 2),
        ("¿Cuándo fue la última vez que el futuro te generó más emoción que miedo?", 2),
        ("¿Cuándo fue la última vez que hiciste algo hoy pensando en quién querés ser en el futuro?", 3),
        ("¿Cuánto de tu felicidad futura depende de lo que hagas o dejes de hacer hoy?", 3),
        ("¿Cuándo fue la última vez que te comprometiste de verdad con la persona que querés ser?", 3),
    ],

    "amor": [
        ("¿Cuándo fue la primera vez que alguien te hizo reír cuando estabas triste?", 1),
        ("¿Cuándo fue la primera vez que sentiste que alguien te elegía a vos entre muchas opciones?", 1),
        ("¿Cuándo fue la última vez que mandaste un mensaje largo de amor?", 1),
        ("¿Cuándo fue la última vez que saliste de tu zona de confort por alguien que te gustaba?", 1),
        ("¿Cuándo fue la primera vez que alguien te hizo ver el mundo diferente?", 1),
        ("¿Cuándo fue la última vez que escuchaste una canción y pensaste en alguien?", 1),
        ("¿Cuándo fue la primera vez que sentiste que el corazón te latía diferente por alguien?", 1),
        ("¿Cuándo fue la última vez que alguien te dijo algo que siempre va a quedar?", 1),
        ("¿Cuándo fue la última vez que te animaste a decirle a alguien lo que sentías?", 1),
        ("¿Cuándo fue la última vez que el amor te hizo mejor persona?", 1),
        ("¿Cuándo fue la última vez que tuviste miedo de perder a alguien que amás?", 2),
        ("¿Cuándo fue la última vez que el amor te costó más de lo que imaginabas?", 2),
        ("¿Cuándo fue la última vez que alguien te amó de una manera que no sabías que necesitabas?", 2),
        ("¿Cuándo fue la última vez que el amor te hizo más pequeño de lo que querías?", 2),
        ("¿Cuándo fue la última vez que sentiste que eras querido por quien sos, no por lo que hacés?", 2),
        ("¿Cuándo fue la última vez que el amor te reveló algo que no sabías de vos?", 2),
        ("¿Cuándo fue la última vez que el amor te dio el coraje que necesitabas?", 2),
        ("¿Cuándo fue la última vez que sentiste que amabas de manera completamente libre?", 3),
        ("¿Cuál es la cosa que más cambia en vos cuando amás de verdad?", 3),
        ("¿Cuándo fue la última vez que el amor fue más grande que tu miedo?", 3),
    ],

    "familia": [
        ("¿Cuándo fue la última vez que tu familia te demostró que te conocía mejor de lo que creías?", 1),
        ("¿Cuándo fue la última vez que alguien de tu familia te escuchó de verdad?", 1),
        ("¿Cuándo fue la última vez que tu familia te hizo sentir en casa sin importar dónde estabas?", 1),
        ("¿Cuándo fue la última vez que tu familia te enseñó algo que no esperabas aprender?", 1),
        ("¿Cuándo fue la última vez que alguien de tu familia te hizo reír cuando más lo necesitabas?", 1),
        ("¿Cuándo fue la última vez que te sentiste orgulloso de ser parte de tu familia?", 1),
        ("¿Cuándo fue la última vez que alguien de tu familia cambió y te alegraste?", 1),
        ("¿Cuándo fue la última vez que tu familia te apoyó en algo que les costaba entender?", 1),
        ("¿Cuándo fue la última vez que un familiar te dijo algo que cambiaste internamente?", 1),
        ("¿Cuándo fue la última vez que tu familia fue tu mayor fuente de fuerza?", 1),
        ("¿Cuándo fue la última vez que sentiste que tu familia no te conocía del todo?", 2),
        ("¿Cuándo fue la última vez que tu familia tomó una decisión que te afectó sin consultarte?", 2),
        ("¿Cuándo fue la última vez que te costó ser parte de tu familia?", 2),
        ("¿Cuándo fue la última vez que tu familia te pidió algo que no podías dar?", 2),
        ("¿Cuándo fue la última vez que sentiste que necesitabas distancia de tu familia?", 2),
        ("¿Cuándo fue la última vez que tu familia cambió algo en cómo te ves a vos mismo?", 2),
        ("¿Cuándo fue la última vez que alguien de tu familia te sorprendió positivamente cuando menos lo esperabas?", 2),
        ("¿Cuándo fue la última vez que sentiste que tu familia era tu mayor ancla?", 3),
        ("¿Cuándo fue la última vez que elegiste a tu familia a pesar de todo lo que había pasado?", 3),
        ("¿Cuál es la cosa de tu familia que más te costó aceptar y que finalmente aceptaste?", 3),
    ],

    "amistades": [
        ("¿Cuándo fue la última vez que un amigo apareció exactamente cuando lo necesitabas?", 1),
        ("¿Cuándo fue la última vez que te juntaste con alguien sin planificarlo y fue increíble?", 1),
        ("¿Cuándo fue la última vez que le dijiste a un amigo algo que le cambió el día?", 1),
        ("¿Cuándo fue la última vez que te reíste hasta que te dolió el estómago con un amigo?", 1),
        ("¿Cuándo fue la última vez que hiciste algo nuevo porque un amigo te lo propuso?", 1),
        ("¿Cuándo fue la última vez que un amigo te dio un consejo que nadie más te daría?", 1),
        ("¿Cuándo fue la última vez que pasaste horas con un amigo y no te diste cuenta del tiempo?", 1),
        ("¿Cuándo fue la última vez que un amigo creyó en vos cuando vos no lo hacías?", 1),
        ("¿Cuándo fue la última vez que hiciste algo solo para que un amigo estuviera feliz?", 1),
        ("¿Cuándo fue la última vez que un amigo te conoció mejor que vos mismo en ese momento?", 1),
        ("¿Cuándo fue la última vez que sentiste que una amistad te exigía demasiado?", 2),
        ("¿Cuándo fue la última vez que alguien que llamabas amigo no estuvo cuando lo necesitabas?", 2),
        ("¿Cuándo fue la última vez que tuviste que elegir entre tu bienestar y una amistad?", 2),
        ("¿Cuándo fue la última vez que le perdonaste a un amigo algo que con otros no perdonarías?", 2),
        ("¿Cuándo fue la última vez que una amistad te cambió de manera que no esperabas?", 2),
        ("¿Cuándo fue la última vez que dejaste de ver a un amigo y lo extrañaste de verdad?", 2),
        ("¿Cuándo fue la última vez que una amistad te dio más de lo que pusiste?", 2),
        ("¿Cuándo fue la última vez que una amistad te hizo mejor persona?", 3),
        ("¿Cuál es la amistad que más te costó y que más valor le das precisamente por eso?", 3),
        ("¿Cuándo fue la última vez que una amistad te dio el coraje de hacer algo difícil?", 3),
    ],

    "exs": [
        ("¿Cuándo fue la última vez que encontraste algo de un ex y sonreíste?", 1),
        ("¿Cuándo fue la primera vez que saliste con alguien y supiste desde el principio que no iba a durar?", 1),
        ("¿Cuándo fue la última vez que alguien del pasado amoroso te mandó un mensaje inesperado?", 1),
        ("¿Cuándo fue la primera vez que te gustó alguien de un grupo de amigos y cambiaste la dinámica?", 1),
        ("¿Cuándo fue la primera vez que estuviste con alguien que ya tenía pareja?", 1),
        ("¿Cuándo fue la primera vez que te dijeron que eras demasiado para alguien?", 1),
        ("¿Cuándo fue la primera vez que alguien que te gustaba no te correspondió?", 1),
        ("¿Cuándo fue la última vez que actuaste de manera que hoy te sorprendería en una relación?", 1),
        ("¿Cuándo fue la primera vez que elegiste salir de una situación en la que no te valoraban?", 1),
        ("¿Cuándo fue la última vez que dejaste de querer saber de alguien del pasado?", 1),
        ("¿Cuándo fue la última vez que te preguntaste si tomaste la decisión correcta en una ruptura?", 2),
        ("¿Cuándo fue la última vez que entendiste una relación pasada de manera completamente diferente?", 2),
        ("¿Cuándo fue la última vez que perdonaste algo de una relación pasada que creías imperdonable?", 2),
        ("¿Cuándo fue la última vez que reconociste que una relación te hizo crecer aunque dolió?", 2),
        ("¿Cuándo fue la última vez que tomaste conciencia de algo que repetís en el amor?", 2),
        ("¿Cuándo fue la última vez que elegiste no repetir algo de una relación pasada y te costó?", 2),
        ("¿Cuándo fue la última vez que el amor del pasado te dio fuerza para algo del presente?", 2),
        ("¿Cuál fue la relación que más te enseñó sobre lo que realmente necesitás en el amor?", 3),
        ("¿Cuándo fue la última vez que una relación pasada te ayudó a entender quién sos hoy?", 3),
        ("¿Cuándo fue la última vez que decidiste amarte más de lo que te amaba alguien más?", 3),
    ],

    "personalidad": [
        ("¿Cuándo fue la última vez que dijiste exactamente lo que pensabas sin filtro?", 1),
        ("¿Cuándo fue la última vez que hiciste algo completamente diferente a lo que se esperaba de vos?", 1),
        ("¿Cuándo fue la última vez que pediste perdón de corazón?", 1),
        ("¿Cuándo fue la última vez que te sorprendiste siendo más paciente de lo habitual?", 1),
        ("¿Cuándo fue la última vez que hiciste algo sin pensar en las consecuencias?", 1),
        ("¿Cuándo fue la última vez que te dejaste llevar completamente?", 1),
        ("¿Cuándo fue la última vez que hiciste algo que alguien más habría hecho mejor pero igual lo hiciste vos?", 1),
        ("¿Cuándo fue la última vez que te sorprendiste a vos mismo con algo que sentiste?", 1),
        ("¿Cuándo fue la última vez que hiciste algo solo porque te daba curiosidad, sin ningún otro motivo?", 1),
        ("¿Cuándo fue la última vez que elegiste incomodarte para hacer crecer a alguien?", 1),
        ("¿Cuándo fue la última vez que alguien te confrontó y tenía razón?", 2),
        ("¿Cuándo fue la última vez que viste algo tuyo que no te gustó y lo cambiaste?", 2),
        ("¿Cuándo fue la última vez que elegiste la honestidad sobre la comodidad?", 2),
        ("¿Cuándo fue la última vez que te diste cuenta de que estabas evitando algo?", 2),
        ("¿Cuándo fue la última vez que actuaste desde la generosidad pura?", 2),
        ("¿Cuándo fue la última vez que algo que querías resultó ser algo que no necesitabas?", 2),
        ("¿Cuándo fue la última vez que priorizaste tu salud mental sobre cualquier otra cosa?", 2),
        ("¿Cuándo fue la última vez que sentiste que eras completamente la persona que querías ser?", 3),
        ("¿Cuándo fue la última vez que elegiste el crecimiento sobre la comodidad?", 3),
        ("¿Cuál es la cosa de vos mismo que más costó trabajo aceptar y que ahora amas?", 3),
    ],

    "miedos": [
        ("¿Cuándo fue la última vez que le pusiste cara a un miedo vago?", 1),
        ("¿Cuándo fue la última vez que el miedo te unió a alguien de manera inesperada?", 1),
        ("¿Cuándo fue la última vez que algo que te daba miedo resultó ser completamente inofensivo?", 1),
        ("¿Cuándo fue la última vez que le contaste a alguien un miedo que tenías?", 1),
        ("¿Cuándo fue la última vez que el miedo te hizo pensar más antes de actuar?", 1),
        ("¿Cuándo fue la última vez que algo que parecía aterrador resultó ser una aventura?", 1),
        ("¿Cuándo fue la última vez que transformaste un miedo en curiosidad?", 1),
        ("¿Cuándo fue la última vez que el miedo te pidió algo que valía la pena escuchar?", 1),
        ("¿Cuándo fue la última vez que el miedo te enseñó algo sobre lo que valorás?", 1),
        ("¿Cuándo fue la última vez que el miedo se convirtió en motivación?", 1),
        ("¿Cuándo fue la última vez que un miedo te dio información útil?", 2),
        ("¿Cuándo fue la última vez que el miedo al fracaso fue más grande que el deseo de intentarlo?", 2),
        ("¿Cuándo fue la última vez que el miedo te hizo una pregunta que no tenías respuesta?", 2),
        ("¿Cuándo fue la última vez que el miedo te puso en contacto con algo que importaba?", 2),
        ("¿Cuándo fue la última vez que el miedo te mostró un límite que no sabías que tenías?", 2),
        ("¿Cuándo fue la última vez que el miedo fue más fácil de cargar porque lo compartiste?", 2),
        ("¿Cuándo fue la última vez que el miedo te hizo más humano?", 2),
        ("¿Cuándo fue la última vez que le agradeciste a un miedo algo que te enseñó?", 3),
        ("¿Cuándo fue la última vez que elegiste moverte hacia lo que te daba miedo?", 3),
        ("¿Cuándo fue la última vez que el miedo te mostró quién sos cuando no hay otra opción?", 3),
    ],

    "logros": [
        ("¿Cuándo fue la última vez que algo que hiciste ayudó a alguien sin que lo supieras?", 1),
        ("¿Cuándo fue la última vez que te animaste a intentar algo que hacía tiempo tenías pendiente?", 1),
        ("¿Cuándo fue la última vez que alguien te dijo que lo que hacías marcaba una diferencia?", 1),
        ("¿Cuándo fue la última vez que aprendiste algo de un fracaso más de lo que esperabas?", 1),
        ("¿Cuándo fue la última vez que algo que hiciste tuvo un resultado inesperadamente bueno?", 1),
        ("¿Cuándo fue la última vez que te sentiste útil de una manera profunda?", 1),
        ("¿Cuándo fue la última vez que terminaste algo que parecía imposible al principio?", 1),
        ("¿Cuándo fue la última vez que te sorprendiste siendo capaz de más de lo que creías?", 1),
        ("¿Cuándo fue la última vez que un logro tuyo unió a gente que querés?", 1),
        ("¿Cuándo fue la última vez que hiciste algo que importaba, aunque nadie lo viera?", 1),
        ("¿Cuándo fue la última vez que reconociste que un fracaso fue necesario?", 2),
        ("¿Cuándo fue la última vez que le diste crédito a alguien que te ayudó a lograr algo?", 2),
        ("¿Cuándo fue la última vez que valoraste más el proceso que el resultado?", 2),
        ("¿Cuándo fue la última vez que algo que lograste cambió cómo te relacionabas con el fracaso?", 2),
        ("¿Cuándo fue la última vez que algo que hiciste te acercó más a la persona que querés ser?", 2),
        ("¿Cuándo fue la última vez que lograste algo que cambiaste completamente de perspectiva?", 2),
        ("¿Cuándo fue la última vez que un logro te hizo sentir que todo valía la pena?", 2),
        ("¿Cuándo fue la última vez que lo que lograste te hizo más humilde?", 3),
        ("¿Cuándo fue la última vez que un logro te liberó de algo que te pesaba?", 3),
        ("¿Cuándo fue la última vez que elegiste no lograr algo para preservar algo más importante?", 3),
    ],

    "sinFiltro": [
        ("¿Cuántas veces al mes te quedás dormido viendo algo que no querías ver?", 1),
        ("¿Cuántas veces tomaste una decisión importante en base a un horóscopo o algo similar?", 1),
        ("¿Cuántas veces dijiste que te gustaba algo que en realidad no te gustaba?", 1),
        ("¿Cuántas veces al mes comprás algo que no necesitás para sentirte mejor?", 1),
        ("¿Cuántas veces dejaste una conversación difícil para 'mañana' y ese mañana nunca llegó?", 1),
        ("¿Cuántas veces al año fingiste que algo no te afectó cuando sí lo hizo?", 1),
        ("¿Cuántas veces te fuiste de algo antes de que terminara?", 1),
        ("¿Cuántas veces revisaste el estado de tus chats cuando debías estar durmiendo?", 1),
        ("¿Cuántas veces dijiste 'estoy bien' cuando en realidad no lo estabas?", 1),
        ("¿Cuántas veces al mes hacés algo que no contarías ni a tu mejor amigo?", 1),
        ("¿Cuándo fue la última vez que dijiste algo con la intención de provocar y lo lograste?", 2),
        ("¿Cuándo fue la última vez que actuaste de manera completamente egoísta y no te importó?", 2),
        ("¿Cuándo fue la última vez que usaste información privilegiada para salir favorecido?", 2),
        ("¿Cuándo fue la última vez que te alegraste de algo malo que le pasó a alguien?", 2),
        ("¿Cuándo fue la última vez que hiciste trampa en algo y nadie lo supo?", 2),
        ("¿Cuándo fue la última vez que manipulaste una situación para salir primero?", 2),
        ("¿Cuándo fue la última vez que dijiste algo sabiendo que iba a herir y lo dijiste igual?", 2),
        ("¿Cuál es la cosa que más te daría vergüenza que leyeran en tu historial de búsquedas?", 3),
        ("¿Cuándo fue la última vez que hiciste algo completamente inapropiado y lo disfrutaste?", 3),
        ("¿Cuál es la verdad que llevarías a la tumba si no fuera por este juego?", 3),
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
        if cat_id not in ADDITIONS10:
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

        for (text, level) in ADDITIONS10[cat_id]:
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
