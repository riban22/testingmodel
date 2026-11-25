// Ergänzt in der Tabelle "(heute)" beim Abholtag, wenn heute eine wöchentliche Abholung ist
const weekdays = ["Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag"];
const today = weekdays[new Date().getDay()];

for (const row of document.querySelectorAl("#abholtage tbody tr")) {
  const dayCell = row.cells[1];
  const rhythmCell = row.cells[2];

  if (dayCell.textContent === today && rhythmCell.textContent === "jede Woche") {
    dayCell.textContent += " (heute)";
  }
}
