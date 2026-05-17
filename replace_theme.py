import re

with open('/Users/emmyweber285gmail.com/Desktop/protfolio-dipto/html-portfolio/index.html', 'r') as f:
    content = f.read()

# 1. Replace the <head> and <style> completely
style_pattern = re.compile(r'<link href="https://fonts.googleapis\.com.*?</style>', re.DOTALL)

new_style = """<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,300;12..96,700;12..96,900&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #020617;
            --accent-1: #10b981; /* Emerald */
            --accent-2: #0ea5e9; /* Sky */
            --bg-grid: rgba(255, 255, 255, 0.03);
        }
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg);
            color: #f8fafc;
            overflow-x: hidden;
            /* Grid Pattern */
            background-image: 
                linear-gradient(var(--bg-grid) 1px, transparent 1px),
                linear-gradient(90deg, var(--bg-grid) 1px, transparent 1px);
            background-size: 40px 40px;
            background-position: center center;
        }
        
        /* Floating Glowing Orbs */
        body::before, body::after {
            content: '';
            position: fixed;
            width: 600px;
            height: 600px;
            border-radius: 50%;
            filter: blur(150px);
            z-index: -1;
            opacity: 0.15;
            pointer-events: none;
        }
        body::before {
            background: var(--accent-1);
            top: -200px;
            left: -200px;
        }
        body::after {
            background: var(--accent-2);
            bottom: -200px;
            right: -200px;
        }

        h1, h2, h3 { font-family: 'Bricolage Grotesque', sans-serif; }

        /* Modern Wave/Soft Section instead of Diagonal */
        .themed-section {
            position: relative;
            padding: 8rem 0;
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(20px);
            border-top: 1px solid rgba(255,255,255,0.05);
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }

        .glass-card {
            background: rgba(255, 255, 255, 0.02);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 24px;
            transition: all 0.5s cubic-bezier(0.25, 1, 0.5, 1);
            box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5);
        }
        .glass-card:hover {
            transform: translateY(-10px);
            border-color: rgba(16, 185, 129, 0.4);
            box-shadow: 0 20px 40px -10px rgba(16, 185, 129, 0.15);
            background: rgba(255, 255, 255, 0.04);
        }

        .gradient-text {
            background: linear-gradient(135deg, var(--accent-1), var(--accent-2));
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .fade-in {
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.8s cubic-bezier(0.25, 1, 0.5, 1);
        }
        .fade-in.visible {
            opacity: 1;
            transform: translateY(0);
        }

        .nav-fixed {
            position: fixed;
            top: 2rem; left: 2rem; bottom: 2rem;
            width: 80px;
            background: rgba(15, 23, 42, 0.4);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 100px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            padding: 3rem 0;
            z-index: 1000;
        }
        .nav-link {
            writing-mode: vertical-rl;
            text-orientation: mixed;
            transform: rotate(180deg);
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.25em;
            opacity: 0.4;
            transition: 0.3s;
        }
        .nav-link:hover { opacity: 1; color: var(--accent-1); }

        .content-wrapper {
            margin-left: 120px;
            padding: 0 4rem;
        }

        .hero-title {
            font-size: clamp(4rem, 10vw, 12rem);
            font-weight: 900;
            line-height: 0.85;
            letter-spacing: -0.03em;
        }

        .skill-circle {
            width: 130px; height: 130px;
            border-radius: 24px; /* Squircle */
            border: 1px solid rgba(255, 255, 255, 0.08);
            background: rgba(255,255,255,0.01);
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            gap: 0.75rem;
            transition: all 0.4s;
        }
        .skill-circle:hover {
            border-color: var(--accent-2);
            background: rgba(14, 165, 233, 0.05);
            transform: scale(1.05) rotate(2deg);
        }

        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-track { background: var(--bg); }
        ::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 4px; }
    </style>"""

content = style_pattern.sub(new_style, content)

# 2. Replace classes in HTML
# holo-text -> gradient-text
content = content.replace('holo-text', 'gradient-text')
# diagonal-section bg-gradient -> themed-section
content = content.replace('diagonal-section bg-gradient', 'themed-section')
content = content.replace('diagonal-section', 'themed-section')

# Colors
content = content.replace('text-pink-400', 'text-sky-400')
content = content.replace('text-cyan-400', 'text-emerald-400')
content = content.replace('text-indigo-400', 'text-indigo-400') # keep indigo
content = content.replace('border-cyan-400', 'border-emerald-400')
content = content.replace('border-pink-400', 'border-sky-400')

with open('/Users/emmyweber285gmail.com/Desktop/protfolio-dipto/html-portfolio/index.html', 'w') as f:
    f.write(content)

print("Replacement complete.")
