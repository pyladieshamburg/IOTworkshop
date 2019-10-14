## First Dashboard

To open dashboard with your data **locally** you can clone this repository to your computer (just like we copied it on Raspberry Pi before). You will need [html file](humidty-and-temp-line.html) with dashboard description. Don't forget to replace `subscribeKey` as we mentioned before (**it appears twice in this file**)!

You can now locally open the [dashboard](humidty-and-temp-line.html) in your browser. Feel free to experiment with this. it's written in java script using the EON PubNub project.

#### Let's publish this page!

The simplest way to do this, as it is a static page is using github pages following the instructions [here](https://hackernoon.com/use-custom-domain-with-github-pages-2-straightforward-steps-cf561eee244f).

These are a few things you will need to do specifically in our case:

- Create a new repo on Github, call it yourgithubuser.github.io (this will basically make it later available at the link http://yourgithubuser.github.io)
- The repo is empty so you will already have the instructions to clone and so on
- clone repo locally
- Copy the file [humidity-and-temperature.html](humidty-and-temp-line.html) to it
- rename it index.html (this will be then implicitly rendered as the default page)
- push the code to github (Step two in the article)
- go to http://yourgithubuser.github.io
