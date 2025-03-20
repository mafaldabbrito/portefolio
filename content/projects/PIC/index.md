---
title: Bachelor's final project
date: 2024-06-29
description: The story behind the my Bachelor's final project, the development process and the outcome.
tags:
  - python
  - Flutter
  - GitLab
  - Google
  - Maps
  - Google
  - API
  - Indoor
  - Directions
  - Figma
---
### VISUALIZE  
*Bridging Vision Gaps in University Spaces*

We were impacted by a visually impaired colleague at Técnico who had to quit his studies due to the lack of accessibility for people like him. The one thing we could help him with was navigation within the campus.

Although he already had a app for it it only pointed to the place so we challenged ourselves to integrate Google Maps' directions in an app that not points (with haptics clues) to the correct direction.

We called it [Visualize](https://pic-visualize-tomasgesteves-9a2c6c6209ed433189c5c458214944da393.gitlab.io/)!

----
### Development and Deployment of the App

#### Research
In the first part of the semester we did a lot of research on the topic. 

We had meetings with APEC (Association for Support to Blind Education) who became our partners in this project. With their help we concluded, per example, that our app must have all **icons labeled for voice-over functionalities** to enable comprehensive audio navigation for both iOS and Android users.

We also researched other existing indoor solutions a few of them with open-source software like Osiris, Anyplace, Navigine and **Google Maps (API)**.

We decided to go with Google Maps since it was already implemented in our university (all rooms were labeled and divided between floors).

#### Implementation
For the design of the app we used **Figma**. and then transferred it to **Flutter**. This way we created a simple app compatible with a wide variety of operating systems (Web, IOS, Android).

I was in charge of **integrating the Google Maps's and the haptics clues** with the cataloged locations. 

**Steps of the Navigation Function**

1. Parses the route provided by the **Routes API** into multiple segments.
2. Determines the **user's current segment** using real-time location data.
3. Utilizes the **phone's compass** to ensure the user is heading towards the **beginning of the next segment**.
4. Transmits **sound and vibration feedback** to indicate the correct direction.
5. Repeats the above steps continuously **until the user reaches the destination**.

*Sneak Peak into our final presentation*
![Image Description](/images/Visualize-ppt.png)


---
### Outcome

We’ve found that this system’s performance is markedly superior outdoors than indoors. Even in Android phones where Google uses Wi-Fi positioning indoor the accuracy is rather low and the routes are very limited.

Overall it was a great experience to learn how to work with **Flutter** and how to use Google's API's (namely **Routes API**).

In the **Demo Day** we were given the award for the **best Website** ([link here](https://pic-visualize-tomasgesteves-9a2c6c6209ed433189c5c458214944da393.gitlab.io/)), **honorable mention** for the **Prototype** and decided by the public **second Best Overall Product**.

![Image Description](/images/DemoDay.jpg)



---
### Important Links

- [Web App](https://picvisualizeapp.web.app/)
- [Website](https://pic-visualize-tomasgesteves-9a2c6c6209ed433189c5c458214944da393.gitlab.io/)
- [Video](https://drive.google.com/file/d/1GkTPM2VJgZ0KTbibQ-1wdJnFUcs3CBCX/view?usp=sharing)

<iframe src="https://drive.google.com/file/d/1GkTPM2VJgZ0KTbibQ-1wdJnFUcs3CBCX/preview" width="640" height="480" allow="autoplay"></iframe>






