  Use the "l10n-sync" skill (read .agents/skills/l10n-sync/SKILL.md).
  
  I want you to update the "nls.jsn"
   
  Let me read the skill file first.
● Read
  /home/zorin/Documents/VSC-extension/F1/.agents/skills/l10n-sync/SKIL
  L.md

  The skill is for README localization, but you mentioned updating
  nls.jsn. Let me find that file to understand what you're working
  with.
● Glob "**/nls*.json"
    ╰ path=/home/zorin/Documents/VSC-extension/F1
  No files found matching pattern: **/nls*.json
● Glob "**/*nls*"
    ╰ path=/home/zorin/Documents/VSC-extension/F1
  12 files
    package.nls.json, package.nls.es.json, package.nls.hi.json +9 more

  Found them. You meant package.nls.json files. Let me read the
  English source and all the translated ones to understand what needs
  updating.
● Read (12 files)
    package.nls.json, package.nls.es.json, package.nls.hi.json
    package.nls.ko.json, package.nls.pt-br.json +7 more

  Now I can see the issue clearly. The English package.nls.json has
  been updated with a new, richer description (and a cleaner
  displayName), but all 11 translated files are still on the old
  content. They need to be synced to match the English source.
  
  The new English content:
  
  - displayName: "F1" (was "F1 [AI] composer")
  - description: full new text listing Kilo Code, OpenCode, @-file
  mentions, images, auto-translation and voice, Install agent Skills,
  etc.
  
  Let me update all translated files now, one by one.
● Task list created
● Write /home/zorin/Documents/VSC-extension/F1/package.nls.es.json
  added 2 lines, removed 2 lines in package.nls.es.json
     1   {
     2-    "displayName": "F1 [AI] composer",                         
     -    "description": "Todo-en-Uno (F1 [AI] composer) — [CLI Hub,  
     My skills, My Memory] Una tecla para lanzar y cambiar entre      
     Claude Code, Codex, Copilot, Cursor, Kiro, Grok, Antigravity o   
     cualquier CLI de IA. Skills, Memory y herramientas de Prompt     
     2+    "displayName": "F1",                                       
     +    "description": "Centro de CLI de IA todo en uno: una tecla  
     para lanzar, cambiar y gestionar Claude Code, Codex, Copilot,    
     Cursor, Kiro, Kilo Code, OpenCode, Grok, Antigravity o cualquier 
     agente de codificación personalizado — en paralelo en tu IDE.    
     Escribe mejores prompts con menciones @-archivo, imágenes,       
     traducción automática y voz. Instala Skills para agentes,        
     monitorea el uso y prepara cada CLI con la memoria de tu proyecto
     para que empiece conociendo tu código."                          
     4   }
● Tasks updated
● Write /home/zorin/Documents/VSC-extension/F1/package.nls.de.json
  added 2 lines, removed 2 lines in package.nls.de.json
     1   {
     2-    "displayName": "F1 [AI] composer",                         
     -    "description": "All-in-One (F1 [AI] composer) — [CLI Hub, My
     skills, My Memory] Eine Taste, um Claude Code, Codex, Copilot,   
     Cursor, Kiro, Grok, Antigravity oder jedes KI-CLI zu starten und 
     zu wechseln. Integrierte Skills, Memory & Prompt-Tools. 雨"      
     2+    "displayName": "F1",                                       
     +    "description": "All-in-One KI-CLI-Hub: eine Taste zum       
     Starten, Wechseln und Verwalten von Claude Code, Codex, Copilot, 
     Cursor, Kiro, Kilo Code, OpenCode, Grok, Antigravity oder einem  
     beliebigen benutzerdefinierten Coding-Agenten — nebeneinander in 
     deiner IDE. Schreibe bessere Prompts mit @-Dateiverweisen,       
     Bildern, automatischer Übersetzung und Sprachausgabe. Installiere
     Agenten-Skills, verfolge die Nutzung und bereite jedes CLI mit   
     dem Projektgedächtnis vor, damit es deine Codebasis von Anfang an
     kennt."                                                          
     4   }
● Write /home/zorin/Documents/VSC-extension/F1/package.nls.fr.json
  added 2 lines, removed 2 lines in package.nls.fr.json
     1   {
     2-    "displayName": "F1 [AI] composer",                         
     -    "description": "Tout-en-Un (F1 [AI] composer) — [CLI Hub, My
     skills, My Memory] Une touche pour lancer et basculer entre      
     Claude Code, Codex, Copilot, Cursor, Kiro, Grok, Antigravity ou  
     toute CLI d'IA. Outils Skills, Memory et Prompt intégrés. 雨"    
     2+    "displayName": "F1",                                       
     +    "description": "Hub CLI IA tout-en-un : une touche pour     
     lancer, basculer et gérer Claude Code, Codex, Copilot, Cursor,   
     Kiro, Kilo Code, OpenCode, Grok, Antigravity ou tout agent de    
     codage personnalisé — côte à côte dans votre IDE. Rédigez de     
     meilleurs prompts avec les mentions @-fichier, les images, la    
     traduction automatique et la voix. Installez des Skills pour les 
     agents, suivez l'utilisation et initialisez chaque CLI avec la   
     mémoire de votre projet pour qu'il connaisse déjà votre code."   
     4   }
● Write /home/zorin/Documents/VSC-extension/F1/package.nls.pt-br.json
  added 2 lines, removed 2 lines in package.nls.pt-br.json
     1   {
     2-    "displayName": "F1 [AI] composer",                         
     -    "description": "Tudo-em-Um (F1 [AI] composer) — [CLI Hub, My
     skills, My Memory] Uma tecla para iniciar e alternar entre Claude
     Code, Codex, Copilot, Cursor, Kiro, Grok, Antigravity ou qualquer
     CLI de IA. Ferramentas Skills, Memory e Prompt integradas. 雨"   
     2+    "displayName": "F1",                                       
     +    "description": "Hub de CLI de IA tudo-em-um: uma tecla para 
     iniciar, alternar e gerenciar Claude Code, Codex, Copilot,       
     Cursor, Kiro, Kilo Code, OpenCode, Grok, Antigravity ou qualquer 
     agente de codificação personalizado — lado a lado na sua IDE.    
     Escreva prompts melhores com menções @-arquivo, imagens, tradução
     automática e voz. Instale Skills para agentes, acompanhe o uso e 
     prepare cada CLI com a memória do seu projeto para que ele já    
     conheça sua base de código."                                     
     4   }
● Write /home/zorin/Documents/VSC-extension/F1/package.nls.ru.json
  added 2 lines, removed 2 lines in package.nls.ru.json
     1   {
     2-    "displayName": "F1 [AI] composer",                         
     -    "description": "Всё-в-Одном (F1 [AI] composer) — [CLI Hub,  
     My skills, My Memory] Одна клавиша для запуска и переключения    
     между Claude Code, Codex, Copilot, Cursor, Kiro, Grok,           
     Antigravity или любым AI CLI. Встроенные инструменты Skills,     
     2+    "displayName": "F1",                                       
     +    "description": "Универсальный хаб AI CLI: одна клавиша для  
     запуска, переключения и управления Claude Code, Codex, Copilot,  
     Cursor, Kiro, Kilo Code, OpenCode, Grok, Antigravity или любым   
     пользовательским агентом — бок о бок в вашей IDE. Пишите лучше   
     промпты с @-упоминаниями файлов, изображениями, автопереводом и  
     голосом. Устанавливайте Skills для агентов, отслеживайте         
     использование и подготавливайте каждый CLI с памятью проекта,    
     чтобы он сразу знал вашу кодовую базу."                          
     4   }
● Write /home/zorin/Documents/VSC-extension/F1/package.nls.ja.json
  added 2 lines, removed 2 lines in package.nls.ja.json
     1   {
     2-    "displayName": "F1 [AI] composer",                         
     -    "description": "オールインワン (F1 [AI] composer) — [CLI    
     Hub, My skills, My Memory] ワンキーで Claude                     
     Code、Codex、Copilot、Cursor、Kiro、Grok、Antigravity            
     または任意の AI CLI を起動・切替。Skills、Memory、Prompt         
     2+    "displayName": "F1",                                       
     +    "description": "オールインワン AI CLI ハブ：1               
     つのホットキーで Claude Code、Codex、Copilot、Cursor、Kiro、Kilo 
     Code、OpenCode、Grok、Antigravity またはカスタム CLI             
     を起動・切り替え・管理 — IDE                                     
     上に並べて表示。@-ファイルメンション、画像、自動翻訳、音声でより 
     良いプロンプトを作成。エージェントのスキルをインストールし、使用 
     状況を追跡し、プロジェクトのメモリで各 CLI                       
     を準備してコードベースを最初から把握させましょう。"              
     4   }
● Write /home/zorin/Documents/VSC-extension/F1/package.nls.zh-cn.json
  added 2 lines, removed 2 lines in package.nls.zh-cn.json
     1   {
     2-    "displayName": "F1 [AI] composer",                         
     -    "description": "一体化 (F1 [AI] composer) — [CLI Hub, My    
     skills, My Memory] 一键启动并切换 Claude                         
     Code、Codex、Copilot、Cursor、Kiro、Grok、Antigravity 或任何 AI  
     CLI。内置 Skills、Memory 和 Prompt 工具。雨"                     
     2+    "displayName": "F1",                                       
     +    "description": "一体化 AI CLI 中心：一键启动、切换和管理    
     Claude Code、Codex、Copilot、Cursor、Kiro、Kilo                  
     Code、OpenCode、Grok、Antigravity 或任何自定义编码代理——在 IDE   
     中并排使用。通过                                                 
     @-文件提及、图片、自动翻译和语音编写更好的提示词。安装代理技能， 
     追踪使用情况，并用项目记忆初始化每个                             
     4   }
● Write /home/zorin/Documents/VSC-extension/F1/package.nls.ko.json
  added 2 lines, removed 2 lines in package.nls.ko.json
     1   {
     2-    "displayName": "F1 [AI] composer",                         
     -    "description": "올인원 (F1 [AI] composer) — [CLI Hub, My    
     skills, My Memory] 단축키 하나로 Claude Code, Codex, Copilot,    
     Cursor, Kiro, Grok, Antigravity 또는 모든 AI CLI를 실행하고      
     전환하세요. Skills, Memory, Prompt 도구 내장. 雨"                
     2+    "displayName": "F1",                                       
     +    "description": "올인원 AI CLI 허브: 단축키 하나로 Claude    
     Code, Codex, Copilot, Cursor, Kiro, Kilo Code, OpenCode, Grok,   
     Antigravity 또는 모든 커스텀 코딩 에이전트를 실행·전환·관리 —    
     IDE에서 나란히. @-파일 언급, 이미지, 자동 번역, 음성으로 더 나은 
     프롬프트를 작성하세요. 에이전트 Skills를 설치하고, 사용량을      
     추적하며, 프로젝트 메모리로 각 CLI를 준비해 코드베이스를 처음부터
     4   }
● Write /home/zorin/Documents/VSC-extension/F1/package.nls.ar.json
  added 2 lines, removed 2 lines in package.nls.ar.json
     1   {
     2-    "displayName": "F1 [AI] composer",                         
     -    "description": "الكل في واحد (F1 [AI] composer) — [CLI Hub, 
     My skills, My Memory] اختصار واحد لتشغيل والتبديل بين Claude Code
     وCodex وCopilot وCursor وKiro وGrok وAntigravity أو أي CLI للذكاء
     الاصطناعي. أدوات Skills وMemory وPrompt مدمجة. 雨"               
     2+    "displayName": "F1",                                       
     +    "description": "مركز CLI للذكاء الاصطناعي متكامل: مفتاح واحد
     لتشغيل وتبديل وإدارة Claude Code وCodex وCopilot وCursor وKiro   
     وKilo Code وOpenCode وGrok وAntigravity أو أي وكيل برمجي مخصص —  
     جنبًا إلى جنب في بيئة التطوير. اكتب تعليمات أفضل مع إشارات @-ملف  
     والصور والترجمة التلقائية والصوت. ثبّت مهارات الوكلاء وتتبع       
     الاستخدام وهيّئ كل CLI بذاكرة مشروعك ليبدأ مدركًا لقاعدة الكود     
     4   }
● Write /home/zorin/Documents/VSC-extension/F1/package.nls.vi.json
  added 2 lines, removed 2 lines in package.nls.vi.json
     1   {
     2-    "displayName": "F1 [AI] composer",                         
     -    "description": "Tất-Cả-Trong-Một (F1 [AI] composer) — [CLI  
     Hub, My skills, My Memory] Một phím tắt để khởi chạy và chuyển   
     đổi giữa Claude Code, Codex, Copilot, Cursor, Kiro, Grok,        
     Antigravity hoặc bất kỳ AI CLI nào. Tích hợp công cụ Skills,     
     2+    "displayName": "F1",                                       
     +    "description": "Trung tâm CLI AI tất-cả-trong-một: một phím 
     tắt để khởi chạy, chuyển đổi và quản lý Claude Code, Codex,      
     Copilot, Cursor, Kiro, Kilo Code, OpenCode, Grok, Antigravity    
     hoặc bất kỳ tác nhân lập trình tùy chỉnh nào — song song trong   
     IDE của bạn. Viết prompt tốt hơn với đề cập @-tệp, hình ảnh, dịch
     tự động và giọng nói. Cài đặt Skills cho tác nhân, theo dõi mức  
     sử dụng và khởi tạo mỗi CLI với bộ nhớ dự án để nó bắt đầu đã    
     4   }
● Write /home/zorin/Documents/VSC-extension/F1/package.nls.vi.json
  added 2 lines, removed 2 lines in package.nls.vi.json
     1   {
     2-    "displayName": "F1 [AI] composer",                         
     -    "description": "Tất-Cả-Trong-Một (F1 [AI] composer) — [CLI  
     Hub, My skills, My Memory] Một phím tắt để khởi chạy và chuyển   
     đổi giữa Claude Code, Codex, Copilot, Cursor, Kiro, Grok,        
     Antigravity hoặc bất kỳ AI CLI nào. Tích hợp công cụ Skills,     
     2+    "displayName": "F1",                                       
     +    "description": "Trung tâm CLI AI tất-cả-trong-một: một phím 
     tắt để khởi chạy, chuyển đổi và quản lý Claude Code, Codex,      
     Copilot, Cursor, Kiro, Kilo Code, OpenCode, Grok, Antigravity    
     hoặc bất kỳ tác nhân lập trình tùy chỉnh nào — song song trong   
     IDE của bạn. Viết prompt tốt hơn với đề cập @-tệp, hình ảnh, dịch
     tự động và giọng nói. Cài đặt Skills cho tác nhân, theo dõi mức  
     sử dụng và khởi tạo mỗi CLI với bộ nhớ dự án để nó bắt đầu đã    
     4   }
● Write /home/zorin/Documents/VSC-extension/F1/package.nls.hi.json
  added 2 lines, removed 2 lines in package.nls.hi.json
     1   {
     2-    "displayName": "F1 [AI] composer",                         
     -    "description": "ऑल-इन-वन (F1 [AI] composer) — [CLI Hub, My  
     skills, My Memory] एक हॉटकी से Claude Code, Codex, Copilot, Cursor,    Skills, Memory और Prompt टूल्स। 雨"                                
● Write /home/zorin/Documents/VSC-extension/F1/package.nls.hi.json
  added 2 lines, removed 2 lines in package.nls.hi.json
     1   {
     2-    "displayName": "F1 [AI] composer",                         
     -    "description": "ऑल-इन-वन (F1 [AI] composer) — [CLI Hub, My  
     skills, My Memory] एक हॉटकी से Claude Code, Codex, Copilot, Cursor,  IDE में    
     Kiro, Grok, Antigravity या किसी भी AI CLI को लॉन्च और स्विच करें। बिल्ट-इन       avity या किसी भी कस्टम कोडिंग एजेंट को लॉन्च, स्विच और मैनेज करें — अ
     Skills, Memory और Prompt टूल्स। 雨"                                     साथ-साथ। @-फ़ाइल मेंशन, इमेज, ऑटो-ट्रांसलेशन और वॉइस के साथ बेहतर प्रॉम्प्ट ल
     2+    "displayName": "F1",                                       
     +    "description": "ऑल-इन-वन AI CLI हब: एक हॉटकी से Claude Code,   ार करें ताकि  
     Codex, Copilot, Cursor, Kiro, Kilo Code, OpenCode, Grok,         
     Antigravity या किसी भी कस्टम कोडिंग एजेंट को लॉन्च, स्विच और मैनेज करें — अपने IDE में    . (esc to cancel)
     साथ-साथ। @-फ़ाइल मेंशन, इमेज, ऑटो-ट्रांसलेशन और वॉइस के साथ बेहतर प्रॉम्प्ट लिखें। एजेंट      ─────────────────────────────────────────────────────────
     Skills इंस्टॉल करें, उपयोग ट्रैक करें और हर CLI को अपने प्रोजेक्ट की मेमोरी से तैयार करें ताकि  
     4   }
● Tasks updated

  Listo 🎉 — localización completada:
  
  ┌────────────────────────┬───────┬──────┬────────┐
  │ file                   │ lang  │ mode │ status │
  ├────────────────────────┼───────┼──────┼────────┤
  │ package.nls.es.json    │ es    │ full │ ✅     │
  ├────────────────────────┼───────┼──────┼────────┤
  │ package.nls.de.json    │ de    │ full │ ✅     │
  ├────────────────────────┼───────┼──────┼────────┤
  │ package.nls.fr.json    │ fr    │ full │ ✅     │
  ├────────────────────────┼───────┼──────┼────────┤
  │ package.nls.pt-br.json │ pt-br │ full │ ✅     │
  ├────────────────────────┼───────┼──────┼────────┤
  │ package.nls.ru.json    │ ru    │ full │ ✅     │
  ├────────────────────────┼───────┼──────┼────────┤
  │ package.nls.ja.json    │ ja    │ full │ ✅     │
  ├────────────────────────┼───────┼──────┼────────┤
  │ package.nls.zh-cn.json │ zh-cn │ full │ ✅     │
  ├────────────────────────┼───────┼──────┼────────┤
  │ package.nls.ko.json    │ ko    │ full │ ✅     │
  ├────────────────────────┼───────┼──────┼────────┤
  │ package.nls.ar.json    │ ar    │ full │ ✅     │
  ├────────────────────────┼───────┼──────┼────────┤
  │ package.nls.vi.json    │ vi    │ full │ ✅     │
  ├────────────────────────┼───────┼──────┼────────┤
  │ package.nls.hi.json    │ hi    │ full │ ✅     │
  └────────────────────────┴───────┴──────┴────────┘
  
  Two changes propagated to all 11 files:
  
  - displayName: "F1 [AI] composer" → "F1"
  - description: updated to include Kilo Code, OpenCode, @-file
  mentions, images, auto-translation, voice, agent Skills, usage
  tracking, and project memory priming.

▸ Credits: 1.74 • Time: 2m 15s
