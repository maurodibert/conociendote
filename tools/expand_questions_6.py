#!/usr/bin/env python3
"""Batch 6 - themes: spirituality, creativity, body, society, work, nature."""
import json

ADDITIONS6 = {
    "infancia": [
        ("¿Cuál fue la primera vez que alguien confió en vos un secreto importante?", 1),
        ("¿Cuál fue el regalo de Navidad que más esperabas y por qué?", 1),
        ("¿Tenías algún ritual de buenas noches en tu familia?", 1),
        ("¿Cuándo fue la primera vez que hiciste algo prohibido y saliste impune?", 1),
        ("¿Cuál fue la primera vez que sentiste que algo era completamente injusto?", 1),
        ("¿Cuándo fue la primera vez que te defendiste solo en el colegio?", 1),
        ("¿Cuál era el juego de palabras o adivinanza favorita de tu infancia?", 1),
        ("¿Cuándo fue la primera vez que sentiste nostalgia de algo que estaba pasando?", 1),
        ("¿Cuántas veces por semana ibas al kiosco o tienda cuando eras chico?", 1),
        ("¿Cuál era tu parte favorita del recreo?", 1),
        ("¿Había algo que dabas por sentado de chico que de adulto te parece un lujo?", 1),
        ("¿Cuándo fue la primera vez que cocinaste con tu madre o abuela?", 1),
        ("¿Cuándo fue la última vez que actuaste desde el mismo lugar que tu yo de 10 años?", 2),
        ("¿Cuál fue el primer libro que lograste entender y que cambió algo en vos?", 2),
        ("¿Hay algo de tu infancia que hoy te parece adorable pero que entonces te parecía serio?", 2),
        ("¿Cuándo empezaste a sentirte más responsable de tu vida?", 2),
        ("¿Cuál fue la primera vez que alguien adulto te trató con respeto como par?", 2),
        ("¿Cuándo fue la primera vez que te diste cuenta de que tus padres no lo sabían todo?", 2),
        ("¿Cuál fue el primer momento en que te sentiste verdaderamente libre?", 3),
        ("¿Hay algo de tu infancia que necesitabas que nadie te diera?", 3),
        ("¿Cuándo fue la primera vez que elegiste vos quién querías ser?", 3),
    ],

    "futuro": [
        ("¿Cuánto tiempo querés pasar en la naturaleza en tu vida futura?", 1),
        ("¿Cuánto querés que cambie tu relación con la tecnología en el futuro?", 1),
        ("¿Cuál es el proyecto creativo que más querés completar?", 1),
        ("¿Cuánto te importa el legado material que vas a dejar?", 1),
        ("¿Cómo querés que sea tu vida espiritual en 10 años?", 1),
        ("¿Qué tipo de relación querés con tu cuerpo en el futuro?", 1),
        ("¿Cuánto tiempo semanal querés dedicar a algo que te apasione?", 1),
        ("¿Cuál es la causa que más te gustaría haber apoyado activamente?", 1),
        ("¿Cómo querés relacionarte con el trabajo cuando seas mayor?", 1),
        ("¿Cuál es el tipo de comunidad en la que querés vivir?", 1),
        ("¿Cuánto querés viajar en comparación a como lo hacés ahora?", 1),
        ("¿Cuál es el idioma en el que más querés ser fluido?", 1),
        ("¿Cuál es el tipo de persona que querés que sea tu pareja en 10 años?", 2),
        ("¿Cuánto de tu futuro está en manos de decisiones que tenés que tomar hoy?", 2),
        ("¿Cuándo fue la última vez que cambió dramáticamente lo que querés?", 2),
        ("¿Cuánto de tu futuro imaginás solo y cuánto acompañado?", 2),
        ("¿Cuándo fue la última vez que te imaginaste en una vida completamente diferente?", 2),
        ("¿Hay algo que sabés que tenés que cambiar para que el futuro que querés sea posible?", 2),
        ("¿Qué versión de vos mismo serías si el miedo no existiera?", 3),
        ("¿Cuándo fue la última vez que creíste de verdad en tu propio potencial?", 3),
        ("¿Cuál es la decisión que más impacto tendría en tu futuro si la tomaras ahora?", 3),
    ],

    "amor": [
        ("¿Cuándo fue la primera vez que supiste que alguien te gustaba por cómo te hacía sentir?", 1),
        ("¿Cuál fue el primer año de pareja más difícil que viviste?", 1),
        ("¿Qué es lo que más extrañás de una relación que no tenés actualmente?", 1),
        ("¿Cuándo fue la última vez que hiciste algo puramente romántico sin esperar nada?", 1),
        ("¿Cuál es la cosa que más te hace sentir querido en una relación?", 1),
        ("¿Sos de los que dice lo que siente o esperás que lo adivinen?", 1),
        ("¿Cuándo fue la última vez que te sorprendiste a vos mismo siendo romántico?", 1),
        ("¿Cuál es la señal que te dice que una relación tiene futuro real?", 1),
        ("¿Cuándo fue la última vez que alguien te hizo sentir realmente visto?", 1),
        ("¿Cuál fue la primera pelea de pareja que recordás?", 1),
        ("¿Cuánto importa la amistad en una relación amorosa para vos?", 1),
        ("¿Cuándo fue la última vez que alguien se sacrificó por vos en una relación?", 1),
        ("¿Cuándo fue la última vez que te dejaste querer sin resistencia?", 2),
        ("¿Cuánto espacio necesitás en una relación para sentirte cómodo?", 2),
        ("¿Cuándo fue la última vez que una pareja te cambió una creencia que tenías?", 2),
        ("¿Cuánto de lo que buscás en el amor hoy cambió desde tu primera relación?", 2),
        ("¿Cuándo fue la última vez que alguien que amabas se fue y lo dejaste ir?", 2),
        ("¿Cuánto de tu felicidad en pareja depende de vos mismo vs. de la otra persona?", 2),
        ("¿Cuál es la forma de amor que más te costó recibir en la vida?", 3),
        ("¿Cuándo fue la última vez que te animaste a amar sin red de seguridad?", 3),
        ("¿Cuál es la diferencia entre el amor que imaginabas y el que viviste?", 3),
    ],

    "familia": [
        ("¿Cuál es la cosa que más extrañás de algún familiar que ya no está?", 1),
        ("¿Cuál fue la última vez que toda tu familia estuvo realmente presente?", 1),
        ("¿Cuál es la cosa que tu familia siempre creyó de vos que no es del todo cierta?", 1),
        ("¿Cuándo fue la última vez que te sentiste orgulloso de tu familia?", 1),
        ("¿Cuál es la historia de tu familia que más te gusta contar a extraños?", 1),
        ("¿Cuándo fue la última vez que tu familia hizo algo inesperadamente generoso?", 1),
        ("¿Cuál fue la crisis que unió más a tu familia?", 1),
        ("¿Cuándo fue la última vez que alguien de tu familia te sorprendió con quién era?", 1),
        ("¿Cuál es el chiste interno de tu familia que dura años?", 1),
        ("¿Cómo describe tu familia a los de afuera?", 1),
        ("¿Cuándo fue la última vez que un familiar te llamó solo para saber cómo estabas?", 1),
        ("¿Cuál fue el viaje familiar que salió completamente diferente a lo planeado?", 1),
        ("¿Cuándo fue la última vez que tu familia te dio exactamente lo que necesitabas?", 2),
        ("¿Cuánto de la manera en que te comunicás viene de tu familia?", 2),
        ("¿Hay algo de tu familia que te resulta difícil explicar a alguien de afuera?", 2),
        ("¿Cuándo fue la última vez que tu familia tuvo que adaptarse a algo tuyo?", 2),
        ("¿Cuánto de cómo amás hoy viene de cómo te amó tu familia?", 2),
        ("¿Cuándo fue la última vez que sentiste que tu familia te conocía de verdad?", 2),
        ("¿Cuándo fue la última vez que perdonaste a tu familia por algo que te costó mucho?", 3),
        ("¿Hay algo que tu familia nunca va a saber de vos? ¿Por qué?", 3),
        ("¿Cuándo fue la última vez que elegiste a alguien que no era tu familia como familia?", 3),
    ],

    "amistades": [
        ("¿Cuál fue el momento que más cimentó la amistad más importante que tenés?", 1),
        ("¿Cuándo fue la última vez que un amigo te dijo algo que no querías escuchar y tenía razón?", 1),
        ("¿Cuándo fue la última vez que sentiste genuinamente orgullo de un amigo?", 1),
        ("¿Hay alguna amistad que nació de una circunstancia muy poco probable?", 1),
        ("¿Cuál fue la primera vez que un amigo te pidió que guardaras un secreto importante?", 1),
        ("¿Cuándo fue la última vez que un amigo te hizo cambiar de opinión sobre algo?", 1),
        ("¿Cuándo fue la última vez que sentiste que tus amigos te conocían mejor que tu familia?", 1),
        ("¿Cuál fue la aventura más loca que viviste con amigos?", 1),
        ("¿Cuándo fue la última vez que un amigo te ayudó a tomar una decisión importante?", 1),
        ("¿Cuánto de tu humor actual viene de tus amigos?", 1),
        ("¿Cuándo fue la última vez que un amigo te hizo reír en el peor momento?", 1),
        ("¿Hay algún amigo cuya opinión valés por encima de la de cualquier otro?", 1),
        ("¿Cuándo fue la última vez que dijiste 'cuento contigo' y lo cumpliste?", 2),
        ("¿Cuándo fue la última vez que un amigo te pidió algo que te costó dar?", 2),
        ("¿Hay alguna amistad que mejoró después de una crisis?", 2),
        ("¿Cuándo fue la última vez que tuviste que elegir entre dos amigos?", 2),
        ("¿Cuánto de tu tiempo le dedicás a las amistades que más importan?", 2),
        ("¿Cuándo fue la última vez que reconociste que eras el amigo que fallaba?", 2),
        ("¿Cuál es la amistad más honesta que tenés y por qué es así?", 3),
        ("¿Cuándo fue la última vez que una amistad te reveló algo de vos mismo?", 3),
        ("¿Cuánto de quién sos viene de las personas que elegiste como amigos?", 3),
    ],

    "exs": [
        ("¿Cuándo fue la primera vez que te diste cuenta de que una relación te había cambiado?", 1),
        ("¿Hay algo de una relación pasada que recordás con pura alegría sin tristeza?", 1),
        ("¿Cuándo fue la primera vez que terminaste una relación y te sentiste aliviado?", 1),
        ("¿Cuándo fue la última vez que agradeciste algo de una relación que terminó mal?", 1),
        ("¿Cuál fue el momento más sincero que tuviste con un ex después de terminar?", 1),
        ("¿Cuándo fue la primera vez que entendiste qué había salido mal en una relación?", 1),
        ("¿Hay alguna ex relación que mirás y ves que fue exactamente lo que necesitabas en ese momento?", 1),
        ("¿Cuándo fue la última vez que te imaginaste cómo sería tu vida si una relación pasada hubiera funcionado?", 1),
        ("¿Cuándo fue la primera vez que te enamoraste de alguien que no encajaba en 'tu tipo'?", 1),
        ("¿Hay algún ex que te enseñó más sobre vos mismo que cualquier terapia?", 1),
        ("¿Cuándo fue la última vez que sentiste que superaste completamente algo del pasado amoroso?", 1),
        ("¿Cuándo fue la última vez que hablaste honestamente sobre cómo terminó algo?", 1),
        ("¿Cuándo fue la última vez que elegiste no repetir un patrón de una relación pasada?", 2),
        ("¿Cuánto peso tienen las relaciones pasadas en tu manera de confiar hoy?", 2),
        ("¿Cuándo fue la primera vez que reconociste tu responsabilidad en una ruptura?", 2),
        ("¿Cuánto de lo que fuiste en una relación pasada ya no sos?", 2),
        ("¿Cuándo fue la última vez que perdonaste a alguien del pasado sin necesitar que lo supiera?", 2),
        ("¿Cuándo fue la última vez que elegiste vos mismo en lugar de quedarte en algo que no te hacía bien?", 2),
        ("¿Cuál es la versión de vos mismo en el amor que ya no querés repetir?", 3),
        ("¿Cuándo fue la última vez que te animaste a empezar algo nuevo sabiendo el riesgo?", 3),
        ("¿Cuál es la cosa que más te costó aprender de tus relaciones pasadas?", 3),
    ],

    "personalidad": [
        ("¿Cuándo fue la última vez que hiciste algo solo porque te daba curiosidad?", 1),
        ("¿Cuántas personas en tu vida saben exactamente cómo sos en privado?", 1),
        ("¿Cuál es la cosa que más sorprende a la gente cuando te conoce mejor?", 1),
        ("¿Cuándo fue la última vez que cambiaste de opinión públicamente?", 1),
        ("¿Cuál es la forma en que preferís que te muestren que te aprecian?", 1),
        ("¿Cuándo fue la última vez que algo te sacudió lo suficiente para cambiar algo?", 1),
        ("¿Cuánto tiempo podés estar sin hacer nada y disfrutarlo?", 1),
        ("¿Cuál es la forma de trabajo que más te acomoda?", 1),
        ("¿Cuándo fue la última vez que hiciste algo que te parecía imposible?", 1),
        ("¿Cuál es el tipo de descanso que te recarga más?", 1),
        ("¿Cuándo fue la última vez que te sentiste completamente en sintonía con los que te rodeaban?", 1),
        ("¿Cuál fue la última vez que dijiste algo en voz alta que nunca antes habías dicho?", 1),
        ("¿Cuándo fue la última vez que te diste el permiso de no estar bien?", 2),
        ("¿Cuánto de tu humor como adulto viene de tus años más difíciles?", 2),
        ("¿Cuándo fue la última vez que elegiste incomodarte para crecer?", 2),
        ("¿Cuánto de vos mismo cambia dependiendo de con quién estás?", 2),
        ("¿Cuándo fue la última vez que alguien te vio de una manera que te hizo repensar algo?", 2),
        ("¿Cuánto de tu forma de ser viene de reaccionar a cómo otros te trataron?", 2),
        ("¿Cuándo fue la última vez que fuiste completamente honesto contigo mismo?", 3),
        ("¿Cuál es la versión de vos mismo que más te cuesta admitir que existe?", 3),
        ("¿Cuándo fue la última vez que elegiste cambiar algo de vos mismo de manera profunda?", 3),
    ],

    "miedos": [
        ("¿Cuál es el tipo de incertidumbre que más te cuesta tolerar?", 1),
        ("¿Cuándo fue la última vez que un miedo te hizo hacer algo que no querías?", 1),
        ("¿Le tenés miedo a la vejez? ¿A qué parte de ella?", 1),
        ("¿Cuándo fue la última vez que un miedo te paralizó físicamente?", 1),
        ("¿Cuál es la cosa que más te da miedo que te pase a vos?", 1),
        ("¿Cuándo fue la última vez que el miedo te protegió de algo real?", 1),
        ("¿Cuándo fue la última vez que reconociste que un miedo tuyo era infundado?", 1),
        ("¿Cuál es el tipo de pérdida que más te aterra?", 1),
        ("¿Cuándo fue la última vez que actuaste a pesar del miedo y te alegró haberlo hecho?", 1),
        ("¿Cuál es el miedo más contagioso que transmitís sin querer?", 1),
        ("¿Cuándo fue la última vez que el miedo fue tu mayor maestro?", 1),
        ("¿Hay algo que hacés para manejar el miedo en el momento que aparece?", 1),
        ("¿Cuándo fue la última vez que el miedo a fallar te impidió disfrutar de algo?", 2),
        ("¿Cuánto del miedo que sentís hoy es heredado de tus padres o entorno?", 2),
        ("¿Cuándo fue la última vez que un miedo se volvió una fortaleza?", 2),
        ("¿Cuánto miedo te genera el cambio en general?", 2),
        ("¿Cuándo fue la última vez que le pusiste nombre a un miedo que tenías sin identificar?", 2),
        ("¿Cuánto tiempo de tu día pensás en cosas que podrían salir mal?", 2),
        ("¿Cuál es el miedo que más te cuesta soltar aunque sepas que te hace daño?", 3),
        ("¿Cuándo fue la última vez que el miedo te hizo más pequeño de lo que sos?", 3),
        ("¿Si el miedo no existiera, qué serías capaz de hacer mañana mismo?", 3),
    ],

    "logros": [
        ("¿Cuándo fue la última vez que te felicitaste a vos mismo por algo pequeño?", 1),
        ("¿Cuál fue la primera vez que lograste algo que nadie más de tu entorno había hecho?", 1),
        ("¿Cuándo fue la última vez que alguien copió algo que hiciste?", 1),
        ("¿Cuál fue el logro que menos celebraste aunque merecía más reconocimiento?", 1),
        ("¿Cuándo fue la última vez que lograste algo que te parecía imposible hace 5 años?", 1),
        ("¿Cuál fue el proyecto que más te enseñó sobre tus propias limitaciones?", 1),
        ("¿Cuándo fue la última vez que un logro tuyo cambió la vida de alguien más?", 1),
        ("¿Cuándo fue la primera vez que ganaste algo que no esperabas ganar?", 1),
        ("¿Cuándo fue la última vez que algo que hiciste generó un resultado inesperadamente bueno?", 1),
        ("¿Cuál fue el obstáculo más difícil que tuviste que superar para llegar donde estás?", 1),
        ("¿Cuándo fue la última vez que hiciste algo que al principio te parecía demasiado difícil?", 1),
        ("¿Cuál fue el logro del que más se orgulleció tu familia?", 1),
        ("¿Cuándo fue la última vez que reconociste el logro de alguien con la misma generosidad que el tuyo?", 2),
        ("¿Cuánto de tus logros los disfrutás en el momento vs. en retrospectiva?", 2),
        ("¿Cuándo fue la última vez que fallaste y no te derrumbaste?", 2),
        ("¿Cuánto de lo que lograste fue el resultado de pedir ayuda?", 2),
        ("¿Cuándo fue la última vez que dejaste ir un logro para abrirte a algo mejor?", 2),
        ("¿Cuánto de vos mismo hay en cada logro que conseguiste?", 2),
        ("¿Cuál es el logro que más te costó aceptar que era tuyo?", 3),
        ("¿Cuándo fue la última vez que un logro te hizo sentir que todo tenía sentido?", 3),
        ("¿Qué necesitás soltar para poder lograr lo que más querés?", 3),
    ],

    "sinFiltro": [
        ("¿Cuántas veces al mes hacés algo que te daría vergüenza ponerlo en un estado?", 1),
        ("¿Cuántas personas en este grupo verías desnudas antes de a otras?", 1),
        ("¿Cuánto tiempo pasás en el baño más de lo necesario?", 1),
        ("¿Cuántas veces al día fingís estar ocupado cuando no lo estás?", 1),
        ("¿Cuál es la cosa más ridícula que compraste en Amazon a las 2 AM?", 1),
        ("¿Cuántas veces al mes dormís con la ropa del día anterior?", 1),
        ("¿Cuántos grupos de WhatsApp silenció permanentemente?", 1),
        ("¿Cuántas veces mandaste el mismo chiste a más de 5 personas?", 1),
        ("¿Cuál es la cosa que hacés en el auto que no harías frente a alguien?", 1),
        ("¿Cuántas veces usaste el baño de alguien y dejaste algo incómodo?", 1),
        ("¿Cuántas veces por semana comés algo parado frente a la heladera abierta?", 1),
        ("¿Cuál fue la cosa más extraña que buscaste en internet a la madrugada?", 1),
        ("¿Cuándo fue la última vez que usaste a alguien sin darte cuenta?", 2),
        ("¿Alguna vez te alegraste del fracaso de alguien y te avergonzaste después?", 2),
        ("¿Cuántas veces dijiste que estabas bien cuando estabas destruido?", 2),
        ("¿Cuándo fue la última vez que actuaste desde la arrogancia y no lo reconociste en el momento?", 2),
        ("¿Alguna vez chismeaste de alguien que tenías enfrente como si no estuviera?", 2),
        ("¿Cuándo fue la última vez que dijiste una verdad cruel y te disfrutaste diciéndola?", 2),
        ("¿Cuál es la cosa más escandalosa que hiciste y que contarías solo aquí?", 3),
        ("¿Cuándo fue la última vez que hiciste algo sabiendo que no estaba bien y lo hiciste igual?", 3),
        ("¿Cuál es la verdad más incómoda que tendrías que decirle a alguien de este grupo?", 3),
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
        if cat_id not in ADDITIONS6:
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

        for (text, level) in ADDITIONS6[cat_id]:
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
