// Rückruf-Anfrage. Es gibt keinen Server: Es wird nichts verschickt.

const callbackButton = document.getElementById("rueckruf-button");
const callbackFields = document.getElementById("rueckruf-felder");
const callbackError = document.getElementById("rueckruf-fehler");
const callbackSuccess = document.getElementById("rueckruf-erfolg");

callbackButton.addEventListener("click", () => {
  const name = document.getElementById("name").value.trim();
  const phone = document.getElementById("telefon").value.trim();

  // Fehlermeldungen sammeln, jeweils mit klarer Anweisung
  const errors = [];
  if (name === "") {
    errors.push("Bitte geben Sie Ihren Namen ein.");
  }
  if (phone === "") {
    errors.push("Bitte geben Sie Ihre Telefonnummer ein.");
  }

  callbackError.replaceChildren();

  if (errors.length > 0) {
    for (const message of errors) {
      const paragraph = document.createElement("p");
      paragraph.textContent = message;
      callbackError.appendChild(paragraph);
    }
    return; // Eingaben bleiben erhalten
  }

  callbackFields.hidden = true;
  callbackSuccess.textContent =
    "Vielen Dank. Wir rufen Sie innerhalb von zwei Werktagen zurück.";
});
