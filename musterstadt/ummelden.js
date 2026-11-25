// Prüfung des Ummeldeformulars.
// Es gibt keinen Server: Das Formular wird NIE wirklich verschickt.

const form = document.getElementById("ummelde-form");
const errorBox = document.getElementById("fehler");
const successBox = document.getElementById("erfolg");

// Prüft alle Pflichtfelder und gibt eine Liste von Fehlermeldungen zurück
function validate() {
  const errors = [];

  for (const field of form.querySelectorAll("[required]")) {
    const name = field.dataset.name;
    let valid;

    if (field.type === "checkbox") {
      valid = field.checked;
    } else if (field.id === "plz") {
      valid = /^\d{5}$/.test(field.value.trim()); // genau 5 Ziffern
    } else {
      valid = field.value.trim() !== "";
    }

    if (!valid) {
      errors.push(name + ": Eingabe ungültig.");
    }
  }

  return errors;
}

// Zeigt die Fehlermeldungen als Liste in der Fehlerbox an
function showErrors(errors) {
  errorBox.replaceChildren(); // alte Meldungen entfernen

  const intro = document.createElement("p");
  intro.textContent = "Bitte prüfen Sie Ihre Angaben:";
  errorBox.appendChild(intro);

  const list = document.createElement("ul");
  for (const message of errors) {
    const item = document.createElement("li");
    item.textContent = message;
    list.appendChild(item);
  }
  errorBox.appendChild(list);
}

form.addEventListener("submit", (event) => {
  event.preventDefault(); // verhindert das echte Absenden

  const errors = validate();

  if (errors.length > 0) {
    showErrors(errors);
    form.reset(); // leert alle Felder
    return;
  }

  // Erfolgsfall: Formular ausblenden und Bestätigung zeigen
  errorBox.replaceChildren();
  form.hidden = true;
  successBox.textContent = "Vielen Dank. Ihre Ummeldung ist eingegangen.";
});
