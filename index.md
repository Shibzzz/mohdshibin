---
layout: default
title: Home
---

# About

<div class="reveal-on-scroll">
  <!-- Add your about content here -->
</div>

# Projects

<div class="reveal-on-scroll">
  <!-- Add your projects content here -->
</div>

# Skills

<div class="reveal-on-scroll">
  <!-- Add your skills content here -->
</div>

# Education

<div class="reveal-on-scroll">
  <!-- Add your education content here -->
</div>

# Contact

<div class="reveal-on-scroll">
  <!-- Add your contact content here -->
</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
  const reveals = document.querySelectorAll('.reveal-on-scroll');
  function revealOnScroll() {
    for (const el of reveals) {
      const rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight - 60) {
        el.classList.add('visible');
      }
    }
  }
  window.addEventListener('scroll', revealOnScroll);
  revealOnScroll();
});
</script>

<style>
.reveal-on-scroll {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.7s cubic-bezier(.4,0,.2,1), transform 0.7s cubic-bezier(.4,0,.2,1);
}
.reveal-on-
