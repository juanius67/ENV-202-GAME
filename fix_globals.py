with open('script.js', 'r') as f:
    script = f.read()

script = script.replace('function startGame() {', 'window.startGame = function startGame() {')
script = script.replace('function returnToMenu() {', 'window.returnToMenu = function returnToMenu() {')

with open('script.js', 'w') as f:
    f.write(script)
