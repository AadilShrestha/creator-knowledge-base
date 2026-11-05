# Test Cream: generation prompts for later use

**Not executed.** These are human-readable briefs. Adapt them to the connected Higgsfield tools and supported models; headings are not API field names. See [research and official sources](research.md) for the evidence behind the workflow.

## 1. Character reference / start-frame prompt

```text
Create one vertical 9:16 reference photograph for a fictional adult presenter named Maya, approximately 29. This is the first frame of a creator-style skincare concept, photographed like a phone resting at eye level on a bathroom shelf.

Maya has a warm medium-brown complexion with visible natural skin texture, shoulder-length dark wavy hair loosely clipped back, and a plain charcoal cotton T-shirt. She looks into the lens with lips gently closed and a relaxed expression. Chest-up framing, shoulders and a little countertop visible. Her hands rest out of frame.

A modest bathroom: off-white tiles, pale wood countertop, a plain towel, three small generic unbranded skincare bottles, and a phone lying on the counter. Warm diffused vanity lighting, plausible shadows, ordinary phone-camera depth of field, restrained natural color. Leave comfortable crop room around her face.

Preserve natural facial asymmetry, pores, under-eye detail, and ordinary skin marks. Avoid retouched beauty lighting, dramatic cinematic styling, text overlays, and watermarks. One adult only. This character is fictional, not a likeness of a real creator or customer.
```

Approve and save this image before generating further shots. Derive additional scene framings from it; for recurring production, inspect the available persistent-identity workflow instead of assuming a filename locks identity.

## 2. Product reference prompt

```text
Create a neutral product-design reference for a fictional face moisturizer called TEST CREAM. Small cylindrical matte ivory jar with a matte sage-green screw lid. Straight-on three-quarter view on a neutral warm-gray surface, soft even lighting, realistic proportions and contact shadow. One jar, no extra packaging, no ingredients, badges, results, price, or skincare claims. The only proposed brand text is TEST CREAM, uppercase, plain dark sans serif. Leave the label area clean and flat enough to apply or correct the exact lettering in the edit. This is a fictional packaging concept.
```

Keep the approved jar reference attached wherever it appears. Check generated lettering; use a controlled label/overlay rather than accept misspellings. Reference-ID syntax and asset slots must come from the live tools.

## 3. Voice and exact audio

```text
One consistent adult English-speaking feminine voice, warm mid-range tone, relaxed conversational delivery. A small smile in the opening question, a dry pause before "homework," and an easier settled delivery at the close. Approximately 130 words per minute across the finished ad, with natural short pauses; measure the result rather than forcing a rushed reading. No exaggerated sales voice. Use one stock synthetic voice for all lines; do not imitate a real person's voice.

Exact dialogue:
Why does getting ready for bed need this many instructions?
Phone open. Three bottles out. Still checking what goes on next.
And now the thing that's supposed to feel relaxing... feels like homework.
Maybe tonight, the moisturizer step doesn't need a whole production.
Meet Test Cream. Open. Apply. Get on with your evening.
A little less routine. A little more you. Explore Test Cream.
```

Generate the approved audio once if the tools support audio-first lip sync. Measure it, then segment it to match the shots. Otherwise preserve the same voice and exact lines in the available supported workflow.

## 4. Talking-shot motion prompt: the opening pilot

Inputs: approved Maya bathroom still and the audio segment for the opening line. Request a supported duration long enough for that line; trim to approximately four seconds only after measuring the speech.

```text
Animate the exact adult presenter and bathroom from the approved start frame. Keep the existing chest-up eye-level phone framing, charcoal shirt, hairstyle, skin texture, room layout, and warm vanity lighting consistent. Camera remains stationary.

She addresses the lens with the supplied opening audio: "Why does getting ready for bed need this many instructions?" Mouth movement follows that audio. On "this many instructions" she lifts one eyebrow and gives a small knowing half-smile. Natural blinks and subtle breathing; hands stay out of frame. End in a relaxed neutral pose.

Ordinary phone-video appearance. No skin smoothing, changing facial features, new props, camera orbit, beauty transformation, music, generated subtitles, or extra speech. Add final captions during editing.
```

This is a pilot, not a whole-ad generation. Check face, mouth, voice, lighting, and pacing before repeating the process for the other talking shots.

## 5. Product insert motion prompt

Inputs: approved jar and bathroom countertop reference. Generate separately from the talking shot.

```text
Vertical close-up of the approved TEST CREAM jar on the established pale wood bathroom countertop under the same warm diffused vanity lighting. Match its ivory body, sage lid, scale, and design to the product reference.

One hand with short unpainted nails gently unscrews and lifts the lid; the other hand keeps the jar steady. One simple continuous action, camera static, physically plausible fingers, contact shadows, and jar geometry. The material inside is ordinary off-white cream. Keep label position stable; final lettering can be corrected in the edit. No magical glow, floating packaging, extra hands, cosmetic-results imagery, generated captions, or spoken dialogue.
```

The face application gets its own insert: same presenter and lighting, one gentle cheek dab, unchanged skin texture and complexion. Do not combine opening the lid, scooping, facial application, talking, and a camera move into the same shot for this pilot.

## 6. Orchestration prompt after Higgsfield is connected

```text
Produce the Test Cream UGC concept using this saved production pack. Read the strategy, script/shot list, and prompts before generating. This is a fictional moisturizer concept and fictional presenter, not a customer testimonial.

First inspect the connected Higgsfield tools and supported workflow. Preserve the approved script rather than silently rewriting it. Identify the required character, scene, product, voice, lip-sync, and assembly capabilities. Use actual supported fields and duration limits. The intended 30-second edit may need multiple clips; do not assume a 30-second generation is available.

Create and review the character, bathroom, and product reference images. Reuse approved references consistently. Make one short opening pilot using the same voice and supplied line. Check identity, mouth movement, skin texture, room, and pacing before producing remaining shots.

Use the seven editorial beats in script-and-shotlist.md. Generate hand/product actions as separate inserts. Assemble in 9:16, conform cuts to measured audio, then add controlled captions, exact TEST CREAM branding, and the single closing CTA. Keep the same lighting and skin texture; no product-result transformation, fabricated endorsements, ingredients, pricing, discounts, or testimonials.

Check estimated credits before production and follow the user's spending authorization. Save source prompts, reference assets/IDs, model/settings, audio, generated clips, selected takes, and the final export in this project folder. Report generated assets and remaining work accurately. A file is finished only after visual/audio QA and a verified playable export.
```
