const hamburger = document.querySelector('.hamburger');
const navOption = document.querySelector('.nav-options');


hamburger.addEventListener("click", (e) => {
    navOption.classList.toggle("show");
    e.stopPropagation(); // Stop click from bubbling to document
});

// Close menu when clicking outside
document.addEventListener("click", (e) => {
    if(navOption.classList.contains("show")) {
        navOption.classList.remove("show");
    }
});

// Prevent menu click from closing
navOption.addEventListener("click", (e) => {
    e.stopPropagation();
});
