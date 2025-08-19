document.addEventListener("DOMContentLoaded", () => {
    const addBtn = document.getElementById("add-experience");
    const container = document.getElementById("experience-container");

    if (addBtn) {
        addBtn.addEventListener("click", () => {
            const entry = document.createElement("div");
            entry.className = "experience-entry";
            entry.innerHTML = `
                <input type="text" name="position" placeholder="Position / Job Title" required><br>
                <input type="text" name="employer" placeholder="Employer" required><br>
                <input type="text" name="dates" placeholder="Dates (e.g. 2020-2022)" required><br>
                <input type="text" name="exp_skills" placeholder="Skills Learned" required><br>
                <textarea name="summary" rows="3" placeholder="Bullet point summary (one per line)" required></textarea>
                <hr>
            `;
            container.appendChild(entry);
        });
    }
});
