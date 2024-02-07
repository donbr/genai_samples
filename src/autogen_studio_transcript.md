AutoGen Studio 2.0 Tutorial - Skills, Multi-Agent Teams, and REAL WORLD Use Cases (NO CODE)
video_url = "https://www.youtube.com/watch?v=4ZqJSfV4818"

ms-autogen/autogen/autogen/dwb/fetch_youtube_transcript.py
we have a brand new version of autogen
Studio that just dropped it has new
features expanded functionality and
we're going to build something for the
real world and this video is going to be
a little different I haven't built this
agent team myself yet so you're going to
build it with me and you're going to see
my mistakes let's get into it the team
we're going to be building today is
going to take a YouTube url grab the
transcript for it and then convert that
transcript into a compelling blog post
and a tweet thread this is something
that I need it's a real world use case
and we're going to build it together all
right so the first thing we're going to
do is install autogen Studio from
scratch now I had an older version of
autogen studio and then when I went to
upgrade to the newer version of autogen
Studio everything broke and I kept
getting all these database issues and
errors and it was just a nightmare and
what finally fixed it was uninstalling
autogen studio with this command pip
uninstall autogen studio and not only
that I actually had to go into my python
site packages and manually delete the
auto gen Studio folders so if you run
into any issues while upgrading to the
new autogen studio be sure to do that
and I already made a beginner tutorial
about autogen Studio I'll drop a link to
that in the description below so the
first thing we're going to do is create
a new cond environment condac create DN
AG python equal 3.11 hit enter so I
already have an existing environment we
are going to remove it and then accept
we're going to install everything we
need then we're going to grab this
Command right here cond to activate AG
paste it in hit enter and now we know
the environment is active because it's
right there next we're going to install
autogen studio and this is super simple
pip install autogen Studio then just hit
enter now once you're done with that
we're going to run autogen Studio ui--
Port 8081 and you can specify any port
you want sometimes if you close autogen
studio in the wrong way it'll say this
port is busy and then you just change it
to 882 or 883 or anything that you want
so I'm going to hit enter on 881 and
there is that issue so I closed down
Port 8 881 in the wrong way last time so
here is the error that you will see so
we're going to change that to 882 now
and now it works I'm going to hold down
command and I'm going to click on this
URL to open up local host in my browser
all right and here it is the newest
version of autogen studio so what is
different about it if you go to the
build tab you'll see we have new tabs
over here for one we have this models
tab now you can predefine different
models to use with your agents and you
can mix and match as you want you can
have specific specific models tailored
for specific agent use cases it is
brilliant so here you can see we have
GPT 4 GPT 4 preview and the BLS Zephyr
7B Alpha if you wanted to add a new
model we'll go do that right there but
we don't need to do that we're going to
be using chat GPT 4 today and we're
going to actually be using this preview
version the other thing that's new and
I'll get to it in a second is the fact
that you can have agent teams greater
than just two agents in the previous
version you could only have two agents a
sender and a receiver now you can have
agent groups where you can group
together multiple agents in addition to
your user proxy now I haven't tested
this yet I'm hoping it works but if it
doesn't you're going to see it so switch
over to open AI if you don't already
have an account go ahead and sign up
come to the API Keys section we're going
to create a new key I'm going to call it
autogen studio hit
enter and it's asking me to verify that
I'm a human so this is something I'd
usually cut out of the video use the
eror to rotate the object to face in the
direction of the hand interesting all
right verification complete all right
now I'm going to copy this yes I am
going to revoke this API key before
publishing the video I know you all are
sick of hearing me say that but if I
don't I get a bunch of comments about
not showing my API key so we'll come
back to autogen Studio we're going to
click on this model right here and then
we're going to enter our API key I don't
believe we need to do anything else for
GPT 4 everything else should stay the
same because the chat GPT T API is the
default then we'll hit enter model
created successfully now the first thing
we want to do is create a skill and the
skill that I need created today is a
function to go grab the transcript from
a YouTube video now how would I go about
writing that I'm actually going to use
chat GPT to write it for me now just to
make sure it is in the format that is
similar to something I already know
works I clicked over to the skills tab
I'm looking at this fetch profile skill
clicking into it and this is pretty
similar where you pass in a URL and it
goes and gets something so this is
probably what I'm going to want to do
something similar to so I'm going to go
ahead and copy it I switched over to
chat GPT I'm going to paste it in and
then under it I'm going to say here's an
example script make something similar to
this but instead make it accept a
YouTube url as a parameter it goes and
gets the transcript from the URL via the
YouTube API and then Returns the
transcript let's see what we get okay so
it looks like this method is going to
accept a video URL so that's right so
far giving me some documentation that's
fine it's going to extract the video ID
from the URL that looks good okay and
it's going to use the Google api's
YouTube API so hopefully this works
we'll see we might need to iterate on
this if it doesn't work I've seen
another method written for this exact
use case to go grab the transcript and
it was a little bit different from this
so I don't know if it's going to work
okay so this one says the YouTube data
API requires an API key which you can
obtain from the Google Cloud console so
this is different I don't want to have
to do that let's try again show me
another way to do it that doesn't
require an API key there should be a
YouTube API that you can hit directly
okay and this looks more akin to what I
saw when I did it last time so it's
using this Library called YouTube
transcript API and hopefully it's able
to do it just with that and it says I
need to install the YouTube transcript
API with Pip but I'm going to try it
without that that so I'm going to go
ahead and copy the code and I believe
autogen Studio when I paste this in will
automatically know that it needs to
install that Library so I copied it
switch back to autogen Studio we're
going to create a new skill I'm going to
call it fetch YouTube transcript I'm
going to take what's in here which is a
sample I'm going to delete it then I'm
going to paste in what I just had it has
an example of how to use it at the
bottom I might as well leave that in and
then I'm going to hit okay so that's
done so now we have our model and our
skill created now let's create an agent
we have our primary assistant and our
user proxy but I want to create an agent
team and the Agents that I want are one
I want an agent to go and get the
YouTube transcript and remove the
timestamps and then return it the second
agent I want is to take that text and
then convert it into a blog post and
into a Twitter thread let's see if we
can do that so I'm going to click new
agent the agent name I'm going to call
it transcript getter for the description
takes a YouTube URL and gets the
transcript from a video I'm going to say
Max consecutive auto reply just leave it
as the default human input mode never
and then the system message this is
where I believe we need to actually tell
it which tool to use you are an AI agent
that uses the fetch YouTube transcript
skill to get a YouTube transcript for
subsequent processing we're going to be
using this model now if you wanted to
add a different model you do so right
here now here for the skills this is
where we need to add our skill so I go
ahead and click plus here we go fetch
YouTube transcript I'm going to go and
say add skill and there it is then I
click okay so now we have our transcript
getter then let's create our second
agent and this one is going to be
content writer takes raw YouTube video
transcripts and converts it into blog
posts and tweet threads Max consecutive
auto reply stays the same human input
mode never now for the system message
you are an insightful intelligent and
witty content writer who is able to take
raw YouTube video transcripts and turn
them into blog posts and tweet threads
we do not need a skill for this guy and
we're going to leave the model the same
as before so now we have our two agents
right there now the last thing we need
to do is create a workflow so we'll
click over to workflows and we're going
to click new workflow now this is
something new previously when you
clicked workflow it just automatically
opened up and you can only have two
agents now you can have two agents and
you can also do this thing called group
chat so we're going to use group chat
because we're going to have three agents
the content writer the YouTube scraper
and then the user proxy so we're going
to hit group chat we're going to call
this YT script to content workflow
description so we're going to say takes
a YouTube url gets the transcript of the
video and then creates a blog post and
tweet thread from that transcript
summary method we're going to leave as
last which is the default the sender is
going to be the user proxy and then the
receiver is going to be the group chat
assistant but we need to fill out the
group chat assistant so go ahead click
into it now we we have two primary
assistants here so I'm going to go ahead
and delete both of those and we're going
to add the content writer and the
transcript getter I'm going to keep it
the same name I'm going to leave the
description default and then for the
system message I'm going to be very
descriptive okay I'm being very explicit
here I actually don't know if you need
to be That explicit in the system
message cuz typically a system message
you're just setting up the role you're
telling the agent who to behave as not
necessarily describing what you want
them to do which we will likely do again
when we actually submit the prompt you
are a helpful assistant skilled at okay
coordinating spelled wrong coordinating
a group of other assistants to solve a
task the task you will solve is taking a
YouTube url having an agent use the
fetch YouTube transcript skill to get
the transcript from the YouTube video
pass that transcript to a Content writer
and then having the content writer
create a blog post and tweet thread
based on that transcript now it's
interesting the group chat manager also
can take a skill and I don't think we
need to give it a skill because the
agent itself has the skill we'll find
out ah and here's a bug that I've
noticed so if you remember I I removed
these primary assistants and I added
other assistants but when I start typing
it reverts back to these primary
assistance so remember fill out
everything first and then modify your
group agents so I'm going to delete
these again and I'm going to add the
content writer back and the transcript
getter and then we're going to hit okay
and okay again let's double check that
it actually does have the correct agent
so I'm going to click here click there
and it does perfect okay so now we're
going to get out of here and let's test
it out I hope it works we're going to go
to the playground we're going to click
new session and we're going to select YT
script to content and then hit create so
here we go take this YouTube URL and I
paste it in one of my YouTube videos use
the fetch YouTube transcript skill to
get the transcript from the YouTube
video remove the timestamps if any then
create a blog post and tweet thread
based on that transcript now the one
thing that's kind of difficult about
autogen is it doesn't have explicit
delegation options I can't explicitly
say this group chat agent should
delegate to the content writer or the
YouTube transcript getter you can't do
that and I think we just have to be
extra explicit in our descriptions to
get it to work that way all right enough
talk let's see what
happens okay so we got an error and it
says that the API key is not there which
is interesting so I'm going to go back
to build I'm going to go to models here
it is and it is there let me see what
that message is one more time so I click
here and I'm just going to say retry so
the API client option must be either set
by passing environment variable okay
that's weird I don't understand why I
have to set the environment variable
since I have it set in the model right
there but that's okay we're going to do
it anyways so I'm going to switch back
to the terminal going to go go to a new
tab and I'm going to type then I'm going
to do cond to activate AG then I'm going
to type export open AI API key and then
equals and then the API key and then hit
enter okay so it should be done now I
think I have to restart autogen studio
so I'm going to do that so I come here
and I'm going to click contrl C okay now
we're going to restart it there it is
going to go back to autogen studio now
going to refresh the page going to go to
playground and let's click retry nope
let's try that again I'm going to quit
out of here again and I'm going to do
export then the API key one more time
and then we'll start it up and let's
refresh the page and let's see if it
worked that time it did okay so for some
reason going into a new tab made it so
that it didn't actually see the API key
which is weird so just keep that in mind
if you run into that issue now we can
tell it's working because we can see
these three dots bouncing right there so
switching over to the terminal I can
actually see the code and the back and
forth between the agents as it's going
so it is saying yes use the fetch
YouTube transcript skill so that's good
and it does know to install the YouTube
transcript API now one thing to note is
that in autogen it doesn't actually show
you the back and forth conversation I do
know that there's an open ticket to make
it do that so you don't have to look at
the terminal while it's going but here
it is so there it got the YouTube
transcript that's perfect okay it's done
look at that all right so here it is
let's take a look look at what we got so
here's the code output okay we got all
that that's great let's look at the
actual agent messages so the user proxy
says take this URL so that's me typing
take the URL use the fetch YouTube
transcript skill get the transcript
remove the timestamps create a blog post
and a tweet thread then the transcript
getter to the content writer is actually
saying to accomplish this task we will
follow these steps so the transcript
getter is actually planning out what we
need to do the transcript getter also
installed everything we needed writes a
p python script to use that skill that
we gave it and then here it is so here
is the actual transcript from the video
and then interestingly it didn't give us
anything after that so it didn't
actually output it okay so interesting
for some reason it didn't actually
output the final blog post and tweet
thread in the UI itself however if I
switch over to terminal here it is
here's a suggested structure for the
blog post and then it actually writes
the blog post and this is pretty good
and then we have a tweet thread so
here's tweet one tweet two uses emojis
uses hashtags I mean this is great now
the one thing I don't understand is why
it didn't actually output that
information into here but I don't think
I'm going to be able to solve that in
this video we do know it worked though
so that's it now you know how to use the
new version of autogen Studio you know
how to create a skill for your agents to
use you know how to assign that skill to
the right agent you know how to create
the agent team and you know how to
execute the task and it did so pretty
darn well I'm happy with this result if
you want to see me create more of these
tutorials with real world use cases let
me know in the comments below if you
enjoyed this video please consider
giving a like And subscribe and I'll see
you in the next one