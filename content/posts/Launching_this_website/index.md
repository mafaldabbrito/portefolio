---
title: Launching this website
date: 2025-03-11
description: A brief story about me and this portfolio
tags:
- markdown
- obsidian
- go
- github
---
### The Mighty Portfolio

Welcome to my corner on the internet! My name is Mafalda, and I’m a Master's student of Networks and Communication Systems at Instituto Superior Técnico, University of Lisbon, Portugal.

This portfolio is a document and showcase of my journey through cybersecurity and network technologies – a project I’ve been working on to document and share my learning experiences.

Here you’ll find my experiments in the [Home Lab]({{< ref "posts" >}}) section and the larger projects I’ve been involved in in the [Projects]({{< ref "projects" >}}).

----

### Development and Deployment of the Portfolio

I built this website with Hugo, a popular open-source static site generator. [Hugo](https://gohugo.io/) is a great choice, offering a wide range of themes to customize the look and feel.  I adapted the [Congo] theme for a starting point, then customized it with a few tweaks.

First, I installed **Go** and ensured I had the latest version of **Git** updated. Then, I installed Hugo and followed the instructions on Congo’s theme page to install the specified theme.

Meanwhile, I secured a domain name and transferred it to **Hostinger** to host my website. I also added a webhook to the [GitHub repo](https://github.com/mafaldabbrito/portefolio) so that every time there are new changes, it automatically sends them to Hostinger – only the hostinger branch.

To streamline the process of adding new articles, I adapted a script created by
[NetworkChuck](https://www.youtube.com/channel/UC9x0AN7BWHpCDHSm9NiJFJQ&ved=2ahUKEwizqIqa3JSMAxU3IhAIHTmBPdYQFnoECBkQAQ&usg=AOvVaw1SQ5El0uL1lsJ6DCW_W4fJ) (The GOAT), which syncs a folder in my **Obsidian** vault with the content on my website.  This script also commits the changes made and pushes them to **GitHub** (master and hostinger branches).  I added a personalized commit message and the ability to
navigate through directories – crucial for synchronizing images.

The credits for this project go to NetworkChuck, who created a fantastic tutorial: [I started a blog ... ](https://youtu.be/dnE7c0ELEH8?si=4yP6pniF4KOdvTXS) 

---

### The Idea Behind the Logo

![Image Description](/images/android-chrome-192x192.png)

According to the internet, my name, **Mafalda**, means **Mighty in battle**.  So, I wanted to represent that with a warrior figure!  There's no better symbol to describe my journey through this course.