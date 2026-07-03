📊 TheAmarillos ⚡ Performance Overview — 28 / 100
  
  🔴 Critical 1    🟡 Improvements 4    🟢 Polish 2
  
  ────────────────────────────────────────────────────────────────────
  
  Understanding
  
  Sitio web estático de una banda musical universitaria: una sola
  página HTML con audio, video e imágenes embebidos directamente. El
  peso total de los assets supera los 75 MB servidos de golpe al
  cargar la página.
  Scope note: src/index.js y imagenes.css/estilos.css no están
  enlazados en index.html — analizados pero excluidos del plan ya que
  no impactan al usuario final.
  
  ────────────────────────────────────────────────────────────────────
  
  ⚠️ Findings:
  
  🔴 Critical
  
    1. El video de fondo y todos los archivos MP3 se descargan al
  cargar la página — no hay preload controlado ni carga diferida.
  
        ↳ index.html líneas 158–162 (<audio>) y 172 (<video>) — ningún
  elemento tiene preload="none", por lo que el navegador inicia la
  descarga inmediatamente; ~46 MB de media bloqueando la carga
  inicial.
  
  🟡 Improvements
  
    1. Las imágenes PNG/GIF son demasiado pesadas y no están
  comprimidas.
  
        ↳ img/gif.gif (1.9 MB), img/mas-mas.gif (1.4 MB),
  imagenes.css/aea.gif (496 KB) — los GIFs podrían reemplazarse con
  WebP animado o video; los PNG con WebP estático, ahorrando 60–80% de
  peso.
  
    2. La imagen del favicon carga desde log2/of.png (2.4 MB) — un
  favicon de más de 2 MB es un desperdicio directo.
  
        ↳ index.html línea 7 — log2/of.png pesa 2.4 MB; debería ser un
  .ico o PNG de 32×32 px (≤5 KB).
  
    3. Seis imágenes del grupo se cargan todas de inmediato sin lazy
  loading.
  
        ↳ index.html líneas 180–185 (<img src="img/1.png"> …
  img/7.png) — agregar loading="lazy" hace que el navegador las
  postergue hasta que el usuario haga scroll.
  
    4. No hay ningún <link rel="preload"> ni orden de carga definida —
  la hoja de estilos y el favicon compiten con el HTML.
  
        ↳ index.html <head> — sin hints de recurso; el CSS crítico
  podría inlinearse o marcarse con preload para evitar
  render-blocking.
  
  🟢 Polish (Optional)
  
    1. Agregar width y height explícitos a las imágenes del grupo
  evita el layout shift (CLS) mientras cargan.
    2. El <video> no tiene poster — mostrar una imagen estática
  mientras el video no se carga mejora la percepción de velocidad.
  
  ────────────────────────────────────────────────────────────────────
  
  🗺️ Plan
  
  Phase 1 — Agregar preload="none" a todos los elementos <audio> y
  <video>
  Outcome: El navegador deja de descargar ~46 MB de media al cargar la
  página; la carga inicial cae drásticamente.
  Files: index.html
  Check: Abrir en navegador y verificar Network tab — audio/video no
  deben iniciar descarga hasta que el usuario presione play.
  
  Phase 2 — Corregir el favicon y añadir loading="lazy" a las imágenes
  de galería
  Outcome: Se eliminan 2.4 MB del bloqueo en <head> y las imágenes
  inferiores se cargan bajo demanda.
  Files: index.html
  Check: Network tab — of.png ya no aparece como recurso; imágenes de
  img/ solo cargan al hacer scroll.
  
  Phase 3 — Comprimir y convertir imágenes a WebP
  Outcome: Reducción estimada de 3–5 MB en assets de imagen (GIFs →
  WebP animado/video, PNGs → WebP).
  Files: img/*.png, img/*.gif, imagenes.css/aea.gif
  Check: Verificar visualmente que las imágenes se muestran
  correctamente en Chrome/Firefox.
  
  ────────────────────────────────────────────────────────────────────
  
  Any questions?
  If not, I'll start with Phase 1.
  
  🚀 Ready when you are.