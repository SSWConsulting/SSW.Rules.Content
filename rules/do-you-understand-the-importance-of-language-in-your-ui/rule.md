---
type: rule
archivedreason: 
title: Do you understand the importance of language in your UI?
guid: 98e7361a-aefa-4d10-aaa1-4bed5d5eb31d
uri: do-you-understand-the-importance-of-language-in-your-ui
created: 2014-12-02T03:09:10.0000000Z
authors: []
related: []

---

The tone of your application speaks volumes about how users view it. Read this [Google documentation on the voice of Android](http&#58;//developer.android.com/design/patterns/help.html). 
<!--endintro-->


| | Bad Example | Good Example |
| --- | --- | --- |
| Keep text as short as possible. Avoid wordy, stilted text. | Consult the documentation that came with your phone for further instructions. | Read the instructions that came with your phone |
| Describe only what the user needs to know and don't provide unnecessary information. | Your phone needs to communicate with Google servers to sign in to your account. This may take up to five minutes. | Your phone is contacting Google. This can take up to 5 minutes. |
| Focus on the user's concern, not technical details | Manually control GPS to prevent other apps from using it. | To save power, switch Location mode to Battery saving |
| Put the most important thing first | 77 other people +1’d this, including Larry Page | Larry Page and 76 others +1’d this |
| Put the user's goal first | Touch Next to complete setup using a Wi-Fi connection | To finish setup using Wi-Fi, touch Next |
| Avoid being confusing or annoying | Sorry! Activity MyAppActivity (in application MyApp) is not responding. | MyApp isn’t responding. Do you want to close it? |


### Words to avoid


| Don't use | Use |
| --- | --- |
| cannot, could not, do not, did not will not, you will | Contractions: can’t, couldn’t, don’t, didn’t, won’t, you’ll, and so on |
| okay, ok | OK |
| please, sorry, thank you | Attempts at politeness can annoy the user, especially in messages that say something has gone wrong. Exception: In Japanese, “please” is mandatory and imperative verbs should be localized accordingly (turn on -&gt; please turn on). |
| fail, failed, negative language | In general, use positive phrasing (for example, “do” rather than “don’t,” except in cases such as “Don’t show again,” “Can’t connect,” and so on.)  |
| me, I, my, mine | you, your, yours |
| Are you sure? Warning! | Tell user the consequence instead, for example, "You’ll lose all photos and media" |


### Formatting text

Use sentence-style capitalization for all UI strings.

Capitalize all important words in:

* App names (Calendar, Google Drive)
* Named features (Android Beam, Face Unlock)
* Proper nouns (Statue of Liberty, San Francisco Giants)


Be conservative. Don't capitalize words that aren't part of a formal feature name: Sim card lock, Home screen, not Sim Card Lock, Home Screen.

### Using Periods 

Don't use a period after a single sentence or phrase used in isolation, such as in a toast, label, or notification. Wherever two or more sentences run together, use a period for each sentence.
