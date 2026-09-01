---
name: zhubao-expression-maker
description: Generate expressive, mischievous, meme-like chibi sticker expressions for “助宝”, the mascot of the 文理助手 campus mini program. Use this skill whenever the user asks to make 助宝表情包、搞怪表情、古灵精怪动作、校园梗图、贴纸、聊天表情、reaction image, or asks to keep 助宝 character consistency while changing pose/expression. Default to upper-body compositions like the provided expression reference; only show the lower body when the requested gag/action clearly depends on a full-body pose.
---

# 助宝搞怪表情生成 Skill

## Goal

Create new “助宝” expression stickers that feel mischievous, lively, meme-aware, and slightly exaggerated rather than formal, elegant, or overly wholesome.

Always preserve the mascot identity first, then exaggerate expression and gesture second.

## Read these references first

Before generating, inspect these bundled assets:

1. `assets/zhubao-turnaround.png` — canonical character design and proportions.
2. `assets/zhubao-expression-reference.png` — target expression/sticker language and degree of exaggeration.
3. `assets/zhubao-badge-logo.png` — canonical 文理助手 mini-program logo used only as the chest pin/badge.

For detailed constraints, read:

- `references/character-spec.md`
- `references/expression-style.md`

## Canonical character identity

Introduce 助宝 internally as this character before composing any expression:

- Chibi anime campus girl mascot, not realistic human illustration.
- Warm dark-brown hair, large head-to-body ratio, soft rounded silhouette.
- One lively ahoge on top of the head.
- Long hair gathered into low twin ponytails with fluffy ends.
- Red bow hair accessory on the viewer-right side of her head.
- Large glossy purple eyes with pink-purple highlights.
- Soft blush on cheeks; small nose; highly elastic cartoon mouth shapes.
- Dark navy JK-style school blazer with white shirt.
- Red bow tie at the collar.
- Dark pleated skirt with subtle red/navy plaid when the lower body is visible.
- White socks and brown loafers only when full body is needed.
- The 文理助手 logo appears as ONE small chest pin/badge on the blazer. Do not place the logo on hair accessories, hats, props, books, boxes, cups, background, or elsewhere unless the user explicitly requests it.

Do not redesign the hairstyle, uniform, face, color palette, or badge placement between expressions.

## Expression style

Use the provided expression sheet as the behavioral reference, not as a literal pose template.

The visual language should be:

- 古灵精怪
- 搞怪、欠欠的、反差萌
- reaction-image / meme energy
- exaggerated but still cute
- quick-read silhouette and emotion
- sticker-friendly, clean white or transparent background

Prefer comedic distortion over “端庄可爱”. Examples of allowed exaggeration:

- eyes turning into blank white circles, spirals, stars, or squeezed shut lines
- huge crying streams, tiny smug eyes, dead-fish eyes, dramatic blush
- tongue-out face, crooked grin, puffed cheeks, shark-like tiny fang, stunned open mouth
- wobble marks, anger veins, sweat drops, question marks, impact stars, dizzy spirals
- pixel sunglasses, blanket cocoon, cardboard-box hiding, collapsing, table-flop, dramatic lying flat, snack frenzy, study meltdown

Avoid defaulting to simple waving, polite smiling, standard heart pose, or model-sheet neutrality unless the user specifically asks.

## Composition rules

Default composition is **upper body / bust / half body**, because the target is a chat-sticker expression pack.

Use full body only when the joke requires the legs/body to sell the gag, for example:

- lying flat / “躺平”
- falling over / fainting
- kicking legs in excitement
- crawling away
- running away
- sitting on the floor
- frozen inside an ice cube
- rolling around

If full body is not necessary, crop around chest or waist and make the face/hand gesture large.

Keep one expression centered and readable at small sticker size. Leave generous white space around the character.

## Badge/logo rules

The badge is an identity anchor, not decoration.

- Use `assets/zhubao-badge-logo.png` as the visual reference.
- Put it on the character's chest as a small circular pin.
- Keep the red outer ring + blue central mini-program icon impression recognizable.
- Do not enlarge it into a focal point.
- Do not duplicate it.
- Do not turn it into a hat emblem, hair clip, watermark, background logo, prop print, or repeated pattern.
- If the pose partially occludes the chest, natural partial occlusion is acceptable; do not distort the body just to expose the badge.

## Workflow

When the user gives a request such as “做一个助宝看到早八崩溃的表情”:

1. Parse the requested emotion, campus context, prop, text, and whether it needs upper body or full body.
2. Re-anchor the generation to `assets/zhubao-turnaround.png` for identity.
3. Re-anchor expression exaggeration to `assets/zhubao-expression-reference.png`.
4. Keep the chest pin consistent with `assets/zhubao-badge-logo.png`.
5. Design a stronger comedic beat than the literal request when appropriate. Example: “困” can become dead-fish eyes + face planted on desk + floating soul.
6. Generate the image directly when an image-generation tool is available.
7. If no image-generation tool is available, output a production-ready image prompt that explicitly cites the three bundled assets as references.

## Prompt construction template

Use this structure internally when generating:

**Character anchor**
“Use `assets/zhubao-turnaround.png` as the strict character identity reference: same brown hair, same low twin ponytails, same ahoge, same red hair bow, same purple eyes, same navy JK uniform, same red neck bow, same proportions.”

**Badge anchor**
“Use `assets/zhubao-badge-logo.png` only as the small chest pin on the blazer; do not place the logo anywhere else.”

**Expression anchor**
“Use `assets/zhubao-expression-reference.png` for the mischievous chibi sticker language, exaggerated facial acting, playful doodle marks, and meme-like comedic timing.”

**User request**
Insert the requested emotion/action/context.

**Composition**
“Upper-body sticker composition by default; only show full body if the gag requires body/leg action.”

**Rendering**
“Clean white or transparent background, crisp chibi linework, soft pastel cel shading, low visual clutter, strong silhouette, readable at chat-sticker scale.”

## Default interpretation examples

- “早八” → upper body, messy sleepy face, one eye barely open, coffee in hand, floating soul, exaggerated dark eye bags.
- “查成绩” → upper body, trembling hands holding phone, blank white eyes, blue-gray face shadow, sweat drops, tiny soul leaving body.
- “抢课成功” → upper body, wild starry eyes, both fists raised, confetti, almost villainous victorious grin.
- “抢课失败” → upper body, dead-fish eyes, cracked expression, mouse/phone slipping from hand, gray aura.
- “干饭” → upper body unless the user asks for more, cheeks stuffed, sparkle eyes, food flying slightly, shameless happy expression.
- “摆烂” → full body, lying flat like a flattened mascot, limbs spread, tiny ghost floating upward.
- “论文周” → upper body or desk scene, spiraled eyes, hair slightly frazzled, buried in papers, pen still in hand.
- “社恐” → upper body hiding behind a book/phone/box with only eyes visible.
- “吃瓜” → upper body holding watermelon or snack, tiny smug eyes, leaning forward as if listening to gossip.
- “无语” → upper body, half-lidded eyes, straight mouth, one tiny sweat drop, hands crossed.

## Text in stickers

Do not add text unless the user asks for wording or the joke benefits strongly from a short caption.

When text is used:

- Prefer 2–6 Chinese characters.
- Use colloquial campus/meme phrasing.
- Keep text secondary to the face.
- Avoid long sentences.
- Examples: “寄”, “绷不住了”, “早八啊…”, “开摆”, “好耶!”, “啊?”, “让我看看”, “已老实”, “救命”, “冲!”, “没睡醒”.

## Multi-expression sheets

If the user asks for a set:

- 4 expressions: 2×2 grid.
- 9 expressions: 3×3 grid.
- 16 expressions: 4×4 grid.

Maintain identical character design across every cell while changing only expression, pose, props, and comedic effects.

Favor a mix of:

- smug / 欠欠
- shocked
- crying
- rage
- sleepy
- dead inside
- food obsession
- study meltdown
- celebration
- embarrassment
- confusion
- hiding / escaping

## Quality checks before finalizing

Reject and regenerate if any of these happen:

- hair becomes silver/gray instead of brown
- the red bow disappears or moves unpredictably
- the face becomes realistic or mature
- the uniform becomes a generic sailor suit unrelated to the established blazer design
- the chest logo is missing in an unobstructed front-facing pose
- the logo appears anywhere other than the chest pin without explicit request
- the expression looks too polite, formal, or generic
- unnecessary full-body framing makes the face too small
- multiple expressions no longer look like the same person
- props or text become more visually important than 助宝

## Expected user experience

The user should be able to type short prompts such as:

- “助宝看到明天早八，生无可恋”
- “做一个助宝查成绩后石化的表情”
- “助宝吃瓜，表情欠一点”
- “给我9个期末周搞怪表情”
- “助宝躺平，做成全身表情”

and receive a character-consistent, chest-badge-consistent, meme-like 助宝 sticker without having to restate the character design each time.
