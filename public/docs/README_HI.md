<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/logo.webp" width="180" />
</p>

<h1 align="center">प्रारंभ / मध्य / अंत</h1>

<p align="center">
  <a href="https://github.com/bastndev/skills/blob/main/README.md">English 🇺🇸</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_ES.md">Español 🇪🇸</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_ZH.md">中文 🇨🇳</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_DE.md">Deutsch 🇩🇪</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_FR.md">Français 🇫🇷</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_JA.md">日本語 🇯🇵</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_KO.md">한국어 🇰🇷</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_PT.md">Português 🇧🇷</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_RU.md">Русский 🇷🇺</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_VI.md">Tiếng Việt 🇻🇳</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_AR.md">العربية 🇸🇦</a>
</p>

<br>

<p align="center">
  नए प्रोजेक्ट्स को आत्मविश्वास के साथ बूटस्ट्रैप करें। जैसे-जैसे वे बढ़ते हैं, उन्हें परिष्कृत और मजबूत करें। वास्तुकला को विकसित होने पर गहन, सुरक्षित रीफैक्टरिंग करें।
</p>

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

## तीन चरण

| चरण | उद्देश्य | प्रमुख क्षमताएं | उदाहरण | स्थिति |
| --- | --- | --- | --- | --- |
| **Start** | प्रोजेक्ट इनिशियलाइजेशन | उत्पादन के लिए तैयार फ़ोल्डर संरचना बनाना, फ्रेमवर्क प्रारंभ करना, पहले कमिट से सर्वोत्तम प्रथाओं को लागू करना। | `start-nextjs`... | योजनाबद्ध |
| **Middle** | निरंतर सुधार | UI/UX बढ़ाएं, सुरक्षा कड़ी करें, प्रदर्शन बढ़ाएं, तर्क साफ करें, मृत कोड हटाएं। | TBD | योजनाबद्ध |
| **End** | ऑडिट और रीफैक्टरिंग | पूर्ण वास्तुकला और गुणवत्ता विश्लेषण। चरणबद्ध योजना **केवल स्पष्ट स्वीकृति के साथ** निष्पादित की गई। | `refactor-project` | ✅ उपलब्ध |

## उपलब्ध कौशल (Skills)

| कौशल | विवरण |
| --- | --- |
| **[end](../../skills/end/README.md)** | **`refactor-project`** — आपके प्रोजेक्ट को शुरू से अंत तक समझता है। ठोस संदर्भों के साथ एक स्पष्ट निदान प्रदान करता है। सही वास्तुकला दिशा की सिफारिश करता है और एक व्यवस्थित निष्पादन योजना बनाता है। आप पूर्ण नियंत्रण में रहते हैं।<br><br>→ [पूर्ण दस्तावेज़ और उदाहरण](../../skills/end/README.md) |

> **नोट:** प्रत्येक skill का अपना विस्तृत README होता है। रूट पृष्ठ उच्च-स्तरीय अवलोकन देता है; गहन उपयोग, रिपोर्ट उदाहरण और गारंटी के लिए `../../skills/<skill>/README.md` देखें।

## स्थापना

```bash
# वर्तमान कौशल जोड़ें (End / refactor-project)
npx skills add bastndev/skills --skill end
```

भविष्य के कौशल भी इसी तरह स्थापित किए जा सकेंगे:

```bash
npx skills add bastndev/skills --skill start-nextjs
```

## End Skill कैसे काम करता है

1. **पहले विश्लेषण** — प्रवेश बिंदुओं को मैप करता है और प्रोजेक्ट को समझता है। **कोई फ़ाइल संशोधित नहीं की जाती है।**
2. **संरचित रिपोर्ट** — चार श्रेणियों (गंभीरता के साथ पुष्ट बग, जोखिम, रिफैक्टरिंग अवसर, तकनीकी ऋण) में स्पष्ट निष्कर्ष + एक वास्तुकला अनुशंसा और आदेशित योजना। सभी आइटम में विशिष्ट फ़ाइल और लाइन संदर्भ शामिल हैं।
3. **आप प्रत्येक चरण को अधिकृत करते हैं** — यह एक समय में **ठीक एक चरण** निष्पादित करता है। प्रत्येक चरण के बाद आपको परिवर्तनों, किए गए सत्यापन और शेष चरणों की सूची का सटीक सारांश मिलता है।
4. **पूर्ण नियंत्रण और सुरक्षा** — यदि प्रोजेक्ट में कोई परीक्षण नहीं था तो कभी परीक्षण नहीं बनाता है। अनुमति के बिना कभी भी निर्भरता नहीं जोड़ता या पैकेज मैनेजर को नहीं बदलता। आपके गैर-प्रतिबद्ध कार्य का सम्मान करता है और हमेशा वर्तमान व्यवहार को सुरक्षित रखता है जब तक कि उचित बग को ठीक न कर रहा हो।

पूर्ण वर्कफ़्लो, सटीक रिपोर्ट प्रारूप, वास्तुकला निर्णय नियम और सभी सुरक्षा गारंटी के लिए, समर्पित skill दस्तावेज़ पढ़ें:

→ **[End – Refactor Project](../../skills/end/README.md)**

पूर्ण आंतरिक विशिष्टता [skills/end/SKILL.md](../../skills/end/SKILL.md) में है।

## रोडमैप

- **Start skills** — लोकप्रिय स्टैक (Next.js, Vite, FastAPI, आदि) के लिए एक-कमांड प्रोजेक्ट मचान।
- **Middle skills** — केंद्रित, ऑन-डिमांड सुधारक (प्रदर्शन, सुरक्षा, यूएक्स, मृत-कोड हटाना, आदि)।
- **End विस्तार** — अधिक रनटाइम, अतिरिक्त विशेष रिफैक्टरिंग मोड और उपयोगिताएँ।

प्रत्येक skill का अपना समर्पित दस्तावेज़ होगा (जैसे वर्तमान [End – Refactor Project](../../skills/end/README.md))।

---

<br>

<div align="center">
  <p align="center">
  <sub>उन डेवलपर्स के लिए बनाया गया है जो चाहते हैं कि उनके एआई एजेंट एक वरिष्ठ इंजीनियर के अनुशासन के साथ काम करें।</sub>
</p>

_If you find any bugs or have feedback, feel free to [open an issue](https://github.com/bastndev/skills/issues/new)._

<sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a></sub>

</div>
