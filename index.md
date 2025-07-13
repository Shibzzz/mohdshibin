---
layout: default
title: Home
---

# MOHAMMED 
SHIBIN K
<section class="reveal-on-scroll">
  <h2>👋 About Me</h2>
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

---

<section class="reveal-on-scroll">
  <h2>🚀 Projects</h2>

  <div class="project-card">
    <h3 class="project-title">🔐 TriCrypt Authentication System</h3>
    <p class="project-desc">A three-level authentication mechanism combining passphrases, image patterns, and gesture-based face recognition.</p>
    <a class="project-link" href="#">View Project</a>
  </div>

  <div class="project-card">
    <h3 class="project-title">📶 WiFi DoS Detection</h3>
    <p class="project-desc">A final year B.Sc. project built using Python and Scapy to detect denial-of-service signals in wireless traffic.</p>
    <a class="project-link" href="#">Read More</a>
  </div>
</section>

---

<section class="reveal-on-scroll">
  <h2>🛠️ Skills</h2>
  <div class="skills-list">
    <span class="skill">Python</span>
    <span class="skill">Burp Suite</span>
    <span class="skill">Wireshark</span>
    <span class="skill">Linux</span>
    <span class="skill">OpenCV</span>
    <span class="skill">Frida</span>
    <span class="skill">ADB</span>
    <span class="skill">Git & GitHub</span>
    <span class="skill">Reverse Engineering</span>
    <span class="skill">Mobile Pentesting</span>
    <span class="skill">Autopsy</span>
    <span class="skill">FTK Imager</span>
    <span class="skill">SQL</span>
    <span class="skill">Jekyll</span>
  </div>
</section>

---

<section class="reveal-on-scroll">
  <h2>🎓 Education</h2>
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

---

<section class="reveal-on-scroll">
  <h2>📬 Contact</h2>
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

---

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
