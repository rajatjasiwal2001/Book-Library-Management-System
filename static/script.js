// Fade in the whole page on load
window.addEventListener('load', () => {
    document.body.style.opacity = '1';
    document.body.style.transition = 'opacity 1.5s ease';
});

// Animate button click
const buttons = document.querySelectorAll("button");
buttons.forEach(btn => {
    btn.addEventListener("click", () => {
        btn.classList.add("clicked");
        setTimeout(() => btn.classList.remove("clicked"), 200);
    });
});

// Simple form validation
document.addEventListener("DOMContentLoaded", () => {
    const forms = document.querySelectorAll("form");
    forms.forEach(form => {
        form.addEventListener("submit", (e) => {
            const inputs = form.querySelectorAll("input[required]");
            let valid = true;
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    input.style.border = "2px solid red";
                    valid = false;
                } else {
                    input.style.border = "none";
                }
            });
            if (!valid) {
                e.preventDefault();
                alert("Please fill all required fields!");
            }
        });
    });
});
