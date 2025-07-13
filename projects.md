---
layout: default
title: Projects
permalink: /projects/
---

# 🧠 Featured Projects

<div class="projects-grid">

  <div class="project-card">
    <h3 class="project-title">🔐 TriCrypt Authentication System</h3>
    <p class="project-desc">
      A multi-level authentication mechanism combining secure passwords, image-based puzzle matching, and gesture-based face recognition for highly sensitive applications.
    </p>
    <a class="project-link" href="#">View Project</a>
  </div>

  <div class="project-card">
    <h3 class="project-title">📶 WiFi DoS Detection</h3>
    <p class="project-desc">
      Built using Python and Scapy, this tool identifies denial-of-service attempts on WiFi networks and alerts users about malicious packets.
    </p>
    <a class="project-link" href="#">Read More</a>
  </div>

  <div class="project-card">
    <h3 class="project-title">🛡️ Windows Logging for SOC</h3>
    <p class="project-desc">
      A security analysis based on TryHackMe’s Windows Logging room. Covers Sysmon, Event Viewer, and PowerShell monitoring for detection engineering.
    </p>
    <a class="project-link" href="https://tryhackme.com/room/windowslogging" target="_blank">View Room</a>
  </div>

  <div class="project-card">
    <h3 class="project-title">📱 InsecureBankv2 Pentesting</h3>
    <p class="project-desc">
      Tested mobile banking app vulnerabilities using Burp Suite and Frida. Demonstrated SSL pinning bypass, insecure HTTP usage, and login activity analysis.
    </p>
    <a class="project-link" href="#">View Report</a>
  </div>

</div>

<style>
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.project-card {
  background: #1f1f23;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.3);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.project-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 6px 30px rgba(0,0,0,0.4);
}
.project-title {
  font-size: 1.3rem;
  font-weight: 600;
  color: #a3e635;
  margin-bottom: 0.5rem;
}
.project-desc {
  font-size: 1rem;
  color: #d4d4d8;
  margin-bottom: 1rem;
}
.project-link {
  color: #38bdf8;
  text-decoration: underline;
  font-weight: 500;
}
</style>
