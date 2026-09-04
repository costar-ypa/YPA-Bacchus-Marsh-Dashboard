from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

css = '''\n<style id="smooth-carousel-style">\n.property-card .card-photo img{\n  transition: opacity .28s ease, transform .42s cubic-bezier(.22,.61,.36,1);\n  transform: scale(1.015);\n  opacity: 1;\n  will-change: opacity, transform;\n}\n.property-card .card-photo img.carousel-fading{\n  opacity: 0;\n  transform: scale(1.03);\n}\n</style>\n'''

js = r'''\n<script id="smooth-carousel-script">\n(function(){\n  const originalUpdate = window.updateCardCarousel;\n  if(typeof originalUpdate !== 'function') return;\n\n  window.updateCardCarousel = function(h){\n    if(!h) return;\n    const id = normaliseId(h.id);\n    const carousel = cardCarousels[id];\n    if(!carousel || !carousel.photos || !carousel.photos.length) return;\n\n    const img = document.getElementById(`img-${id}`);\n    const target = carousel.photos[Math.max(0, Math.min(carousel.index || 0, carousel.photos.length - 1))];\n\n    if(!img || !target || img.src === target){\n      originalUpdate(h);\n      return;\n    }\n\n    if(img.dataset.carouselAnimating === '1') return;\n    img.dataset.carouselAnimating = '1';\n    img.classList.add('carousel-fading');\n\n    const preload = new Image();\n    preload.onload = preload.onerror = function(){\n      setTimeout(function(){\n        originalUpdate(h);\n        requestAnimationFrame(function(){\n          requestAnimationFrame(function(){\n            img.classList.remove('carousel-fading');\n            img.dataset.carouselAnimating = '0';\n          });\n        });\n      }, 140);\n    };\n    preload.src = target;\n  };\n})();\n</script>\n'''

if 'id="smooth-carousel-style"' not in text:
    text = text.replace('</head>', css + '\n</head>', 1)

if 'id="smooth-carousel-script"' not in text:
    text = text.replace('</body>', js + '\n</body>', 1)

path.write_text(text, encoding='utf-8')
