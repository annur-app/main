import fs from "fs";
import path from "path";
import readline from "readline";

const DIR = "homeworks-files";
const OUT_DIR = "data";
const OUT_FILE = path.join(OUT_DIR, "homeworks.json");

// create data folder if it doesn't exist
if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR);

// load previous homeworks.json if exists
let previous = [];
if (fs.existsSync(OUT_FILE)) {
  previous = JSON.parse(fs.readFileSync(OUT_FILE, "utf-8"));
}

// read all files in folder
const filesInDir = fs.readdirSync(DIR);

// filter new files not already in JSON
const newFiles = filesInDir.filter(f => !previous.find(p => p.url.endsWith(f)));

if (newFiles.length === 0) {
  console.log("✅ No new files found.");
} else {
  console.log("🆕 New files detected:");
  newFiles.forEach(f => console.log("  " + f));
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// helper to ask question
const ask = (question) => new Promise(resolve => rl.question(question, resolve));

(async () => {
  // handle new files
  for (const filename of newFiles) {
    const full = path.join(DIR, filename);
    const stats = fs.statSync(full);

    const d = stats.birthtime;
    const dateFormatted = `${String(d.getDate()).padStart(2,'0')}.${String(d.getMonth()+1).padStart(2,'0')}.${d.getFullYear()}`;

    console.log(`\nNew file detected: ${filename}`);
    const name = await ask("Enter display name: ");
    const description = await ask("Enter description: ");

    previous.push({
      name: name || filename,
      date: dateFormatted,
      url: `homeworks-files/${filename}`, // GitHub Pages safe path
      description: description || "Homework file"
    });
  }

  rl.close();

// check for deleted files
const deletedFiles = previous.filter(p => !fs.existsSync(path.join(DIR, path.basename(p.url))));

if (deletedFiles.length > 0) {
  console.log("\n⚠️ The following files are missing and will be removed from JSON:");
  deletedFiles.forEach(p => console.log("  " + p.name));
}

// remove all deleted files from JSON
previous = previous.filter(p => fs.existsSync(path.join(DIR, path.basename(p.url))));


  // remove deleted files from JSON
  previous = previous.filter(p => fs.existsSync(path.join(DIR, path.basename(p.url))));

  // save updated JSON
  fs.writeFileSync(OUT_FILE, JSON.stringify(previous, null, 2));
  console.log("\n✅ Homeworks list updated!");
})();
