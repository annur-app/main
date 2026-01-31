import fs from "fs";
import path from "path";

const DIR = "homeworks-files";
const OUT_DIR = "data";
const OUT_FILE = path.join(OUT_DIR, "homeworks.json");

// create the folder if it doesn't exist
if (!fs.existsSync(OUT_DIR)) {
  fs.mkdirSync(OUT_DIR);
}

const files = fs.readdirSync(DIR).map(name => {
  const full = path.join(DIR, name);
  const stats = fs.statSync(full);

  const d = stats.birthtime;
  const dateFormatted = `${String(d.getDate()).padStart(2,'0')}.${String(d.getMonth()+1).padStart(2,'0')}.${d.getFullYear()}`;

  return {
    name,
    date: dateFormatted,       // DD.MM.YYYY
    url: `../homeworks-files/${name}`,
    description: "Homework file"
  };
});

fs.writeFileSync(OUT_FILE, JSON.stringify(files, null, 2));
console.log("✅ Homeworks list generated in data/homeworks.json with DD.MM.YYYY dates");
