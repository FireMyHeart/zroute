# -*- coding: utf-8 -*-
"""One-shot patcher: add i18n to mission-ready.html like tilda guides."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "tilda" / "mission-ready.html"
text = PATH.read_text(encoding="utf-8")

LANG_CSS = """
.lang {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
  justify-content: flex-end;
}
.lang button {
  appearance: none;
  border: 1px solid rgba(255, 140, 66, 0.25);
  background: rgba(255, 255, 255, 0.03);
  color: #a89a8d;
  font: inherit;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  padding: 0.4rem 0.55rem;
  border-radius: 999px;
  cursor: pointer;
  transition: 0.2s ease;
}
.lang button:hover {
  color: #f3ebe3;
  border-color: rgba(255, 140, 66, 0.55);
}
.lang button.active {
  color: #1a0f08;
  background: linear-gradient(135deg, #ffb347, #ff8c42);
  border-color: transparent;
  box-shadow: 0 0 18px rgba(255, 140, 66, 0.35);
}
@media (max-width: 560px) {
  .lang button { padding: 0.35rem 0.45rem; font-size: 0.68rem; }
}
"""

if ".lang button.active" not in text:
    text = text.replace(
        "html[data-theme=\"light\"] .theme-toggle .icon-moon { display: none; }\n@media (max-width: 560px) {\n  .hero-controls { top: 0.85rem; right: 0.85rem; }\n  .hero-content { padding-top: 3.25rem; }\n}",
        "html[data-theme=\"light\"] .theme-toggle .icon-moon { display: none; }\n"
        + LANG_CSS
        + "@media (max-width: 560px) {\n  .hero-controls { top: 0.85rem; right: 0.85rem; }\n  .hero-content { padding-top: 3.25rem; }\n}",
    )

HERO_CONTROLS = """      <div class="hero-controls">
        <button type="button" class="theme-toggle" id="theme-toggle" aria-label="Тема" title="Тема">
          <span class="icon-moon" aria-hidden="true">&#9790;</span>
          <span class="icon-sun" aria-hidden="true">&#9728;</span>
        </button>
        <div class="lang hero-lang" role="group" aria-label="Language">
          <button type="button" data-lang="ru" class="active">RU</button>
          <button type="button" data-lang="en">EN</button>
          <button type="button" data-lang="es">ES</button>
          <button type="button" data-lang="pl">PL</button>
          <button type="button" data-lang="cs">CS</button>
        </div>
      </div>"""

# Replace hero-controls block (without lang) if needed
import re
text = re.sub(
    r'<div class="hero-controls">\s*<button type="button" class="theme-toggle"[\s\S]*?</button>\s*</div>',
    HERO_CONTROLS,
    text,
    count=1,
)

BODY_MAIN = r'''      <div class="hero-content">
        <h1 data-i18n="heroTitle">Готовность к миссии</h1>
        <p data-i18n="heroLead">Короткий гайд по ГкМ: какие фазы закрывать, когда совмещать с VS и как не сливать ресурсы зря.</p>
      </div>
    </section>

    <main>
      <section class="panel" id="begin">
        <p data-i18n-html="beginIntro">ГкМ проходит каждые <strong>4 часа</strong> и даёт награды + очки Безумия экспедиции.</p>
        <div class="chips">
          <div class="chip">
            <small data-i18n="chipTimesLabel">⏰ Старт фаз по МСК:</small>
            <span>05:00 · 09:00 · 13:00 · 17:00 · 21:00 · 01:00</span>
          </div>
          <div class="chip">
            <small data-i18n="chipPhasesLabel">5 типов фаз:</small>
            <span data-i18n="chipPhasesValue">🏗 стройка · 🪖 солдаты · 🔬 исследования · ⚡ боец · ⭐ герой</span>
          </div>
        </div>
        <div class="hint" data-i18n-html="beginHint">
          💡 Не сливайте ресурсы только ради ГкМ. Самые дорогие задания совмещайте с нужным днём <strong>VS</strong> — одна трата даёт очки сразу в двух событиях.
        </div>
      </section>

      <h2 class="section-title" data-i18n="rewardsTitle">🎁 Награды</h2>
      <section class="panel">
        <p data-i18n-html="rewardsIntro">Цель дня — закрыть <strong>3 самые выгодные фазы</strong>, а не всё подряд. За это открываются ежедневные сундуки и награда за сами фазы.</p>
        <ul>
          <li>
            <span data-i18n="rewardsDailyLabel">Ежедневные сундуки:</span>
            <ul class="reward-lines">
              <li data-i18n="rewardsDaily1">🟡 2 золотых фрагмента</li>
              <li data-i18n="rewardsDaily2">🟣 7 фиолетовых фрагментов</li>
              <li data-i18n="rewardsDaily3">🎫 10 карт найма</li>
              <li data-i18n="rewardsDaily4">💎 350 алмазов</li>
            </ul>
          </li>
          <li>
            <span data-i18n="rewardsPhasesLabel">За 3 фазы:</span>
            <ul class="reward-lines">
              <li data-i18n="rewardsPhases1">📚 3600 книг навыков</li>
              <li data-i18n="rewardsPhases2">⌚ 150 ускорений ×5 мин</li>
              <li data-i18n="rewardsPhases3">📦 по 72 сундука пищи/металла/нефти</li>
              <li data-i18n="rewardsPhases4">🏅 18 ежедневных медалей</li>
            </ul>
          </li>
          <li data-i18n="rewardsPhaseChests">В каждой фазе попутно можно забрать до 4 сундуков (обнуляются каждые 4 часа) 👇</li>
        </ul>
        <p data-i18n="rewardsDiamondNote">Алмазами игра помечает ценность наград внутри.</p>
        <div class="shots shots-grid">
          <figure class="shot" data-full="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/rewards-overview.webp">
            <img src="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/rewards-overview.webp" alt="Награды ГкМ" data-i18n-alt="altRewardsOverview" loading="lazy" />
            <figcaption class="shot-caption" data-i18n="capRewardsOverview">Обзор наград</figcaption>
          </figure>
          <figure class="shot" data-full="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/rewards-daily.webp">
            <img src="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/rewards-daily.webp" alt="Ежедневные сундуки" data-i18n-alt="altRewardsDaily" loading="lazy" />
            <figcaption class="shot-caption" data-i18n="capRewardsDaily">3 ежедневных сундука</figcaption>
          </figure>
          <figure class="shot" data-full="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/rewards-phase-chests.webp">
            <img src="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/rewards-phase-chests.webp" alt="Сундуки фазы" data-i18n-alt="altRewardsPhase" loading="lazy" />
            <figcaption class="shot-caption" data-i18n="capRewardsPhase">Сундуки фазы</figcaption>
          </figure>
          <figure class="shot" data-full="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/rewards-medals.webp">
            <img src="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/rewards-medals.webp" alt="Медали за фазы" data-i18n-alt="altRewardsMedals" loading="lazy" />
            <figcaption class="shot-caption" data-i18n="capRewardsMedals">Медали и ресурсы</figcaption>
          </figure>
        </div>
      </section>

      <h2 class="section-title" data-i18n="phasesTitle">Фазы ГкМ</h2>

      <div class="accordion">
        <details class="acc" open>
          <summary>
            <span class="acc-num">1</span>
            <span class="acc-summary-text">
              <strong data-i18n="p1Title">🏗 Строительство базы</strong>
              <span data-i18n="p1Sub">🔥 Лучший день — вторник (совпадение с VS)</span>
            </span>
            <span class="acc-chevron" aria-hidden="true">▾</span>
          </summary>
          <div class="acc-body">
            <div class="score-grid">
              <div class="score-row"><span data-i18n="p1Score1L">⌚ 1 минута ускорения</span><strong data-i18n="p1Score1R">10 очков</strong></div>
              <div class="score-row"><span data-i18n="p1Score2L">🏗 +10 мощи здания</span><strong data-i18n="p1Score2R">1 очко</strong></div>
              <div class="score-example">
                <strong data-i18n="exampleLabel">Например:</strong>
                <p data-i18n-html="p1Ex1">1 час ускорений = <span class="pts">600 очков</span></p>
                <p data-i18n-html="p1Ex2">+1000 мощи здания = <span class="pts">100 очков</span></p>
              </div>
            </div>
            <div class="hint" data-i18n-html="p1Hint1">💡 Можно заранее построить здания и <strong>не нажимать галочки</strong>, пока не начнётся нужная фаза.</div>
            <div class="hint strong" data-i18n-html="p1Hint2">🔥 Во вторник прожимаем галочки готовых зданий.<br>❗ В другие дни не стоит сливать ускорения только ради ГкМ.</div>
            <div class="shots">
              <figure class="shot" data-full="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/phase-build.webp">
                <img src="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/phase-build.webp" alt="Фаза строительства" data-i18n-alt="altP1" loading="lazy" />
              </figure>
            </div>
          </div>
        </details>

        <details class="acc">
          <summary>
            <span class="acc-num">2</span>
            <span class="acc-summary-text">
              <strong data-i18n="p2Title">🪖 Обучение солдат</strong>
              <span data-i18n="p2Sub">Готовьте заранее · «лесенка» экономит ускорения</span>
            </span>
            <span class="acc-chevron" aria-hidden="true">▾</span>
          </summary>
          <div class="acc-body">
            <div class="score-grid">
              <div class="score-row"><span data-i18n="p2Score1L">⌚ 1 минута ускорения тренировок</span><strong data-i18n="p2Score1R">10 очков</strong></div>
              <div class="score-row"><span data-i18n="p2Score2L">💎 1 алмаз набора</span><strong data-i18n="p2Score2R">30 очков</strong></div>
            </div>
            <p data-i18n="p2ScaleLabel">🪖 Шкала за обучение солдат:</p>
            <div class="score-grid">
              <div class="score-row"><span data-i18n="p2T1L">Солдат T1</span><strong data-i18n="p2T1R">5 очков</strong></div>
              <div class="score-row"><span data-i18n="p2T2L">Солдат T2</span><strong data-i18n="p2T2R">6 очков</strong></div>
              <div class="score-row"><span data-i18n="p2T3L">Солдат T3</span><strong data-i18n="p2T3R">7 очков</strong></div>
              <div class="score-row"><span data-i18n="p2T4L">Солдат T4</span><strong data-i18n="p2T4R">13 очков</strong></div>
              <div class="score-row"><span data-i18n="p2T5L">Солдат T5</span><strong data-i18n="p2T5R">15 очков</strong></div>
              <div class="score-row"><span data-i18n="p2T6L">Солдат T6</span><strong data-i18n="p2T6R">19 очков</strong></div>
              <div class="score-row"><span data-i18n="p2T7L">Солдат T7</span><strong data-i18n="p2T7R">22 очка</strong></div>
              <div class="score-row"><span data-i18n="p2T8L">Солдат T8</span><strong data-i18n="p2T8R">25 очков</strong></div>
              <div class="score-row"><span data-i18n="p2T9L">Солдат T9</span><strong data-i18n="p2T9R">28 очков</strong></div>
              <div class="score-row"><span data-i18n="p2T10L">Солдат T10</span><strong data-i18n="p2T10R">31 очко</strong></div>
            </div>
            <div class="hint" data-i18n="p2Hint">💡 Запускайте обучение заранее к старту ГкМ. «Лесенка»: обучайте низкий T и повышайте — один солдат даёт очки несколько раз.</div>
            <div class="shots">
              <figure class="shot" data-full="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/phase-soldiers.webp">
                <img src="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/phase-soldiers.webp" alt="Фаза солдат" data-i18n-alt="altP2" loading="lazy" />
              </figure>
            </div>
          </div>
        </details>

        <details class="acc">
          <summary>
            <span class="acc-num">3</span>
            <span class="acc-summary-text">
              <strong data-i18n="p3Title">🔬 Исследования</strong>
              <span data-i18n="p3Sub">🔥 Лучший день — среда · ⏰ 09:00–12:59 МСК</span>
            </span>
            <span class="acc-chevron" aria-hidden="true">▾</span>
          </summary>
          <div class="acc-body">
            <div class="score-grid">
              <div class="score-row"><span data-i18n="p3Score1L">⌚ 1 минута ускорения</span><strong data-i18n="p3Score1R">10 очков</strong></div>
              <div class="score-row"><span data-i18n="p3Score2L">🔬 +10 силы исследования</span><strong data-i18n="p3Score2R">1 очко</strong></div>
            </div>
            <div class="hint strong" data-i18n-html="p3Hint">🔥 Готовые исследования выгоднее снимать <strong>⏰ 09:00–12:59 МСК</strong> в среду.<br>❗ В остальные дни специально закрывать ими ГкМ обычно невыгодно.</div>
            <div class="shots">
              <figure class="shot" data-full="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/phase-research.webp">
                <img src="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/phase-research.webp" alt="Фаза исследований" data-i18n-alt="altP3" loading="lazy" />
              </figure>
            </div>

            <details class="nested">
              <summary data-i18n="lifehackTitle">🧠 Лайфхак: как ускорить исследования в двух центрах</summary>
              <div class="nested-body">
                <p data-i18n-html="lifehackP1">❗ Выжившие влияют на время <strong><u>в момент запуска</u></strong> исследования.</p>
                <p data-i18n-html="lifehackP2">После того как исследование уже запущено, время <strong><u>зафиксировано</u></strong>. Выживших можно убрать и переставить во второй центр. Текущее исследование от этого дольше не станет.</p>
                <ul class="lifehack-steps">
                  <li data-i18n="lifehackS1">1️⃣ Разместите в Центре №1 лучших UR-выживших.</li>
                  <li data-i18n="lifehackS2">2️⃣ Запустите исследование.</li>
                  <li data-i18n-html="lifehackS3">3️⃣ Нажмите на Центр №1 → <strong>Выжившие</strong></li>
                  <li data-i18n-html="lifehackS4">4️⃣ Нажмите на каждого UR-выжившего отдельно и поменяйте на других (синих/зеленых) — время выполнения исследования <strong><u>не изменится</u></strong>.</li>
                  <li data-i18n="lifehackS5">5️⃣ Через «Быстрое развертывание» поставьте UR в Центр №2.</li>
                  <li data-i18n="lifehackS6">6️⃣ Только после этого запускайте исследование в Центре №2.</li>
                </ul>
                <p style="margin-top:0.55rem" data-i18n="lifehackP3">🔄 Дальше гоняйте лучших выживших между центрами перед каждым новым запуском.</p>
                <p data-i18n="lifehackP4">❗ Аналогично работает ускорение министра:</p>
                <p data-i18n-html="lifehackP5">Поставьте максимальное ускорение → запустите исследование → Время <strong><u>зафиксируется</u></strong> → Заберите ускорение → Используйте его для следующего исследования.</p>
              </div>
            </details>
          </div>
        </details>

        <details class="acc">
          <summary>
            <span class="acc-num">4</span>
            <span class="acc-summary-text">
              <strong data-i18n="p4Title">⚡ Улучшение бойца</strong>
              <span data-i18n="p4Sub">🔧 Чипы использовать только в понедельник. В остальные дни набивать сундуки выносливостью</span>
            </span>
            <span class="acc-chevron" aria-hidden="true">▾</span>
          </summary>
          <div class="acc-body">
            <div class="score-grid">
              <div class="score-row"><span data-i18n="p4Score1L">⚡ 1 выносливость</span><strong data-i18n="p4Score1R">100 очков</strong></div>
              <div class="score-row"><span data-i18n="p4Score2L">🔧 10 боевых чипов</span><strong data-i18n="p4Score2R">1 очко</strong></div>
              <div class="score-row"><span data-i18n="p4Score3L">15 элитных зомби</span><strong data-i18n="p4Score3R">фаза закрыта</strong></div>
            </div>
            <div class="hint" data-i18n="p4Hint1">💡 Берите бесплатную выносливость + восстановление + банки по 10. ❗ Чипы ради ГкМ не тратьте: 22k чипов ≈ 2200 ГкМ, а в VS те же чипы — десятки/сотни тысяч очков.</div>
            <div class="hint strong" data-i18n-html="p4Hint2">🔥 Исключение — <strong>понедельник</strong>: улучшение бойца совпадает с VS, тогда тратить можно и нужно чипы и части.</div>
            <div class="shots">
              <figure class="shot" data-full="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/phase-fighter.webp">
                <img src="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/phase-fighter.webp" alt="Фаза бойца" data-i18n-alt="altP4" loading="lazy" />
              </figure>
            </div>
          </div>
        </details>

        <details class="acc">
          <summary>
            <span class="acc-num">5</span>
            <span class="acc-summary-text">
              <strong data-i18n="p5Title">⭐ Улучшение героя</strong>
              <span data-i18n="p5Sub">Самый быстрый способ закрыть фазу ⌚ ~1 мин</span>
            </span>
            <span class="acc-chevron" aria-hidden="true">▾</span>
          </summary>
          <div class="acc-body">
            <p data-i18n="p5Intro">Самый простой способ закрыть фазу — поднять уровень героя. Для полного закрытия понадобится около 24 млн опыта. Для высокого уровня героя будет достаточно сделать один раз.</p>
            <div class="score-grid">
              <div class="score-row"><span data-i18n="p5Score1L">🎫 1 карта найма</span><strong data-i18n="p5Score1R">400 очков</strong></div>
              <div class="score-row"><span data-i18n="p5Score2L">✨ 2000 опыта героя</span><strong data-i18n="p5Score2R">1 очко</strong></div>
              <div class="score-row"><span data-i18n="p5Score3L">Полное закрытие опытом</span><strong data-i18n="p5Score3R">~24 млн</strong></div>
            </div>
            <div class="hint strong" data-i18n-html="p5Hint">
              🔥 ПН — опыт + VS.<br>
              🔥 ЧТ — опыт + карты + тренировка героев VS.<br>
              ❗ В четверг сначала используйте карты найма, а уже потом универсальные фрагменты на звёзды, т.к. из найма могут выпасть нужные персональные осколки.
            </div>
            <div class="shots">
              <figure class="shot" data-full="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/phase-hero.webp">
                <img src="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/phase-hero.webp" alt="Фаза героя" data-i18n-alt="altP5" loading="lazy" />
              </figure>
            </div>
          </div>
        </details>
      </div>

      <h2 class="section-title" data-i18n="cheatTitle">📅 ГкМ + VS — шпаргалка</h2>
      <section class="panel">
        <div class="weekday">
          <article>
            <h3 data-i18n="dayMonTitle">ПН — Радар</h3>
            <p data-i18n="dayMonText">⭐ Опыт героя · ⚡ Выносливость · 🔧 Боец: чипы + части</p>
          </article>
          <article>
            <h3 data-i18n="dayTueTitle">ВТ — Строительство</h3>
            <p data-i18n="dayTueText">🏗 Галочки зданий · ⌚ Строительные ускорения</p>
          </article>
          <article>
            <h3 data-i18n="dayWedTitle">СР — Исследования</h3>
            <p data-i18n="dayWedText">🔬 Галочки исследований · ⌚ Ускорения исследований</p>
          </article>
          <article>
            <h3 data-i18n="dayThuTitle">ЧТ — Герои</h3>
            <p data-i18n="dayThuText">🎫 Карты найма · ⭐ Опыт героя · 💎 Затем прокачка звёзд</p>
          </article>
          <article>
            <h3 data-i18n="dayFriTitle">ПТ — Военная подготовка</h3>
            <p data-i18n="dayFriText">🪖 Обучение/повышение солдат · ⏰ Лучше 17:00–20:59 МСК. Стройку и исследования — только если не хватает очков VS.</p>
          </article>
          <article>
            <h3 data-i18n="daySatTitle">СБ — Нападение</h3>
            <p data-i18n="daySatText">⌚ Ускорения дают очки, но специально сливать запасы ради ГкМ не стоит.</p>
          </article>
        </div>
        <div class="shots shots-featured">
          <figure class="shot" data-full="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/cheat-sheet.webp">
            <img src="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/cheat-sheet.webp" alt="Шпаргалка ГкМ и VS" data-i18n-alt="altCheat" loading="lazy" />
            <figcaption class="shot-caption" data-i18n="capCheat">Шпаргалка</figcaption>
          </figure>
        </div>
      </section>

      <h2 class="section-title" data-i18n="boostTitle">🏆 Маленький буст</h2>
      <section class="panel">
        <p data-i18n="boostIntro">Если можете, то заранее займите очередь на нужного министра:</p>
        <ul>
          <li data-i18n="boostL1">🏗 Строительство → Министр строительства</li>
          <li data-i18n="boostL2">🔬 Исследования → Министр исследований</li>
          <li data-i18n="boostL3">🪖 Солдаты → Министр обороны</li>
        </ul>
        <div class="shots shots-featured">
          <figure class="shot" data-full="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/ministers.webp">
            <img src="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/ministers.webp" alt="Министры" data-i18n-alt="altMinisters" loading="lazy" />
            <figcaption class="shot-caption" data-i18n="capMinisters">Очередь министров</figcaption>
          </figure>
        </div>
        <p data-i18n="boostNote">Это бесплатный бонус игры, который помогает экономить ресурсы.</p>
        <p data-i18n="boostCompare">Наглядное сравнение количества солдат без должности и с должностью:</p>
        <div class="shots shots-featured">
          <figure class="shot" data-full="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/minister-soldiers-compare.webp">
            <img src="https://raw.githubusercontent.com/FireMyHeart/zroute/main/assets/screenshots/mission-ready/minister-soldiers-compare.webp" alt="Сравнение солдат без министра и с министром обороны" data-i18n-alt="altMinisterCompare" loading="lazy" />
            <figcaption class="shot-caption" data-i18n="capMinisterCompare">Без министра / с министром обороны</figcaption>
          </figure>
        </div>
      </section>

      <section class="panel takeaway">
        <h2 data-i18n="takeawayTitle">🔥 Самое главное</h2>
        <ul>
          <li data-i18n-html="takeaway1"><strong>Каждый день закрываем 3 выгодные фазы ради наград.</strong></li>
          <li data-i18n="takeaway2">⭐ Герой — быстро и просто</li>
          <li data-i18n="takeaway3">⚡ Боец — выносливостью</li>
          <li data-i18n="takeaway4">🪖 Солдат — готовим заранее</li>
          <li data-i18n="takeaway5">А стройку, исследования, чипы, части и большие запасы ускорений не сливаем просто ради ГкМ — ждём совпадения с VS.</li>
          <li data-i18n="takeaway6">👉 Одна трата → ГкМ + VS → двойная выгода.</li>
        </ul>
      </section>
    </main>
  </div>

  <footer>
    <div class="wrap" data-i18n="footer">Неофициальный гайд сервера 98 · Z Route: Redemption</div>
  </footer>

  <div class="lightbox" id="lightbox" hidden>
    <button type="button" class="lightbox-close" id="lightbox-close" aria-label="Закрыть" data-i18n-aria="closeAria">&times;</button>
    <img id="lightbox-img" alt="" />
  </div>
'''

# Replace from hero-content through lightbox (before first script)
text = re.sub(
    r'      <div class="hero-content">[\s\S]*?<div class="lightbox" id="lightbox" hidden>[\s\S]*?</div>\s*\n\s*<script>',
    BODY_MAIN + "\n  <script>",
    text,
    count=1,
)

# Build I18N dictionaries
def pts(n, lang):
    # short score labels
    forms = {
        "en": f"{n} pts",
        "es": f"{n} pts",
        "pl": f"{n} pkt",
        "cs": f"{n} b.",
    }
    return forms[lang]

EN = {
    "themeToLight": "Light theme",
    "themeToDark": "Dark theme",
    "closeAria": "Close",
    "docTitle": "Mission Readiness | Server 98 · Z Route: Redemption",
    "heroTitle": "Mission Readiness",
    "heroLead": "A short Mission Readiness (MR) guide: which phases to clear, when to combine with VS, and how not to waste resources.",
    "beginIntro": "MR runs every <strong>4 hours</strong> and gives rewards + Expedition Madness points.",
    "chipTimesLabel": "⏰ Phase start times (MSK):",
    "chipPhasesLabel": "5 phase types:",
    "chipPhasesValue": "🏗 build · 🪖 soldiers · 🔬 research · ⚡ fighter · ⭐ hero",
    "beginHint": "💡 Don’t spend resources only for MR. Combine the most expensive tasks with the matching <strong>VS</strong> day — one spend scores in both events.",
    "rewardsTitle": "🎁 Rewards",
    "rewardsIntro": "The daily goal is to clear the <strong>3 most valuable phases</strong>, not everything. That unlocks daily chests and phase rewards.",
    "rewardsDailyLabel": "Daily chests:",
    "rewardsDaily1": "🟡 2 gold fragments",
    "rewardsDaily2": "🟣 7 purple fragments",
    "rewardsDaily3": "🎫 10 recruit cards",
    "rewardsDaily4": "💎 350 diamonds",
    "rewardsPhasesLabel": "For 3 phases:",
    "rewardsPhases1": "📚 3600 skill books",
    "rewardsPhases2": "⌚ 150 speedups ×5 min",
    "rewardsPhases3": "📦 72 food/metal/oil chests each",
    "rewardsPhases4": "🏅 18 daily medals",
    "rewardsPhaseChests": "In each phase you can also claim up to 4 chests (reset every 4 hours) 👇",
    "rewardsDiamondNote": "Diamonds in the UI mark how valuable rewards are.",
    "altRewardsOverview": "MR rewards",
    "capRewardsOverview": "Rewards overview",
    "altRewardsDaily": "Daily chests",
    "capRewardsDaily": "3 daily chests",
    "altRewardsPhase": "Phase chests",
    "capRewardsPhase": "Phase chests",
    "altRewardsMedals": "Phase medals",
    "capRewardsMedals": "Medals and resources",
    "phasesTitle": "MR phases",
    "p1Title": "🏗 Base building",
    "p1Sub": "🔥 Best day — Tuesday (matches VS)",
    "p1Score1L": "⌚ 1 minute of speedups",
    "p1Score1R": "10 pts",
    "p1Score2L": "🏗 +10 building power",
    "p1Score2R": "1 pt",
    "exampleLabel": "Example:",
    "p1Ex1": "1 hour of speedups = <span class=\"pts\">600 pts</span>",
    "p1Ex2": "+1000 building power = <span class=\"pts\">100 pts</span>",
    "p1Hint1": "💡 You can finish buildings in advance and <strong>not tap the checkmarks</strong> until the right phase starts.",
    "p1Hint2": "🔥 On Tuesday, claim checkmarks on finished buildings.<br>❗ On other days, don’t burn speedups just for MR.",
    "altP1": "Building phase",
    "p2Title": "🪖 Training soldiers",
    "p2Sub": "Prepare early · the “ladder” saves speedups",
    "p2Score1L": "⌚ 1 minute of training speedups",
    "p2Score1R": "10 pts",
    "p2Score2L": "💎 1 diamond of packs",
    "p2Score2R": "30 pts",
    "p2ScaleLabel": "🪖 Points for training soldiers:",
    "p2T1L": "Soldier T1", "p2T1R": "5 pts",
    "p2T2L": "Soldier T2", "p2T2R": "6 pts",
    "p2T3L": "Soldier T3", "p2T3R": "7 pts",
    "p2T4L": "Soldier T4", "p2T4R": "13 pts",
    "p2T5L": "Soldier T5", "p2T5R": "15 pts",
    "p2T6L": "Soldier T6", "p2T6R": "19 pts",
    "p2T7L": "Soldier T7", "p2T7R": "22 pts",
    "p2T8L": "Soldier T8", "p2T8R": "25 pts",
    "p2T9L": "Soldier T9", "p2T9R": "28 pts",
    "p2T10L": "Soldier T10", "p2T10R": "31 pts",
    "p2Hint": "💡 Start training before MR begins. “Ladder”: train a low T and promote — one soldier scores several times.",
    "altP2": "Soldiers phase",
    "p3Title": "🔬 Research",
    "p3Sub": "🔥 Best day — Wednesday · ⏰ 09:00–12:59 MSK",
    "p3Score1L": "⌚ 1 minute of speedups",
    "p3Score1R": "10 pts",
    "p3Score2L": "🔬 +10 research power",
    "p3Score2R": "1 pt",
    "p3Hint": "🔥 Ready research is best claimed <strong>⏰ 09:00–12:59 MSK</strong> on Wednesday.<br>❗ On other days, clearing MR with research is usually not worth it.",
    "altP3": "Research phase",
    "lifehackTitle": "🧠 Lifehack: speed up research in two centers",
    "lifehackP1": "❗ Survivors affect time <strong><u>at the moment you start</u></strong> research.",
    "lifehackP2": "Once research has started, time is <strong><u>locked</u></strong>. You can remove survivors and move them to the second center. The current research will not get longer.",
    "lifehackS1": "1️⃣ Put your best UR survivors in Center #1.",
    "lifehackS2": "2️⃣ Start the research.",
    "lifehackS3": "3️⃣ Tap Center #1 → <strong>Survivors</strong>",
    "lifehackS4": "4️⃣ Tap each UR survivor and swap to others (blue/green) — research time <strong><u>will not change</u></strong>.",
    "lifehackS5": "5️⃣ Use Quick Deploy to put URs in Center #2.",
    "lifehackS6": "6️⃣ Only then start research in Center #2.",
    "lifehackP3": "🔄 Keep rotating your best survivors between centers before each new start.",
    "lifehackP4": "❗ Minister speedup works the same way:",
    "lifehackP5": "Set max speedup → start research → Time is <strong><u>locked</u></strong> → Take the speedup back → Use it for the next research.",
    "p4Title": "⚡ Fighter upgrade",
    "p4Sub": "🔧 Use chips on Monday only. On other days fill chests with stamina",
    "p4Score1L": "⚡ 1 stamina",
    "p4Score1R": "100 pts",
    "p4Score2L": "🔧 10 combat chips",
    "p4Score2R": "1 pt",
    "p4Score3L": "15 elite zombies",
    "p4Score3R": "phase cleared",
    "p4Hint1": "💡 Take free stamina + recovery + ×10 cans. ❗ Don’t spend chips for MR: 22k chips ≈ 2200 MR, while in VS the same chips are tens/hundreds of thousands of points.",
    "p4Hint2": "🔥 Exception — <strong>Monday</strong>: fighter upgrade matches VS, so chips and parts are worth spending.",
    "altP4": "Fighter phase",
    "p5Title": "⭐ Hero upgrade",
    "p5Sub": "Fastest way to clear the phase ⌚ ~1 min",
    "p5Intro": "The easiest clear is leveling a hero. Full clear needs about 24M XP. At high hero level, one level-up is enough.",
    "p5Score1L": "🎫 1 recruit card",
    "p5Score1R": "400 pts",
    "p5Score2L": "✨ 2000 hero XP",
    "p5Score2R": "1 pt",
    "p5Score3L": "Full clear with XP",
    "p5Score3R": "~24M",
    "p5Hint": "🔥 Mon — XP + VS.<br>🔥 Thu — XP + cards + hero training VS.<br>❗ On Thursday use recruit cards first, then universal star fragments — recruit may drop the personal shards you need.",
    "altP5": "Hero phase",
    "cheatTitle": "📅 MR + VS — cheat sheet",
    "dayMonTitle": "Mon — Radar",
    "dayMonText": "⭐ Hero XP · ⚡ Stamina · 🔧 Fighter: chips + parts",
    "dayTueTitle": "Tue — Building",
    "dayTueText": "🏗 Building checkmarks · ⌚ Building speedups",
    "dayWedTitle": "Wed — Research",
    "dayWedText": "🔬 Research checkmarks · ⌚ Research speedups",
    "dayThuTitle": "Thu — Heroes",
    "dayThuText": "🎫 Recruit cards · ⭐ Hero XP · 💎 Then star upgrades",
    "dayFriTitle": "Fri — Military training",
    "dayFriText": "🪖 Train/promote soldiers · ⏰ Best 17:00–20:59 MSK. Building and research only if you still need VS points.",
    "daySatTitle": "Sat — Assault",
    "daySatText": "⌚ Speedups give points, but don’t dump stocks just for MR.",
    "altCheat": "MR and VS cheat sheet",
    "capCheat": "Cheat sheet",
    "boostTitle": "🏆 Small boost",
    "boostIntro": "If you can, queue the right minister in advance:",
    "boostL1": "🏗 Building → Construction Minister",
    "boostL2": "🔬 Research → Research Minister",
    "boostL3": "🪖 Soldiers → Defense Minister",
    "altMinisters": "Ministers",
    "capMinisters": "Minister queue",
    "boostNote": "It’s a free in-game bonus that helps save resources.",
    "boostCompare": "A clear comparison of soldier count without and with the office:",
    "altMinisterCompare": "Soldiers without a minister vs with Defense Minister",
    "capMinisterCompare": "Without minister / with Defense Minister",
    "takeawayTitle": "🔥 Key takeaways",
    "takeaway1": "<strong>Every day clear 3 valuable phases for the rewards.</strong>",
    "takeaway2": "⭐ Hero — fast and simple",
    "takeaway3": "⚡ Fighter — with stamina",
    "takeaway4": "🪖 Soldiers — prepare early",
    "takeaway5": "Don’t dump building, research, chips, parts, or big speedup stocks just for MR — wait for a VS match.",
    "takeaway6": "👉 One spend → MR + VS → double value.",
    "footer": "Unofficial Server 98 guide · Z Route: Redemption",
}

ES = {
    "themeToLight": "Tema claro",
    "themeToDark": "Tema oscuro",
    "closeAria": "Cerrar",
    "docTitle": "Preparación de misión | Servidor 98 · Z Route: Redemption",
    "heroTitle": "Preparación de misión",
    "heroLead": "Guía corta de Preparación de misión (PM): qué fases completar, cuándo combinar con VS y cómo no malgastar recursos.",
    "beginIntro": "La PM se repite cada <strong>4 horas</strong> y da recompensas + puntos de Locura de expedición.",
    "chipTimesLabel": "⏰ Inicio de fases (MSK):",
    "chipPhasesLabel": "5 tipos de fase:",
    "chipPhasesValue": "🏗 construcción · 🪖 soldados · 🔬 investigación · ⚡ luchador · ⭐ héroe",
    "beginHint": "💡 No gastes recursos solo por la PM. Combina las tareas más caras con el día de <strong>VS</strong> adecuado: un gasto suma en ambos eventos.",
    "rewardsTitle": "🎁 Recompensas",
    "rewardsIntro": "El objetivo del día es completar las <strong>3 fases más rentables</strong>, no todas. Así se abren cofres diarios y recompensas de fase.",
    "rewardsDailyLabel": "Cofres diarios:",
    "rewardsDaily1": "🟡 2 fragmentos dorados",
    "rewardsDaily2": "🟣 7 fragmentos morados",
    "rewardsDaily3": "🎫 10 cartas de reclutamiento",
    "rewardsDaily4": "💎 350 diamantes",
    "rewardsPhasesLabel": "Por 3 fases:",
    "rewardsPhases1": "📚 3600 libros de habilidad",
    "rewardsPhases2": "⌚ 150 aceleraciones ×5 min",
    "rewardsPhases3": "📦 72 cofres de comida/metal/petróleo cada uno",
    "rewardsPhases4": "🏅 18 medallas diarias",
    "rewardsPhaseChests": "En cada fase también puedes reclamar hasta 4 cofres (se reinician cada 4 horas) 👇",
    "rewardsDiamondNote": "Los diamantes en la interfaz marcan el valor de las recompensas.",
    "altRewardsOverview": "Recompensas de PM",
    "capRewardsOverview": "Resumen de recompensas",
    "altRewardsDaily": "Cofres diarios",
    "capRewardsDaily": "3 cofres diarios",
    "altRewardsPhase": "Cofres de fase",
    "capRewardsPhase": "Cofres de fase",
    "altRewardsMedals": "Medallas de fase",
    "capRewardsMedals": "Medallas y recursos",
    "phasesTitle": "Fases de PM",
    "p1Title": "🏗 Construcción de base",
    "p1Sub": "🔥 Mejor día — martes (coincide con VS)",
    "p1Score1L": "⌚ 1 minuto de aceleraciones",
    "p1Score1R": "10 pts",
    "p1Score2L": "🏗 +10 poder de edificio",
    "p1Score2R": "1 pt",
    "exampleLabel": "Ejemplo:",
    "p1Ex1": "1 hora de aceleraciones = <span class=\"pts\">600 pts</span>",
    "p1Ex2": "+1000 poder de edificio = <span class=\"pts\">100 pts</span>",
    "p1Hint1": "💡 Puedes terminar edificios antes y <strong>no pulsar las marcas</strong> hasta que empiece la fase correcta.",
    "p1Hint2": "🔥 El martes reclama las marcas de edificios listos.<br>❗ Otros días no gastes aceleraciones solo por la PM.",
    "altP1": "Fase de construcción",
    "p2Title": "🪖 Entrenar soldados",
    "p2Sub": "Prepara con antelación · la “escalera” ahorra aceleraciones",
    "p2Score1L": "⌚ 1 minuto de aceleraciones de entrenamiento",
    "p2Score1R": "10 pts",
    "p2Score2L": "💎 1 diamante de packs",
    "p2Score2R": "30 pts",
    "p2ScaleLabel": "🪖 Puntos por entrenar soldados:",
    "p2T1L": "Soldado T1", "p2T1R": "5 pts",
    "p2T2L": "Soldado T2", "p2T2R": "6 pts",
    "p2T3L": "Soldado T3", "p2T3R": "7 pts",
    "p2T4L": "Soldado T4", "p2T4R": "13 pts",
    "p2T5L": "Soldado T5", "p2T5R": "15 pts",
    "p2T6L": "Soldado T6", "p2T6R": "19 pts",
    "p2T7L": "Soldado T7", "p2T7R": "22 pts",
    "p2T8L": "Soldado T8", "p2T8R": "25 pts",
    "p2T9L": "Soldado T9", "p2T9R": "28 pts",
    "p2T10L": "Soldado T10", "p2T10R": "31 pts",
    "p2Hint": "💡 Empieza el entrenamiento antes de la PM. “Escalera”: entrena un T bajo y súbelo — un soldado puntúa varias veces.",
    "altP2": "Fase de soldados",
    "p3Title": "🔬 Investigación",
    "p3Sub": "🔥 Mejor día — miércoles · ⏰ 09:00–12:59 MSK",
    "p3Score1L": "⌚ 1 minuto de aceleraciones",
    "p3Score1R": "10 pts",
    "p3Score2L": "🔬 +10 poder de investigación",
    "p3Score2R": "1 pt",
    "p3Hint": "🔥 Conviene reclamar investigación lista <strong>⏰ 09:00–12:59 MSK</strong> el miércoles.<br>❗ Otros días cerrar la PM con investigación suele no compensar.",
    "altP3": "Fase de investigación",
    "lifehackTitle": "🧠 Truco: acelerar investigación en dos centros",
    "lifehackP1": "❗ Los supervivientes afectan el tiempo <strong><u>al iniciar</u></strong> la investigación.",
    "lifehackP2": "Cuando ya está lanzada, el tiempo queda <strong><u>fijado</u></strong>. Puedes quitar supervivientes y moverlos al segundo centro. La investigación actual no se alargará.",
    "lifehackS1": "1️⃣ Pon los mejores UR en el Centro nº 1.",
    "lifehackS2": "2️⃣ Lanza la investigación.",
    "lifehackS3": "3️⃣ Toca Centro nº 1 → <strong>Supervivientes</strong>",
    "lifehackS4": "4️⃣ Cambia cada UR por otros (azul/verde): el tiempo <strong><u>no cambia</u></strong>.",
    "lifehackS5": "5️⃣ Con Despliegue rápido pon UR en el Centro nº 2.",
    "lifehackS6": "6️⃣ Solo entonces lanza investigación en el Centro nº 2.",
    "lifehackP3": "🔄 Sigue rotando a los mejores entre centros antes de cada nuevo inicio.",
    "lifehackP4": "❗ La aceleración del ministro funciona igual:",
    "lifehackP5": "Pon la aceleración máxima → lanza investigación → El tiempo se <strong><u>fija</u></strong> → Retira la aceleración → Úsala en la siguiente.",
    "p4Title": "⚡ Mejora del luchador",
    "p4Sub": "🔧 Usa chips solo el lunes. Otros días llena cofres con resistencia",
    "p4Score1L": "⚡ 1 resistencia",
    "p4Score1R": "100 pts",
    "p4Score2L": "🔧 10 chips de combate",
    "p4Score2R": "1 pt",
    "p4Score3L": "15 zombis élite",
    "p4Score3R": "fase completada",
    "p4Hint1": "💡 Coge resistencia gratis + recuperación + botes ×10. ❗ No gastes chips por la PM: 22k chips ≈ 2200 PM; en VS valen decenas/cientos de miles de puntos.",
    "p4Hint2": "🔥 Excepción — <strong>lunes</strong>: la mejora del luchador coincide con VS; entonces sí conviene gastar chips y piezas.",
    "altP4": "Fase de luchador",
    "p5Title": "⭐ Mejora de héroe",
    "p5Sub": "La forma más rápida de cerrar la fase ⌚ ~1 min",
    "p5Intro": "Lo más fácil es subir el nivel del héroe. El cierre total necesita unos 24M de XP. Con un héroe alto, una subida basta.",
    "p5Score1L": "🎫 1 carta de reclutamiento",
    "p5Score1R": "400 pts",
    "p5Score2L": "✨ 2000 XP de héroe",
    "p5Score2R": "1 pt",
    "p5Score3L": "Cierre total con XP",
    "p5Score3R": "~24M",
    "p5Hint": "🔥 Lun — XP + VS.<br>🔥 Jue — XP + cartas + entrenamiento de héroes VS.<br>❗ El jueves usa primero cartas de reclutamiento y luego fragmentos universales de estrellas: del reclutamiento pueden salir fragmentos personales.",
    "altP5": "Fase de héroe",
    "cheatTitle": "📅 PM + VS — chuleta",
    "dayMonTitle": "Lun — Radar",
    "dayMonText": "⭐ XP de héroe · ⚡ Resistencia · 🔧 Luchador: chips + piezas",
    "dayTueTitle": "Mar — Construcción",
    "dayTueText": "🏗 Marcas de edificios · ⌚ Aceleraciones de construcción",
    "dayWedTitle": "Mié — Investigación",
    "dayWedText": "🔬 Marcas de investigación · ⌚ Aceleraciones de investigación",
    "dayThuTitle": "Jue — Héroes",
    "dayThuText": "🎫 Cartas de reclutamiento · ⭐ XP de héroe · 💎 Luego estrellas",
    "dayFriTitle": "Vie — Entrenamiento militar",
    "dayFriText": "🪖 Entrenar/subir soldados · ⏰ Mejor 17:00–20:59 MSK. Construcción e investigación solo si faltan puntos de VS.",
    "daySatTitle": "Sáb — Asalto",
    "daySatText": "⌚ Las aceleraciones dan puntos, pero no vacíes reservas solo por la PM.",
    "altCheat": "Chuleta PM y VS",
    "capCheat": "Chuleta",
    "boostTitle": "🏆 Pequeño boost",
    "boostIntro": "Si puedes, reserva con antelación al ministro adecuado:",
    "boostL1": "🏗 Construcción → Ministro de construcción",
    "boostL2": "🔬 Investigación → Ministro de investigación",
    "boostL3": "🪖 Soldados → Ministro de defensa",
    "altMinisters": "Ministros",
    "capMinisters": "Cola de ministros",
    "boostNote": "Es un bonus gratis del juego que ayuda a ahorrar recursos.",
    "boostCompare": "Comparación clara de soldados sin cargo y con cargo:",
    "altMinisterCompare": "Soldados sin ministro vs con ministro de defensa",
    "capMinisterCompare": "Sin ministro / con ministro de defensa",
    "takeawayTitle": "🔥 Lo esencial",
    "takeaway1": "<strong>Cada día completa 3 fases rentables por las recompensas.</strong>",
    "takeaway2": "⭐ Héroe — rápido y sencillo",
    "takeaway3": "⚡ Luchador — con resistencia",
    "takeaway4": "🪖 Soldados — prepáralos antes",
    "takeaway5": "No gastes construcción, investigación, chips, piezas ni grandes aceleraciones solo por la PM: espera el cruce con VS.",
    "takeaway6": "👉 Un gasto → PM + VS → doble beneficio.",
    "footer": "Guía no oficial del servidor 98 · Z Route: Redemption",
}

PL = {
    "themeToLight": "Jasny motyw",
    "themeToDark": "Ciemny motyw",
    "closeAria": "Zamknij",
    "docTitle": "Gotowość do misji | Serwer 98 · Z Route: Redemption",
    "heroTitle": "Gotowość do misji",
    "heroLead": "Krótki poradnik Gotowości do misji (GdM): które fazy domykać, kiedy łączyć z VS i jak nie marnować zasobów.",
    "beginIntro": "GdM odbywa się co <strong>4 godziny</strong> i daje nagrody + punkty Szaleństwa ekspedycji.",
    "chipTimesLabel": "⏰ Start faz (MSK):",
    "chipPhasesLabel": "5 typów faz:",
    "chipPhasesValue": "🏗 budowa · 🪖 żołnierze · 🔬 badania · ⚡ bojownik · ⭐ bohater",
    "beginHint": "💡 Nie wydawaj zasobów tylko pod GdM. Najdroższe zadania łącz z właściwym dniem <strong>VS</strong> — jeden wydatek daje punkty w obu eventach.",
    "rewardsTitle": "🎁 Nagrody",
    "rewardsIntro": "Cel dnia to domknięcie <strong>3 najbardziej opłacalnych faz</strong>, a nie wszystkiego. Za to otwierają się dzienne skrzynie i nagrody za fazy.",
    "rewardsDailyLabel": "Dzienne skrzynie:",
    "rewardsDaily1": "🟡 2 złote fragmenty",
    "rewardsDaily2": "🟣 7 fioletowych fragmentów",
    "rewardsDaily3": "🎫 10 kart rekrutacji",
    "rewardsDaily4": "💎 350 diamentów",
    "rewardsPhasesLabel": "Za 3 fazy:",
    "rewardsPhases1": "📚 3600 książek umiejętności",
    "rewardsPhases2": "⌚ 150 przyspieszeń ×5 min",
    "rewardsPhases3": "📦 po 72 skrzynie żywności/metalu/ropy",
    "rewardsPhases4": "🏅 18 dziennych medali",
    "rewardsPhaseChests": "W każdej fazie możesz też zabrać do 4 skrzyń (reset co 4 godziny) 👇",
    "rewardsDiamondNote": "Diamenty w grze oznaczają wartość nagród.",
    "altRewardsOverview": "Nagrody GdM",
    "capRewardsOverview": "Przegląd nagród",
    "altRewardsDaily": "Dzienne skrzynie",
    "capRewardsDaily": "3 dzienne skrzynie",
    "altRewardsPhase": "Skrzynie fazy",
    "capRewardsPhase": "Skrzynie fazy",
    "altRewardsMedals": "Medale za fazy",
    "capRewardsMedals": "Medale i zasoby",
    "phasesTitle": "Fazy GdM",
    "p1Title": "🏗 Budowa bazy",
    "p1Sub": "🔥 Najlepszy dzień — wtorek (zbieżność z VS)",
    "p1Score1L": "⌚ 1 minuta przyspieszeń",
    "p1Score1R": "10 pkt",
    "p1Score2L": "🏗 +10 mocy budynku",
    "p1Score2R": "1 pkt",
    "exampleLabel": "Na przykład:",
    "p1Ex1": "1 godzina przyspieszeń = <span class=\"pts\">600 pkt</span>",
    "p1Ex2": "+1000 mocy budynku = <span class=\"pts\">100 pkt</span>",
    "p1Hint1": "💡 Możesz wcześniej dokończyć budynki i <strong>nie klikać znaczników</strong>, dopóki nie zacznie się właściwa faza.",
    "p1Hint2": "🔥 We wtorek odbieraj znaczniki gotowych budynków.<br>❗ W inne dni nie spalaj przyspieszeń tylko pod GdM.",
    "altP1": "Faza budowy",
    "p2Title": "🪖 Szkolenie żołnierzy",
    "p2Sub": "Przygotuj wcześniej · „drabinka” oszczędza przyspieszenia",
    "p2Score1L": "⌚ 1 minuta przyspieszeń szkolenia",
    "p2Score1R": "10 pkt",
    "p2Score2L": "💎 1 diament paczek",
    "p2Score2R": "30 pkt",
    "p2ScaleLabel": "🪖 Punkty za szkolenie żołnierzy:",
    "p2T1L": "Żołnierz T1", "p2T1R": "5 pkt",
    "p2T2L": "Żołnierz T2", "p2T2R": "6 pkt",
    "p2T3L": "Żołnierz T3", "p2T3R": "7 pkt",
    "p2T4L": "Żołnierz T4", "p2T4R": "13 pkt",
    "p2T5L": "Żołnierz T5", "p2T5R": "15 pkt",
    "p2T6L": "Żołnierz T6", "p2T6R": "19 pkt",
    "p2T7L": "Żołnierz T7", "p2T7R": "22 pkt",
    "p2T8L": "Żołnierz T8", "p2T8R": "25 pkt",
    "p2T9L": "Żołnierz T9", "p2T9R": "28 pkt",
    "p2T10L": "Żołnierz T10", "p2T10R": "31 pkt",
    "p2Hint": "💡 Uruchamiaj szkolenie przed startem GdM. „Drabinka”: trenuj niski T i awansuj — jeden żołnierz daje punkty kilka razy.",
    "altP2": "Faza żołnierzy",
    "p3Title": "🔬 Badania",
    "p3Sub": "🔥 Najlepszy dzień — środa · ⏰ 09:00–12:59 MSK",
    "p3Score1L": "⌚ 1 minuta przyspieszeń",
    "p3Score1R": "10 pkt",
    "p3Score2L": "🔬 +10 siły badań",
    "p3Score2R": "1 pkt",
    "p3Hint": "🔥 Gotowe badania najlepiej odbierać <strong>⏰ 09:00–12:59 MSK</strong> w środę.<br>❗ W inne dni domykanie GdM badaniami zwykle się nie opłaca.",
    "altP3": "Faza badań",
    "lifehackTitle": "🧠 Lifehack: przyspiesz badania w dwóch centrach",
    "lifehackP1": "❗ Ocalali wpływają na czas <strong><u>w momencie startu</u></strong> badania.",
    "lifehackP2": "Gdy badanie już ruszyło, czas jest <strong><u>zablokowany</u></strong>. Możesz zdjąć ocalałych i przenieść ich do drugiego centrum. Bieżące badanie się nie wydłuży.",
    "lifehackS1": "1️⃣ Umieść najlepszych UR w Centrum nr 1.",
    "lifehackS2": "2️⃣ Uruchom badanie.",
    "lifehackS3": "3️⃣ Kliknij Centrum nr 1 → <strong>Ocalali</strong>",
    "lifehackS4": "4️⃣ Zmień każdego UR na innych (niebieskich/zielonych) — czas <strong><u>się nie zmieni</u></strong>.",
    "lifehackS5": "5️⃣ Przez Szybkie rozmieszczenie ustaw UR w Centrum nr 2.",
    "lifehackS6": "6️⃣ Dopiero potem uruchom badanie w Centrum nr 2.",
    "lifehackP3": "🔄 Dalej rotuj najlepszych ocalałych między centrami przed każdym nowym startem.",
    "lifehackP4": "❗ Przyspieszenie ministra działa tak samo:",
    "lifehackP5": "Ustaw max przyspieszenie → uruchom badanie → Czas się <strong><u>zablokuje</u></strong> → Zabierz przyspieszenie → Użyj go do kolejnego badania.",
    "p4Title": "⚡ Ulepszanie bojownika",
    "p4Sub": "🔧 Chipów używaj tylko w poniedziałek. W inne dni zbieraj skrzynie wytrzymałością",
    "p4Score1L": "⚡ 1 wytrzymałość",
    "p4Score1R": "100 pkt",
    "p4Score2L": "🔧 10 chipów bojowych",
    "p4Score2R": "1 pkt",
    "p4Score3L": "15 elitarnych zombie",
    "p4Score3R": "faza domknięta",
    "p4Hint1": "💡 Bierz darmową wytrzymałość + regenerację + puszki ×10. ❗ Nie wydawaj chipów pod GdM: 22k chipów ≈ 2200 GdM, a w VS te same chipy to dziesiątki/setki tysięcy punktów.",
    "p4Hint2": "🔥 Wyjątek — <strong>poniedziałek</strong>: ulepszanie bojownika zbiega się z VS, wtedy warto wydawać chipy i części.",
    "altP4": "Faza bojownika",
    "p5Title": "⭐ Ulepszanie bohatera",
    "p5Sub": "Najszybszy sposób na domknięcie fazy ⌚ ~1 min",
    "p5Intro": "Najłatwiej domknąć fazę podnosząc poziom bohatera. Pełne domknięcie to ok. 24 mln XP. Przy wysokim poziomie wystarczy jeden awans.",
    "p5Score1L": "🎫 1 karta rekrutacji",
    "p5Score1R": "400 pkt",
    "p5Score2L": "✨ 2000 XP bohatera",
    "p5Score2R": "1 pkt",
    "p5Score3L": "Pełne domknięcie XP",
    "p5Score3R": "~24 mln",
    "p5Hint": "🔥 Pn — XP + VS.<br>🔥 Czw — XP + karty + trening bohaterów VS.<br>❗ W czwartek najpierw karty rekrutacji, potem uniwersalne fragmenty na gwiazdy — z rekrutacji mogą wypaść osobiste odłamki.",
    "altP5": "Faza bohatera",
    "cheatTitle": "📅 GdM + VS — ściąga",
    "dayMonTitle": "Pn — Radar",
    "dayMonText": "⭐ XP bohatera · ⚡ Wytrzymałość · 🔧 Bojownik: chipy + części",
    "dayTueTitle": "Wt — Budowa",
    "dayTueText": "🏗 Znaczniki budynków · ⌚ Przyspieszenia budowy",
    "dayWedTitle": "Śr — Badania",
    "dayWedText": "🔬 Znaczniki badań · ⌚ Przyspieszenia badań",
    "dayThuTitle": "Czw — Bohaterowie",
    "dayThuText": "🎫 Karty rekrutacji · ⭐ XP bohatera · 💎 Potem gwiazdy",
    "dayFriTitle": "Pt — Szkolenie wojskowe",
    "dayFriText": "🪖 Szkolenie/awans żołnierzy · ⏰ Najlepiej 17:00–20:59 MSK. Budowę i badania tylko gdy brakuje punktów VS.",
    "daySatTitle": "Sob — Atak",
    "daySatText": "⌚ Przyspieszenia dają punkty, ale nie warto specjalnie opróżniać zapasów pod GdM.",
    "altCheat": "Ściąga GdM i VS",
    "capCheat": "Ściąga",
    "boostTitle": "🏆 Mały boost",
    "boostIntro": "Jeśli możesz, wcześniej zajmij kolejkę na właściwego ministra:",
    "boostL1": "🏗 Budowa → Minister budowy",
    "boostL2": "🔬 Badania → Minister badań",
    "boostL3": "🪖 Żołnierze → Minister obrony",
    "altMinisters": "Ministrowie",
    "capMinisters": "Kolejka ministrów",
    "boostNote": "To darmowy bonus gry, który pomaga oszczędzać zasoby.",
    "boostCompare": "Porównanie liczby żołnierzy bez urzędu i z urzędem:",
    "altMinisterCompare": "Żołnierze bez ministra vs z ministrem obrony",
    "capMinisterCompare": "Bez ministra / z ministrem obrony",
    "takeawayTitle": "🔥 Najważniejsze",
    "takeaway1": "<strong>Codziennie domykamy 3 opłacalne fazy dla nagród.</strong>",
    "takeaway2": "⭐ Bohater — szybko i prosto",
    "takeaway3": "⚡ Bojownik — wytrzymałością",
    "takeaway4": "🪖 Żołnierze — przygotuj wcześniej",
    "takeaway5": "Budowy, badań, chipów, części i dużych zapasów przyspieszeń nie spalaj tylko pod GdM — czekaj na zbieżność z VS.",
    "takeaway6": "👉 Jeden wydatek → GdM + VS → podwójna korzyść.",
    "footer": "Nieoficjalny poradnik serwera 98 · Z Route: Redemption",
}

CS = {
    "themeToLight": "Světlý motiv",
    "themeToDark": "Tmavý motiv",
    "closeAria": "Zavřít",
    "docTitle": "Připravenost na misi | Server 98 · Z Route: Redemption",
    "heroTitle": "Připravenost na misi",
    "heroLead": "Krátký návod Připravenosti na misi (PnM): které fáze uzavírat, kdy spojit s VS a jak neplýtvat zdroji.",
    "beginIntro": "PnM běží každých <strong>4 hodiny</strong> a dává odměny + body Šílenství expedice.",
    "chipTimesLabel": "⏰ Start fází (MSK):",
    "chipPhasesLabel": "5 typů fází:",
    "chipPhasesValue": "🏗 stavba · 🪖 vojáci · 🔬 výzkum · ⚡ bojovník · ⭐ hrdina",
    "beginHint": "💡 Nevyhazujte zdroje jen kvůli PnM. Nejdražší úkoly spojte se správným dnem <strong>VS</strong> — jeden výdej dává body v obou eventech.",
    "rewardsTitle": "🎁 Odměny",
    "rewardsIntro": "Cíl dne je uzavřít <strong>3 nejvýhodnější fáze</strong>, ne všechno. Otevřou se denní truhly a odměny za fáze.",
    "rewardsDailyLabel": "Denní truhly:",
    "rewardsDaily1": "🟡 2 zlaté fragmenty",
    "rewardsDaily2": "🟣 7 fialových fragmentů",
    "rewardsDaily3": "🎫 10 náborových karet",
    "rewardsDaily4": "💎 350 diamantů",
    "rewardsPhasesLabel": "Za 3 fáze:",
    "rewardsPhases1": "📚 3600 knih dovedností",
    "rewardsPhases2": "⌚ 150 zrychlení ×5 min",
    "rewardsPhases3": "📦 po 72 truhlách jídla/kovu/ropy",
    "rewardsPhases4": "🏅 18 denních medailí",
    "rewardsPhaseChests": "V každé fázi můžete navíc vzít až 4 truhly (reset každých 4 hodiny) 👇",
    "rewardsDiamondNote": "Diamanty ve hře označují hodnotu odměn.",
    "altRewardsOverview": "Odměny PnM",
    "capRewardsOverview": "Přehled odměn",
    "altRewardsDaily": "Denní truhly",
    "capRewardsDaily": "3 denní truhly",
    "altRewardsPhase": "Truhly fáze",
    "capRewardsPhase": "Truhly fáze",
    "altRewardsMedals": "Medaile za fáze",
    "capRewardsMedals": "Medaile a zdroje",
    "phasesTitle": "Fáze PnM",
    "p1Title": "🏗 Stavba základny",
    "p1Sub": "🔥 Nejlepší den — úterý (shoda s VS)",
    "p1Score1L": "⌚ 1 minuta zrychlení",
    "p1Score1R": "10 b.",
    "p1Score2L": "🏗 +10 síly budovy",
    "p1Score2R": "1 b.",
    "exampleLabel": "Například:",
    "p1Ex1": "1 hodina zrychlení = <span class=\"pts\">600 b.</span>",
    "p1Ex2": "+1000 síly budovy = <span class=\"pts\">100 b.</span>",
    "p1Hint1": "💡 Budovy můžete dokončit předem a <strong>nekákat fajfky</strong>, dokud nezačne správná fáze.",
    "p1Hint2": "🔥 V úterý odebírejte fajfky hotových budov.<br>❗ Jindy nespalujte zrychlení jen kvůli PnM.",
    "altP1": "Fáze stavby",
    "p2Title": "🪖 Výcvik vojáků",
    "p2Sub": "Připravte předem · „žebřík“ šetří zrychlení",
    "p2Score1L": "⌚ 1 minuta zrychlení výcviku",
    "p2Score1R": "10 b.",
    "p2Score2L": "💎 1 diamant balíčků",
    "p2Score2R": "30 b.",
    "p2ScaleLabel": "🪖 Body za výcvik vojáků:",
    "p2T1L": "Voják T1", "p2T1R": "5 b.",
    "p2T2L": "Voják T2", "p2T2R": "6 b.",
    "p2T3L": "Voják T3", "p2T3R": "7 b.",
    "p2T4L": "Voják T4", "p2T4R": "13 b.",
    "p2T5L": "Voják T5", "p2T5R": "15 b.",
    "p2T6L": "Voják T6", "p2T6R": "19 b.",
    "p2T7L": "Voják T7", "p2T7R": "22 b.",
    "p2T8L": "Voják T8", "p2T8R": "25 b.",
    "p2T9L": "Voják T9", "p2T9R": "28 b.",
    "p2T10L": "Voják T10", "p2T10R": "31 b.",
    "p2Hint": "💡 Spouštějte výcvik před startem PnM. „Žebřík“: cvičte nízké T a povyšujte — jeden voják dává body víckrát.",
    "altP2": "Fáze vojáků",
    "p3Title": "🔬 Výzkum",
    "p3Sub": "🔥 Nejlepší den — středa · ⏰ 09:00–12:59 MSK",
    "p3Score1L": "⌚ 1 minuta zrychlení",
    "p3Score1R": "10 b.",
    "p3Score2L": "🔬 +10 síly výzkumu",
    "p3Score2R": "1 b.",
    "p3Hint": "🔥 Hotový výzkum je nejlepší odebírat <strong>⏰ 09:00–12:59 MSK</strong> ve středu.<br>❗ Jindy uzavírat PnM výzkumem obvykle nestojí za to.",
    "altP3": "Fáze výzkumu",
    "lifehackTitle": "🧠 Fígl: zrychlete výzkum ve dvou centrech",
    "lifehackP1": "❗ Přeživší ovlivňují čas <strong><u>v okamžiku spuštění</u></strong> výzkumu.",
    "lifehackP2": "Jakmile výzkum běží, čas je <strong><u>zafixovaný</u></strong>. Přeživší můžete sundat a přesunout do druhého centra. Aktuální výzkum se neprodlouží.",
    "lifehackS1": "1️⃣ Dejte nejlepší UR do Centra č. 1.",
    "lifehackS2": "2️⃣ Spusťte výzkum.",
    "lifehackS3": "3️⃣ Klepněte Centrum č. 1 → <strong>Přeživší</strong>",
    "lifehackS4": "4️⃣ Každého UR vyměňte za jiné (modré/zelené) — čas <strong><u>se nezmění</u></strong>.",
    "lifehackS5": "5️⃣ Rychlým rozmístěním dejte UR do Centra č. 2.",
    "lifehackS6": "6️⃣ Teprve potom spusťte výzkum v Centru č. 2.",
    "lifehackP3": "🔄 Dál střídejte nejlepší přeživší mezi centry před každým novým startem.",
    "lifehackP4": "❗ Zrychlení ministra funguje stejně:",
    "lifehackP5": "Nastavte max zrychlení → spusťte výzkum → Čas se <strong><u>zafixuje</u></strong> → Vezměte zrychlení zpět → Použijte ho na další výzkum.",
    "p4Title": "⚡ Vylepšení bojovníka",
    "p4Sub": "🔧 Čipy používejte jen v pondělí. Jindy plňte truhly výdrží",
    "p4Score1L": "⚡ 1 výdrž",
    "p4Score1R": "100 b.",
    "p4Score2L": "🔧 10 bojových čipů",
    "p4Score2R": "1 b.",
    "p4Score3L": "15 elitních zombie",
    "p4Score3R": "fáze uzavřena",
    "p4Hint1": "💡 Berte zdarma výdrž + regeneraci + dózy ×10. ❗ Čipy kvůli PnM nepoužívejte: 22k čipů ≈ 2200 PnM, ve VS stejné čipy = desítky/stovky tisíc bodů.",
    "p4Hint2": "🔥 Výjimka — <strong>pondělí</strong>: vylepšení bojovníka sedí s VS, tehdy čipy a díly dávají smysl.",
    "altP4": "Fáze bojovníka",
    "p5Title": "⭐ Vylepšení hrdiny",
    "p5Sub": "Nejrychlejší způsob uzavření fáze ⌚ ~1 min",
    "p5Intro": "Nejjednodušší je zvednout úroveň hrdiny. Plné uzavření potřebuje asi 24 mil. XP. U vysoké úrovně stačí jeden level.",
    "p5Score1L": "🎫 1 náborová karta",
    "p5Score1R": "400 b.",
    "p5Score2L": "✨ 2000 XP hrdiny",
    "p5Score2R": "1 b.",
    "p5Score3L": "Plné uzavření XP",
    "p5Score3R": "~24 mil.",
    "p5Hint": "🔥 Po — XP + VS.<br>🔥 Čt — XP + karty + trénink hrdinů VS.<br>❗ Ve čtvrtek nejdřív náborové karty, teprve pak univerzální fragmenty na hvězdy — z náboru mohou padnout osobní střepy.",
    "altP5": "Fáze hrdiny",
    "cheatTitle": "📅 PnM + VS — tahák",
    "dayMonTitle": "Po — Radar",
    "dayMonText": "⭐ XP hrdiny · ⚡ Výdrž · 🔧 Bojovník: čipy + díly",
    "dayTueTitle": "Út — Stavba",
    "dayTueText": "🏗 Fajfky budov · ⌚ Stavební zrychlení",
    "dayWedTitle": "St — Výzkum",
    "dayWedText": "🔬 Fajfky výzkumu · ⌚ Zrychlení výzkumu",
    "dayThuTitle": "Čt — Hrdinové",
    "dayThuText": "🎫 Náborové karty · ⭐ XP hrdiny · 💎 Pak hvězdy",
    "dayFriTitle": "Pá — Vojenský výcvik",
    "dayFriText": "🪖 Výcvik/povýšení vojáků · ⏰ Nejlépe 17:00–20:59 MSK. Stavbu a výzkum jen když chybí body VS.",
    "daySatTitle": "So — Útok",
    "daySatText": "⌚ Zrychlení dávají body, ale zásoby jen kvůli PnM nevyhazujte.",
    "altCheat": "Tahák PnM a VS",
    "capCheat": "Tahák",
    "boostTitle": "🏆 Malý boost",
    "boostIntro": "Pokud můžete, předem si zajistěte frontu na správného ministra:",
    "boostL1": "🏗 Stavba → Ministr stavby",
    "boostL2": "🔬 Výzkum → Ministr výzkumu",
    "boostL3": "🪖 Vojáci → Ministr obrany",
    "altMinisters": "Ministři",
    "capMinisters": "Fronta ministrů",
    "boostNote": "Je to bezplatný bonus hry, který pomáhá šetřit zdroje.",
    "boostCompare": "Srovnání počtu vojáků bez úřadu a s úřadem:",
    "altMinisterCompare": "Vojáci bez ministra vs s ministrem obrany",
    "capMinisterCompare": "Bez ministra / s ministrem obrany",
    "takeawayTitle": "🔥 Nejdůležitější",
    "takeaway1": "<strong>Každý den uzavíráme 3 výhodné fáze kvůli odměnám.</strong>",
    "takeaway2": "⭐ Hrdina — rychle a jednoduše",
    "takeaway3": "⚡ Bojovník — výdrží",
    "takeaway4": "🪖 Vojáci — připravte předem",
    "takeaway5": "Stavbu, výzkum, čipy, díly a velké zásoby zrychlení nespalujte jen kvůli PnM — čekejte na shodu s VS.",
    "takeaway6": "👉 Jeden výdej → PnM + VS → dvojí užitek.",
    "footer": "Neoficiální návod serveru 98 · Z Route: Redemption",
}


def js_escape(s: str) -> str:
    return (
        s.replace("\\", "\\\\")
        .replace("'", "\\'")
        .replace("\n", "\\n")
        .replace("\r", "")
    )


def dict_to_js(d: dict, indent=8) -> str:
    pad = " " * indent
    lines = ["{"]
    for k, v in d.items():
        lines.append(f"{pad}{k}: '{js_escape(v)}',")
    lines.append(" " * (indent - 2) + "}")
    return "\n".join(lines)


SCRIPT = f'''<script>
(function () {{
  var I18N = {{
    ru: {{
      themeToLight: 'Светлая тема',
      themeToDark: 'Тёмная тема',
      closeAria: 'Закрыть',
      docTitle: 'Готовность к миссии | Сервер 98 · Z Route: Redemption'
    }},
    en: {dict_to_js(EN)},
    es: {dict_to_js(ES)},
    pl: {dict_to_js(PL)},
    cs: {dict_to_js(CS)}
  }};

  function seedRuFromDom() {{
    document.querySelectorAll('[data-i18n]').forEach(function (el) {{
      var key = el.getAttribute('data-i18n');
      if (!key) return;
      if (I18N.ru[key] == null) I18N.ru[key] = el.textContent;
    }});
    document.querySelectorAll('[data-i18n-html]').forEach(function (el) {{
      var key = el.getAttribute('data-i18n-html');
      if (!key) return;
      if (I18N.ru[key] == null) I18N.ru[key] = el.innerHTML;
    }});
    document.querySelectorAll('[data-i18n-alt]').forEach(function (el) {{
      var key = el.getAttribute('data-i18n-alt');
      if (!key) return;
      if (I18N.ru[key] == null) I18N.ru[key] = el.getAttribute('alt') || '';
    }});
    document.querySelectorAll('[data-i18n-aria]').forEach(function (el) {{
      var key = el.getAttribute('data-i18n-aria');
      if (!key) return;
      if (I18N.ru[key] == null) I18N.ru[key] = el.getAttribute('aria-label') || '';
    }});
  }}

  function applyLang(lang) {{
    var dict = I18N[lang] || I18N.ru;
    document.documentElement.lang = lang;
    document.querySelectorAll('[data-i18n]').forEach(function (el) {{
      var key = el.getAttribute('data-i18n');
      if (dict[key] != null) el.textContent = dict[key];
    }});
    document.querySelectorAll('[data-i18n-html]').forEach(function (el) {{
      var key = el.getAttribute('data-i18n-html');
      if (dict[key] != null) el.innerHTML = dict[key];
    }});
    document.querySelectorAll('[data-i18n-alt]').forEach(function (el) {{
      var key = el.getAttribute('data-i18n-alt');
      if (dict[key] != null) el.alt = dict[key];
    }});
    document.querySelectorAll('[data-i18n-aria]').forEach(function (el) {{
      var key = el.getAttribute('data-i18n-aria');
      if (dict[key] != null) el.setAttribute('aria-label', dict[key]);
    }});
    document.querySelectorAll('.lang button').forEach(function (btn) {{
      btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
    }});
    if (dict.docTitle) document.title = dict.docTitle;
    try {{ localStorage.setItem('guide-lang', lang); }} catch (e) {{}}
    applyTheme(document.documentElement.getAttribute('data-theme') || 'dark');
  }}

  function applyTheme(theme) {{
    var next = theme === 'light' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    try {{ localStorage.setItem('guide-theme', next); }} catch (e) {{}}
    var btn = document.getElementById('theme-toggle');
    if (!btn) return;
    var lang = 'ru';
    try {{ lang = localStorage.getItem('guide-lang') || document.documentElement.lang || 'ru'; }} catch (e) {{}}
    var dict = I18N[lang] || I18N.ru;
    var label = next === 'light'
      ? (dict.themeToDark || 'Dark theme')
      : (dict.themeToLight || 'Light theme');
    btn.setAttribute('aria-label', label);
    btn.title = label;
  }}

  var lightbox = document.getElementById('lightbox');
  var lightboxImg = document.getElementById('lightbox-img');
  var lightboxClose = document.getElementById('lightbox-close');

  function openLightbox(src, alt) {{
    lightboxImg.src = src;
    lightboxImg.alt = alt || '';
    lightbox.hidden = false;
    document.body.classList.add('lightbox-open');
  }}
  function closeLightbox() {{
    lightbox.hidden = true;
    lightboxImg.removeAttribute('src');
    document.body.classList.remove('lightbox-open');
  }}

  if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
  if (lightbox) {{
    lightbox.addEventListener('click', function (e) {{
      if (e.target === lightbox) closeLightbox();
    }});
  }}
  document.addEventListener('keydown', function (e) {{
    if (e.key === 'Escape' && lightbox && !lightbox.hidden) closeLightbox();
  }});
  document.querySelectorAll('.shot').forEach(function (box) {{
    box.addEventListener('click', function () {{
      var img = box.querySelector('img');
      var src = box.getAttribute('data-full') || (img && (img.currentSrc || img.src));
      if (src) openLightbox(src, img ? img.alt : '');
    }});
  }});

  document.querySelectorAll('.lang button').forEach(function (btn) {{
    btn.addEventListener('click', function () {{
      applyLang(btn.getAttribute('data-lang'));
    }});
  }});

  var themeBtn = document.getElementById('theme-toggle');
  if (themeBtn) {{
    themeBtn.addEventListener('click', function () {{
      var cur = document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
      applyTheme(cur === 'light' ? 'dark' : 'light');
    }});
  }}

  seedRuFromDom();
  var savedTheme = null;
  try {{ savedTheme = localStorage.getItem('guide-theme'); }} catch (e) {{}}
  if (!savedTheme && window.matchMedia) {{
    savedTheme = window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
  }}
  applyTheme(savedTheme || 'dark');

  var savedLang = null;
  try {{ savedLang = localStorage.getItem('guide-lang'); }} catch (e) {{}}
  var prefer = savedLang && I18N[savedLang] ? savedLang : 'ru';
  applyLang(prefer);

  window.__zrouteApplyTheme = applyTheme;
}})();
</script>
'''

# Remove old scripts and append new one
text = re.sub(
    r'\s*<script>[\s\S]*?</script>\s*<script>[\s\S]*?</script>\s*</body>',
    "\n" + SCRIPT + "\n</body>",
    text,
    count=1,
)

PATH.write_text(text, encoding="utf-8")
print("Patched", PATH)
print("keys en:", len(EN))
