# Project Title
AthleticUsLeague

## Description
A flask web application for AthleticUsLeague, which is a platform designed to promote community sports, provide resources for athletes, and advocate for inclusivity, especially for girls in sports.

## Installation
Steps to install and set up your project.
git clone https://github.com/liana-26/Projectfinal.git
cd Projectfinal

## Usage
Examples of how to use your project.
To run Project:
type,
export FLASK_APP=app.py
and then,
flask run
into the terminal

## License
For information about the project's license, refer to 
https://cs50.harvard.edu/x/2021/license/

## Introduction

Overview of interface:
https://www.youtube.com/watch?v=NMbIoY9VUQA

I made this website for my final project because according to me, girls must participate more in sports to 

## Backend

app.py
Starts with the usual import declarations.
The next lines of code refer to the different routes of the application:
homepage
page 2 
page 3 
page 4
page 5
page 6
page 7
page 8
page 9 
page 10
submit suggestion
topics
submit feedback

## Implementation

Every website page has a menu bar that opens upon clicking ☰ at the top right and bottom right of every page.
Using functions on and off in JavaScript and navigation class and overlay in HTML, was possible.
#overlay {
    position: fixed;
    display: none;
    width: -50%;
    height: 100%;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0,0,0,0.5);
    z-index: 2;
    cursor: pointer;
}gives a grey overlay

#text{
    position: fixed;
    top: 100%;
    left: 90%;
    font-size: 10px;
    color: white;
    transform: translate(-100%,-100%);
    -ms-transform: translate(-100%,-100%);
    background-color: #CA7B7B;

} 
Every page also has a footer with a "centered" Page no. .centered allows the page no. to be written in the middle of the webpage with a 1px dashed black border till both ends of the screen.
.centered {
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
  }

.centered::before,
.centered::after {
    content: "";
    flex:1;
    border-bottom: 1px dashed black;
    margin: 1px;
}

homepage.html
- has a rotating banner made with HTML, JavaScript and CSS

page2.html
- has a collage of 4 images styled by style.css
- .collage {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    place-items: center;
}
.collage img {
    width: 100%;
    height: auto;
}


page3.html
- shows details of upcoming events using a table in HTML.
- the table is styled to become #f1f1f1 when hovered over and even rows and <th> have different background colors.
tr:nth-child(even) {
    background-color: #A66F6F;
} to style even numbered rows
tr:hover {
    background-color: #f1f1f1;
} to style table rows when hovered over by cursor.

page4.html
- information about the Girls in Sports Initiative.

page5.html
- links to tutorials for different sports.
- nested unordered lists in ordered lists.
- hyperlinks were styled to turn red when hovered and turn #7D5555 when visited.

page6.html
- nested unordered lists in ordered lists.
- <strong> used to emphasize words.

page7.html
- three forms- one discussion board, event feedback, and suggestions for the website.
- upon getting answers for discussion, /topics takes place where answer_1 goes to answer_1.txt, answer_2 to answer_2.txt and so on, once submit button is pressed.
- upon getting feedback for events, /submit_feedback takes the name of event as feedbackn and the suggestion as feedback and it is written in feedback.txt as feedbackn:feedback, once submit button is pressed.
- upon getting suggestions, /submit_suggestion takes the user's suggestion as a suggestion and it is written in suggestion.txt, once the submit button is pressed.
- These Txt files can be checked by the developers every month or week.

page8.html
- shows volunteer opportunities.
- nested unordered list in an ordered list.

page9.html
- success stories
- awards and recognition

page10.html
- FAQ section
