document.addEventListener('DOMContentLoaded', function() {
    const output = document.getElementById('output');
    const input = document.getElementById('command-input');

    input.focus();

    input.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            const command = input.value.trim();
            input.value = '';
            executeCommand(command);
        }
    });

    function executeCommand(command) {
        const xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    appendOutput(xhr.responseText);
                } else {
                    appendOutput('Error: ' + xhr.responseText);
                }
            }
        };
        xhr.open('POST', '/execute_command', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({ command: command }));
    }

    function appendOutput(text) {
        const div = document.createElement('div');
        div.textContent = text;
        output.appendChild(div);
        output.scrollTop = output.scrollHeight;
    }
});
