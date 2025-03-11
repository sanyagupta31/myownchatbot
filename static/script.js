document.addEventListener("DOMContentLoaded", function () {
    function sendMessage(event) {
        if (event.key === "Enter") {
            let userInput = document.getElementById("user-input").value;
            if (userInput.trim() === "") return;

            let chatBox = document.getElementById("chat-box");
            
            // Display user message
            let userMessage = document.createElement("p");
            userMessage.className = "user-message";
            userMessage.textContent = "You: " + userInput;
            chatBox.appendChild(userMessage);

            // Send request to Flask server
            fetch("/get_response", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ user_input: userInput }),
            })
            .then(response => response.json())
            .then(data => {
                let botMessage = document.createElement("p");
                botMessage.className = "bot-message";
                botMessage.textContent = "Bot: " + data.response;
                chatBox.appendChild(botMessage);
            })
            .catch(error => console.error("Error:", error));

            document.getElementById("user-input").value = ""; // Clear input field
        }
    }

    // Attach function to `window` so it can be accessed in HTML
    window.sendMessage = sendMessage;
});
