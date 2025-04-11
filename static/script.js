// Confirm before deleting a post
document.addEventListener("DOMContentLoaded", function () {
        const deleteLinks = document.querySelectorAll("a[href*='delete']");
    
        deleteLinks.forEach(link => {
            link.addEventListener("click", function (event) {
                const confirmDelete = confirm("Are you sure you want to delete this post?");
                if (!confirmDelete) {
                    event.preventDefault();
                }
            });
        });
    
        // Optional: Prevent empty submissions (extra layer)
        const forms = document.querySelectorAll("form");
        forms.forEach(form => {
            form.addEventListener("submit", function (e) {
                const inputs = form.querySelectorAll("input[required], textarea[required]");
                let valid = true;
    
                inputs.forEach(input => {
                    if (!input.value.trim()) {
                        valid = false;
                        input.classList.add("input-error");
                    } else {
                        input.classList.remove("input-error");
                    }
                });
    
                if (!valid) {
                    alert("Please fill in all required fields.");
                    e.preventDefault();
                }
            });
        });
    });
    