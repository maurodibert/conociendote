#!/usr/bin/env python3
"""Batch 20 - reflection, mindfulness, present moment, gratitude."""
import json

ADDITIONS20 = {
    "infancia": [
        ("¿Qué objeto de tu infancia conservarías si pudieras elegir solo uno?", 1),
        ("¿Cuándo fue la primera vez que algo que veías como normal resultó ser extraordinario?", 1),
        ("¿Cuándo fue la primera vez que te diste cuenta de que alguien te quería sin que lo dijera?", 1),
        ("¿Cuándo fue la primera vez que elegiste quedarte cuando todo te decía que te fueras?", 1),
        ("¿Cuándo fue la primera vez que hiciste algo gracioso sin querer?", 1),
        ("¿Cuándo fue la primera vez que entendiste qué era la soledad de verdad?", 1),
        ("¿Cuándo fue la primera vez que te emocionaste con algo de la naturaleza?", 1),
        ("¿Cuándo fue la primera vez que el mundo te pareció mágico de manera genuina?", 1),
        ("¿Cuándo fue la primera vez que algo cotidiano se convirtió en tu mejor recuerdo?", 1),
        ("¿Cuándo fue la primera vez que algo de lo que dabas por sentado desapareció?", 1),
        ("¿Cuándo fue la primera vez que alguien te pidió perdón y lo entendiste de verdad?", 2),
        ("¿Cuándo fue la primera vez que algo doloroso tuvo sentido mucho después?", 2),
        ("¿Cuándo fue la primera vez que algo que perdiste volvió de una manera diferente?", 2),
        ("¿Cuándo fue la primera vez que elegiste perdonar sin esperar que cambie nada?", 2),
        ("¿Cuándo fue la primera vez que algo que te parecía difícil resultó ser exactamente lo que necesitabas?", 2),
        ("¿Cuándo fue la primera vez que algo de tu infancia que te parecía ordinario resultó ser un tesoro?", 3),
        ("¿Cuándo fue la primera vez que sentiste gratitud por algo que en el momento parecía malo?", 3),
        ("¿Cuándo fue la primera vez que tu infancia te dio algo que ningún adulto te podría dar?", 3),
    ],

    "futuro": [
        ("¿Qué es lo primero que harías si mañana todo cambiara para mejor?", 1),
        ("¿Cuándo fue la última vez que algo del presente fue exactamente la semilla del futuro que querés?", 1),
        ("¿Cuándo fue la última vez que el presente fue suficiente para el futuro que imaginás?", 1),
        ("¿Cuándo fue la última vez que algo que hacías hoy fue exactamente lo que el futuro necesitaba?", 1),
        ("¿Cuándo fue la última vez que algo del presente te hizo sentir que el futuro estaba construyéndose bien?", 1),
        ("¿Cuándo fue la última vez que algo cotidiano fue exactamente la respuesta a una meta del futuro?", 1),
        ("¿Cuándo fue la última vez que algo del presente fue la razón por la que el futuro te importó más?", 1),
        ("¿Cuándo fue la última vez que algo de hoy fue exactamente el punto de inflexión para mañana?", 1),
        ("¿Cuándo fue la última vez que algo del presente fue más valioso de lo que esperabas para el futuro?", 1),
        ("¿Cuándo fue la última vez que el presente fue exactamente el lugar desde el que querías construir el futuro?", 1),
        ("¿Cuándo fue la última vez que algo que no planeabas del futuro fue exactamente lo que necesitabas?", 2),
        ("¿Cuándo fue la última vez que algo que dejaste ir en el presente abrió algo en el futuro?", 2),
        ("¿Cuándo fue la última vez que algo que construiste en silencio fue exactamente la base del futuro?", 2),
        ("¿Cuándo fue la última vez que el presente fue exactamente la preparación para lo que más querés?", 2),
        ("¿Cuándo fue la última vez que algo del presente fue exactamente la promesa del futuro que más querés?", 2),
        ("¿Cuándo fue la última vez que el presente fue tan pleno que el futuro dejó de ser lo único que importaba?", 3),
        ("¿Cuándo fue la última vez que algo del presente fue exactamente el futuro que imaginabas hace años?", 3),
        ("¿Cuándo fue la última vez que el presente fue exactamente el regalo que el futuro te iba a dar?", 3),
    ],

    "amor": [
        ("¿Cuándo fue la última vez que el amor fue exactamente lo que querías sin ningún pero?", 1),
        ("¿Cuándo fue la última vez que algo cotidiano fue exactamente lo más romántico?", 1),
        ("¿Cuándo fue la última vez que el silencio con alguien fue exactamente perfecto?", 1),
        ("¿Cuándo fue la última vez que algo pequeño de alguien fue exactamente lo más grande?", 1),
        ("¿Cuándo fue la última vez que el amor fue más liviano de lo que esperabas?", 1),
        ("¿Cuándo fue la última vez que algo del amor fue exactamente lo que no sabías que necesitabas?", 1),
        ("¿Cuándo fue la última vez que el amor fue exactamente la razón por la que todo tenía sentido?", 1),
        ("¿Cuándo fue la última vez que algo del amor fue exactamente la respuesta que buscabas?", 1),
        ("¿Cuándo fue la última vez que el amor fue exactamente el refugio correcto?", 1),
        ("¿Cuándo fue la última vez que algo del amor fue exactamente más de lo que imaginabas que podía ser?", 1),
        ("¿Cuándo fue la última vez que el amor fue exactamente la razón por la que crecer valió la pena?", 2),
        ("¿Cuándo fue la última vez que el amor fue exactamente la razón por la que seguiste?", 2),
        ("¿Cuándo fue la última vez que el amor fue exactamente la causa de tu mejor versión?", 2),
        ("¿Cuándo fue la última vez que el amor fue exactamente lo que le faltaba a algo?", 2),
        ("¿Cuándo fue la última vez que el amor fue exactamente la diferencia entre lo ordinario y lo extraordinario?", 2),
        ("¿Cuándo fue la última vez que el amor fue exactamente lo que te hizo querer ser mejor?", 3),
        ("¿Cuándo fue la última vez que el amor fue exactamente lo que le dio sentido a todo lo demás?", 3),
        ("¿Cuándo fue la última vez que el amor fue exactamente el por qué de todo?", 3),
    ],

    "familia": [
        ("¿Cuál es el momento familiar más reciente que querés que dure para siempre?", 1),
        ("¿Cuándo fue la última vez que algo de tu familia fue exactamente lo que más necesitabas?", 1),
        ("¿Cuándo fue la última vez que un momento familiar fue exactamente perfecto?", 1),
        ("¿Cuándo fue la última vez que algo de tu familia fue el mejor recuerdo del año?", 1),
        ("¿Cuándo fue la última vez que algo de tu familia fue exactamente el hogar que imaginabas?", 1),
        ("¿Cuándo fue la última vez que algo de tu familia fue exactamente lo que necesitabas escuchar?", 1),
        ("¿Cuándo fue la última vez que algo de tu familia fue exactamente la fuerza que te faltaba?", 1),
        ("¿Cuándo fue la última vez que algo de tu familia fue exactamente la respuesta a algo que te preguntabas?", 1),
        ("¿Cuándo fue la última vez que algo de tu familia fue exactamente el amor que necesitabas?", 1),
        ("¿Cuándo fue la última vez que algo de tu familia fue exactamente el lugar al que querías volver?", 1),
        ("¿Cuándo fue la última vez que tu familia fue exactamente la razón por la que algo difícil fue posible?", 2),
        ("¿Cuándo fue la última vez que tu familia fue exactamente la razón por la que elegiste seguir?", 2),
        ("¿Cuándo fue la última vez que tu familia fue exactamente la razón por la que te perdonaste algo?", 2),
        ("¿Cuándo fue la última vez que tu familia fue exactamente la razón por la que creíste en algo?", 2),
        ("¿Cuándo fue la última vez que tu familia fue exactamente la razón por la que todo valió la pena?", 2),
        ("¿Cuándo fue la última vez que tu familia fue exactamente el ancla correcta?", 3),
        ("¿Cuándo fue la última vez que tu familia fue exactamente la razón por la que todo tuvo sentido?", 3),
        ("¿Cuándo fue la última vez que tu familia fue exactamente el motivo por el que elegiste ser quien sos?", 3),
    ],

    "amistades": [
        ("¿Cuándo fue la última vez que un amigo fue exactamente lo que necesitabas?", 1),
        ("¿Cuándo fue la última vez que algo de una amistad fue exactamente el recuerdo que querés llevarte?", 1),
        ("¿Cuándo fue la última vez que un amigo fue exactamente la persona correcta en el momento correcto?", 1),
        ("¿Cuándo fue la última vez que algo de una amistad fue exactamente lo más valioso del año?", 1),
        ("¿Cuándo fue la última vez que un amigo fue exactamente la razón de algo bueno?", 1),
        ("¿Cuándo fue la última vez que algo de una amistad fue exactamente lo que te faltaba?", 1),
        ("¿Cuándo fue la última vez que un amigo fue exactamente el espejo que necesitabas?", 1),
        ("¿Cuándo fue la última vez que algo de una amistad fue exactamente la alegría que necesitabas?", 1),
        ("¿Cuándo fue la última vez que un amigo fue exactamente la razón por la que el día fue mejor?", 1),
        ("¿Cuándo fue la última vez que algo de una amistad fue exactamente lo más generoso que recibiste?", 1),
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón por la que algo imposible fue posible?", 2),
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón por la que seguiste creyendo?", 2),
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón por la que te animaste a algo?", 2),
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón por la que sos quien sos?", 2),
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón por la que todo valió?", 2),
        ("¿Cuándo fue la última vez que una amistad fue exactamente el amor que más necesitabas?", 3),
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón por la que todo tenía sentido?", 3),
        ("¿Cuándo fue la última vez que una amistad fue exactamente el regalo más inesperado?", 3),
    ],

    "exs": [
        ("¿Cuándo fue la última vez que algo del pasado amoroso fue exactamente la lección más valiosa?", 1),
        ("¿Cuándo fue la última vez que algo del pasado amoroso fue exactamente la razón de algo bueno del presente?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente lo que necesitabas haber vivido?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de algo que sos hoy?", 1),
        ("¿Cuándo fue la última vez que algo de una relación pasada fue exactamente lo que el presente necesitaba?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la base de algo del presente?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que amás mejor ahora?", 1),
        ("¿Cuándo fue la última vez que algo del pasado amoroso fue exactamente el regalo del que no te diste cuenta en el momento?", 1),
        ("¿Cuándo fue la última vez que algo del pasado amoroso fue exactamente la fortaleza del presente?", 1),
        ("¿Cuándo fue la última vez que algo del pasado amoroso fue exactamente la respuesta a algo del presente?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón por la que elegís mejor?", 2),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que confías diferente?", 2),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que amás más libremente?", 2),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que sos más vos?", 2),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que el presente es mejor?", 2),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que podés amar plenamente?", 3),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que el amor actual es más real?", 3),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente el camino correcto hacia donde estás?", 3),
    ],

    "personalidad": [
        ("¿Cuándo fue la última vez que algo de vos fue exactamente lo que alguien necesitaba?", 1),
        ("¿Cuándo fue la última vez que algo tuyo fue exactamente lo que completó algo?", 1),
        ("¿Cuándo fue la última vez que algo de tu manera de ser fue exactamente el regalo correcto?", 1),
        ("¿Cuándo fue la última vez que algo tuyo fue exactamente la diferencia?", 1),
        ("¿Cuándo fue la última vez que algo de vos fue exactamente lo que faltaba en algún lugar?", 1),
        ("¿Cuándo fue la última vez que algo de tu carácter fue exactamente lo más valioso?", 1),
        ("¿Cuándo fue la última vez que algo tuyo fue exactamente el motivo por el que algo funcionó?", 1),
        ("¿Cuándo fue la última vez que algo de tu forma de ser fue exactamente lo que te hizo único?", 1),
        ("¿Cuándo fue la última vez que algo de vos fue exactamente lo que alguien recordó?", 1),
        ("¿Cuándo fue la última vez que algo tuyo fue exactamente lo que marcó la diferencia?", 1),
        ("¿Cuándo fue la última vez que ser completamente vos fue exactamente la razón por la que algo fue bien?", 2),
        ("¿Cuándo fue la última vez que ser completamente vos fue exactamente la razón por la que alguien confió?", 2),
        ("¿Cuándo fue la última vez que ser completamente vos fue exactamente la razón por la que algo cambió?", 2),
        ("¿Cuándo fue la última vez que ser completamente vos fue exactamente lo que alguien necesitaba ver?", 2),
        ("¿Cuándo fue la última vez que ser completamente vos fue exactamente la razón por la que algo fue posible?", 2),
        ("¿Cuándo fue la última vez que ser auténtico fue exactamente el acto más transformador?", 3),
        ("¿Cuándo fue la última vez que ser exactamente quien sos fue exactamente lo que el mundo necesitaba?", 3),
        ("¿Cuándo fue la última vez que ser vos mismo fue la decisión más perfecta?", 3),
    ],

    "miedos": [
        ("¿Cuándo fue la última vez que algo que antes te asustaba ahora te parece completamente manejable?", 1),
        ("¿Cuándo fue la última vez que superaste algo sin darte cuenta de que lo estabas superando?", 1),
        ("¿Cuándo fue la última vez que el miedo desapareció sin que hicieras nada especial?", 1),
        ("¿Cuándo fue la última vez que algo que temías fue exactamente lo que te liberó?", 1),
        ("¿Cuándo fue la última vez que el miedo fue más pequeño que la gratitud?", 1),
        ("¿Cuándo fue la última vez que algo que temías fue exactamente la razón por la que creciste?", 1),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la señal de que algo importaba?", 1),
        ("¿Cuándo fue la última vez que algo que temías fue exactamente lo que te acercó a alguien?", 1),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón por la que eligiste bien?", 1),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la información que necesitabas?", 1),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón por la que algo fue posible?", 2),
        ("¿Cuándo fue la última vez que el miedo fue exactamente el camino hacia algo que querías?", 2),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón por la que confiaste más?", 2),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón por la que te pusiste en movimiento?", 2),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón por la que algo fue mejor?", 2),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón por la que fuiste capaz?", 3),
        ("¿Cuándo fue la última vez que el miedo fue exactamente el camino correcto hacia quien querés ser?", 3),
        ("¿Cuándo fue la última vez que algo que temías fue exactamente el regalo más inesperado?", 3),
    ],

    "logros": [
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente el motivo para seguir?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la respuesta que buscabas?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente lo que alguien necesitaba ver?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la razón de que algo más fue posible?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente el punto de inflexión?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente más de lo que imaginabas?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la razón de que te elegiste?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la razón de que seguiste intentando?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la razón de que algo imposible fue posible?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la razón de que creíste en vos?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la razón de que el esfuerzo tiene sentido?", 2),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la razón de que el camino valió?", 2),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la razón de que el fracaso fue necesario?", 2),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la razón de que todo tuvo sentido?", 2),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente el legado que querías dejar?", 2),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la expresión más completa de quien sos?", 3),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la razón de que el mundo fue mejor?", 3),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente lo que el mundo necesitaba de vos?", 3),
    ],

    "sinFiltro": [
        ("¿Cuándo fue la última vez que hiciste algo que te pareció extraño y después resultó completamente normal?", 1),
        ("¿Cuándo fue la última vez que algo que hacías en privado fue exactamente lo más genuino?", 1),
        ("¿Cuándo fue la última vez que algo tuyo que escondías fue exactamente tu mayor fortaleza?", 1),
        ("¿Cuándo fue la última vez que algo de lo que te avergonzabas fue exactamente lo más humano?", 1),
        ("¿Cuándo fue la última vez que algo que creías vergonzoso fue exactamente lo que alguien necesitaba escuchar?", 1),
        ("¿Cuándo fue la última vez que algo tuyo que ocultabas fue exactamente lo más poderoso?", 1),
        ("¿Cuándo fue la última vez que ser completamente honesto fue exactamente lo más valiente?", 1),
        ("¿Cuándo fue la última vez que algo que no ibas a contar fue exactamente lo que más conectó?", 1),
        ("¿Cuándo fue la última vez que algo que creías inapropiado fue exactamente apropiado?", 1),
        ("¿Cuándo fue la última vez que ser transparente fue exactamente lo más liberador?", 1),
        ("¿Cuándo fue la última vez que mostrar tu lado más oscuro fue exactamente lo que alguien más necesitaba ver para no sentirse solo?", 2),
        ("¿Cuándo fue la última vez que algo que considerabas un defecto fue exactamente lo que alguien amó?", 2),
        ("¿Cuándo fue la última vez que algo de lo que te avergonzabas fue exactamente lo que te hizo conectar?", 2),
        ("¿Cuándo fue la última vez que la honestidad brutal fue exactamente el mayor acto de amor?", 2),
        ("¿Cuándo fue la última vez que algo que ocultabas fue exactamente la clave de algo importante?", 2),
        ("¿Cuándo fue la última vez que la versión más sin filtros de vos fue exactamente la más amada?", 3),
        ("¿Cuándo fue la última vez que mostrar exactamente quien sos fue exactamente lo que el mundo necesitaba?", 3),
        ("¿Cuándo fue la última vez que dejar de performar fue exactamente el acto más transformador?", 3),
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
        if cat_id not in ADDITIONS20:
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

        for (text, level) in ADDITIONS20[cat_id]:
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
