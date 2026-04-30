#!/usr/bin/env python3
"""Batch 15 - themes: travel, adventure, discovery, wonder, senses."""
import json

ADDITIONS15 = {
    "infancia": [
        ("¿Cuál fue el primer viaje que recordás haber hecho?", 1),
        ("¿Cuál era el aroma que más asociás con la cocina de tu abuela?", 1),
        ("¿Cuándo fue la primera vez que viste el mar, la montaña o un lago?", 1),
        ("¿Cuál fue tu primer recuerdo de ver algo que te dejó sin palabras?", 1),
        ("¿Cuál era la textura que más detestabas de chico?", 1),
        ("¿Cuál era el sonido de fondo que más asociás a tu infancia?", 1),
        ("¿Cuándo fue la primera vez que viste una obra de teatro o un circo?", 1),
        ("¿Cuál fue el primer concierto o espectáculo musical al que fuiste?", 1),
        ("¿Tenías algún lugar secreto en tu barrio o casa?", 1),
        ("¿Cuál fue el primer animal salvaje o exótico que viste en persona?", 1),
        ("¿Cuándo fue la primera vez que viajaste en avión?", 1),
        ("¿Cuándo fue la primera vez que te perdiste en un lugar desconocido?", 1),
        ("¿Cuál era la ciudad o lugar al que querías ir de chico y nunca llegaste?", 1),
        ("¿Cuándo fue la primera vez que sentiste que el mundo era más grande de lo que pensabas?", 2),
        ("¿Cuál fue la experiencia de viaje de chico que más te marcó?", 2),
        ("¿Cuándo fue la primera vez que sentiste añoranza de un lugar?", 2),
        ("¿Cuándo fue la primera vez que viste algo bello que no podías describir?", 2),
        ("¿Cuándo fue la primera vez que el mundo te sorprendió de manera inesperada?", 3),
        ("¿Cuál es el lugar de tu infancia que más te gustaría volver a ver con los ojos de ahora?", 3),
        ("¿Cuándo fue la primera vez que sentiste que el mundo era tuyo para explorarlo?", 3),
    ],

    "futuro": [
        ("¿Cuál es el país que definitivamente querés conocer antes de morir?", 1),
        ("¿Cuántos continentes querés visitar en tu vida?", 1),
        ("¿Cuál es la maravilla natural que más querés ver en persona?", 1),
        ("¿Cuál es el tipo de aventura que querés vivir al menos una vez?", 1),
        ("¿Cuánto querés viajar comparado con cómo lo hacés ahora?", 1),
        ("¿Cuál es el destino de viaje que le recomendarías a todos?", 1),
        ("¿Cuándo fue la última vez que te imaginaste viviendo en otro país?", 1),
        ("¿Cuál es la experiencia gastronómica que querés vivir en el extranjero?", 1),
        ("¿Cuándo fue la última vez que planificaste un viaje con detalle?", 1),
        ("¿Cuál es el modo de transporte más loco con el que querés viajar?", 1),
        ("¿Cuánto de tu futuro querés que esté relacionado con el movimiento y el cambio de lugar?", 1),
        ("¿Cuál es la cultura que más te gustaría conocer desde adentro?", 1),
        ("¿Cuándo fue la última vez que un viaje te cambió?", 1),
        ("¿Qué llevarías en tu mochila si tuvieras que salir mañana?", 1),
        ("¿Cuál es el miedo de viaje que querés superar?", 2),
        ("¿Cuándo fue la última vez que un viaje te sacó de quicio pero valió la pena?", 2),
        ("¿Cuándo fue la última vez que un lugar te hizo sentir que pertenecías ahí?", 2),
        ("¿Cuál es el viaje que pospusiste por miedo y que más lamentás no haber hecho?", 3),
        ("¿Cuándo fue la última vez que un lugar te enseñó algo sobre vos mismo?", 3),
        ("¿Cuál es el viaje que harías mañana si no hubiera impedimentos?", 3),
    ],

    "amor": [
        ("¿Cuándo fue la primera vez que alguien te cocinó algo con amor?", 1),
        ("¿Cuándo fue la primera vez que alguien te regaló algo que claramente eligió pensando en vos?", 1),
        ("¿Cuándo fue la última vez que alguien te dijo algo en el momento exacto en que lo necesitabas?", 1),
        ("¿Cuándo fue la primera vez que te perdiste en una ciudad con alguien que te gustaba?", 1),
        ("¿Cuándo fue la primera vez que bailaste lento con alguien?", 1),
        ("¿Cuándo fue la última vez que te enamoraste de algo que hacía alguien?", 1),
        ("¿Cuándo fue la primera vez que alguien te llamó solo para escucharte?", 1),
        ("¿Cuándo fue la primera vez que el amor te hizo ver algo bello que antes no veías?", 1),
        ("¿Cuándo fue la última vez que alguien te hizo sentir que eras interesante de verdad?", 1),
        ("¿Cuándo fue la última vez que alguien te miró de una manera que te detuvo?", 1),
        ("¿Cuándo fue la última vez que alguien te hizo sentir completamente seguro?", 1),
        ("¿Cuándo fue la última vez que el amor fue pura alegría sin complicaciones?", 1),
        ("¿Cuándo fue la última vez que algo pequeño de alguien te enamoró completamente?", 1),
        ("¿Cuándo fue la última vez que alguien te extrañó de manera que podías sentirlo?", 2),
        ("¿Cuándo fue la última vez que te sentiste profundamente visto por alguien?", 2),
        ("¿Cuándo fue la última vez que el amor fue más que sentimiento y fue acción?", 2),
        ("¿Cuándo fue la última vez que alguien te amó exactamente como sos?", 2),
        ("¿Cuándo fue la última vez que el amor te hizo sentir que el mundo valía la pena?", 3),
        ("¿Cuándo fue la última vez que sentiste amor por alguien sin la menor duda?", 3),
        ("¿Cuándo fue la última vez que el amor fue exactamente lo que esperabas y más?", 3),
    ],

    "familia": [
        ("¿Cuál es la historia de amor entre tus padres que más te gusta?", 1),
        ("¿Cuándo fue la última vez que alguien de tu familia te sorprendió con un gesto?", 1),
        ("¿Cuándo fue la última vez que sentiste el amor de tu familia sin que nadie dijera nada?", 1),
        ("¿Cuándo fue la última vez que recordaste a alguien de tu familia que ya no está?", 1),
        ("¿Cuándo fue la última vez que tu familia estuvo completamente presente para vos?", 1),
        ("¿Cuál es la cosa más tierna que hace alguien de tu familia y que tal vez nunca se lo dijiste?", 1),
        ("¿Cuándo fue la última vez que tu familia celebró algo tuyo con genuina alegría?", 1),
        ("¿Cuándo fue la última vez que alguien de tu familia te llamó solo para escucharte?", 1),
        ("¿Cuándo fue la última vez que tu familia se unió para atravesar algo difícil?", 1),
        ("¿Cuándo fue la última vez que tu familia te hizo sentir que eras suficiente?", 1),
        ("¿Cuándo fue la última vez que tu familia te sorprendió siendo más comprensiva de lo que esperabas?", 1),
        ("¿Cuándo fue la última vez que tu familia te hizo reír de corazón?", 1),
        ("¿Cuándo fue la última vez que alguien de tu familia hizo algo que todavía te emociona?", 1),
        ("¿Cuándo fue la última vez que tu familia te enseñó algo que nadie más te enseñó?", 2),
        ("¿Cuándo fue la última vez que tu familia estuvo ahí cuando nadie más lo estuvo?", 2),
        ("¿Cuándo fue la última vez que perdonaste a tu familia algo que te costó mucho?", 2),
        ("¿Cuándo fue la última vez que tu familia te ayudó a ser mejor persona?", 2),
        ("¿Cuándo fue la última vez que te sentiste completamente aceptado por tu familia?", 3),
        ("¿Cuándo fue la última vez que tu familia te demostró que te amaba a pesar de todo?", 3),
        ("¿Cuándo fue la última vez que elegiste a tu familia sobre cualquier otra cosa?", 3),
    ],

    "amistades": [
        ("¿Cuándo fue la última vez que viajaste con amigos?", 1),
        ("¿Cuándo fue la última vez que se juntaron en un lugar nuevo con amigos?", 1),
        ("¿Cuál fue el viaje o aventura más memorable que tuviste con amigos?", 1),
        ("¿Cuándo fue la última vez que exploraste algo desconocido con amigos?", 1),
        ("¿Cuándo fue la última vez que un amigo te llevó a un lugar que no conocías?", 1),
        ("¿Cuándo fue la última vez que conociste amigos de amigos y te llevaste bien?", 1),
        ("¿Cuándo fue la última vez que un amigo te presentó algo que te cambió la vida?", 1),
        ("¿Cuándo fue la última vez que un amigo te recomendó algo que terminaste amando?", 1),
        ("¿Cuándo fue la última vez que un amigo te acompañó a algo que a él o ella no le gustaba?", 1),
        ("¿Cuándo fue la última vez que un amigo te sacó de tu zona de confort de manera buena?", 1),
        ("¿Cuándo fue la última vez que un amigo te enseñó algo que no esperabas aprender?", 1),
        ("¿Cuándo fue la última vez que te pusiste en contacto con un amigo después de mucho tiempo?", 1),
        ("¿Cuándo fue la última vez que hiciste algo espontáneo con amigos y fue perfecto?", 1),
        ("¿Cuándo fue la última vez que un amigo te ayudó a ver algo diferente?", 2),
        ("¿Cuándo fue la última vez que un amigo hizo algo por vos que lo cambió todo?", 2),
        ("¿Cuándo fue la última vez que una amistad te dio el coraje de hacer algo nuevo?", 2),
        ("¿Cuándo fue la última vez que una amistad te hizo sentir que el mundo era más grande?", 2),
        ("¿Cuándo fue la última vez que una amistad te ayudó a descubrir algo de vos mismo?", 3),
        ("¿Cuándo fue la última vez que una amistad transformó tu manera de ver el mundo?", 3),
        ("¿Cuándo fue la última vez que una amistad fue exactamente lo que necesitabas?", 3),
    ],

    "exs": [
        ("¿Cuándo fue la primera vez que viajaste con una pareja?", 1),
        ("¿Cuál fue el mejor viaje que hiciste con un ex?", 1),
        ("¿Cuál fue el lugar que más asociás a una relación pasada?", 1),
        ("¿Cuándo fue la primera vez que te perdiste con una pareja y fue bueno?", 1),
        ("¿Cuándo fue la primera vez que una pareja te presentó un mundo que no conocías?", 1),
        ("¿Cuándo fue la primera vez que alguien que te gustaba te llevó a su lugar favorito?", 1),
        ("¿Cuál fue la aventura más loca que viviste con un ex?", 1),
        ("¿Cuándo fue la primera vez que descubriste algo sobre vos mismo gracias a una relación?", 1),
        ("¿Cuándo fue la primera vez que una relación te hizo querer ser alguien diferente?", 1),
        ("¿Cuándo fue la primera vez que una relación te hizo ver el mundo de otra manera?", 1),
        ("¿Cuándo fue la primera vez que alguien que te gustaba te recomendó algo que te encantó?", 1),
        ("¿Cuándo fue la última vez que un recuerdo de una relación pasada te hizo sonreír puro?", 1),
        ("¿Cuándo fue la última vez que agradeciste algo que te enseñó una relación pasada?", 1),
        ("¿Cuándo fue la última vez que le diste crédito a una relación pasada por algo que tenés hoy?", 2),
        ("¿Cuándo fue la última vez que una relación pasada te ayudó a ser mejor en el presente?", 2),
        ("¿Cuándo fue la última vez que entendiste algo de una relación pasada que antes no podías ver?", 2),
        ("¿Cuándo fue la última vez que perdonaste algo del pasado sin necesitar que la otra persona lo supiera?", 2),
        ("¿Cuándo fue la última vez que una relación pasada te enseñó algo que nadie más pudo?", 3),
        ("¿Cuándo fue la última vez que le agradeciste mentalmente a alguien del pasado?", 3),
        ("¿Cuándo fue la última vez que el pasado amoroso te liberó en lugar de atraparte?", 3),
    ],

    "personalidad": [
        ("¿Cuándo fue la última vez que algo te dejó sin palabras de pura belleza?", 1),
        ("¿Cuál es el tipo de paisaje que más te conecta con vos mismo?", 1),
        ("¿Cuándo fue la última vez que algo te movió sin poder explicar por qué?", 1),
        ("¿Cuándo fue la última vez que la música te llevó a un estado diferente?", 1),
        ("¿Cuándo fue la última vez que te perdiste en algo creativo?", 1),
        ("¿Cuándo fue la última vez que algo cotidiano te pareció extraordinario?", 1),
        ("¿Cuándo fue la última vez que dedicaste tiempo a algo bello sin ningún propósito práctico?", 1),
        ("¿Cuándo fue la última vez que sentiste genuina maravilla ante algo?", 1),
        ("¿Cuándo fue la última vez que el arte de alguien más te llegó al alma?", 1),
        ("¿Cuándo fue la última vez que hiciste algo creativo sin importarte si era bueno?", 1),
        ("¿Cuándo fue la última vez que algo que viste o escuchaste te cambió algo adentro?", 1),
        ("¿Cuándo fue la última vez que te permitiste simplemente contemplar sin hacer nada más?", 1),
        ("¿Cuándo fue la última vez que algo te hizo sentir que la vida valía la pena?", 1),
        ("¿Cuándo fue la última vez que algo te sacó completamente de la cotidianidad?", 2),
        ("¿Cuándo fue la última vez que algo te conectó con algo más grande que vos?", 2),
        ("¿Cuándo fue la última vez que el mundo te pareció completamente bueno aunque sea por un momento?", 2),
        ("¿Cuándo fue la última vez que algo bello te hizo llorar?", 2),
        ("¿Cuándo fue la última vez que la belleza de algo te hizo entender algo sobre vos?", 3),
        ("¿Cuándo fue la última vez que te perdiste completamente en algo y regresaste diferente?", 3),
        ("¿Cuándo fue la última vez que algo te hizo querer crear o hacer algo para el mundo?", 3),
    ],

    "miedos": [
        ("¿Le tenés miedo a las tormentas eléctricas?", 1),
        ("¿Cuándo fue la última vez que algo inesperado te asustó de verdad?", 1),
        ("¿Cuál es el ruido que más te paraliza?", 1),
        ("¿Le tenés miedo a algún tipo de agua específica?", 1),
        ("¿Cuál es el tipo de lugar que más evitás por incomodidad?", 1),
        ("¿Cuándo fue la última vez que algo pequeño te generó un miedo desproporcionado?", 1),
        ("¿Le tenés miedo a ver sangre?", 1),
        ("¿Cuándo fue la última vez que un miedo te apareció de la nada?", 1),
        ("¿Cuál es el miedo que más le ocultás a la gente que querés impresionar?", 1),
        ("¿Le tenés miedo a algo que la mayoría de la gente no encuentra aterrador?", 1),
        ("¿Cuándo fue la última vez que el miedo te hizo mejor compañía que la tranquilidad?", 1),
        ("¿Cuándo fue la última vez que el miedo te conectó con alguien?", 1),
        ("¿Cuándo fue la última vez que el miedo te abrió los ojos sobre algo?", 1),
        ("¿Cuándo fue la última vez que reconociste un miedo nuevo que no tenías antes?", 2),
        ("¿Cuándo fue la última vez que el miedo te hizo tomar una decisión que fue buena?", 2),
        ("¿Cuándo fue la última vez que el miedo te conectó con algo que valorás?", 2),
        ("¿Cuándo fue la última vez que el miedo te obligó a ser más honesto?", 2),
        ("¿Cuándo fue la última vez que el miedo te reveló algo esencial sobre quién sos?", 3),
        ("¿Cuándo fue la última vez que enfrentaste un miedo y te cambió?", 3),
        ("¿Cuándo fue la última vez que el miedo fue tu mejor maestro?", 3),
    ],

    "logros": [
        ("¿Cuándo fue la última vez que lograste algo que te llenó de orgullo sin necesitar que nadie lo supiera?", 1),
        ("¿Cuándo fue la última vez que algo que hiciste fue más bello de lo que esperabas?", 1),
        ("¿Cuándo fue la última vez que tu trabajo fue reconocido por alguien que admiras?", 1),
        ("¿Cuándo fue la última vez que algo que creaste fue usado por alguien más?", 1),
        ("¿Cuándo fue la última vez que lograste algo que abrió una puerta que no esperabas?", 1),
        ("¿Cuándo fue la última vez que algo que lograste llegó a gente que no conocés?", 1),
        ("¿Cuándo fue la última vez que un logro tuyo te hizo conocer a alguien?", 1),
        ("¿Cuándo fue la última vez que algo que hiciste superó tus propias expectativas?", 1),
        ("¿Cuándo fue la última vez que lograste algo a partir de un fracaso anterior?", 1),
        ("¿Cuándo fue la última vez que un logro te hizo sentir que pertenecías a algo?", 1),
        ("¿Cuándo fue la última vez que algo que lograste fue exactamente como lo habías imaginado?", 1),
        ("¿Cuándo fue la última vez que tu logro tuvo un impacto que no esperabas?", 1),
        ("¿Cuándo fue la última vez que lo que lograste fue una respuesta a algo que el mundo necesitaba?", 1),
        ("¿Cuándo fue la última vez que lograste algo que cambió tu relación con la exigencia?", 2),
        ("¿Cuándo fue la última vez que un logro tuyo cambió cómo te ven los demás?", 2),
        ("¿Cuándo fue la última vez que un logro te hizo sentir que todo el esfuerzo anterior tenía sentido?", 2),
        ("¿Cuándo fue la última vez que lograste algo que querías desde hace tanto que ya casi lo habías olvidado?", 2),
        ("¿Cuándo fue la última vez que un logro te hizo sentir que podías confiar en vos mismo?", 3),
        ("¿Cuándo fue la última vez que un logro tuyo te puso en contacto con tu mejor versión?", 3),
        ("¿Cuándo fue la última vez que algo que lograste fue la respuesta a una pregunta que llevabas años haciéndote?", 3),
    ],

    "sinFiltro": [
        ("¿Cuántas veces al año decís que vas a hacer ejercicio y no lo hacés?", 1),
        ("¿Cuántas cosas tenés en 'pendientes' desde hace más de un año?", 1),
        ("¿Cuántas veces por semana comés algo directamente del envase?", 1),
        ("¿Cuántas series o películas dijiste que ibas a ver y nunca arrancaste?", 1),
        ("¿Cuántas veces le pediste consejo a alguien y no lo seguiste?", 1),
        ("¿Cuántas veces diste el mismo consejo que vos mismo no seguís?", 1),
        ("¿Cuántas veces al mes decís 'mañana lo hago' y ese mañana no llega?", 1),
        ("¿Cuántas veces le respondiste un mensaje a alguien días después sin explicación?", 1),
        ("¿Cuántas veces comparte contenido que ni vos entendiste bien?", 1),
        ("¿Cuántas veces al mes comprás algo que 'necesitás' y después ni lo usás?", 1),
        ("¿Cuántas aplicaciones de bienestar instalaste y usaste menos de tres veces?", 1),
        ("¿Cuántas veces al año hacés algo malo para tu salud consciente y deliberadamente?", 1),
        ("¿Cuántas veces pusiste 'Me gusta' en algo que en realidad no te gustaba?", 1),
        ("¿Cuándo fue la última vez que reíste de alguien que no te cae bien y no te sentiste mal?", 2),
        ("¿Cuándo fue la última vez que dejaste que alguien pensara mal de un tercero sin aclararlo?", 2),
        ("¿Cuándo fue la última vez que sacaste ventaja de algo sin que nadie se enterara?", 2),
        ("¿Cuándo fue la última vez que actuaste por conveniencia pura y lo disfrutaste?", 2),
        ("¿Cuándo fue la última vez que hiciste algo absolutamente vergonzoso y te reíste solo?", 3),
        ("¿Cuál es la cosa que hacés regularmente que si la subís a redes cambiaría cómo te ven?", 3),
        ("¿Cuándo fue la última vez que rompiste una promesa y no te importó tanto como debería?", 3),
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
        if cat_id not in ADDITIONS15:
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

        for (text, level) in ADDITIONS15[cat_id]:
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
