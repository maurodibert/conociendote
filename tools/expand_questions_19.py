#!/usr/bin/env python3
"""Batch 19 - deeper emotional intelligence, patterns, growth."""
import json

ADDITIONS19 = {
    "infancia": [
        ("¿Cuál fue la primera vez que alguien te hizo sentir importante?", 1),
        ("¿Cuándo fue la primera vez que algo que aprendiste en la calle te sirvió más que en la escuela?", 1),
        ("¿Cuándo fue la primera vez que viste algo injusto y pudiste hacer algo al respecto?", 1),
        ("¿Cuándo fue la primera vez que hiciste reír a alguien cuando estaba triste?", 1),
        ("¿Cuándo fue la primera vez que alguien confió en vos con algo importante?", 1),
        ("¿Cuándo fue la primera vez que te emocionaste con algo que no era para nada emocionante para los demás?", 1),
        ("¿Cuándo fue la primera vez que elegiste no hacer algo porque no era lo correcto?", 1),
        ("¿Cuándo fue la primera vez que algo de lo que veías en el mundo te preocupó?", 1),
        ("¿Cuándo fue la primera vez que le pediste a alguien que se quedara?", 1),
        ("¿Cuándo fue la primera vez que algo externo a tu familia influenció tus valores?", 1),
        ("¿Cuándo fue la primera vez que alguien que más admirabas te decepcionó?", 2),
        ("¿Cuándo fue la primera vez que hiciste algo generoso sin que nadie te lo pidiera?", 2),
        ("¿Cuándo fue la primera vez que te pusiste en los zapatos de alguien diferente a vos?", 2),
        ("¿Cuándo fue la primera vez que tuviste que defenderte de alguien que amabas?", 2),
        ("¿Cuándo fue la primera vez que tu corazón y tu cabeza dijeron cosas distintas?", 2),
        ("¿Cuándo fue la primera vez que sentiste que tenías que elegir entre quién eras y quién querían que fueras?", 3),
        ("¿Cuál fue la experiencia de infancia que más te hizo entender quién no querías ser?", 3),
        ("¿Cuándo fue la primera vez que te diste cuenta de que el amor también se aprende?", 3),
    ],

    "futuro": [
        ("¿Cuándo fue la última vez que algo del presente te hizo sentir preparado para el futuro?", 1),
        ("¿Cuánto querés que cambie tu vida social en el futuro?", 1),
        ("¿Cuánto querés que cambie tu relación con el dinero en los próximos años?", 1),
        ("¿Cuánto querés que cambie tu vida espiritual en los próximos años?", 1),
        ("¿Cuánto querés que cambie tu relación con el trabajo en los próximos años?", 1),
        ("¿Cuánto querés que cambie tu relación con el cuerpo en los próximos años?", 1),
        ("¿Cuándo fue la última vez que construiste algo que va a durar más que vos?", 1),
        ("¿Cuándo fue la última vez que algo del futuro te generó más ilusión que ansiedad?", 1),
        ("¿Cuándo fue la última vez que el futuro te pareció exactamente lo que querías construir?", 1),
        ("¿Cuándo fue la última vez que algo del presente fue la semilla de algo grande en el futuro?", 1),
        ("¿Cuándo fue la última vez que tomaste una decisión sin saber si era la correcta y estuvo bien?", 2),
        ("¿Cuándo fue la última vez que el futuro te dio más razones para quedarte que para irse?", 2),
        ("¿Cuándo fue la última vez que confiaste en que el futuro se iba a encargar de lo que vos no podías controlar?", 2),
        ("¿Cuándo fue la última vez que algo que parecía el fin fue el principio de algo mejor?", 2),
        ("¿Cuándo fue la última vez que el miedo al futuro fue más pequeño que la ilusión?", 2),
        ("¿Cuándo fue la última vez que elegiste construir el futuro en lugar de esperarlo?", 3),
        ("¿Cuándo fue la última vez que algo del futuro te hizo sentir que ya valía la pena?", 3),
        ("¿Cuándo fue la última vez que el futuro que construiste superó el que imaginabas?", 3),
    ],

    "amor": [
        ("¿Cuándo fue la última vez que el amor fue más sencillo de lo que esperabas?", 1),
        ("¿Cuándo fue la última vez que te enamoraste de algo cotidiano de alguien?", 1),
        ("¿Cuándo fue la última vez que el amor te hizo ver algo diferente en vos mismo?", 1),
        ("¿Cuándo fue la última vez que el amor fue más un regalo que un esfuerzo?", 1),
        ("¿Cuándo fue la última vez que el amor fue algo que diste sin pensarlo?", 1),
        ("¿Cuándo fue la última vez que algo de alguien te llegó directo al corazón sin pasar por la mente?", 1),
        ("¿Cuándo fue la última vez que el amor te hizo sentir que el mundo era más luminoso?", 1),
        ("¿Cuándo fue la última vez que algo de alguien te hizo querer ser mejor?", 1),
        ("¿Cuándo fue la última vez que el amor fue la explicación de algo que no tenía otra?", 1),
        ("¿Cuándo fue la última vez que algo de una relación te hizo sonreír de manera inesperada?", 1),
        ("¿Cuándo fue la última vez que el amor fue más sobre dar que sobre recibir?", 2),
        ("¿Cuándo fue la última vez que el amor fue más sobre estar que sobre hacer?", 2),
        ("¿Cuándo fue la última vez que el amor fue más sobre confiar que sobre entender?", 2),
        ("¿Cuándo fue la última vez que el amor fue más sobre soltar que sobre aferrar?", 2),
        ("¿Cuándo fue la última vez que el amor fue exactamente proporcional a lo que dabas?", 2),
        ("¿Cuándo fue la última vez que el amor fue la cosa más valiente que elegiste?", 3),
        ("¿Cuándo fue la última vez que el amor fue exactamente lo que necesitabas para seguir?", 3),
        ("¿Cuándo fue la última vez que el amor fue la respuesta que no sabías que buscabas?", 3),
    ],

    "familia": [
        ("¿Cuándo fue la última vez que tu familia fue exactamente lo que necesitabas aunque no lo pediste?", 1),
        ("¿Cuándo fue la última vez que tu familia fue la razón por la que algo difícil valió la pena?", 1),
        ("¿Cuándo fue la última vez que tu familia te dio lo que nadie más podía darte?", 1),
        ("¿Cuándo fue la última vez que tu familia fue tu fuerza cuando no te quedaba ninguna?", 1),
        ("¿Cuándo fue la última vez que tu familia fue más grande de lo que la imaginabas?", 1),
        ("¿Cuándo fue la última vez que tu familia fue la razón por la que algo imposible fue posible?", 1),
        ("¿Cuándo fue la última vez que tu familia te enseñó algo sobre el amor que ningún libro enseña?", 1),
        ("¿Cuándo fue la última vez que tu familia fue tu espejo más honesto?", 1),
        ("¿Cuándo fue la última vez que tu familia fue tu mayor ventaja en algo?", 1),
        ("¿Cuándo fue la última vez que tu familia fue el lugar al que quisiste volver?", 1),
        ("¿Cuándo fue la última vez que tu familia fue más que lo que viste de ella en tu infancia?", 2),
        ("¿Cuándo fue la última vez que tu familia fue más resiliente de lo que creías?", 2),
        ("¿Cuándo fue la última vez que tu familia te mostró una fortaleza que no sabías que tenía?", 2),
        ("¿Cuándo fue la última vez que tu familia fue la razón por la que cambiaste algo de vos?", 2),
        ("¿Cuándo fue la última vez que tu familia fue la razón por la que te perdonaste algo?", 2),
        ("¿Cuándo fue la última vez que tu familia fue exactamente el hogar que necesitabas?", 3),
        ("¿Cuándo fue la última vez que tu familia fue la razón por la que elegiste seguir?", 3),
        ("¿Cuándo fue la última vez que tu familia fue todo lo que necesitabas sin saber que lo era?", 3),
    ],

    "amistades": [
        ("¿Cuándo fue la última vez que un amigo fue exactamente lo que necesitabas en el momento exacto?", 1),
        ("¿Cuándo fue la última vez que un amigo te hizo sentir que todo iba a estar bien sin decir nada?", 1),
        ("¿Cuándo fue la última vez que un amigo te dio algo que no sabías que necesitabas?", 1),
        ("¿Cuándo fue la última vez que un amigo fue más honesto con vos que vos mismo?", 1),
        ("¿Cuándo fue la última vez que un amigo fue tu mayor fuente de fortaleza?", 1),
        ("¿Cuándo fue la última vez que una amistad fue la razón por la que algo difícil fue más liviano?", 1),
        ("¿Cuándo fue la última vez que un amigo fue tu mejor ejemplo sin proponérselo?", 1),
        ("¿Cuándo fue la última vez que un amigo fue la razón por la que algo que parecía imposible fue posible?", 1),
        ("¿Cuándo fue la última vez que una amistad fue exactamente lo que necesitabas para avanzar?", 1),
        ("¿Cuándo fue la última vez que un amigo fue más familia que cualquier familiar?", 1),
        ("¿Cuándo fue la última vez que una amistad fue más transformadora que cualquier relación amorosa?", 2),
        ("¿Cuándo fue la última vez que una amistad te cambió de adentro hacia afuera?", 2),
        ("¿Cuándo fue la última vez que una amistad fue la razón por la que te convertiste en alguien mejor?", 2),
        ("¿Cuándo fue la última vez que una amistad fue el espejo más honesto que tuviste?", 2),
        ("¿Cuándo fue la última vez que una amistad fue la razón por la que algo que creías imposible fue posible?", 2),
        ("¿Cuándo fue la última vez que una amistad fue el amor más incondicional que recibiste?", 3),
        ("¿Cuándo fue la última vez que una amistad fue la razón por la que seguiste cuando querías parar?", 3),
        ("¿Cuándo fue la última vez que una amistad fue exactamente el regalo más inesperado de tu vida?", 3),
    ],

    "exs": [
        ("¿Cuándo fue la última vez que algo del pasado amoroso fue exactamente lo que necesitabas para crecer?", 1),
        ("¿Cuándo fue la última vez que algo de una relación pasada te ayudó a tomar una decisión en el presente?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso fue una fortaleza en lugar de un peso?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso fue más una escuela que un trauma?", 1),
        ("¿Cuándo fue la última vez que algo del pasado amoroso te dio claridad sobre lo que querés?", 1),
        ("¿Cuándo fue la última vez que agradeciste algo que aprendiste de una relación difícil?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso fue la razón de algo bueno del presente?", 1),
        ("¿Cuándo fue la última vez que algo del pasado amoroso fue exactamente lo que te faltaba entender?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso fue más un maestro que un verdugo?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso te hizo mejor en algo del presente?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso fue la razón por la que amás diferente hoy?", 2),
        ("¿Cuándo fue la última vez que el pasado amoroso fue la razón por la que elegís mejor hoy?", 2),
        ("¿Cuándo fue la última vez que el pasado amoroso fue la razón por la que sos más vos?", 2),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la enseñanza que necesitabas?", 2),
        ("¿Cuándo fue la última vez que el pasado amoroso fue la razón por la que te perdonaste algo?", 2),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente el camino hacia lo que querés?", 3),
        ("¿Cuándo fue la última vez que el pasado amoroso fue la razón por la que podés amar mejor?", 3),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente lo que el vos de ahora necesitaba que viviera el vos de antes?", 3),
    ],

    "personalidad": [
        ("¿Cuándo fue la última vez que algo tuyo que considerabas una debilidad fue exactamente lo que alguien necesitaba?", 1),
        ("¿Cuándo fue la última vez que algo que creías que te definía resultó ser solo una fase?", 1),
        ("¿Cuándo fue la última vez que algo de vos que escondías resultó ser lo más auténtico?", 1),
        ("¿Cuándo fue la última vez que algo que hacías por hábito resultó ser exactamente lo correcto?", 1),
        ("¿Cuándo fue la última vez que algo que pensabas que era único en vos resultó ser universal?", 1),
        ("¿Cuándo fue la última vez que algo tuyo que parecía una contradicción fue exactamente lo que te hacía especial?", 1),
        ("¿Cuándo fue la última vez que algo de vos que creías que no servía sirvió exactamente?", 1),
        ("¿Cuándo fue la última vez que algo tuyo que parecía imperfecto fue exactamente perfecto?", 1),
        ("¿Cuándo fue la última vez que algo de vos que considerabas un error fue la razón de algo bueno?", 1),
        ("¿Cuándo fue la última vez que algo que rechazabas de vos fue lo que alguien más amó?", 1),
        ("¿Cuándo fue la última vez que algo que aceptaste de vos mismo te abrió algo que estaba cerrado?", 2),
        ("¿Cuándo fue la última vez que algo de vos que considerabas pequeño tuvo un impacto enorme?", 2),
        ("¿Cuándo fue la última vez que ser completamente vos fue la cosa más valiente?", 2),
        ("¿Cuándo fue la última vez que algo de vos que parecía un límite fue en realidad una fortaleza?", 2),
        ("¿Cuándo fue la última vez que algo de vos mismo te sorprendió positivamente?", 2),
        ("¿Cuándo fue la última vez que ser auténtico fue exactamente lo que el mundo necesitaba de vos?", 3),
        ("¿Cuándo fue la última vez que algo de vos mismo fue la razón por la que alguien cambió algo?", 3),
        ("¿Cuándo fue la última vez que ser exactamente quien sos fue el regalo más grande que podías dar?", 3),
    ],

    "miedos": [
        ("¿Cuándo fue la última vez que algo que parecía tu mayor debilidad fue exactamente tu mayor fortaleza?", 1),
        ("¿Cuándo fue la última vez que algo que temías fue exactamente lo que te cambió para mejor?", 1),
        ("¿Cuándo fue la última vez que algo que evitabas fue exactamente lo que debías hacer?", 1),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la señal de que ibas bien?", 1),
        ("¿Cuándo fue la última vez que algo que te asustaba fue exactamente lo que te hacía falta?", 1),
        ("¿Cuándo fue la última vez que algo que temías resultó ser lo más seguro?", 1),
        ("¿Cuándo fue la última vez que el miedo fue exactamente proporcional a lo que importaba?", 1),
        ("¿Cuándo fue la última vez que algo que evitabas fue la razón de algo bueno?", 1),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la preparación que necesitabas?", 1),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la brújula correcta?", 1),
        ("¿Cuándo fue la última vez que el miedo fue más información que obstáculo?", 2),
        ("¿Cuándo fue la última vez que enfrentar un miedo cambió algo en vos que no esperabas?", 2),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la invitación que necesitabas?", 2),
        ("¿Cuándo fue la última vez que el miedo fue el comienzo de algo que valió completamente?", 2),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón por la que lograste algo?", 2),
        ("¿Cuándo fue la última vez que el miedo fue exactamente el camino hacia lo que más querías?", 3),
        ("¿Cuándo fue la última vez que el miedo fue la razón por la que fuiste capaz de algo que creías imposible?", 3),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la puerta hacia quién querías ser?", 3),
    ],

    "logros": [
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente lo que alguien necesitaba ver para creer?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue más grande de lo que te diste cuenta en el momento?", 1),
        ("¿Cuándo fue la última vez que algo que considerabas pequeño resultó ser exactamente lo más grande?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue la razón por la que alguien intentó algo?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la prueba de que podías?", 1),
        ("¿Cuándo fue la última vez que un logro fue exactamente la respuesta a una duda que tenías sobre vos?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue el resultado de haber fallado primero?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente lo que necesitabas para creer en vos?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue la razón por la que seguiste intentando?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente el regalo que no sabías que te ibas a dar?", 1),
        ("¿Cuándo fue la última vez que un logro fue exactamente la razón por la que todo el camino valió?", 2),
        ("¿Cuándo fue la última vez que algo que lograste fue más para otros que para vos?", 2),
        ("¿Cuándo fue la última vez que un logro fue exactamente la prueba de que el esfuerzo tiene sentido?", 2),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente lo que necesitabas para perdonarte algo?", 2),
        ("¿Cuándo fue la última vez que un logro fue exactamente la razón por la que volviste a creer en vos?", 2),
        ("¿Cuándo fue la última vez que un logro fue exactamente la razón por la que todo cobró sentido?", 3),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente el legado que querías dejar?", 3),
        ("¿Cuándo fue la última vez que un logro fue exactamente la expresión más completa de quien sos?", 3),
    ],

    "sinFiltro": [
        ("¿Cuántas veces por mes hacés algo que nadie espera de alguien como vos?", 1),
        ("¿Cuándo fue la última vez que revelaste algo tuyo que nadie esperaba que revelaras?", 1),
        ("¿Cuándo fue la última vez que hiciste algo completamente honesto que te costó más de lo que esperabas?", 1),
        ("¿Cuántas veces por mes te comportás completamente diferente con personas diferentes?", 1),
        ("¿Cuándo fue la última vez que algo que creías que ibas a arrepentirte de hacer resultó lo mejor?", 1),
        ("¿Cuándo fue la última vez que algo que parecía una vergüenza resultó ser exactamente lo correcto?", 1),
        ("¿Cuándo fue la última vez que algo de vos que escondías fue exactamente lo que alguien necesitaba ver?", 1),
        ("¿Cuándo fue la última vez que algo que hacías por diversión privada resultó ser tu mayor fortaleza?", 1),
        ("¿Cuándo fue la última vez que algo que parecía inapropiado fue exactamente adecuado?", 1),
        ("¿Cuándo fue la última vez que algo tuyo que se veía mal resultó ser exactamente bueno?", 1),
        ("¿Cuándo fue la última vez que algo que hiciste por impulso fue exactamente lo correcto?", 2),
        ("¿Cuándo fue la última vez que algo que parecía una debilidad fue tu mayor ventaja?", 2),
        ("¿Cuándo fue la última vez que algo de lo más oscuro de vos fue exactamente la fuente de algo bueno?", 2),
        ("¿Cuándo fue la última vez que lo que querías esconder fue exactamente lo que tenías que mostrar?", 2),
        ("¿Cuándo fue la última vez que algo tuyo que parecía un problema fue exactamente la solución?", 2),
        ("¿Cuándo fue la última vez que algo de vos que ocultabas fue exactamente lo más poderoso?", 3),
        ("¿Cuándo fue la última vez que la versión más honesta de vos fue exactamente la que más conectó con alguien?", 3),
        ("¿Cuándo fue la última vez que soltar la imagen fue la decisión más liberadora que tomaste?", 3),
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
        if cat_id not in ADDITIONS19:
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

        for (text, level) in ADDITIONS19[cat_id]:
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
