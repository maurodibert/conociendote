#!/usr/bin/env python3
"""Batch 9 - hypotheticals, philosophy, culture, values, world view."""
import json

ADDITIONS9 = {
    "infancia": [
        ("¿Cuál fue la primera vez que alguien te dijo 'no' y fue lo mejor que te podía pasar?", 1),
        ("¿Tenías algún ritual de suerte antes de algo importante en la escuela?", 1),
        ("¿Cuándo fue la primera vez que te diste cuenta de que eras bueno en algo?", 1),
        ("¿Cuál fue el nombre que le pusiste a algún juguete o peluche?", 1),
        ("¿Cuándo fue la primera vez que viajaste sin tus padres?", 1),
        ("¿Cuántos resfríos fingiste para no ir a la escuela?", 1),
        ("¿Cuál fue la primera vez que participaste en una obra de teatro o acto escolar?", 1),
        ("¿Cuándo fue la primera vez que viste a alguien que admiras en persona?", 1),
        ("¿Cuál era el lugar al que siempre querías ir y nunca podías?", 1),
        ("¿Cuál fue tu primer trabajo o tarea por la que recibiste dinero?", 1),
        ("¿Cómo era la relación de tus padres cuando eras chico? ¿Discutían mucho?", 2),
        ("¿Cuál fue el momento en que dejaste de creer en la magia o en los personajes fantásticos?", 2),
        ("¿Cuándo fue la primera vez que ayudaste a alguien en serio?", 2),
        ("¿Cuál fue la primera vez que te diste cuenta de que la vida no era justa?", 2),
        ("¿Cuándo fue la primera vez que tuviste que cuidar a alguien?", 2),
        ("¿Cuándo fue la primera vez que te enamoraste y qué pasó?", 2),
        ("¿Cuándo fue la primera vez que hiciste algo malo y no te castigaron?", 2),
        ("¿Cuándo te diste cuenta de que crecer tenía un costo?", 3),
        ("¿Hay algo de tu infancia que te molesta haber perdido?", 3),
        ("¿Qué parte de tu niñez extrañás cuando más te cuesta la vida adulta?", 3),
    ],

    "futuro": [
        ("¿Si pudieras vivir en cualquier época histórica, cuál elegiría y por qué?", 1),
        ("¿Cuál es la tecnología del futuro que más te asusta?", 1),
        ("¿Cuál es la tecnología del futuro que más te emociona?", 1),
        ("¿En qué país del mundo vivirías si pudieras elegir mañana?", 1),
        ("¿Cómo querés pasar el último día de tu vida si pudieras elegirlo?", 1),
        ("¿Qué harías si supieras que en 10 años el mundo cambia completamente?", 1),
        ("¿Cuánto querés que cambie tu cuerpo en los próximos 10 años?", 1),
        ("¿Cuál sería tu plan para los próximos 6 meses si todo fuera posible?", 1),
        ("¿Cuánto querés parecerte a la persona que eras hace 5 años en el futuro?", 1),
        ("¿Cuál es el miedo al futuro que más trabajo te cuesta transformar?", 1),
        ("¿Qué área de tu vida más necesita un cambio profundo pronto?", 2),
        ("¿Cuándo fue la última vez que te imaginaste fallando en algo y te preparaste igual?", 2),
        ("¿Cuánto de tu futuro está ya decidido y cuánto todavía podés moldear?", 2),
        ("¿Cuándo fue la última vez que te animaste a pedir lo que necesitás para avanzar?", 2),
        ("¿Hay algún rol o papel en tu comunidad que te gustaría jugar en el futuro?", 2),
        ("¿Cuánto de tu futuro te da miedo y cuánto te entusiasma?", 2),
        ("¿Cuándo fue la última vez que realmente te imaginaste viejo y lo aceptaste?", 2),
        ("¿Cuál es el mayor regalo que podrías darle al vos del futuro hoy?", 3),
        ("¿Cuándo fue la última vez que sentiste que el futuro valía la pena?", 3),
        ("¿Cuánto de tu futuro ideal depende de que primero sueltes algo del pasado?", 3),
    ],

    "amor": [
        ("¿Cuándo fue la primera vez que alguien te miró de una manera que te cambió?", 1),
        ("¿Cuánto importa el humor de alguien para que te guste?", 1),
        ("¿Cuándo fue la última vez que fuiste vos quien empezó algo romántico?", 1),
        ("¿Cuándo fue la última vez que alguien te cortejó y te gustó?", 1),
        ("¿Cuál es la cosa más honesta que le dijiste a alguien que te gustaba?", 1),
        ("¿Cuánto tiempo antes de conocer a alguien ya te imaginabas su personalidad?", 1),
        ("¿Cuándo fue la última vez que te enamoraste de alguien que no esperabas?", 1),
        ("¿Cuánto importa el olor de alguien en tu atracción hacia él o ella?", 1),
        ("¿Cuándo fue la última vez que alguien te hizo sonreír sin decir nada?", 1),
        ("¿Cuándo fue la última vez que hiciste algo loco por amor o por que alguien te gustaba?", 1),
        ("¿Cuándo fue la última vez que dejaste entrar a alguien más de lo que esperabas?", 2),
        ("¿Cuánto de lo que sentís en una relación te lo guardás para vos?", 2),
        ("¿Cuándo fue la última vez que te sorprendiste sintiendo algo por alguien que no esperabas?", 2),
        ("¿Cuándo fue la última vez que alguien te hizo sentir verdaderamente especial?", 2),
        ("¿Cuánto importa el pasado de alguien en tu disposición a amarlo?", 2),
        ("¿Cuándo fue la última vez que confiaste completamente en alguien?", 2),
        ("¿Cuándo fue la última vez que el amor fue más fácil de lo que esperabas?", 2),
        ("¿Cuándo fue la última vez que amaste a alguien desde la libertad total?", 3),
        ("¿Cuál es la cosa que más necesitás de una pareja que nunca pediste directamente?", 3),
        ("¿Cuándo fue la última vez que el amor te hizo más vos mismo?", 3),
    ],

    "familia": [
        ("¿Cuándo fue la última vez que le preguntaste a un familiar sobre su vida antes de que vos nacieras?", 1),
        ("¿Cuántos secretos de tu familia no sabrás nunca?", 1),
        ("¿Cuándo fue la última vez que tu familia te sorprendió con su amor?", 1),
        ("¿Cuándo fue la última vez que entendiste a uno de tus padres de una manera completamente nueva?", 1),
        ("¿Cuándo fue la última vez que tu familia se rió de algo juntos de corazón?", 1),
        ("¿Cuándo fue la última vez que alguien de tu familia te dijo algo que te transformó?", 1),
        ("¿Cuándo fue la última vez que un familiar te pidió perdón?", 1),
        ("¿Cuándo fue la última vez que fuiste vos el que necesitó a su familia?", 1),
        ("¿Cuándo fue la última vez que te sentiste completamente seguro dentro de tu familia?", 1),
        ("¿Cuándo fue la última vez que defendiste a un familiar frente a alguien?", 1),
        ("¿Cuándo fue la última vez que alguien de tu familia cambió algo de cómo te ves?", 2),
        ("¿Cuándo fue la última vez que te diste cuenta de que repetías algo de tus padres?", 2),
        ("¿Cuándo fue la última vez que tu familia tuvo que adaptarse a algo nuevo?", 2),
        ("¿Cuándo fue la última vez que extrañaste a alguien de tu familia con toda fuerza?", 2),
        ("¿Cuándo fue la última vez que tu familia te conoció mejor de lo que esperabas?", 2),
        ("¿Cuándo fue la última vez que te perdonaste por algo que le hiciste a un familiar?", 2),
        ("¿Cuándo fue la última vez que pusiste a tu familia por encima de vos mismo?", 2),
        ("¿Cuándo fue la última vez que sentiste que tu familia te amaba incondicionalmente?", 3),
        ("¿Hay algo que necesitabas escuchar de un familiar y que nunca llegaste a escuchar?", 3),
        ("¿Cuándo fue la última vez que elegiste a tu familia a pesar de todo?", 3),
    ],

    "amistades": [
        ("¿Cuándo fue la última vez que llamaste a un amigo solo para saber cómo estaba?", 1),
        ("¿Cuándo fue la última vez que un amigo te ayudó con algo que no le pediste?", 1),
        ("¿Cuándo fue la última vez que hiciste algo por un amigo sin esperar nada a cambio?", 1),
        ("¿Cuándo fue la última vez que le dijiste a un amigo que te importa?", 1),
        ("¿Cuándo fue la última vez que un amigo te hizo algo que no olvidarás?", 1),
        ("¿Cuándo fue la última vez que reíste de algo que solo vos y un amigo entienden?", 1),
        ("¿Cuándo fue la última vez que un amigo te dijo algo que necesitabas escuchar?", 1),
        ("¿Cuándo fue la última vez que conociste a alguien y sentiste que ya lo conocías?", 1),
        ("¿Cuándo fue la última vez que estuviste presente de verdad para un amigo?", 1),
        ("¿Cuándo fue la última vez que un amigo te salvó de algo sin saber que lo hacía?", 1),
        ("¿Cuándo fue la última vez que sentiste que tenías que dejar ir una amistad?", 2),
        ("¿Cuándo fue la última vez que un amigo te decepcionó y lo perdonaste igual?", 2),
        ("¿Cuándo fue la última vez que reconociste que tú eras el problema en una amistad?", 2),
        ("¿Cuándo fue la última vez que una amistad te costó más de lo que te dio?", 2),
        ("¿Cuándo fue la última vez que hiciste algo por un amigo que no era fácil para vos?", 2),
        ("¿Cuándo fue la última vez que dejaste de actuar frente a un amigo?", 2),
        ("¿Cuándo fue la última vez que una amistad te cambió profundamente?", 2),
        ("¿Cuándo fue la última vez que una amistad te hizo más libre?", 3),
        ("¿Cuál es la amistad que más te costó mantener y por qué valió la pena?", 3),
        ("¿Cuándo fue la última vez que un amigo te conoció mejor de lo que te conocés vos?", 3),
    ],

    "exs": [
        ("¿Cuándo fue la primera vez que saliste con alguien completamente diferente a vos?", 1),
        ("¿Cuándo fue la primera vez que te gustó alguien y no hiciste nada al respecto?", 1),
        ("¿Cuándo fue la última vez que pensaste en alguien con quien saliste brevemente?", 1),
        ("¿Hay alguna relación de la que te arrepentiste de haber salido corriendo?", 1),
        ("¿Cuándo fue la última vez que hablaste bien de un ex con quien terminó mal?", 1),
        ("¿Cuándo fue la última vez que le deseaste genuinamente el bien a alguien con quien terminaste?", 1),
        ("¿Cuándo fue la primera vez que terminaste algo sabiendo que era lo mejor aunque doliera?", 1),
        ("¿Cuándo fue la última vez que una canción te recordó a alguien del pasado?", 1),
        ("¿Cuándo fue la última vez que te imaginaste cómo hubiera sido si algo pasado hubiera resultado diferente?", 1),
        ("¿Cuándo fue la primera vez que te animaste a empezar algo nuevo después de una ruptura?", 1),
        ("¿Cuándo fue la última vez que elegiste no repetir un error amoroso del pasado?", 2),
        ("¿Cuándo fue la última vez que reconociste tu parte en una ruptura?", 2),
        ("¿Cuándo fue la última vez que alguien del pasado amoroso te enseñó algo nuevo sobre vos?", 2),
        ("¿Cuándo fue la última vez que perdonaste de verdad a alguien que te lastimó?", 2),
        ("¿Cuándo fue la última vez que dejaste ir algo del pasado que te pesaba?", 2),
        ("¿Cuándo fue la última vez que te diste cuenta de que ya superaste algo que creías imposible de superar?", 2),
        ("¿Cuándo fue la última vez que amaste sin miedo a que terminara?", 2),
        ("¿Cuál es la cosa que más te costó aceptar de vos mismo en el amor?", 3),
        ("¿Cuándo fue la última vez que sentiste que estabas completamente libre de tu pasado amoroso?", 3),
        ("¿Qué necesitás sanar en vos mismo para poder amar completamente?", 3),
    ],

    "personalidad": [
        ("¿Cuándo fue la última vez que te sorprendiste a vos mismo siendo generoso?", 1),
        ("¿Cuándo fue la última vez que priorizaste tu bienestar sin culpa?", 1),
        ("¿Cuándo fue la última vez que hiciste algo solo porque te hacía feliz a vos?", 1),
        ("¿Cuándo fue la última vez que te reíste de algo de vos mismo?", 1),
        ("¿Cuándo fue la última vez que hiciste algo que te salió bien a la primera?", 1),
        ("¿Cuándo fue la última vez que alguien te agradeció algo inesperadamente?", 1),
        ("¿Cuándo fue la última vez que cambiaste de opinión sobre algo importante?", 1),
        ("¿Cuándo fue la última vez que te permitiste estar sin hacer nada?", 1),
        ("¿Cuándo fue la última vez que te sentiste completamente en paz?", 1),
        ("¿Cuándo fue la última vez que hiciste algo por alguien sin que te lo pidieran?", 1),
        ("¿Cuándo fue la última vez que una conversación cambió algo en cómo te ves?", 2),
        ("¿Cuándo fue la última vez que hiciste algo que te daba vergüenza y lo hiciste igual?", 2),
        ("¿Cuándo fue la última vez que te diste el permiso de no saber qué hacer?", 2),
        ("¿Cuándo fue la última vez que fuiste completamente honesto con alguien sobre cómo te sentías?", 2),
        ("¿Cuándo fue la última vez que dejaste de pretender que todo estaba bien?", 2),
        ("¿Cuándo fue la última vez que te animaste a pedir lo que necesitabas?", 2),
        ("¿Cuándo fue la última vez que cambiaste algo de vos mismo que te costaba admitir que necesitabas cambiar?", 2),
        ("¿Cuándo fue la última vez que te sentiste completamente auténtico?", 3),
        ("¿Cuál es la parte de vos mismo que más querés que los demás vean?", 3),
        ("¿Cuándo fue la última vez que te eligiste completamente a vos mismo?", 3),
    ],

    "miedos": [
        ("¿Cuándo fue la última vez que un miedo te enseñó algo sobre quién sos?", 1),
        ("¿Cuál es el tipo de conversación que más evitás?", 1),
        ("¿Le tenés miedo al cambio de opiniones de la gente que te importa?", 1),
        ("¿Cuándo fue la última vez que el miedo te hizo más cuidadoso de manera positiva?", 1),
        ("¿Cuándo fue la última vez que superaste un miedo que creías permanente?", 1),
        ("¿Cuándo fue la última vez que el miedo te unió a alguien?", 1),
        ("¿Cuándo fue la última vez que el miedo fue tu mayor fuente de aprendizaje?", 1),
        ("¿Cuándo fue la última vez que el miedo te hizo actuar con más cuidado?", 1),
        ("¿Cuándo fue la última vez que reconociste un miedo que tenías sin saber?", 1),
        ("¿Cuándo fue la última vez que te reíste de algo que antes te daba miedo?", 1),
        ("¿Cuándo fue la última vez que el miedo al juicio te hizo callar algo importante?", 2),
        ("¿Cuándo fue la última vez que un miedo te impidió crecer?", 2),
        ("¿Cuándo fue la última vez que decidiste ignorar un miedo y funcionó?", 2),
        ("¿Cuándo fue la última vez que hablaste de tus miedos con alguien que te comprendió?", 2),
        ("¿Cuándo fue la última vez que el miedo te unió a alguien de manera inesperada?", 2),
        ("¿Cuándo fue la última vez que te diste cuenta de que un miedo estaba moldeando tu vida?", 2),
        ("¿Cuándo fue la última vez que pusiste a prueba un miedo y sobreviviste?", 2),
        ("¿Cuál es el miedo que más te acerca a quien realmente sos cuando lo enfrentás?", 3),
        ("¿Cuándo fue la última vez que el miedo te enseñó algo que el éxito nunca hubiera podido?", 3),
        ("¿Cuándo fue la última vez que elegiste la valentía sobre la seguridad?", 3),
    ],

    "logros": [
        ("¿Cuándo fue la última vez que hiciste algo que te parecía inalcanzable?", 1),
        ("¿Cuándo fue la última vez que ayudaste a alguien a lograr algo?", 1),
        ("¿Cuándo fue la última vez que algo que lograste ayudó a alguien más?", 1),
        ("¿Cuándo fue la última vez que lograste algo sin que nadie lo esperara?", 1),
        ("¿Cuándo fue la última vez que te animaste a intentar algo sin garantías?", 1),
        ("¿Cuándo fue la última vez que recibiste reconocimiento que no esperabas?", 1),
        ("¿Cuándo fue la última vez que completaste algo que parecía imposible al principio?", 1),
        ("¿Cuándo fue la última vez que un logro te sorprendió a vos mismo?", 1),
        ("¿Cuándo fue la última vez que lo que lograste fue mejor de lo que habías planeado?", 1),
        ("¿Cuándo fue la última vez que te felicitaste de corazón?", 1),
        ("¿Cuándo fue la última vez que un logro tuyo inspiró a alguien?", 2),
        ("¿Cuándo fue la última vez que algo que intentaste no funcionó y lo intentaste de nuevo?", 2),
        ("¿Cuándo fue la última vez que reconociste el logro de alguien que no te caía bien?", 2),
        ("¿Cuándo fue la última vez que hiciste algo que valió más por el proceso que por el resultado?", 2),
        ("¿Cuándo fue la última vez que perdonaste a alguien que no te apoyó en un logro tuyo?", 2),
        ("¿Cuándo fue la última vez que reconociste que sin ayuda no lo hubieras logrado?", 2),
        ("¿Cuándo fue la última vez que lo que lograste cambió algo dentro de vos?", 2),
        ("¿Cuál fue el logro que más te costó creer que merecías?", 3),
        ("¿Cuándo fue la última vez que algo que lograste te llenó de verdad?", 3),
        ("¿Cuándo fue la última vez que elegiste fallar dignamente en lugar de no intentarlo?", 3),
    ],

    "sinFiltro": [
        ("¿Cuándo fue la última vez que revisaste el perfil de alguien que no debías estar revisando?", 1),
        ("¿Cuántas veces por semana llegás tarde a algo sin una buena razón?", 1),
        ("¿Cuál fue la cosa más extraña que alguien te mandó por mensaje?", 1),
        ("¿Cuántas veces lloraste con algo que no debería hacerte llorar?", 1),
        ("¿Cuándo fue la última vez que le mentiste a alguien sobre dónde estabas?", 1),
        ("¿Cuántas veces viste algo que no te gustó en el teléfono de alguien?", 1),
        ("¿Cuándo fue la última vez que usaste 'se me fue la batería' como excusa?", 1),
        ("¿Cuántas veces fingiste escuchar a alguien mientras pensabas en otra cosa?", 1),
        ("¿Cuál es la cosa más ridícula que hiciste cuando estabas aburrido?", 1),
        ("¿Cuándo fue la última vez que comiste algo que encontraste en el fondo de la cartera o mochila?", 1),
        ("¿Cuándo fue la última vez que actuaste desde los celos y lo reconociste?", 2),
        ("¿Cuántas veces al mes decís algo para quedar bien que no creés?", 2),
        ("¿Cuándo fue la última vez que te beneficiaste de algo que no te correspondía?", 2),
        ("¿Cuántas veces te prometiste empezar algo el lunes y no lo hiciste?", 2),
        ("¿Cuándo fue la última vez que hablaste mal de alguien que tenías enfrente?", 2),
        ("¿Cuántas veces al mes actuás desde la envidia aunque no lo admitás?", 2),
        ("¿Cuándo fue la última vez que hiciste algo que te avergüenza y lo disfrutaste?", 2),
        ("¿Cuál es la cosa más escandalosa que hiciste en un estado de aburrimiento total?", 3),
        ("¿Hay algo que hiciste que, si lo supieran, cambiaría cómo te ven en este grupo?", 3),
        ("¿Cuándo fue la última vez que cruzaste un límite propio y no te arrepentiste?", 3),
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
        if cat_id not in ADDITIONS9:
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

        for (text, level) in ADDITIONS9[cat_id]:
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
