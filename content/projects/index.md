---
title: Launching this website
date: 2025-03-11
description: A brief story about me and this portfolio
tags:
  - markdown
  - obsidian
  - go
  - github
  - intro
  - Hostinger
---
### The Mighty Portfolio

Welcome to my corner on the internet ! 
My name is Mafalda and I am a Master's student of Networks and Communication Systems at Instituto Superior Técnico, University of Lisbon, Portugal.

To document and share my journey through the fields of Cybersecurity and Networks I created this little portfolio.

In here you will find my small experiments in the [Home Lab]({{< ref "posts" >}}) section and the bigger projects I have been a part of in [Projects]({{< ref "projects" >}}).

----
### Development and Deployment of the Portfolio

So as you may have noticed this website was made with Hugo. [Hugo](https://gohugo.io/) is one of the most popular open-source static site generators. It offers a bunch of themes you can choose from this one is an adaptation of the [Congo](https://jpanther.github.io/congo) theme.

So first I needed to install **Go** and make sure **Git** was updated. Then install **Hugo** and follow the instructions on Congo's theme page to install the specified theme.

Meanwhile I bought a domain name and transferred it to **Hostinger** so I could host my website in it. Also added a webhook to the [GitHub repo](https://github.com/mafaldabbrito/portefolio) so that every time there are new changes it sends them Hostinger (only the hostinger branch).

To simplify the process of adding new articles to the portfolio I adapted a script created by [NetworkChuck](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.youtube.com/channel/UC9x0AN7BWHpCDHSm9NiJFJQ&ved=2ahUKEwizqIqa3JSMAxU3IhAIHTmBPdYQFnoECBkQAQ&usg=AOvVaw1SQ5El0uL1lsJ6DCW_W4fJ) (The GOAT), that syncs a folder in my Obsidian vault with the content on my website. Not only that but it commits the changes made and pushes them to GitHub (master and hostinger branch). To this script I added the input argument with a personalized commit message and the ability to navigate through directories (needed for synchronizing the images).

All the credits go out to NetworkChuck who did a beautiful tutorial on this $\rightarrow$ [I started a blog ...](https://youtu.be/dnE7c0ELEH8?si=4yP6pniF4KOdvTXS) 


---
### The Idea Behind the Logo

!![Image Description](/images/android-chrome-512x512.png)

According to the internet :Clown: my name Mafalda means **Mighty in battle**. So of course I had to get a Mighty Warrior to represent me.