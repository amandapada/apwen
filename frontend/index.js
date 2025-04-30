// Mobile Navigation Menu Functionality
document.addEventListener("DOMContentLoaded", function () {
  const mobileNav = document.getElementById("mobile-nav");
  const openMobileNavButton = document.getElementById("open-mobile-nav");
  const closeMobileNavButton = document.getElementById("close-mobile-nav");

  // Function to open mobile navigation
  function openMobileNav() {
    mobileNav.classList.add("active");
    document.body.style.overflow = "hidden"; // Prevent scrolling when menu is open
  }

  // Function to close mobile navigation
  function closeMobileNav() {
    mobileNav.classList.remove("active");
    document.body.style.overflow = ""; // Restore scrolling
  }

  // Event listeners
  openMobileNavButton.addEventListener("click", openMobileNav);
  closeMobileNavButton.addEventListener("click", closeMobileNav);

  // Close mobile nav when clicking on a link (optional)
  const mobileNavLinks = mobileNav.querySelectorAll("a");
  mobileNavLinks.forEach((link) => {
    link.addEventListener("click", closeMobileNav);
  });

  // Close mobile nav when clicking outside of it (optional)
  document.addEventListener("click", function (event) {
    const isClickInside =
      mobileNav.contains(event.target) ||
      openMobileNavButton.contains(event.target);
    if (mobileNav.classList.contains("active") && !isClickInside) {
      closeMobileNav();
    }
  });

  // Handle window resize - close mobile menu if screen becomes larger
  window.addEventListener("resize", function () {
    if (window.innerWidth >= 768 && mobileNav.classList.contains("active")) {
      closeMobileNav();
    }
  });
});

// Add smooth scrolling for anchor links (optional)
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();

    const targetId = this.getAttribute("href");
    if (targetId === "#") return; // Skip if href is just "#"

    const targetElement = document.querySelector(targetId);
    if (targetElement) {
      targetElement.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }
  });
});

// Form validation for any forms on the page (optional, can be expanded as needed)
const forms = document.querySelectorAll("form");
forms.forEach((form) => {
  form.addEventListener("submit", function (e) {
    let isValid = true;
    const requiredFields = form.querySelectorAll("[required]");

    requiredFields.forEach((field) => {
      if (!field.value.trim()) {
        isValid = false;
        field.classList.add("error");

        // Create error message if it doesn't exist
        if (
          !field.nextElementSibling ||
          !field.nextElementSibling.classList.contains("error-message")
        ) {
          const errorMessage = document.createElement("div");
          errorMessage.classList.add("error-message");
          errorMessage.textContent = "This field is required";
          field.after(errorMessage);
        }
      } else {
        field.classList.remove("error");
        if (
          field.nextElementSibling &&
          field.nextElementSibling.classList.contains("error-message")
        ) {
          field.nextElementSibling.remove();
        }
      }
    });

    if (!isValid) {
      e.preventDefault();
    }
  });
});
