with open('style.css', 'r') as f:
    css = f.read()

# Add hover effect and transition for card to make it look punchier
css += '''
/* Enhance visual feedback for questions */
#card {
    transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
#card:hover {
    transform: scale(1.01);
}

/* Sound effects styling */
.feedback-overlay {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    pointer-events: none;
    z-index: 9999;
    transition: background 0.3s ease;
}
.feedback-overlay.correct {
    background: rgba(0, 255, 136, 0.1);
}
.feedback-overlay.wrong {
    background: rgba(255, 51, 102, 0.15);
}
'''
with open('style.css', 'w') as f:
    f.write(css)

with open('index.html', 'r') as f:
    html = f.read()

html = html.replace('<body>', '<body>\n    <div id="feedback-overlay" class="feedback-overlay"></div>')

with open('index.html', 'w') as f:
    f.write(html)

with open('script.js', 'r') as f:
    script = f.read()

# Add logic for visual overlay
overlay_logic = '''
        buttonEl.classList.add('flash-correct');
        const overlay = document.getElementById('feedback-overlay');
        overlay.classList.add('correct');
        setTimeout(() => overlay.classList.remove('correct'), 300);
        updateEffects();
'''
script = script.replace('''        buttonEl.classList.add('flash-correct');
        updateEffects();''', overlay_logic)

overlay_logic_wrong = '''
        buttonEl.classList.add('flash-wrong');
        const overlay = document.getElementById('feedback-overlay');
        overlay.classList.add('wrong');
        setTimeout(() => overlay.classList.remove('wrong'), 300);
'''
script = script.replace('''        buttonEl.classList.add('flash-wrong');''', overlay_logic_wrong)

with open('script.js', 'w') as f:
    f.write(script)
