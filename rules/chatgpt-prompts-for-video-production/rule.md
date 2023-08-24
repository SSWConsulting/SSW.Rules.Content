---
type: rule
title: Do you use ChatGPT prompts for video production?
uri: chatgpt-prompts-for-video-production
authors:
  - title: Jonty Gardner
    url: https://www.ssw.com.au/people/jonty-gardner
    img: https://www.ssw.com.au/people/static/Jonty-Gardner-Sketch-ce8e4837b6f66dbcbb2a7591ad60a644.jpg
  - url: https://www.ssw.com.au/people/uly
    title: Ulysses Maclaren (Uly)
    img: https://www.ssw.com.au/people/static/Ulysses-Maclaren-Sketch-6042cb6a5f142d79914dfc7aeaf7e985.jpg
created: 2023-04-30T23:32:49.109Z
guid: 9fa828fe-3004-4a18-af43-bfed1d7dd489
---
Are you a video producer looking to take your content to the next level? Here are some painful things video producer's go through when creating content:

* Writer's block - thinking of new video ideas can difficult 
* Chapter Markers - making chapter markers is particularly time consuming for longer form videos 
* Title and description - it can be overwhelming to try and think of the best title and description for your video. 

With the help of ChatGPT, our SSW Rule for video production can help you create compelling video scripts, optimize your SEO, and streamline your workflow. Say goodbye to disorganized content and hello to the power of AI-assisted video production.

By utilizing ChatGPT, our SSW Rule for video production can help you save time and produce high-quality videos that engage your audience and generate traffic. 

You can get AI-generated ideas for your video concepts, generate effective titles and descriptions, and even create a script template for future videos. 

Don't let the admin side of video production hold you back - spend more time making the actual video with the below prompts:

1. ### **Video concept + outline**:

::: greybox
   "\
   As an SSW TV video producer, create a project outline for a video script. (Goal: Organize content, Constraint: Use bullet points)\
   \
   Concept: {{ insert your concept }} \
   \
   Write it back to me using these subheadings:

    1. What is the Concept? (30 words or less):

   {{ Answer }} 

   2. What is the Goal?  

   {{ Answer }}

   or if it is a CTF, pick from these:

   Educating others \
   Gathering opinions \
   Aligning us (about solving the problem consistently)

   3. Who is your audience and what do you want them to do immediately after this video? 

   {{ Answer }}

   ·         To developers - beginner

   ·         To developers - advanced

   ·         Through developers to business decision makers

   ·         other

          4. What are 5 options for the working video title?  \
   {{ Answer }}

          5. What are the key messages? (List 2-3)

   {{ Answer }}"
:::
   
  
2. ### **Video title and description**:


::: greybox 
   "Video title + description: As a SSW TV video producer, create:\
   An SEO effective title (give 5 options)\
   Description (500 character limit)\
   Hashtags (give 30 max)\
   Chapter Markers (chapter markers based on the important sections of content. Put the time stamp first and for the beginning of the section of the content. Do not give more than {{ xx }}.\
   My Goal is to get lots of views\
   Use the below transcription for a YouTube video: 

   {{ transcript }}"
:::

3. ### **Chapter Markers**:


::: greybox 
"User
Let's think step by step
First, I am going to give you a video transcript. 
Second, you are going to read the transcript as if it were an essay 
Third, you will identify the main chapters of the essay. 
Fourth, you will identify the most fitting title for each chapter. 
Fifth, you will list the chapter markers that you've made, with accurate timestamps, in the format: '00:00 - {{ chapter title }}' 
Sixth, do not give a summary, only give the chapter markers

{{ transcript }}"
:::

4. ### **Thumbnail creation**:


::: greybox  
   "As a SSW TV video producer, what is a good thumbnail for this video content type. (Goal: Improve click-through rate, Constraint: Use proper design guidelines)\
   \
   {{ insert title and description }}"
:::
   
   
5. ### **Blog Post**: 

::: greybox  
   "As a SSW TV content creator, write a blog post about a video project. (Goal: Generate traffic, Constraint: Use proper SEO guidelines)\
   \
   {{ insert video transcript }}" 
:::

6. ### **Planning video content**: 

::: greybox
   "As a SSW TV content manager, create a yearly content calendar for a video projects. Research and pitch new video ideas.(Goal: Plan ahead, Constraint: Use proper scheduling tools)"
:::

. ### **Script Templates**: 

::: greybox
   "As a SSW TV video producer, create a script template for future videos based on the below transcript. (Goal: Streamline workflow, Constraint: Use proper formatting guidelines)

   \
   {{ insert video transcript }}"
:::
