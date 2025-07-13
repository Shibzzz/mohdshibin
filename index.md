---
layout: default
title: Home
---

# About

<div class="reveal-on-scroll">
 I'm **Mohammed Shibin K**, a passionate cybersecurity student with a focus on hands-on problem solving, tool development, and digital investigations. I enjoy exploring offensive and defensive techniques through real-world scenarios and CTFs.

I’ve participated in multiple cybersecurity events, completed practical labs (TryHackMe, DVIA, Burp Suite testing), and worked on projects related to multi-factor authentication, mobile app security, and WiFi DoS detection.

Currently, I’m diving deeper into reverse engineering, malware analysis, and cyber forensics — aiming to contribute to both technical communities and secure systems design.
</div>

# Projects

<div class="reveal-on-scroll">
  <div class="project-card">
    <h3 class="project-title">🔐 TriCrypt Authentication System</h3>
    <p class="project-desc">A three-level authentication mechanism combining passphrases, image patterns, and gesture-based face recognition.</p>
    <a class="project-link" href="#">View Project</a>
  </div>

  <div class="project-card">
    <h3 class="project-title">📶 WiFi DoS Detection</h3>
    <p class="project-desc">A final year B.Sc. project built using Python and Scapy to detect denial-of-service signals in wireless traffic.</p>
    <a class="project-link" href="#">Read More</a>
  </div><!-- Add your projects content here -->
</div>

# Skills

<div class="reveal-on-scroll">
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
  <span class="skill">Forensics Tools (Autopsy, FTK Imager)</span>
  <span class="skill">SQL</span>
  <span class="skill">Jekyll</span>
</div>

# Education

<div class="reveal-on-scroll">
  ### M.Sc. Cyber Security  
**National Forensic Sciences University, Bhopal**  
*2023 – 2025*  
Focus Areas: Cybercrime Investigation, Mobile App Testing, Digital Forensics, Advanced Networking, Legal Procedures

---

### B.Sc. Cyber Forensics  
**[Your Previous University Name]**  
*2020 – 2023*  
Projects: WiFi DoS Detection, TriCrypt Authentication  
Learned: Packet analysis, Network Security, System Forensics, Encryption basics
</div>

# Contact

<div class="reveal-on-scroll">
  Feel free to reach out for:

- CTF collaborations
- Research projects
- Cybersecurity internships
- Freelance testing work

### 📧 Email
[mohammedshibin@example.com](mailto:mohammedshibin@example.com)

### 💼 LinkedIn
[linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)

### 💻 GitHub
[github.com/shibzzz](https://github.com/shibzzz)
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
