document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.getElementById("themeToggle");

  /* ---------- THEME MEMORY ---------- */
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme === "dark") document.body.classList.add("dark");

  /* ---------- THEME TOGGLE ---------- */
  if (toggle) {
    toggle.addEventListener("click", () => {
      document.body.classList.add("theme-animate");
      const isDark = document.body.classList.toggle("dark");
      localStorage.setItem("theme", isDark ? "dark" : "light");
    });
  }

  /* ---------- CARD NAVIGATION ---------- */
  document.querySelectorAll(".card[data-link]").forEach(card => {
    card.addEventListener("click", () => {
      window.location.href = card.dataset.link;
    });
  });

  /* ---------- LOAD HOMEWORK FILES ---------- */
  const base = location.pathname.endsWith("/")
  ? location.pathname
  : location.pathname.replace(/\/[^/]*$/, "/");

  fetch(base + "data/homeworks.json")
    .then(r => r.json())
    .then(files => {
      const container = document.getElementById("homeworksList");
      container.innerHTML = "";

      files.forEach(file => {
        const a = document.createElement("a");
        a.href = base + file.url; // 🔥 THIS LINE FIXES IT
        a.download = "";
        a.className = "project-item";
        a.target = "_blank";

        a.innerHTML = `
          <h3>${file.name}</h3>
          <p>Uploaded: ${file.date}</p>
          <p>${file.description}</p>
        `;

        container.appendChild(a);
      });
    });

});
