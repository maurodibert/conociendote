#!/usr/bin/env python3
"""Batch 17 - hypotheticals, philosophy, legacy, identity, values."""
import json

ADDITIONS17 = {
    "infancia": [
        ("¿Cuándo fue la primera vez que alguien mayor te pidió consejo?", 1),
        ("¿Cuándo fue la primera vez que algo que leíste te cambió?", 1),
        ("¿Cuándo fue la primera vez que te quedaste sin dormir pensando en algo?", 1),
        ("¿Cuándo fue la primera vez que hiciste algo solo que antes hacías con ayuda?", 1),
        ("¿Cuándo fue la primera vez que elegiste quedarte cuando querías irte?", 1),
        ("¿Cuándo fue la primera vez que alguien reconoció algo tuyo frente a otros?", 1),
        ("¿Cuándo fue la primera vez que te diste cuenta de que el tiempo pasaba demasiado rápido?", 1),
        ("¿Cuándo fue la primera vez que hiciste algo solo porque querías, sin que nadie te lo pidiera?", 1),
        ("¿Cuándo fue la primera vez que alguien te trató como si ya fueras grande?", 1),
        ("¿Cuándo fue la primera vez que sentiste que tu opinión importaba?", 1),
        ("¿Cuándo fue la primera vez que cometiste un error grave y lo admitiste?", 2),
        ("¿Cuándo fue la primera vez que eligiste no hacer algo para no lastimar a alguien?", 2),
        ("¿Cuándo fue la primera vez que pusiste algo de tu vida en perspectiva?", 2),
        ("¿Cuándo fue la primera vez que algo que te parecía injusto resultó tener sentido después?", 2),
        ("¿Cuándo fue la primera vez que le pediste perdón a alguien de corazón?", 2),
        ("¿Cuándo fue la primera vez que sentiste que algo de vos era especial aunque nadie lo dijera?", 3),
        ("¿Qué parte de quien eras de chico te gustaría recuperar hoy?", 3),
        ("¿Cuándo fue la primera vez que entendiste que crecer tenía cosas que no querías perder?", 3),
    ],

    "futuro": [
        ("¿Si pudieras hacer una sola cosa que impactara a millones de personas, qué harías?", 1),
        ("¿Si tuvieras cinco años de vida asegurados, cómo los usarías?", 1),
        ("¿Si pudieras vivir de lo que más amás, qué sería?", 1),
        ("¿Si el dinero no fuera un límite, en qué pasarías el próximo año?", 1),
        ("¿Si supieras que en 10 años todo va a estar bien, qué riesgo tomarías hoy?", 1),
        ("¿Si pudieras elegir a quién ayudar con todo lo que sabés, a quién elegirías?", 1),
        ("¿Si pudieras volver atrás 5 años con lo que sabés ahora, qué cambiarías primero?", 1),
        ("¿Si mañana empezaras de cero, qué te llevarías y qué dejarías?", 1),
        ("¿Si pudieras vivir en otro siglo, en cuál vivirías y por qué?", 1),
        ("¿Si el éxito estuviera garantizado, qué intentarías?", 1),
        ("¿Si pudieras dejarle una sola enseñanza a alguien más joven, cuál sería?", 2),
        ("¿Si el legado fuera lo único que importara, qué querrías que recordaran de vos?", 2),
        ("¿Si el fracaso no existiera, qué harías diferente mañana?", 2),
        ("¿Si pudieras hablar con la persona que vas a ser en 20 años, qué le preguntarías?", 2),
        ("¿Si la única forma de crecer fuera a través del dolor, cuánto dolor estarías dispuesto a aceptar?", 2),
        ("¿Si pudieras vivir tu sueño más grande sin consecuencias, lo harías?", 3),
        ("¿Si supieras exactamente cuándo vas a morir, qué harías diferente hoy?", 3),
        ("¿Si el único límite fuera el que vos te ponés, qué seríass?", 3),
    ],

    "amor": [
        ("¿Si pudieras elegir a alguien con quien pasar el resto de tu vida, qué cualidad sería la primera que buscarías?", 1),
        ("¿Si el amor no doliera nunca, sería el mismo amor?", 1),
        ("¿Si pudieras borrar una ruptura de tu memoria, la borrarías?", 1),
        ("¿Si pudieras enamorarte a voluntad, lo harías?", 1),
        ("¿Si el amor te garantizara sufrimiento pero también la mayor alegría posible, lo elegirías igual?", 1),
        ("¿Si pudieras saber de antemano cuánto te va a durar una relación, querrías saberlo?", 1),
        ("¿Si el amor perfecto existiera, qué tendría que tener para que fuera perfecto para vos?", 1),
        ("¿Si pudieras elegir entre amor intenso breve o amor tranquilo largo, cuál elegirías?", 1),
        ("¿Si pudieras vivir el primer enamoramiento otra vez, lo harías?", 1),
        ("¿Si pudieras saber si alguien te ama de verdad, querrías saber la respuesta aunque fuera que no?", 1),
        ("¿Si el amor te exigiera cambiar algo fundamental de vos, lo cambiarías?", 2),
        ("¿Si pudieras elegir no enamorarte nunca más para no sufrir, lo elegirías?", 2),
        ("¿Si pudieras revivir un momento con alguien que ya no está en tu vida, cuál sería?", 2),
        ("¿Si pudieras decirle una sola cosa a alguien que amaste y ya no podés decirle, qué sería?", 2),
        ("¿Si el amor que diste siempre fuera correspondido, qué cambiaría en vos?", 2),
        ("¿Si pudieras elegir cuánto amar para nunca sufrir, cuánto elegirías?", 3),
        ("¿Si pudieras vivir sin amor para nunca perderlo, lo harías?", 3),
        ("¿Si el amor fuera la única respuesta a todo, qué preguntarías?", 3),
    ],

    "familia": [
        ("¿Si pudieras elegir una sola tradición familiar para transmitir, cuál sería?", 1),
        ("¿Si pudieras decirle una sola cosa a cada uno de tus padres, qué sería?", 1),
        ("¿Si pudieras agregar a alguien a tu familia, quién sería?", 1),
        ("¿Si pudieras revivir un momento familiar, cuál elegirías?", 1),
        ("¿Si tu familia pudiera verte tal y como sos realmente, qué pasaría?", 1),
        ("¿Si pudieras cambiar una sola cosa de cómo te criaron, qué cambiarías?", 1),
        ("¿Si pudieras darle algo a tu familia que nunca tuvo, qué sería?", 1),
        ("¿Si pudieras hablar con un abuelo que ya no está, qué le preguntarías?", 1),
        ("¿Si pudieras elegir el tipo de familia que tendrías, cómo sería?", 1),
        ("¿Si la familia que elegís fuera más importante que la de origen, quién sería tu familia?", 1),
        ("¿Si pudieras sanar una sola herida de tu historia familiar, cuál elegiría?", 2),
        ("¿Si pudieras pedirle una sola cosa a tu familia, qué pedirías?", 2),
        ("¿Si pudieras darle a tu familia algo que te faltó a vos de chico, qué darías?", 2),
        ("¿Si tu familia supiera todo de vos, cambiaría algo en tu relación con ellos?", 2),
        ("¿Si pudieras liberar a alguien de tu familia de algo que lo pesa, qué sería?", 2),
        ("¿Si pudieras decirle una sola verdad difícil a un familiar, a quién se la dirías y cuál sería?", 3),
        ("¿Si tu familia fuera un espejo de lo que sos, qué verías?", 3),
        ("¿Si la familia que construís fuera el legado más importante de tu vida, cómo la construirías?", 3),
    ],

    "amistades": [
        ("¿Si pudieras llamar a alguien en este momento, a quién llamarías y para qué?", 1),
        ("¿Si pudieras recuperar una amistad perdida, cuál recuperarías?", 1),
        ("¿Si pudieras tener un amigo perfecto, qué tendría?", 1),
        ("¿Si pudieras elegir con quién pasar el último día de tu vida, con quién estarías?", 1),
        ("¿Si pudieras darle a un amigo algo que nunca tuvo, qué darías?", 1),
        ("¿Si los amigos te conocieran de verdad, cambiaría algo en vuestra amistad?", 1),
        ("¿Si pudieras decirle una sola cosa a tu mejor amigo que nunca dijiste, qué sería?", 1),
        ("¿Si pudieras crear la tradición perfecta de amigos, cuál sería?", 1),
        ("¿Si pudieras elegir el tipo de amigo que querés ser, cómo serías?", 1),
        ("¿Si la amistad fuera el amor más importante de tu vida, qué cambiaría en cómo la vivís?", 1),
        ("¿Si pudieras pedirle perdón a un amigo sin consecuencias, lo harías?", 2),
        ("¿Si un amigo te dijera que lo decepcionaste, cómo reaccionarías?", 2),
        ("¿Si pudieras ser el amigo que alguien necesita pero no tiene, para quién lo harías?", 2),
        ("¿Si la amistad te exigiera cambiar algo de vos, lo cambiarías?", 2),
        ("¿Si pudieras sanar una amistad que está rota, cómo lo harías?", 2),
        ("¿Si la amistad fuera la única relación verdadera, cómo cambiaría tu vida?", 3),
        ("¿Si pudieras crear el amigo ideal sin que existiera, qué te diría en el peor momento?", 3),
        ("¿Si el amor y la amistad fueran lo mismo, qué cambiaría?", 3),
    ],

    "exs": [
        ("¿Si pudieras revivir un momento de una relación pasada, cuál sería?", 1),
        ("¿Si pudieras cambiar una sola cosa de cómo terminó tu relación más importante, qué cambiarías?", 1),
        ("¿Si pudieras hablar con tu ex más significativo sin consecuencias, qué le dirías?", 1),
        ("¿Si pudieras saber si tu ex está bien, querrías saberlo?", 1),
        ("¿Si el pasado amoroso no tuviera peso, cómo amarías diferente?", 1),
        ("¿Si pudieras borrar una sola relación de tu historia, la borrarías?", 1),
        ("¿Si pudieras darle las gracias a un ex por algo, a quién se las darías y por qué?", 1),
        ("¿Si pudieras pedirle perdón a un ex de corazón, lo harías?", 1),
        ("¿Si pudieras saber si una relación pasada hubiera funcionado si las circunstancias fueran diferentes, querrías saberlo?", 1),
        ("¿Si el amor que diste en cada relación fuera perfecto, cómo sería hoy?", 1),
        ("¿Si pudieras decirle algo a la persona que fuiste en tu relación más difícil, qué le dirías?", 2),
        ("¿Si pudieras elegir cargar con el dolor de una ruptura para siempre o no haberla vivido, qué elegirías?", 2),
        ("¿Si la relación más difícil que tuviste te hubiera dado exactamente lo que necesitabas, qué sería eso?", 2),
        ("¿Si el amor del pasado te preparara para algo del futuro, para qué te preparó?", 2),
        ("¿Si pudieras vivir de nuevo tu primera relación con lo que sabés ahora, la vivirías igual?", 2),
        ("¿Si pudieras escribirle una carta a tu ex más importante hoy, qué diría?", 3),
        ("¿Si todo el amor que diste en el pasado volviera de alguna manera, cómo lo recibirías?", 3),
        ("¿Si el dolor de una ruptura fue el precio de conocerte mejor, valió la pena?", 3),
    ],

    "personalidad": [
        ("¿Si pudieras cambiar una sola cosa de vos mismo de manera instantánea, qué sería?", 1),
        ("¿Si pudieras vivir un día siendo exactamente como querés ser, cómo sería?", 1),
        ("¿Si el mundo te viera tal y como sos, qué cambiaría?", 1),
        ("¿Si pudieras elegir tu legado, qué sería?", 1),
        ("¿Si pudieras hablar con tu yo de dentro de 20 años, qué te preguntaría?", 1),
        ("¿Si pudieras ser invisible por un día, qué harías?", 1),
        ("¿Si pudieras conocer tu propósito de vida de manera clara, querrías saberlo?", 1),
        ("¿Si pudieras eliminar un defecto tuyo, cuál sería?", 1),
        ("¿Si el mundo supiera algo tuyo que no sabe, qué cambiaría?", 1),
        ("¿Si pudieras vivir completamente alineado con tus valores, cómo sería tu día?", 1),
        ("¿Si pudieras elegir tu carácter de cero, qué conservarías?", 2),
        ("¿Si pudieras darle algo a quien vendrá después de vos, qué sería?", 2),
        ("¿Si pudieras vivir sin el juicio de los demás, qué harías diferente?", 2),
        ("¿Si la persona que querés ser te viera ahora, qué diría?", 2),
        ("¿Si pudieras elegir con qué parte de vos quedarte y cuál soltar, qué harías?", 2),
        ("¿Si quién sos fuera suficiente siempre, cómo vivirías diferente?", 3),
        ("¿Si pudieras conocer la versión más profunda de vos mismo, te gustaría lo que encontrarías?", 3),
        ("¿Si no hubiera nada que probar, quién serías?", 3),
    ],

    "miedos": [
        ("¿Si el miedo desapareciera por un día, qué harías primero?", 1),
        ("¿Si pudieras elegir no tener ningún miedo, lo harías?", 1),
        ("¿Si el miedo fuera tu mejor consejero, qué te diría?", 1),
        ("¿Si pudieras enfrentar tu mayor miedo con garantía de éxito, lo harías?", 1),
        ("¿Si el miedo al fracaso no existiera, cuántos intentos harías que hoy evitás?", 1),
        ("¿Si pudieras compartir tu mayor miedo con alguien sin consecuencias, lo compartirías?", 1),
        ("¿Si el miedo tuviera una voz, qué te diría?", 1),
        ("¿Si pudieras comprar valentía, cuánto pagarías?", 1),
        ("¿Si el miedo fuera información pura sin emoción, qué te estaría diciendo ahora mismo?", 1),
        ("¿Si el miedo desapareciera, qué versión de vos aparecería?", 1),
        ("¿Si pudieras ver tu mayor miedo de afuera, se vería diferente?", 2),
        ("¿Si el miedo fuera un amigo que te cuida demasiado, qué límites le pondrías?", 2),
        ("¿Si enfrentar tu mayor miedo cambiara todo, lo enfrentarías hoy?", 2),
        ("¿Si el miedo te enseñara sobre lo que más amás, qué te estaría mostrando?", 2),
        ("¿Si pudieras elegir el miedo que te queda, cuál sería?", 2),
        ("¿Si el miedo fuera el mapa hacia tu mejor versión, lo seguirías?", 3),
        ("¿Si el único camino hacia lo que más querés pasara por lo que más temés, lo tomarías?", 3),
        ("¿Si pudieran ver tu miedo más profundo, qué parte de vos revelaría?", 3),
    ],

    "logros": [
        ("¿Si pudieras elegir el legado más importante que vas a dejar, cuál sería?", 1),
        ("¿Si pudieras alcanzar una meta en 24 horas, cuál elegiría?", 1),
        ("¿Si el éxito estuviera garantizado, qué intentarías mañana mismo?", 1),
        ("¿Si pudieras darle tu mayor logro a alguien más, se lo darías?", 1),
        ("¿Si pudieras saber de antemano que algo va a funcionar, qué harías diferente?", 1),
        ("¿Si el trabajo que hacés fuera lo único que recordaran de vos, estarías conforme?", 1),
        ("¿Si pudieras aprender cualquier habilidad instantáneamente, cuál elegiría?", 1),
        ("¿Si el fracaso fuera imposible, qué proyecto empezarías mañana?", 1),
        ("¿Si pudieras vivir de tu mayor talento, cuál sería?", 1),
        ("¿Si pudieras elegir una sola cosa en la que ser el mejor del mundo, qué sería?", 1),
        ("¿Si pudieras elegir que te recuerden por una sola cosa, cuál sería?", 2),
        ("¿Si el éxito y la paz fueran incompatibles, cuál elegirías?", 2),
        ("¿Si pudieras saber el impacto exacto que tuviste en el mundo, querrías saberlo?", 2),
        ("¿Si lograr lo que más querés implicara sacrificar algo que amás, lo harías?", 2),
        ("¿Si el camino al éxito fuera diferente para vos que para todos los demás, lo seguirías igual?", 2),
        ("¿Si pudieras elegir entre el reconocimiento y el impacto real, cuál elegirías?", 3),
        ("¿Si el único logro que importara fuera el que nadie ve, cuál sería el tuyo?", 3),
        ("¿Si lo que lograste en silencio fuera tu legado, qué quedaría?", 3),
    ],

    "sinFiltro": [
        ("¿Si pudieras hacer una pregunta sin consecuencias a alguien de este grupo, cuál sería?", 1),
        ("¿Si pudieras saber un secreto de cualquiera de este grupo, de quién lo querrías saber?", 1),
        ("¿Si pudieras ser otro de los presentes por un día, a quién elegirías?", 1),
        ("¿Si pudieras decirle una verdad a cualquiera de este grupo sin que cambie nada, qué dirías?", 1),
        ("¿Si pudieras eliminar una persona de tu vida sin drama, lo harías? ¿A quién?", 1),
        ("¿Si pudieras saber lo que piensan realmente los demás de vos, querrías saberlo?", 1),
        ("¿Si pudieras vivir un día como alguien completamente diferente, quién elegiría?", 1),
        ("¿Si pudieras hacer algo escandaloso sin consecuencias, qué sería?", 1),
        ("¿Si pudieras leer la mente de alguien de este grupo por 10 segundos, a quién leerías?", 1),
        ("¿Si pudieran ver tu historial de búsquedas de la última semana, cómo reaccionarías?", 1),
        ("¿Si pudieras vivir sin filtros durante una semana, qué cambiaría en tus relaciones?", 2),
        ("¿Si pudieras hacer algo que la gente te reprocharía pero que vos sabés que está bien, lo harías?", 2),
        ("¿Si todos supieran lo que pensás en silencio, qué impacto tendría?", 2),
        ("¿Si pudieras ignorar completamente lo que piensa el mundo de vos, qué cambiaría primero?", 2),
        ("¿Si pudieras hacer algo que definitivamente nadie aprobaría pero que te haría feliz, lo harías?", 2),
        ("¿Si pudieras soltar toda la imagen que construiste, qué quedaría de vos?", 3),
        ("¿Si todos tus pensamientos más oscuros fueran conocidos, qué parte de vos cambiría?", 3),
        ("¿Cuánto de quien mostrás es quien realmente sos y cuánto es pura performance?", 3),
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
        if cat_id not in ADDITIONS17:
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

        for (text, level) in ADDITIONS17[cat_id]:
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
