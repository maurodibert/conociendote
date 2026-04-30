# Monument — Design System

Sistema de diseño para Conociéndote. Inspirado en Monument Valley: geométrico, isométrico, plano como ilustración. Claro, contemplativo, con profundidad generada por perspectiva y no por sombras reales.

---

## Filosofía

- **Light-first**: fondo cálido crema, nunca blanco puro
- **Isometría como profundidad**: la perspectiva 45° reemplaza el 3D real
- **Paleta desaturada + acentos nítidos**: base neutra, color como señal
- **Sin emojis**: íconos isométricos SVG geométricos, siempre
- **Movimiento contemplativo**: animaciones lentas, con peso, que respiran

---

## Tipografía

### Familias
| Rol | Fuente | Fallback |
|-----|--------|---------|
| UI principal | Geist Sans | `system-ui, sans-serif` |
| Monoespaciado / datos | Geist Mono | `monospace` |

### Escala
| Token | rem | px | Uso |
|-------|-----|----|-----|
| `text-5xl` | 3rem | 48px | Número de puntos hero, pregunta grande |
| `text-3xl` | 1.875rem | 30px | Heading de pantalla |
| `text-xl` | 1.25rem | 20px | Subheading, nombre de categoría |
| `text-base` | 1rem | 16px | Cuerpo por defecto |
| `text-sm` | 0.875rem | 14px | Labels, botones, secundario |
| `text-xs` | 0.75rem | 12px | Metadata, hints |

### Pesos
| Token | Valor | Uso |
|-------|-------|-----|
| `font-light` | 300 | Preguntas largas, texto secundario calmo |
| `font-normal` | 400 | Body, descripciones |
| `font-medium` | 500 | Labels, nombres |
| `font-semibold` | 600 | Botones, títulos de sección |
| `font-bold` | 700 | Headings grandes, puntos |

---

## Colores

### Backgrounds
| Token | Hex | Uso |
|-------|-----|-----|
| `bg-[#F2ECE4]` | #F2ECE4 | Fondo global (crema cálido) |
| `bg-[#E8E0D0]` | #E8E0D0 | Surface de cards |
| `bg-[#DDD4C2]` | #DDD4C2 | Surface elevada, inputs |
| `bg-[#D0C6B2]` | #D0C6B2 | Bordes, divisores |

### Colores de acento (Monument palette)
| Nombre | Hex base | Hex oscuro | Uso |
|--------|----------|------------|-----|
| Teal | `#6BB5B5` | `#4A9494` | Primario, selección activa |
| Rose | `#D4888A` | `#B56870` | Secundario, ex parejas, intensidad |
| Lavender | `#B5A8CE` | `#9487B5` | Sueños, futuro, espiritualidad |
| Gold | `#E8B86A` | `#CC9A4A` | Logros, familia, calidez |
| Sage | `#8FB5A4` | `#6E9487` | Amistades, naturaleza, calma |
| Mauve | `#C4A0A8` | `#A8808A` | Amor, romanticismo |
| Coral | `#E8906A` | `#CC7050` | Picante / Sin Filtro |
| Slate | `#8AAAB8` | `#6A8898` | Miedos, profundidad |

### Texto (jerarquía por opacidad sobre navy)
| Token | Uso |
|-------|-----|
| `text-[#1A2535]` | Texto principal |
| `text-[#1A2535]/80` | Body primario |
| `text-[#1A2535]/60` | Texto secundario |
| `text-[#1A2535]/40` | Subtítulos, hints |
| `text-[#1A2535]/25` | Disabled, muted |

### Sombras isométricas
| Token | Hex | Uso |
|-------|-----|-----|
| `bg-[#3A2558]` | #3A2558 | Sombra derecha (purple-deep) |
| `bg-[#1A2535]` | #1A2535 | Sombra inferior (navy-deep) |

### CSS Variables
```css
:root {
  --bg-base: #F2ECE4;
  --bg-surface: #E8E0D0;
  --bg-elevated: #DDD4C2;
  --border: #D0C6B2;
  --text: #1A2535;
  --teal: #6BB5B5;
  --teal-dark: #4A9494;
  --rose: #D4888A;
  --lavender: #B5A8CE;
  --gold: #E8B86A;
  --sage: #8FB5A4;
  --mauve: #C4A0A8;
  --coral: #E8906A;
  --slate: #8AAAB8;
  --iso-shadow-right: #3A2558;
  --iso-shadow-bottom: #1A2535;
}
```

---

## Perspectiva Isométrica

### La proyección base
```css
/* Isometría estándar: rotar sobre X e Y */
.iso {
  transform: rotateX(-30deg) rotateY(45deg);
  transform-style: preserve-3d;
}

/* Para SVGs: usar las fórmulas de proyección directamente */
/* x_iso = (x - y) * cos(30°) = (x - y) * 0.866 */
/* y_iso = (x + y) * sin(30°) - z = (x + y) * 0.5 - z */
```

### Estructura de un cubo isométrico CSS
```html
<div class="iso-cube">
  <div class="iso-face iso-top"><!-- cara superior --></div>
  <div class="iso-face iso-left"><!-- cara izquierda --></div>
  <div class="iso-face iso-right"><!-- cara derecha --></div>
</div>
```

```css
.iso-cube { position: relative; width: 60px; height: 60px; transform-style: preserve-3d; }
.iso-face  { position: absolute; width: 60px; height: 60px; }
.iso-top   { background: var(--color-top); transform: rotateX(90deg) translateZ(30px); }
.iso-left  { background: var(--color-left); transform: rotateY(-30deg) translateX(-15px) translateZ(15px); }
.iso-right { background: var(--color-right); transform: rotateY(30deg) translateX(15px) translateZ(15px); }
```

---

## Bordes y Radio

| Token | px | Uso |
|-------|----|-----|
| `rounded-none` | 0 | Tiles isométricos, formas geométricas |
| `rounded` | 4px | Inputs, badges pequeños |
| `rounded-lg` | 8px | Cards secundarias |
| `rounded-xl` | 12px | Cards principales, botones |
| `rounded-2xl` | 16px | Modales, overlays |

Bordes siempre en `border-[#D0C6B2]` o variante de color de la categoría con `/40`.

---

## Espaciado

| Contexto | Clases |
|---------|--------|
| Layout principal | `px-4 py-6` (mobile-first) |
| Max width | `max-w-md` (modal), `max-w-lg` (pantallas anchas) |
| Cards | `p-5` (principal), `p-4` (secundaria) |
| Gaps | `gap-3` (elementos), `gap-6` (secciones) |

---

## Animaciones

### Principios
- **Easing**: `ease-out` para entradas, `ease-in` para salidas, `spring` para elementos que "tienen peso"
- **Duración base**: 400ms para transiciones de pantalla, 200ms para feedback de tap

### Reveal de categoría (reemplaza ruleta)
```js
// Tiles en grid: entrada escalonada
initial={{ opacity: 0, scale: 0.8, y: 20 }}
animate={{ opacity: 1, scale: 1, y: 0 }}
transition={{ delay: index * 0.06, type: "spring", stiffness: 200, damping: 20 }}

// Shuffle (todos se mueven a posiciones random)
transition={{ duration: 0.15, ease: "easeInOut" }}

// Tile ganador: expand full screen
animate={{ scale: 20, opacity: 0 }}
transition={{ duration: 0.6, ease: [0.25, 0.46, 0.45, 0.94] }}
```

### Transición de pantalla
```js
initial={{ opacity: 0, y: 24 }}
animate={{ opacity: 1, y: 0 }}
exit={{ opacity: 0, y: -16 }}
transition={{ duration: 0.35, ease: "easeOut" }}
```

### Feedback de tap
```js
whileTap={{ scale: 0.96 }}
```

### Spring para elementos con peso
```js
transition={{ type: "spring", stiffness: 180, damping: 22 }}
```

---

## Componentes

### Tile isométrico (categoría)
```html
<!-- El tile es un cubo CSS con cara top visible -->
<div class="relative w-24 h-24 cursor-pointer group">
  <!-- Face top -->
  <div class="absolute inset-0 bg-[color] border border-[color]/40 rounded-sm">
    <!-- ícono isométrico SVG centrado -->
  </div>
  <!-- Shadow right (iso) -->
  <div class="absolute top-1 right-[-6px] w-1.5 h-full bg-[#3A2558]/30 skew-y-[30deg]" />
  <!-- Shadow bottom (iso) -->
  <div class="absolute bottom-[-6px] left-1 w-full h-1.5 bg-[#1A2535]/20 skew-x-[30deg]" />
</div>
```

### Botón primario
```html
<button class="w-full py-3.5 rounded-xl font-semibold text-sm bg-[#6BB5B5] hover:bg-[#4A9494] text-white transition-colors duration-200">
```

### Botón secundario
```html
<button class="w-full py-3.5 rounded-xl font-medium text-sm bg-[#E8E0D0] hover:bg-[#DDD4C2] text-[#1A2535]/70 border border-[#D0C6B2] transition-colors duration-200">
```

### Card principal
```html
<div class="bg-[#E8E0D0] border border-[#D0C6B2] rounded-2xl p-5">
```

### Badge de nivel
```html
<!-- Nivel 1 - Suave -->
<div class="px-3 py-1 rounded-full bg-[#6BB5B5]/15 border border-[#6BB5B5]/30">
  <span class="text-[#4A9494] text-xs font-medium">Suave</span>
</div>
<!-- Nivel 2 - Medio -->
<div class="px-3 py-1 rounded-full bg-[#E8B86A]/15 border border-[#E8B86A]/30">
  <span class="text-[#CC9A4A] text-xs font-medium">Medio</span>
</div>
<!-- Nivel 3 - Profundo -->
<div class="px-3 py-1 rounded-full bg-[#D4888A]/15 border border-[#D4888A]/30">
  <span class="text-[#B56870] text-xs font-medium">Profundo</span>
</div>
```

### Input de texto
```html
<input class="w-full bg-[#DDD4C2] border border-[#D0C6B2] rounded-xl px-4 py-3 text-[#1A2535] placeholder:text-[#1A2535]/30 text-sm focus:outline-none focus:border-[#6BB5B5] transition-colors duration-200">
```

### Barra de puntos (valentía)
```html
<div class="h-1.5 bg-[#D0C6B2] rounded-full overflow-hidden">
  <div class="h-full bg-[#6BB5B5] rounded-full transition-all duration-500" style="width: 65%" />
</div>
```

---

## Layout General (mobile-first)

```
min-h-screen bg-[#F2ECE4] text-[#1A2535] flex flex-col
  ├── <header> px-5 py-4 border-b border-[#D0C6B2]
  │     ├── Logo (left)
  │     └── Turno / puntos (right)
  ├── <main> flex-1 flex flex-col items-center justify-center px-4
  │     └── AnimatePresence > pantalla activa (max-w-md w-full)
  └── [sin footer visible — todo en pantalla]
```

---

## Categorías y su color

| Categoría | ID | Color | Hex |
|-----------|----|-------|-----|
| Infancia y Recuerdos | `infancia` | Rose | `#D4888A` |
| Sueños y Futuro | `futuro` | Lavender | `#B5A8CE` |
| Amor y Relaciones | `amor` | Mauve | `#C4A0A8` |
| Familia | `familia` | Gold | `#E8B86A` |
| Amistades | `amistades` | Sage | `#8FB5A4` |
| Ex Parejas | `exs` | Slate | `#8AAAB8` |
| Personalidad y Valores | `personalidad` | Teal | `#6BB5B5` |
| Miedos y Vergüenzas | `miedos` | Lavender oscuro | `#9487B5` |
| Logros y Fracasos | `logros` | Gold oscuro | `#CC9A4A` |
| Sin Filtro | `sinFiltro` | Coral | `#E8906A` |

---

## Paleta rápida

```
BG base:     #F2ECE4
BG surface:  #E8E0D0 · #DDD4C2
Border:      #D0C6B2
Texto:       #1A2535 → /80 → /60 → /40 → /25

Teal:        #6BB5B5 / #4A9494
Rose:        #D4888A / #B56870
Lavender:    #B5A8CE / #9487B5
Gold:        #E8B86A / #CC9A4A
Sage:        #8FB5A4 / #6E9487
Mauve:       #C4A0A8 / #A8808A
Coral:       #E8906A / #CC7050
Slate:       #8AAAB8 / #6A8898

ISO shadow:  #3A2558 (right) · #1A2535 (bottom)
```
