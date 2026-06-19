const chatLog = document.querySelector("#chatLog");
const chatForm = document.querySelector("#chatForm");
const messageInput = document.querySelector("#messageInput");
const quickActionButtons = document.querySelectorAll("[data-message]");

function addMessage(text, sender, metaText = "") {
  const article = document.createElement("article");
  article.className = `message ${sender}`;

  const paragraph = document.createElement("p");
  paragraph.textContent = text;
  article.appendChild(paragraph);

  if (metaText) {
    const meta = document.createElement("span");
    meta.className = "meta";
    meta.textContent = metaText;
    article.appendChild(meta);
  }

  chatLog.appendChild(article);
  chatLog.scrollTop = chatLog.scrollHeight;
}

async function sendMessage(message) {
  const trimmedMessage = message.trim();
  if (!trimmedMessage) {
    return;
  }

  addMessage(trimmedMessage, "user");
  messageInput.value = "";

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message: trimmedMessage })
    });

    const result = await response.json();
    const metaText = `Intent: ${result.intent} | Confidence: ${result.confidence}`;
    addMessage(result.reply, "bot", metaText);
  } catch (error) {
    addMessage("The chatbot server is not responding. Please restart the Python app.", "bot");
  }
}

chatForm.addEventListener("submit", (event) => {
  event.preventDefault();
  sendMessage(messageInput.value);
});

quickActionButtons.forEach((button) => {
  button.addEventListener("click", () => {
    sendMessage(button.dataset.message);
  });
});
