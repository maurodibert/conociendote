#!/usr/bin/env python3
"""Batch 18 - playful, unexpected, funny, light angle on all categories."""
import json

ADDITIONS18 = {
    "infancia": [
        ("¿Cuántas veces te chocaste con una puerta de vidrio de chico?", 1),
        ("¿Cuál fue el apodo más ridículo que te pusieron en la escuela?", 1),
        ("¿Cuántas veces lloraste porque 'no era justo' siendo que sí era justo?", 1),
        ("¿Cuál fue la cosa más exagerada que hiciste para llamar la atención de chico?", 1),
        ("¿Cuándo fue la primera vez que te caíste de manera espectacular?", 1),
        ("¿Cuál fue la excusa más absurda que inventaste para no hacer la tarea?", 1),
        ("¿Cuántas veces dijiste que no querías comer algo y después te lo comiste todo?", 1),
        ("¿Cuál fue la mentira más elaborada que construiste de chico?", 1),
        ("¿Cuál era la cosa que hacías que tus padres nunca supieron que hacías?", 1),
        ("¿Cuándo fue la primera vez que te dormiste en el acto de la escuela?", 1),
        ("¿Cuál fue el regalo de navidad que pediste y después nunca usaste?", 1),
        ("¿Cuál fue la frase de tus padres que más odiabas escuchar y que ahora decís?", 1),
        ("¿Cuándo fue la primera vez que le echaste la culpa a alguien más de algo tuyo?", 1),
        ("¿Cuándo fue la primera vez que fingiste estar dormido para escuchar una conversación?", 1),
        ("¿Cuándo fue la primera vez que algo que hiciste fue completamente al revés de lo que planeabas?", 2),
        ("¿Cuándo fue la primera vez que algo que creías que era serio resultó completamente gracioso después?", 2),
        ("¿Cuándo fue la primera vez que te metiste en un problema por querer ayudar?", 2),
        ("¿Cuándo fue la primera vez que te diste cuenta de que eras más parecido a tus padres de lo que querías?", 3),
        ("¿Qué parte de vos de chico que antes te avergonzaba hoy te da ternura?", 3),
        ("¿Cuándo fue la primera vez que algo de tu infancia que te parecía traumático te pareció gracioso?", 3),
    ],

    "futuro": [
        ("¿Si pudieras tener un robot asistente, qué le pedirías que hiciera primero?", 1),
        ("¿Cuál es la app que más desearías que existiera?", 1),
        ("¿Si tuvieras que elegir entre vivir 200 años o que todos tus sueños se cumplan en 50, qué elegirías?", 1),
        ("¿Si pudieras teleportarte a cualquier lugar del mundo ahora, adónde irías?", 1),
        ("¿Si el futuro incluyera colonias en Marte, irías?", 1),
        ("¿Si pudieras saber cómo va a terminar tu historia, querrías saberlo?", 1),
        ("¿Si pudieras eliminar una sola molestia cotidiana para siempre, cuál sería?", 1),
        ("¿Si en el futuro pudieras vivir 200 años pero solo si cambiás de personalidad, lo harías?", 1),
        ("¿Si pudieras programar tu vida perfecta para los próximos 10 años, cómo sería?", 1),
        ("¿Si tuvieras que apostar por una sola cosa que va a cambiar el mundo en los próximos 20 años, qué apostarías?", 1),
        ("¿Cuánto te gustaría que cambiara la tecnología en tu vida en los próximos 5 años?", 2),
        ("¿Si el futuro te ofreciera todo lo que querés pero a un costo que no esperás, lo aceptarías?", 2),
        ("¿Si pudieras dejar de envejecer a la edad que querés, a cuál elegirías?", 2),
        ("¿Si el futuro ideal fuera completamente diferente de lo que imaginabas, lo abrazarías?", 2),
        ("¿Si el futuro dependiera de algo que tenés que cambiar hoy, lo cambiarías?", 2),
        ("¿Si el futuro que querés requiere soltar todo lo que tenés ahora, lo soltarías?", 3),
        ("¿Si pudieras ver el futuro una sola vez, el de quién elegiría ver?", 3),
        ("¿Si el único camino al futuro que querés fuera diferente de lo que imaginabas, lo tomarías?", 3),
    ],

    "amor": [
        ("¿Cuál fue la cosa más ridícula que hiciste para impresionar a alguien que te gustaba?", 1),
        ("¿Cuándo fue la última vez que le mandaste un mensaje de amor al contacto equivocado?", 1),
        ("¿Cuándo fue la última vez que tu confesión de amor fue completamente mal interpretada?", 1),
        ("¿Cuál fue el plan romántico más elaborado que hiciste y salió completamente diferente?", 1),
        ("¿Cuándo fue la última vez que quedaste con alguien y llegaste demasiado temprano por los nervios?", 1),
        ("¿Cuál fue el chiste más malo que hiciste en una cita y funcionó de todas formas?", 1),
        ("¿Cuándo fue la última vez que usaste la excusa más absurda para hablarle a alguien que te gustaba?", 1),
        ("¿Cuándo fue la primera vez que te pusiste rojo sin querer frente a alguien?", 1),
        ("¿Cuándo fue la última vez que alguien te hizo pensar que te gustaba y resultó que no?", 1),
        ("¿Cuál fue la situación más incómoda que viviste en una primera cita?", 1),
        ("¿Cuándo fue la última vez que alguien te gustó y te comportaste completamente distinto a como querías?", 2),
        ("¿Cuándo fue la última vez que intentaste ser romántico y resultó completamente opuesto?", 2),
        ("¿Cuándo fue la última vez que el amor te hizo hacer algo que con la mente fría nunca harías?", 2),
        ("¿Cuándo fue la última vez que quedaste mal frente a alguien que te gustaba y no pudiste recuperarte?", 2),
        ("¿Cuándo fue la última vez que el amor te sorprendió en el momento menos esperado?", 2),
        ("¿Cuándo fue la última vez que el amor te hizo completamente irracional y te alegró?", 3),
        ("¿Cuándo fue la última vez que el amor fue exactamente lo que no esperabas y fue perfecto?", 3),
        ("¿Cuándo fue la última vez que el amor te derribó completamente y lo elegiste igual?", 3),
    ],

    "familia": [
        ("¿Cuál fue la discusión familiar más ridícula que recordás?", 1),
        ("¿Cuál fue la vez que toda la familia hizo algo completamente diferente a lo planeado y fue mejor?", 1),
        ("¿Cuándo fue la última vez que alguien de tu familia hizo algo tan inesperado que no pudiste creerlo?", 1),
        ("¿Cuándo fue la última vez que toda la familia se equivocó junta?", 1),
        ("¿Cuál fue el chiste familiar que ya no puede escuchar nadie pero igual lo cuentan?", 1),
        ("¿Cuándo fue la última vez que alguien de tu familia te sorprendió siendo completamente distinto a como lo conocías?", 1),
        ("¿Cuándo fue la última vez que la familia entera se rió de algo completamente inapropiado?", 1),
        ("¿Cuál fue la reunión familiar que salió completamente diferente a como debía y fue mejor así?", 1),
        ("¿Cuándo fue la última vez que un familiar hizo algo que todavía no entendés?", 1),
        ("¿Cuándo fue la última vez que toda la familia tuvo la misma reacción irracional ante algo?", 1),
        ("¿Cuándo fue la última vez que un familiar te conoció de una manera que te desconcertó?", 2),
        ("¿Cuándo fue la última vez que algo absurdo de tu familia te hizo quererlos más?", 2),
        ("¿Cuándo fue la última vez que un familiar fue la persona menos esperada que más ayudó?", 2),
        ("¿Cuándo fue la última vez que algo que parecía un desastre familiar terminó siendo un recuerdo perfecto?", 2),
        ("¿Cuándo fue la última vez que tu familia fue exactamente lo que necesitabas aunque no de la manera que esperabas?", 2),
        ("¿Cuándo fue la última vez que tu familia te enseñó algo que ningún libro podría enseñarte?", 3),
        ("¿Cuándo fue la última vez que la caos familiar fue la cosa más amorosa del mundo?", 3),
        ("¿Cuándo fue la última vez que elegiste a tu familia incluso cuando eran completamente irracionales?", 3),
    ],

    "amistades": [
        ("¿Cuál fue el plan de amigos más desastroso que terminó siendo perfecto?", 1),
        ("¿Cuándo fue la última vez que algo completamente estúpido con amigos se convirtió en un recuerdo legendario?", 1),
        ("¿Cuándo fue la última vez que un amigo hizo algo tan inesperado que no pudiste creerlo?", 1),
        ("¿Cuándo fue la última vez que el grupo de amigos tomó una decisión horrible unánimemente?", 1),
        ("¿Cuándo fue la última vez que hicieron algo completamente sin sentido y fue perfecto?", 1),
        ("¿Cuál fue la travesura más ridícula que hiciste con amigos?", 1),
        ("¿Cuándo fue la última vez que un amigo te hizo quedar mal frente a alguien y te reíste igual?", 1),
        ("¿Cuándo fue la última vez que el chiste interno de tu grupo fue completamente incomprensible para alguien de afuera?", 1),
        ("¿Cuándo fue la última vez que un plan con amigos falló catastróficamente y fue mejor que el plan original?", 1),
        ("¿Cuándo fue la última vez que alguien del grupo dijo algo que ya nadie puede olvidar?", 1),
        ("¿Cuándo fue la última vez que un amigo te conoció en un momento en que no querías ser conocido?", 2),
        ("¿Cuándo fue la última vez que la honestidad brutal de un amigo fue exactamente lo que necesitabas?", 2),
        ("¿Cuándo fue la última vez que el caos de una noche con amigos resultó ser el mejor recuerdo?", 2),
        ("¿Cuándo fue la última vez que un amigo te salvó de vos mismo sin que lo supieras?", 2),
        ("¿Cuándo fue la última vez que la locura de alguien fue el amor más grande?", 2),
        ("¿Cuándo fue la última vez que el grupo de amigos estuvo completamente equivocado y lo admitió?", 3),
        ("¿Cuándo fue la última vez que un amigo te dejó sin palabras de una manera completamente inesperada?", 3),
        ("¿Cuándo fue la última vez que la amistad fue exactamente lo que el manual no dice que debe ser?", 3),
    ],

    "exs": [
        ("¿Cuándo fue la ruptura más incómoda que viviste en un espacio pequeño?", 1),
        ("¿Cuándo fue la vez que tu ex apareció en el peor momento posible?", 1),
        ("¿Cuándo fue la primera vez que viste a un ex con alguien nuevo antes de estar listo?", 1),
        ("¿Cuándo fue la vez que encontraste algo de un ex y no sabías qué hacer con eso?", 1),
        ("¿Cuándo fue la vez que te encontraste con un ex y no supiste qué decir?", 1),
        ("¿Cuándo fue la vez que alguien te mandó un meme de un ex en el peor momento?", 1),
        ("¿Cuál fue la excusa más ridícula que inventaste para no ver a un ex?", 1),
        ("¿Cuándo fue la vez que te enteraste de algo de un ex en el peor contexto posible?", 1),
        ("¿Cuándo fue la vez que tu ex te mandó un mensaje en el momento más inoportuno?", 1),
        ("¿Cuándo fue la vez que algo de una relación pasada apareció cuando menos lo esperabas?", 1),
        ("¿Cuándo fue la última vez que algo de una relación pasada te hizo reír de la situación?", 2),
        ("¿Cuándo fue la última vez que algo que parecía un desastre de una relación resultó ser una lección perfecta?", 2),
        ("¿Cuándo fue la última vez que algo de una relación pasada que te pesaba de repente se hizo liviano?", 2),
        ("¿Cuándo fue la última vez que una relación pasada te dio una perspectiva completamente diferente de vos?", 2),
        ("¿Cuándo fue la última vez que perdonar a alguien del pasado fue más fácil de lo que esperabas?", 2),
        ("¿Cuándo fue la última vez que algo ridículo de una relación pasada te hizo entender algo profundo?", 3),
        ("¿Cuándo fue la última vez que el pasado amoroso fue más una comedia que un drama?", 3),
        ("¿Cuándo fue la última vez que lo que parecía el peor final fue el mejor comienzo?", 3),
    ],

    "personalidad": [
        ("¿Cuál es la cosa más ridícula que hacés cuando no hay nadie mirando?", 1),
        ("¿Cuándo fue la última vez que hiciste algo completamente irracional y te encantó?", 1),
        ("¿Cuál fue la vez que algo que dijiste fue interpretado completamente al revés de lo que querías decir?", 1),
        ("¿Cuándo fue la última vez que actuaste completamente diferente a como querías y resultó mejor?", 1),
        ("¿Cuál es la contradicción más grande que hay en tu carácter?", 1),
        ("¿Cuándo fue la última vez que algo absurdo tuyo resultó ser exactamente lo correcto?", 1),
        ("¿Cuándo fue la última vez que fallaste de la manera más inesperada y te reíste?", 1),
        ("¿Cuándo fue la última vez que algo completamente fuera de tu carácter te salió perfecto?", 1),
        ("¿Cuándo fue la última vez que dijiste la cosa menos esperada y fue exactamente lo correcto?", 1),
        ("¿Cuál es el hábito más raro que tenés que solo la gente más cercana conoce?", 1),
        ("¿Cuándo fue la última vez que alguien te describió de una manera que no reconocías pero era verdad?", 2),
        ("¿Cuándo fue la última vez que actuaste desde vos mismo sin ningún filtro y sorprendiste?", 2),
        ("¿Cuándo fue la última vez que algo que considerabas un defecto resultó ser exactamente lo que alguien necesitaba?", 2),
        ("¿Cuándo fue la última vez que algo tuyo que te parecía raro fue exactamente perfecto para alguien?", 2),
        ("¿Cuándo fue la última vez que tu carácter más irracional salvó una situación?", 2),
        ("¿Cuándo fue la última vez que algo completamente inesperado de vos fue tu mejor versión?", 3),
        ("¿Cuándo fue la última vez que la contradicción que hay en vos fue exactamente lo que alguien necesitaba ver?", 3),
        ("¿Cuándo fue la última vez que aceptaste algo de vos mismo que antes rechazabas y cambió todo?", 3),
    ],

    "miedos": [
        ("¿Cuál fue la vez que algo que te daba miedo resultó ser completamente inofensivo y estúpido?", 1),
        ("¿Cuándo fue la última vez que algo que parecía aterrador fue gracioso después?", 1),
        ("¿Cuándo fue la última vez que el miedo te hizo actuar de una manera que después te pareció ridícula?", 1),
        ("¿Cuándo fue la última vez que algo que te asustó fue exactamente lo que necesitabas?", 1),
        ("¿Cuándo fue la última vez que el miedo a algo resultó ser miedo a la versión más pequeña del problema?", 1),
        ("¿Cuándo fue la última vez que un miedo se convirtió en algo que hoy te parece gracioso?", 1),
        ("¿Cuándo fue la última vez que el miedo te hizo hacer algo que después te encantó?", 1),
        ("¿Cuándo fue la última vez que algo que te parecía aterrador fue completamente trivial para los demás?", 1),
        ("¿Cuándo fue la última vez que reíste de algo que antes te daba miedo?", 1),
        ("¿Cuándo fue la última vez que el miedo fue más pequeño de lo que te hacía creer?", 1),
        ("¿Cuándo fue la última vez que el miedo fue la señal de que ibas exactamente en la dirección correcta?", 2),
        ("¿Cuándo fue la última vez que el miedo fue más honesto que cualquier razón que podías darte?", 2),
        ("¿Cuándo fue la última vez que algo que temías fue exactamente lo que cambiaste todo para mejor?", 2),
        ("¿Cuándo fue la última vez que el miedo te salvó de algo peor?", 2),
        ("¿Cuándo fue la última vez que el miedo resultó ser la señal de que algo importaba profundamente?", 2),
        ("¿Cuándo fue la última vez que enfrentaste un miedo y descubriste que eras más grande que él?", 3),
        ("¿Cuándo fue la última vez que el miedo reveló algo de vos que de otra manera no hubieras visto?", 3),
        ("¿Cuándo fue la última vez que el miedo más irracional resultó ser el más legítimo?", 3),
    ],

    "logros": [
        ("¿Cuándo fue la última vez que algo que intentaste falló de manera épica y fue genial de todas formas?", 1),
        ("¿Cuándo fue la última vez que algo que parecía un fracaso resultó ser un logro en disguise?", 1),
        ("¿Cuándo fue la última vez que algo que hiciste por accidente resultó ser lo mejor?", 1),
        ("¿Cuándo fue la última vez que lograste algo completamente diferente a lo que intentabas?", 1),
        ("¿Cuándo fue la última vez que algo que hiciste mal resultó mejor que hacerlo bien?", 1),
        ("¿Cuándo fue la última vez que el camino más inusual fue el que llegó primero?", 1),
        ("¿Cuándo fue la última vez que algo que no planeabas resultó ser tu mayor logro del año?", 1),
        ("¿Cuándo fue la última vez que el proceso fue mejor que el resultado?", 1),
        ("¿Cuándo fue la última vez que algo que empezaste por obligación terminó siendo lo que más amás?", 1),
        ("¿Cuándo fue la última vez que lograste algo importante completamente diferente de como lo imaginabas?", 1),
        ("¿Cuándo fue la última vez que un fracaso fue más rico en aprendizajes que un éxito?", 2),
        ("¿Cuándo fue la última vez que algo que considerabas un fracaso fue visto como un logro por alguien más?", 2),
        ("¿Cuándo fue la última vez que el logro fue completamente inesperado y por eso valió el doble?", 2),
        ("¿Cuándo fue la última vez que algo que hiciste fue absurdo en el proceso pero brillante en el resultado?", 2),
        ("¿Cuándo fue la última vez que la ruta más complicada fue exactamente la correcta?", 2),
        ("¿Cuándo fue la última vez que un logro tuyo fue el resultado de no tener ningún plan?", 3),
        ("¿Cuándo fue la última vez que algo que lograste fue completamente diferente a lo que esperabas y mejor?", 3),
        ("¿Cuándo fue la última vez que lo inesperado fue exactamente el logro que necesitabas?", 3),
    ],

    "sinFiltro": [
        ("¿Cuántas veces al día fingís prestar atención cuando en realidad estás en otro planeta?", 1),
        ("¿Cuántas veces por semana te reís de algo que nadie más vio?", 1),
        ("¿Cuándo fue la última vez que mandaste un audio sin escucharlo antes y te arrepentiste?", 1),
        ("¿Cuántas veces por mes decís 'qué buena idea' de algo que nunca vas a hacer?", 1),
        ("¿Cuándo fue la última vez que te quedaste callado cuando definitivamente debías hablar?", 1),
        ("¿Cuántas veces por semana buscás algo en Google que no le contarías a nadie?", 1),
        ("¿Cuándo fue la última vez que hiciste algo ridículo en privado y te sentiste completamente bien?", 1),
        ("¿Cuántas veces te reíste de un chiste que después te pareció que no debías haberlo contado?", 1),
        ("¿Cuándo fue la última vez que lo que más te hizo reír fue completamente inapropiado?", 1),
        ("¿Cuántas veces al mes hacés algo que si lo pusieras en una historia, nadie le creería?", 1),
        ("¿Cuándo fue la última vez que algo que hiciste fue completamente irracional y te alegró de todas formas?", 2),
        ("¿Cuándo fue la última vez que algo que te avergüenza confesarlo fue exactamente lo que necesitabas?", 2),
        ("¿Cuándo fue la última vez que actuaste completamente fuera de tu personaje público y fue un alivio?", 2),
        ("¿Cuándo fue la última vez que algo que hacés en secreto resultó ser exactamente lo más sano?", 2),
        ("¿Cuándo fue la última vez que algo que pensabas que era solo tuyo resultó ser universal?", 2),
        ("¿Cuándo fue la última vez que te dejaste completamente ver en toda tu rareza y fue la mejor decisión?", 3),
        ("¿Cuándo fue la última vez que algo de vos que escondías resultó ser exactamente lo que alguien más necesitaba?", 3),
        ("¿Cuándo fue la última vez que la versión más genuina de vos fue exactamente la versión que el mundo más apreció?", 3),
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
        if cat_id not in ADDITIONS18:
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

        for (text, level) in ADDITIONS18[cat_id]:
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
