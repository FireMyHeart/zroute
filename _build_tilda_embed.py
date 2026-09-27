# -*- coding: utf-8 -*-
"""Build three Tilda embed pages with hero language switcher + i18n."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
html = (ROOT / "index.html").read_text(encoding="utf-8")
raw_css = (ROOT / "css" / "styles.css").read_text(encoding="utf-8")
ASSET_BASE = "https://raw.githubusercontent.com/FireMyHeart/zroute/main/"

LANG_HTML = """
      <div class="lang hero-lang" role="group" aria-label="Language">
        <button type="button" data-lang="ru" class="active">RU</button>
        <button type="button" data-lang="en">EN</button>
        <button type="button" data-lang="es">ES</button>
        <button type="button" data-lang="pl">PL</button>
        <button type="button" data-lang="cs">CS</button>
      </div>
"""


def prefix_selector(sel: str) -> str:
    sel = sel.strip()
    if not sel:
        return sel
    parts = [p.strip() for p in sel.split(",")]
    result = []
    for p in parts:
        if p.startswith("@"):
            result.append(p)
            continue
        if p == ":root":
            result.append("#zroute-guide")
        elif p == "html":
            result.append("#zroute-guide")
        elif p == "body":
            result.append("#zroute-guide")
        elif p.startswith("body."):
            result.append("#zroute-guide" + p[4:])
        elif p.startswith("body "):
            result.append("#zroute-guide" + p[4:])
        elif p == "*":
            result.append("#zroute-guide, #zroute-guide *")
        elif p.startswith("#zroute-guide"):
            result.append(p)
        else:
            result.append("#zroute-guide " + p)
    return ", ".join(result)


def process_css(text: str) -> str:
    i = 0
    n = len(text)
    scoped = []
    while i < n:
        if text.startswith("/*", i):
            end = text.find("*/", i + 2)
            if end == -1:
                break
            scoped.append(text[i : end + 2])
            i = end + 2
            continue
        if text[i].isspace():
            scoped.append(text[i])
            i += 1
            continue
        if (
            text.startswith("@media", i)
            or text.startswith("@keyframes", i)
            or text.startswith("@supports", i)
        ):
            brace_pos = text.find("{", i)
            header = text[i:brace_pos]
            depth = 0
            j = brace_pos
            while j < n:
                if text[j] == "{":
                    depth += 1
                elif text[j] == "}":
                    depth -= 1
                    if depth == 0:
                        j += 1
                        break
                j += 1
            block = text[brace_pos + 1 : j - 1]
            scoped.append(header + "{")
            scoped.append(process_css(block))
            scoped.append("}")
            i = j
            continue
        brace_pos = text.find("{", i)
        if brace_pos == -1:
            scoped.append(text[i:])
            break
        selectors = text[i:brace_pos]
        depth = 0
        j = brace_pos
        while j < n:
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    j += 1
                    break
            j += 1
        rule_body = text[brace_pos:j]
        sel = selectors.strip()
        # Keep .lang styles; drop header/nav chrome
        if any(token in sel for token in (".topbar", ".brand", ".site-nav")):
            i = j
            continue
        if sel.startswith("@"):
            scoped.append(selectors + rule_body)
        else:
            scoped.append(prefix_selector(selectors) + rule_body)
        i = j
    return "".join(scoped)


extra_css = """
/* Tilda embed: scoped guide block */
#zroute-guide {
  position: relative;
  isolation: isolate;
  -webkit-text-size-adjust: 100%;
  min-height: 0;
  box-sizing: border-box;
}
#zroute-guide .page {
  padding-top: 0.25rem;
}
/* Language switcher over hero, top-right at eyebrow level */
#zroute-guide .hero-lang {
  position: absolute;
  z-index: 2;
  top: clamp(1.25rem, 4vw, 2.25rem);
  right: clamp(1.25rem, 4vw, 2.25rem);
  justify-content: flex-end;
  max-width: calc(100% - 2.5rem);
}
@media (max-width: 560px) {
  #zroute-guide .hero-content {
    padding-top: 3.25rem;
  }
  #zroute-guide .hero-lang {
    top: 0.85rem;
    right: 0.85rem;
  }
}
"""

css = extra_css + "\n" + process_css(raw_css)
css += """
#zroute-guide {
  /* Отступ под фиксированный хедер сайта (80px) */
  padding-top: 80px !important;
}
/* Lightbox: не заезжать под хедер Tilda */
#zroute-guide .lightbox {
  padding-top: calc(80px + 1.25rem);
  padding-bottom: 1.25rem;
  padding-left: 1.25rem;
  padding-right: 1.25rem;
  align-items: center;
  justify-items: center;
}
#zroute-guide .lightbox img {
  max-height: calc(100vh - 80px - 2.5rem);
}
#zroute-guide .lightbox-close {
  top: calc(80px + 0.85rem);
}
"""

# Extract I18N object from original script
i18n_m = re.search(r"const I18N = (\{.*?\});\s*\n\s*document\.querySelectorAll", html, re.S)
if not i18n_m:
    raise SystemExit("I18N object not found in index.html")
I18N_JS = i18n_m.group(1)

body = re.search(r"<body>(.*)</body>", html, re.S).group(1)
body = re.sub(r'<header class="topbar">.*?</header>\s*', "", body, flags=re.S)
body = re.sub(r"<script>.*?</script>\s*", "", body, flags=re.S)
# Keep data-i18n* attributes for translations
body = body.replace('aria-label="Close"', 'aria-label="Закрыть"')
body = body.replace("url('assets/", f"url('{ASSET_BASE}assets/")
body = body.replace('src="assets/', f'src="{ASSET_BASE}assets/')

panels = {}
for key in ("teleport", "format", "promo"):
    m = re.search(
        rf'(<div class="wrap page" id="page-{key}"[^>]*>.*?</div>\s*)(?=<div class="wrap page"|<footer>|$)',
        body,
        re.S,
    )
    if not m:
        raise SystemExit(f"panel not found: {key}")
    panel = m.group(1)
    panel = re.sub(r"\s+hidden(?=[\s>])", "", panel, count=1)
    panel = re.sub(r'\s+data-page-panel="[^"]*"', "", panel)
    # Insert lang switcher inside hero (first hero only)
    panel = panel.replace(
        '<section class="hero"',
        '<section class="hero"',
        1,
    )
    # After opening hero tag + attrs + >, inject lang before hero-content
    panel = re.sub(
        r'(<section class="hero"[^>]*>)',
        r"\1" + LANG_HTML,
        panel,
        count=1,
    )
    panels[key] = panel

footer_m = re.search(r"(<footer>.*?</footer>)", body, re.S)
footer = footer_m.group(1) if footer_m else ""
lightbox_m = re.search(r'(<div class="lightbox".*?</div>\s*)', body, re.S)
lightbox = lightbox_m.group(1) if lightbox_m else ""

COPY_ICON = (
    '\'<span class="icon-copy" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" '
    'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
    '<rect x="9" y="9" width="13" height="13" rx="2"/>'
    '<path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg></span>\' + '
    '\'<span class="icon-check" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" '
    'fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M20 6 9 17l-5-5"/></svg></span>\''
)

COMMON_JS_HEAD = f"""
<script>
(function () {{
  var root = document.getElementById("zroute-guide");
  if (!root) return;

  var ASSET_BASE = "{ASSET_BASE}";
  var I18N = {I18N_JS};

  function seedRuFromDom() {{
    root.querySelectorAll("[data-i18n]").forEach(function (el) {{
      var key = el.getAttribute("data-i18n");
      if (!key || el.classList.contains("has-image")) return;
      if (I18N.ru[key] == null) I18N.ru[key] = el.textContent;
    }});
    root.querySelectorAll("[data-i18n-html]").forEach(function (el) {{
      var key = el.getAttribute("data-i18n-html");
      if (!key) return;
      if (I18N.ru[key] == null) I18N.ru[key] = el.innerHTML;
    }});
  }}

  function applyPlaceAlts(dict) {{
    root.querySelectorAll("[data-i18n-alt]").forEach(function (el) {{
      var key = el.getAttribute("data-i18n-alt");
      if (dict[key] != null) el.alt = dict[key];
    }});
  }}

  function refreshCopyButtons(dict) {{
    root.querySelectorAll(".copy-btn").forEach(function (btn) {{
      if (!btn.classList.contains("copied") && !btn.classList.contains("icon-only")) {{
        btn.textContent = dict.copyBtn || "Copy";
      }}
    }});
  }}

  function applyLang(lang) {{
    var dict = I18N[lang] || I18N.ru;
    root.setAttribute("lang", lang);
    root.querySelectorAll("[data-i18n]").forEach(function (el) {{
      var key = el.getAttribute("data-i18n");
      if (dict[key] != null && !el.classList.contains("has-image")) {{
        el.textContent = dict[key];
      }}
    }});
    root.querySelectorAll("[data-i18n-html]").forEach(function (el) {{
      var key = el.getAttribute("data-i18n-html");
      if (dict[key] != null) el.innerHTML = dict[key];
    }});
    root.querySelectorAll(".lang button").forEach(function (btn) {{
      btn.classList.toggle("active", btn.getAttribute("data-lang") === lang);
    }});
    root.querySelectorAll(".promo-copy.icon-only").forEach(function (btn) {{
      btn.setAttribute("aria-label", dict.copyCodeAria || "Copy code");
    }});
    applyPlaceAlts(dict);
    try {{ localStorage.setItem("guide-lang", lang); }} catch (e) {{}}
    refreshCopyButtons(dict);
  }}

  var lightbox = root.querySelector("#lightbox");
  var lightboxImg = root.querySelector("#lightbox-img");
  var lightboxClose = root.querySelector("#lightbox-close");

  function openLightbox(src, alt) {{
    if (!lightbox || !lightboxImg) return;
    lightboxImg.src = src;
    lightboxImg.alt = alt || "";
    lightbox.hidden = false;
    root.classList.add("lightbox-open");
    document.body.classList.add("lightbox-open");
  }}

  function closeLightbox() {{
    if (!lightbox || !lightboxImg) return;
    lightbox.hidden = true;
    lightboxImg.removeAttribute("src");
    root.classList.remove("lightbox-open");
    document.body.classList.remove("lightbox-open");
  }}

  if (lightboxClose) lightboxClose.addEventListener("click", closeLightbox);
  if (lightbox) {{
    lightbox.addEventListener("click", function (e) {{
      if (e.target === lightbox) closeLightbox();
    }});
  }}
  document.addEventListener("keydown", function (e) {{
    if (e.key === "Escape" && lightbox && !lightbox.hidden) closeLightbox();
  }});

  async function copyText(text, btn) {{
    var lang = "ru";
    try {{ lang = localStorage.getItem("guide-lang") || "ru"; }} catch (e) {{}}
    var dict = I18N[lang] || I18N.ru;
    var iconOnly = btn.classList.contains("icon-only");
    try {{
      if (navigator.clipboard && window.isSecureContext) {{
        await navigator.clipboard.writeText(text);
      }} else {{
        var ta = document.createElement("textarea");
        ta.value = text;
        ta.setAttribute("readonly", "");
        ta.style.position = "fixed";
        ta.style.left = "-9999px";
        document.body.appendChild(ta);
        ta.select();
        document.execCommand("copy");
        document.body.removeChild(ta);
      }}
      btn.classList.add("copied");
      if (!iconOnly) btn.textContent = dict.copiedBtn || "Copied";
      clearTimeout(btn._copyTimer);
      btn._copyTimer = setTimeout(function () {{
        btn.classList.remove("copied");
        if (!iconOnly) btn.textContent = dict.copyBtn || "Copy";
      }}, 1600);
    }} catch (err) {{
      if (!iconOnly) btn.textContent = "Error";
    }}
  }}

  root.querySelectorAll(".copy-btn").forEach(function (btn) {{
    btn.addEventListener("click", function () {{
      copyText(btn.getAttribute("data-copy") || "", btn);
    }});
  }});

  root.querySelectorAll(".lang button").forEach(function (btn) {{
    btn.addEventListener("click", function () {{
      applyLang(btn.getAttribute("data-lang"));
    }});
  }});

  function tryLoadScreenshots(shotFiles) {{
    root.querySelectorAll(".shot[data-shot]").forEach(function (box) {{
      var id = box.getAttribute("data-shot");
      var src = shotFiles[id];
      if (!src) return;
      var img = new Image();
      img.onload = function () {{
        box.classList.add("has-image");
        box.innerHTML = "";
        img.alt = "";
        img.title = "Click to enlarge";
        box.appendChild(img);
        box.addEventListener("click", function () {{ openLightbox(src, img.alt); }});
      }};
      img.src = src;
    }});
  }}

  function bindZoomable() {{
    root.querySelectorAll("img.zoomable").forEach(function (img) {{
      if (img.dataset.zoomBound) return;
      img.dataset.zoomBound = "1";
      img.addEventListener("click", function () {{
        openLightbox(img.currentSrc || img.src, img.alt);
      }});
    }});
  }}

  seedRuFromDom();
  var saved = null;
  try {{ saved = localStorage.getItem("guide-lang"); }} catch (e) {{}}
  var prefer = saved && I18N[saved] ? saved : "ru";
  applyLang(prefer);
"""

COMMON_JS_TAIL = """
})();
</script>
"""

PAGES = {
    "teleport": {
        "file": "tilda-embed-teleport-ru.html",
        "title": "Бесплатный телепорт",
        "js": f"""
  var shotFiles = {{
    1: ASSET_BASE + "assets/screenshots/01-vs.jpg",
    2: ASSET_BASE + "assets/screenshots/02-raid-tab.jpg",
    3: ASSET_BASE + "assets/screenshots/03-forward.jpg",
    4: ASSET_BASE + "assets/screenshots/04-enemy-map.jpg",
    5: ASSET_BASE + "assets/screenshots/05-combat-zone-back.png",
    6: ASSET_BASE + "assets/screenshots/06-home-align.jpg"
  }};
  tryLoadScreenshots(shotFiles);
  bindZoomable();
""",
    },
    "format": {
        "file": "tilda-embed-format-ru.html",
        "title": "Форматирование текста",
        "js": """
""",
    },
    "promo": {
        "file": "tilda-embed-promo-ru.html",
        "title": "Актуальные промокоды",
        "js": f"""
  var PROMO_CODES = [
    "VK110KQBR", "ZRTSML09", "OKTOBER26", "ZRR6666", "ZRR999", "ZR26PLAY",
    "ZRRKR617", "ZRDAD26", "LOUNGE619", "WELCOME26", "26CHOCO", "ZRRLW2AC",
    "ZRR2NX6Q", "ZR26ALLY", "ZRRVJ4YD", "ZRR0ZWEN", "ZRRC7WES", "VK100KLYS",
    "26SCHOOL", "ZRR2573Q", "DC65KZPW"
  ];
  var COPY_ICON_SVG = {COPY_ICON};

  function renderPromoCodes() {{
    var grid = root.querySelector("#promo-grid");
    if (!grid || grid.childElementCount) return;
    var lang = "ru";
    try {{ lang = localStorage.getItem("guide-lang") || "ru"; }} catch (e) {{}}
    var dict = I18N[lang] || I18N.ru;
    var frag = document.createDocumentFragment();
    PROMO_CODES.forEach(function (code) {{
      var item = document.createElement("div");
      item.className = "promo-item";
      var label = document.createElement("code");
      label.textContent = code;
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "promo-copy icon-only";
      btn.setAttribute("data-copy", code);
      btn.setAttribute("aria-label", dict.copyCodeAria || "Copy code");
      btn.innerHTML = COPY_ICON_SVG;
      btn.addEventListener("click", function () {{ copyText(code, btn); }});
      item.appendChild(label);
      item.appendChild(btn);
      frag.appendChild(item);
    }});
    grid.appendChild(frag);
  }}

  var shotFiles = {{
    p1: ASSET_BASE + "assets/screenshots/promo-01-profile.jpg",
    p2: ASSET_BASE + "assets/screenshots/promo-02-settings.jpg",
    p3: ASSET_BASE + "assets/screenshots/promo-03-enter-code.jpg",
    p4: ASSET_BASE + "assets/screenshots/promo-04-confirm.jpg"
  }};
  renderPromoCodes();
  tryLoadScreenshots(shotFiles);
""",
    },
}

for key, meta in PAGES.items():
    comment = f"""<!--
  Tilda HTML-блок: {meta["title"]}.
  Языки: RU / EN / ES / PL / CS (кнопки на hero, справа сверху).
  Картинки: GitHub raw ({ASSET_BASE}...).
-->
"""
    page_js = COMMON_JS_HEAD + meta["js"] + COMMON_JS_TAIL
    content = (
        comment
        + '<link rel="preconnect" href="https://fonts.googleapis.com" />\n'
        + '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n'
        + '<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet" />\n'
        + "<style>\n"
        + css
        + "\nbody.lightbox-open { overflow: hidden; }\n"
        + "</style>\n"
        + f'<div id="zroute-guide" lang="ru" data-page="{key}">\n'
        + panels[key]
        + "\n"
        + footer
        + "\n"
        + lightbox
        + page_js
        + "\n</div>\n"
    )
    out_path = ROOT / meta["file"]
    out_path.write_text(content, encoding="utf-8")
    text = content
    assert "site-nav" not in text
    assert "hero-lang" in text
    assert "data-lang" in text
    assert "I18N" in text
    assert "data-i18n" in text
    print("written", out_path.name, "bytes", out_path.stat().st_size)
