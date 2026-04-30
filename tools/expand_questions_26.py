#!/usr/bin/env python3
"""Batch 26 - emotions, vulnerability, resilience, healing."""
import json

ADDITIONS26 = {
    "infancia": [
        ("¿Cuándo fue la primera vez que un extraño fue amable con vos de manera que te sorprendió?", 1),
        ("¿Cuándo fue la primera vez que algo que tenías miedo de hacer resultó ser divertido?", 1),
        ("¿Cuándo fue la primera vez que hiciste algo que te hizo sentir orgulloso de manera inesperada?", 1),
        ("¿Cuándo fue la primera vez que algo simple fue exactamente lo que más te alegró?", 1),
        ("¿Cuándo fue la primera vez que alguien te explicó algo difícil de una manera que lo entendiste?", 1),
        ("¿Cuándo fue la primera vez que dejaste de tenerle miedo a algo que antes era enorme?", 1),
        ("¿Cuándo fue la primera vez que algo que debías hacer te resultó completamente emocionante?", 1),
        ("¿Cuándo fue la primera vez que entendiste que algo pequeño podía ser enorme?", 1),
        ("¿Cuándo fue la primera vez que alguien te sorprendió con algo que no esperabas recibir?", 1),
        ("¿Cuándo fue la primera vez que algo que creías difícil fue completamente fácil?", 1),
        ("¿Cuándo fue la primera vez que elegiste hacer algo difícil solo porque sabías que era lo correcto?", 2),
        ("¿Cuándo fue la primera vez que algo que dabas por sentado se volvió un regalo?", 2),
        ("¿Cuándo fue la primera vez que entendiste que pedir ayuda no era debilidad?", 2),
        ("¿Cuándo fue la primera vez que algo doloroso te enseñó algo que el placer nunca hubiera podido?", 2),
        ("¿Cuándo fue la primera vez que te diste cuenta de que eras más resiliente de lo que creías?", 2),
        ("¿Cuándo fue la primera vez que algo de vos mismo te sorprendió positivamente en un momento difícil?", 3),
        ("¿Cuándo fue la primera vez que superaste algo que creías que te iba a destruir?", 3),
        ("¿Cuándo fue la primera vez que la vida te enseñó algo que ningún adulto había podido enseñarte?", 3),
    ],

    "futuro": [
        ("¿Qué versión de vos mismo querés que sea la que lidera tu vida en 10 años?", 1),
        ("¿Cuánto querés que evolucione tu relación con la creatividad en el futuro?", 1),
        ("¿Cuánto querés que cambie tu impacto en la comunidad en los próximos años?", 1),
        ("¿Cuánto querés que evolucione tu relación con el aprendizaje continuo?", 1),
        ("¿Cuánto querés que cambie tu relación con la salud física en el futuro?", 1),
        ("¿Cuánto querés que evolucione tu relación con la generosidad?", 1),
        ("¿Cuánto querés que cambie tu relación con la paciencia en el futuro?", 1),
        ("¿Cuánto querés que evolucione tu relación con la autenticidad?", 1),
        ("¿Cuánto querés que cambie tu relación con los límites en el futuro?", 1),
        ("¿Cuánto querés que evolucione tu relación con el descanso?", 1),
        ("¿Cuándo fue la última vez que algo que planeabas para el futuro cambió por algo que pasó en el presente?", 2),
        ("¿Cuándo fue la última vez que algo que no planeabas fue mejor que todo lo que planeaste?", 2),
        ("¿Cuándo fue la última vez que el futuro te pareció exactamente tan lleno de posibilidades como imaginabas?", 2),
        ("¿Cuándo fue la última vez que algo del presente fue exactamente la promesa del futuro que querés?", 2),
        ("¿Cuándo fue la última vez que eligiste el proceso sobre el resultado futuro?", 2),
        ("¿Cuándo fue la última vez que el futuro que querés te pareció completamente tuyo para construir?", 3),
        ("¿Cuándo fue la última vez que algo del presente fue exactamente el primer paso hacia el futuro que querés?", 3),
        ("¿Cuándo fue la última vez que el futuro fue exactamente la razón para vivir mejor el presente?", 3),
    ],

    "amor": [
        ("¿Cuándo fue la última vez que el amor fue exactamente más fácil de lo que imaginabas que sería?", 1),
        ("¿Cuándo fue la última vez que el amor fue exactamente más profundo de lo que esperabas?", 1),
        ("¿Cuándo fue la última vez que el amor fue exactamente la razón de que algo difícil valió la pena?", 1),
        ("¿Cuándo fue la última vez que el amor fue exactamente lo que te faltaba para estar bien?", 1),
        ("¿Cuándo fue la última vez que el amor fue exactamente la respuesta más sencilla a algo complicado?", 1),
        ("¿Cuándo fue la última vez que el amor fue exactamente la razón de que el mundo te pareciera más bueno?", 1),
        ("¿Cuándo fue la última vez que el amor fue exactamente el motivo de que te arriesgaras?", 1),
        ("¿Cuándo fue la última vez que el amor fue exactamente la razón de que no renunciaras?", 1),
        ("¿Cuándo fue la última vez que el amor fue exactamente el punto de inflexión?", 1),
        ("¿Cuándo fue la última vez que el amor fue exactamente lo que le dio color a algo gris?", 1),
        ("¿Cuándo fue la última vez que el amor fue exactamente más valioso que cualquier otra cosa?", 2),
        ("¿Cuándo fue la última vez que el amor fue exactamente la razón de que creciste?", 2),
        ("¿Cuándo fue la última vez que el amor fue exactamente la razón de que te perdonaste?", 2),
        ("¿Cuándo fue la última vez que el amor fue exactamente más de lo que creías merecer?", 2),
        ("¿Cuándo fue la última vez que el amor fue exactamente la razón de que elegiste ser mejor?", 2),
        ("¿Cuándo fue la última vez que el amor fue exactamente el origen de tu mejor versión?", 3),
        ("¿Cuándo fue la última vez que el amor fue exactamente la razón de que el mundo valiera la pena?", 3),
        ("¿Cuándo fue la última vez que el amor fue exactamente el por qué de todo?", 3),
    ],

    "familia": [
        ("¿Cuándo fue la última vez que algo de tu familia fue exactamente lo que necesitabas para sanar algo?", 1),
        ("¿Cuándo fue la última vez que algo de tu familia fue exactamente la razón de que creíste en algo?", 1),
        ("¿Cuándo fue la última vez que algo de tu familia fue exactamente el amor más incondicional?", 1),
        ("¿Cuándo fue la última vez que algo de tu familia fue exactamente la razón de que seguiste?", 1),
        ("¿Cuándo fue la última vez que algo de tu familia fue exactamente la fuerza que necesitabas?", 1),
        ("¿Cuándo fue la última vez que algo de tu familia fue exactamente la razón de que algo fue posible?", 1),
        ("¿Cuándo fue la última vez que algo de tu familia fue exactamente el refugio correcto?", 1),
        ("¿Cuándo fue la última vez que algo de tu familia fue exactamente la razón de que algo dolió menos?", 1),
        ("¿Cuándo fue la última vez que algo de tu familia fue exactamente lo que más necesitabas escuchar?", 1),
        ("¿Cuándo fue la última vez que algo de tu familia fue exactamente el amor que más te transformó?", 1),
        ("¿Cuándo fue la última vez que tu familia fue exactamente la razón de que algo que parecía imposible fue posible?", 2),
        ("¿Cuándo fue la última vez que tu familia fue exactamente la razón de que elegiste algo difícil?", 2),
        ("¿Cuándo fue la última vez que tu familia fue exactamente la razón de que confiaste en vos mismo?", 2),
        ("¿Cuándo fue la última vez que tu familia fue exactamente la razón de que fuiste capaz de algo?", 2),
        ("¿Cuándo fue la última vez que tu familia fue exactamente la razón de que todo cobró sentido?", 2),
        ("¿Cuándo fue la última vez que tu familia fue exactamente el origen de algo de lo que más orgulloso estás?", 3),
        ("¿Cuándo fue la última vez que tu familia fue exactamente la razón de que sos quien querés ser?", 3),
        ("¿Cuándo fue la última vez que tu familia fue exactamente el regalo más profundo de tu vida?", 3),
    ],

    "amistades": [
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón de que algo difícil fue posible?", 1),
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón de que te perdonaste algo?", 1),
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón de que seguiste creyendo?", 1),
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón de que algo dolió menos?", 1),
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón de que sos más vos?", 1),
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón de que algo imposible fue posible?", 1),
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón de que creíste en algo?", 1),
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón de que algo fue mejor?", 1),
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón de que seguiste?", 1),
        ("¿Cuándo fue la última vez que una amistad fue exactamente el amor que más necesitabas?", 1),
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón de que algo que creías perdido volvió?", 2),
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón de que elegiste ser mejor?", 2),
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón de que confiaste más en vos?", 2),
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón de que algo que parecía malo fue bueno?", 2),
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón de que todo tuvo sentido?", 2),
        ("¿Cuándo fue la última vez que una amistad fue exactamente el legado más bello de un período de tu vida?", 3),
        ("¿Cuándo fue la última vez que una amistad fue exactamente la razón de que sos quien querés ser?", 3),
        ("¿Cuándo fue la última vez que una amistad fue exactamente el regalo que nunca pediste pero más necesitabas?", 3),
    ],

    "exs": [
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que sos mejor en el amor?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que elegís con más claridad?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que confiás diferente?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que amás más libremente?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que tenés límites más claros?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que sabés lo que no querés?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que te perdonaste más fácil?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que te conocés mejor?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que algo del presente fue posible?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que sos quien sos hoy?", 1),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que el presente es más rico?", 2),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que el amor actual es más real?", 2),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que podés dar más?", 2),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que algo que dolió valió?", 2),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que sos más libre hoy?", 2),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que el amor de ahora es mejor?", 3),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente el camino necesario hacia quien sos?", 3),
        ("¿Cuándo fue la última vez que el pasado amoroso fue exactamente la razón de que podés amar como querés?", 3),
    ],

    "personalidad": [
        ("¿Cuándo fue la última vez que algo de vos mismo fue exactamente lo que alguien más necesitaba ver?", 1),
        ("¿Cuándo fue la última vez que algo de vos mismo fue exactamente la razón de que algo fue posible?", 1),
        ("¿Cuándo fue la última vez que algo de vos mismo fue exactamente más de lo que esperabas de vos?", 1),
        ("¿Cuándo fue la última vez que algo de vos mismo fue exactamente la razón de que alguien confió?", 1),
        ("¿Cuándo fue la última vez que algo de vos mismo fue exactamente el regalo que alguien necesitaba?", 1),
        ("¿Cuándo fue la última vez que algo de vos mismo fue exactamente la razón de que algo fue mejor?", 1),
        ("¿Cuándo fue la última vez que algo de vos mismo fue exactamente la diferencia entre lo ordinario y lo especial?", 1),
        ("¿Cuándo fue la última vez que algo de vos mismo fue exactamente lo que faltaba?", 1),
        ("¿Cuándo fue la última vez que algo de vos mismo fue exactamente la razón de que seguiste?", 1),
        ("¿Cuándo fue la última vez que algo de vos mismo fue exactamente lo que alguien recordó?", 1),
        ("¿Cuándo fue la última vez que ser completamente vos fue exactamente la razón por la que algo funcionó?", 2),
        ("¿Cuándo fue la última vez que ser completamente vos fue exactamente la razón de que alguien creciera?", 2),
        ("¿Cuándo fue la última vez que ser completamente vos fue exactamente la razón de que algo cambió para mejor?", 2),
        ("¿Cuándo fue la última vez que ser completamente vos fue exactamente la razón de que todo fue posible?", 2),
        ("¿Cuándo fue la última vez que ser completamente vos fue exactamente el acto más generoso?", 2),
        ("¿Cuándo fue la última vez que ser exactamente quien sos fue exactamente la razón de que el mundo fue mejor?", 3),
        ("¿Cuándo fue la última vez que ser vos mismo fue exactamente la decisión más transformadora que tomaste?", 3),
        ("¿Cuándo fue la última vez que algo de tu identidad más profunda fue exactamente lo que alguien más necesitaba ver?", 3),
    ],

    "miedos": [
        ("¿Cuándo fue la última vez que el miedo fue exactamente más pequeño de lo que parecía cuando lo enfrentaste?", 1),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón de que algo fue mejor de lo que esperabas?", 1),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón de que algo que parecía imposible fue posible?", 1),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón de que algo fue más significativo?", 1),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón de que elegiste el camino correcto?", 1),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón de que algo fue más valioso?", 1),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón de que te preparaste mejor?", 1),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón de que algo dolió menos?", 1),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón de que algo fue más auténtico?", 1),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón de que algo fue más real?", 1),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón de que fuiste más vos mismo?", 2),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón de que algo fue más profundo?", 2),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón de que algo fue más necesario?", 2),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón de que algo fue más transformador?", 2),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón de que algo fue exactamente correcto?", 2),
        ("¿Cuándo fue la última vez que el miedo fue exactamente el camino hacia quién más querés ser?", 3),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón de que todo lo que construiste valió?", 3),
        ("¿Cuándo fue la última vez que el miedo fue exactamente la razón de que podés decir que fuiste valiente?", 3),
    ],

    "logros": [
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente más valioso por lo que costó?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la razón de que seguiste?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la razón de que algo más fue posible?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la razón de que alguien más creyó?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente más de lo que pedías?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la razón de que algo dolió menos?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la razón de que te perdonaste algo?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la razón de que algo fue mejor?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la razón de que el camino valió?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente la razón de que todo tuvo sentido?", 1),
        ("¿Cuándo fue la última vez que un logro fue exactamente la razón de que todo lo que vino antes valió?", 2),
        ("¿Cuándo fue la última vez que un logro fue exactamente la razón de que confiaste más en vos?", 2),
        ("¿Cuándo fue la última vez que un logro fue exactamente la razón de que algo imposible fue posible?", 2),
        ("¿Cuándo fue la última vez que un logro fue exactamente la razón de que el futuro pareció más posible?", 2),
        ("¿Cuándo fue la última vez que un logro fue exactamente la razón de que algo de vos mismo se fortaleció?", 2),
        ("¿Cuándo fue la última vez que un logro fue exactamente la expresión más completa de lo que sos capaz?", 3),
        ("¿Cuándo fue la última vez que un logro fue exactamente la razón de que todo el esfuerzo anterior cobró sentido?", 3),
        ("¿Cuándo fue la última vez que un logro fue exactamente la razón de que sos quien querés ser?", 3),
    ],

    "sinFiltro": [
        ("¿Cuántas veces al mes haces algo solo porque te da curiosidad aunque no tenga ninguna utilidad práctica?", 1),
        ("¿Cuándo fue la última vez que hiciste algo completamente inesperado y te salió perfecto?", 1),
        ("¿Cuándo fue la última vez que algo que te parecía vergonzoso resultó ser lo más genuino?", 1),
        ("¿Cuándo fue la última vez que algo que ocultabas fue exactamente lo que alguien más necesitaba ver?", 1),
        ("¿Cuándo fue la última vez que algo de vos que considerabas un defecto fue lo que más conectó?", 1),
        ("¿Cuándo fue la última vez que algo que creías inapropiado fue exactamente lo apropiado?", 1),
        ("¿Cuándo fue la última vez que mostrar tu lado más raro fue exactamente lo correcto?", 1),
        ("¿Cuándo fue la última vez que algo de lo que te avergonzabas fue exactamente lo que alguien necesitaba?", 1),
        ("¿Cuándo fue la última vez que ser completamente honesto fue exactamente lo más liberador?", 1),
        ("¿Cuándo fue la última vez que algo que hacías en privado resultó ser tu mayor fortaleza?", 1),
        ("¿Cuándo fue la última vez que algo de vos que escondías fue exactamente lo que alguien amó?", 2),
        ("¿Cuándo fue la última vez que la versión más sin filtros de vos fue exactamente la más conectada?", 2),
        ("¿Cuándo fue la última vez que dejar de performar fue exactamente el acto más valiente?", 2),
        ("¿Cuándo fue la última vez que algo que considerabas oscuro en vos fue exactamente la luz para alguien?", 2),
        ("¿Cuándo fue la última vez que la honestidad más incómoda fue exactamente lo que más unió?", 2),
        ("¿Cuándo fue la última vez que la versión más real de vos fue exactamente la más poderosa?", 3),
        ("¿Cuándo fue la última vez que mostrar todo lo que sos fue exactamente el acto de amor más grande?", 3),
        ("¿Cuándo fue la última vez que la cosa que más te costaba admitir fue exactamente lo que te liberó?", 3),
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
        if cat_id not in ADDITIONS26:
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

        for (text, level) in ADDITIONS26[cat_id]:
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
