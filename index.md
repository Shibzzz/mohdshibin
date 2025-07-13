---
layout: default
title: Home
---

<div class="hero-section">
  <div class="hero-left">
    <h1 class="hero-name">
      <span>Mohammed</span><br>
      <span>Shibin K</span>
    </h1>
    <h2 class="hero-role">Cybersecurity Student</h2>
    <p class="hero-desc">
      A passionate cybersecurity enthusiast focused on reverse engineering, CTFs, mobile app testing, and digital forensics. I enjoy turning complex security problems into practical solutions.
    </p>
    <div class="social-icons">
      <a href="https://www.linkedin.com/in/shibin-k-ba3095205/" target="_blank">🔗</a>
      <a href="https://github.com/shibzzz" target="_blank">💻</a>
      <a href="mohdshibin.k@gmail.com">📧</a>
    </div>
  </div>

  <div class="hero-right">
    <img src="/assets/img/profile.jpg" alt="Mohammed Shibin K" class="hero-img">
  </div>
</div>
<section class="reveal-on-scroll">
  <h2> About Me</h2>
  <p>
    I'm <strong>Mohammed Shibin K</strong>, a passionate cybersecurity student focused on hands-on problem solving, tool development, and digital investigations. I enjoy exploring offensive and defensive techniques through real-world scenarios and CTFs.
  </p>
  <p>
    I’ve participated in multiple cybersecurity events, completed practical labs (TryHackMe, DVIA, Burp Suite testing), and worked on projects related to multi-factor authentication, mobile app security, and WiFi DoS detection.
  </p>
  <p>
    Currently, I’m diving deeper into reverse engineering, malware analysis, and cyber forensics — aiming to contribute to both technical communities and secure systems design.
  </p>
</section>


<section class="reveal-on-scroll">
  <h2> Projects</h2>

  <div class="project-card">
    <h3 class="project-title">🔐 TriCrypt Authentication System</h3>
    <p class="project-desc">A three-level authentication mechanism combining passphrases, image patterns, and gesture-based face recognition.</p>
    <a class="project-link" href="{{'/projects/tricrypt/' | relative_url }}">View Project</a>
  </div>

  <div class="project-card">
    <h3 class="project-title">📶 WiFi DoS Detection</h3>
    <p class="project-desc">A final year B.Sc. project built using Python and Scapy to detect denial-of-service signals in wireless traffic.</p>
    <a class="project-link" href="{{ '/projects/wifi-dos/' | relative_url }}">View Project</a>
  </div>
</section>


<section class="reveal-on-scroll">
  <h2>🛠️ Skills</h2>
  <div class="skills-grid">
    <div class="skill-card">Python</div>
    <div class="skill-card">Burp Suite</div>
    <div class="skill-card">Wireshark</div>
    <div class="skill-card">Linux</div>
    <div class="skill-card">OpenCV</div>
    <div class="skill-card">Frida</div>
    <div class="skill-card">ADB</div>
    <div class="skill-card">Git & GitHub</div>
    <div class="skill-card">Reverse Engineering</div>
    <div class="skill-card">Mobile Pentesting</div>
    <div class="skill-card">Autopsy</div>
    <div class="skill-card">FTK Imager</div>
    <div class="skill-card">SQL</div>
    <div class="skill-card">Jekyll</div>
  </div>
</section>




<section class="reveal-on-scroll">
  <h2> Education</h2>
  <h3>M.Sc. Cyber Security</h3>
  <p><strong>National Forensic Sciences University, Bhopal</strong><br>
  <em>2023 – 2025</em></p>
  <p>Focus Areas: Cybercrime Investigation, Mobile App Testing, Digital Forensics, Advanced Networking, Legal Procedures</p>

  <h3>B.Sc. Cyber Forensics</h3>
  <p><strong>[Your Previous University Name]</strong><br>
  <em>2020 – 2023</em></p>
  <p>Projects: WiFi DoS Detection, TriCrypt Authentication<br>
  Learned: Packet analysis, Network Security, System Forensics, Encryption basics</p>
</section>


<section class="reveal-on-scroll">
  <h2> Contact</h2>
  <p>Feel free to reach out for:</p>
  <ul>
    <li>CTF collaborations</li>
    <li>Research projects</li>
    <li>Cybersecurity internships</li>
    <li>Freelance testing work</li>
  </ul>

  <p><strong>📧 Email:</strong> <a href="mailto:mohammedshibin@example.com">mohammedshibin@example.com</a></p>
  <p><strong>💼 LinkedIn:</strong> <a href="https://linkedin.com/in/yourprofile">linkedin.com/in/yourprofile</a></p>
  <p><strong>💻 GitHub:</strong> <a href="https://github.com/shibzzz">github.com/shibzzz</a></p>
</section>



<script>
document.addEventListener("DOMContentLoaded", function () {
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
/* Layout grid for top hero section */
.hero-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  align-items: center;
  margin-bottom: 4rem;
}
.hero-left {
  padding-left: 2rem;
}
.hero-name {
  font-size: 3.5rem;
  line-height: 1.1;
  margin: 0;
}
.hero-role {
  font-size: 1.5rem;
  color: #a1a1aa;
  margin: 0.5rem 0;
}
.hero-desc {
  font-size: 1.1rem;
  color: #d4d4d8;
  max-width: 90%;
}
.social-icons a {
  font-size: 1.5rem;
  margin-right: 1rem;
  text-decoration: none;
}
.hero-right {
  text-align: right;
}
.hero-img {
  width: 300px;
  border-radius: 12px;
  filter: grayscale(100%);
  box-shadow: 0 0 15px rgba(0,0,0,0.5);
}

/* Responsive behavior */
@media (max-width: 768px) {
  .hero-section {
    grid-template-columns: 1fr;
    text-align: center;
  }
  .hero-left {
    padding-left: 0;
  }
  .hero-right {
    margin-top: 2rem;
    text-align: center;
  }
  .hero-img {
    width: 70%;
  }
}
</style>
<style>
.reveal-on-scroll {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.7s ease, transform 0.7s ease;
}
.reveal-on-scroll.visible {
  opacity: 1;
  transform: translateY(0);
}
section {
  margin-bottom: 4rem;
}
</style>
