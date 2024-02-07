# Matthew Berman
# Power Each AI Agent With A Different LOCAL LLM (AutoGen + Ollama Tutorial)
# https://youtu.be/y7wMTwJN7rA?si=6YmkOyoAabm700d2

I'm going to show you how to use autogen
powered by olama which means you can use
any open- Source model and run it
completely locally not only that we're
going to hook up each individual agent
to a different model and you don't need
a superpowered computer to do this you
can pretty much do it on any modern
machine so let's go so autogen has had a
ton of updates since I last made a video
and I did make a bunch of videos about
it so if you're just getting introduced
to autogen check the description below
I'll link all of my tutorials
including the beginner one all the way
through advanced and yes the expert
video is still coming and so to do this
we're going to need three things
obviously we're going to need autogen
we're going to be using olama to power
the models locally and then we're going
to be using light llm to wrap the model
so that we have an API Endo to hit and
we're going to spin up multiple models
at the same time that are powering
individual agents and this is really the
dream of Open Source agent usage when
you can have each agent powered by a
fine-tuned vertical ized model that is
really good at just a couple things so
for example if you wanted to have a
coding agent we can use code llama if
you wanted to have a generalized agent
you can use mistol you can use a model
fine-tuned on creative writing if that's
the agent you want to build pretty much
the options are endless but enough talk
let me show you how to do this so if you
don't already have oama installed go
ahead and install it it could not be
easier you just click this download
button install it and then that's it and
then you're going to see this little ol
llama icon in your taskbar up at the top
and that's it that's really all you need
to do oama doesn't have an interface it
runs completely from your command line
all right so in this example I'm going
to install two models we're going to be
using mistol as the main kind of
orchestration model and then we're going
to be using Cod llama as the coding
model so all you need to do to download
the model is type this command olama run
mistol and of course you can replace
mistol with any model that you want so
I'm going to hit enter and it should
start downloading it yep there it goes
very easy now while it's downloading I
want to mention one thing this video is
purely showing you how to get this up
and running I'm not going to spend much
time optimizing autogen to use these
models and really be successful with it
maybe I'll save that for another video
let me know in the comments below if you
want to see that but for today I'm just
going to show you that we can get it up
and running using multiple models at the
same time okay looks like it's done
downloading now it's probably getting
the metadata okay there we go it's up
and running now if you remember from my
previous olama video I was absolutely
Blown Away by the fact that you can have
multiple models up and running at the
same time and if you prompt each of them
at the same time they'll queue up and
then run sequentially and swap in and
out of memory so quickly literally
within like 1 to two seconds it was
extremely impressive and of course that
gave me the idea that well agents should
be able to use multiple models now and
so now that it's up and running let's
make sure it works tell me a joke now
remember this is the mistel model look
how fast that is for those of you
wondering I'm on a MacBook Pro M2 Max 32
GB of RAM so it's a pretty beefy laptop
but it's still just a laptop I'm not
using my RTX 490 so there we go sure
here's a joke for you why don't
scientists trust atams because they make
up everything okay so now we know what
working so let's quit out of here next
I'm going to do the same thing but I'm
going to say o llama run code llama now
it's going to download another model now
while we're waiting for that I've
switched back to the olama homepage and
if you click up in this top right corner
where it says models we can actually get
a list of the models that are available
through olama so here we have the find
model which I've heard is incredible and
I've been meaning to test that wizard
coder mistl open Orca nous Hermes Zephyr
I mean these are all just the best
models out there here's deep seat coder
which I just tested and was phenomenal
here's Orca 2 from just a few days ago
which again that's another model that
I've been meaning to test STAR coder
dolphin 2.2 mistol which is definitely
the best open source model that I've
tested so far and it's by Eric Hartford
here's Samantha mistol if you want to do
creative writing here's the Y model
which didn't really perform all that
well if you watched my last testing
video sequel coder if you want to do
some SQL writing and so yeah it has a
bunch of different models that you can
use all right switching back it looks
like it downloaded successfully let's
give it a test write a python script to
Output numbers 1 to 100 there it is done
so fast and that is correct so we know
that we have both models downloaded to
our machine now I'm going to exit out of
there by hitting control D and now let's
get our environment set up using cond so
that we can actually write some code and
get this all working together so cond
create DN autogen python equals 3.11 hit
enter now I already have an envir ment
that's named the same thing so it's
going to ask me if I want to remove it
and yes I do but you won't get that
message we're going to accept to proceed
all right now that it's done installing
we're going to grab this Command right
here cond to activate autogen and then
hit enter and we can tell that it's
activated because it says autogen right
there next we're going to check which
python we're using and the reason for
this is just to Triple verify that when
we install things using pip it's using
the right python environment so I do
which python hit enter and there we go
and now I'm just going to copy this and
then I'm going to paste that in and then
type-m pip install pi autogen and then
hit enter and that's going to install
autogen obviously and now it's done the
next thing we're going to install is
light llm which just provides a wrapper
around olama that exposes an API that we
can use with autogen and it's integrated
really nicely don't really need to do
anything it just knows it's there so
here we go same thing we're going to
Output the python location DM pip
install Light llm and then hit enter now
once that's done we should be able to
just type light llm M -- model oama SL
mistol and you can follow this pattern
to load up any model that you want that
you have downloaded so here we go let's
try it looks like it worked there we go
so we have uicorn running at Local Host
Port 8000 so that's perfect now we're
going to open up a new tab and we're
going to get a second model loaded and
running and then we need to activate the
environment again because if you notice
right here it says base so the
environment is not activated Honda
activate autogen now that that's
activated we can type light lm-- model o
llama SL Cod llama hit enter there we go
and it automatically puts it on another
Port as you can tell here so now we have
two servers running using olama we have
two models that are ready to be served
through the light llm API which really
just mimics the open AI API and now
we're ready to write some code so I have
a new file ready to go it's a python
file this is Visual Studio code if you
look in the bottom right you can see
which python version and which conduit
environment we're using and it says
autogen right there so that's perfect so
the first thing we need to do import
autogen now there's a red underline here
and it says autogen is not access
pylance import autogen cannot be
resolved usually that means the module
and the version of python the version of
cond they're not matching in some way so
I'm not sure why it says that but it
still should work and if it doesn't
we'll fix it when we get there next
we're going to create our config list
and here's where we're going to do
something different than what we
normally do usually you're either
plugging in your gp4 API key or you're
listing a local URL that you want to hit
for the API but in this instance we're
going to list our local model URL but
we're also going to have other ones so
let's make sure to name it properly so
that we can distinguish between which
one's mistol and which one's code llama
so let's type config list mistal equals
and then Open brackets and this is a
Json object so this is the right
formatting for Json so autogen did
change something recently and this is
now base URL I can't remember what it
used to be I think it was like API URL
or something like that but now it's base
URL and that's the URL of the API
endpoint that we're going to be hitting
then we type colon and let's open up
some quotes switching back to our
terminal let's grab the mistal model
first so here it is down here here's the
URL and we're just going to copy that
switch back and we're going to paste it
in right here and then we're going to
type API key but since we don't have one
we can just say null and now we have the
config list for mistol but now let's
create one for code llama as well so I
copied that part of the code I'm just
going to delete this and we're going to
call it code llama and let's switch back
to the terminal and here's the port
we're going to be using for this one so
I'll copy that switch back paste it in
there so now we have one for mistol and
one for code llama now we can pass each
of these config lists to the agent so
they know which model to use for its
task next we're going to create the llm
config parameter so we're going to
create two of them and I just copy
pasted one that I already had so llm
config mistol then we type config list
and then we're going to insert our
config list mistal and then same thing
for code llama right here so llm config
code llama then the config list gets
passed in config list code llama now
let's create our first assistant so
assistant equals autogen do assistant
agent open up parenthesis and then the
first thing we're going to need is a
name equals assistant we're going to be
boring and then the second thing we're
going to need is an llm config and then
we equal and what we're going to be
using for the assistant the general
assistant is the llm config mistal we're
going to be using the mistal model so we
paste it in right there now let's go
ahead and create a second one so save
I'm going to copy it paste it in and
we're going to call this one coder and
it's the same thing we're going to do
autogen do assistant agent we're going
to call it coder here and the llm config
we're going to be using Code llama so
now we have two agents one assistant
agent that uses the mistl model and then
a coding agent that uses the code llama
model next we have to create our user
proxy and I just grabbed this from
another file I have I'll put all of this
in a gist so you don't have to retype it
manually you can find the gist in the
description below so now we're creating
our user proxy agent so we have autogen
do user proxy agent we're going to name
it user proxy for human input mode we're
going to do terminate Max consecutive
Auto rep we'll just leave that at 10 is
termination message we'll leave it as is
now this is really where you're going to
need to play around and try to optimize
for your open source models because
sometimes they say terminate correctly
sometimes there's a trailing white space
and so you're going to have to play
around with it and figure out what works
best for you for code execution config
we're going to keep it in the work
directory web and then for the llm
config here's what's important we're
going to pass in the mistal model
because again we just want a general
model for the user proxy agent we don't
want it to be a coding model then here's
the system message reply terminate if
the task has been solved at full
satisfaction otherwise reply continue
next let's write out our task so we're
going to type task equals quote quote
quote and we'll type tell me a joke just
to see if it works next we're going to
set up our group chat and the reason
we're using group chat is because we
have more than just one agent and one
user proxy if we just had one agent plus
one user proxy we wouldn't need group
chat but we have an assistant we have
the coder and we have the user proxy so
here we're going to type group chat
equals autogen dog group chat then we're
going to pass in the agents so agents
equals the user proxy agent the coder
agent and the assistant agent we're
going to pass a blank messages cuz we
don't have any yet and max round 12 you
can mess around with these settings as
much as you you like next we need a
manager and the manager is going to
coordinate the different agents within
this group chat so here we go we have
autogen group chat manager we pass in
the group chat that we just created
right there so group chat equals group
chat then we're going to pass in an llm
config and once again because this is
kind of an orchestration agent we're
just going to use the general mistal
model so llm config mistal last we need
to actually execute the task so user
proxy do initiate chat we pass in the
manager and we pass in the message of
task which is right here tell me a joke
let's save it still says autogen is not
available but let's see if it works
hopefully it does so let's hit play in
the top right corner and let's see so
you can see right here the first thing
it did was cond to activate autogen so
that might be why it showed that the
autogen library wasn't available yet
because we hadn't yet run activate
autogen and while that's loading up to
see that it's actually working we should
see some output on these two tabs we
have this right here with no output yet
and this one right here with no output
as well this one is code llama and this
other tab is mistol okay tell me a joke
and it looks like it's working here it
is I switch back and there's the prompt
to mistel okay so the assistant wrote
print why did the Scarecrow win an award
because he was outstanding in his field
great but then of course it continues on
task solve the given equation so now
it's just making stuff up so again this
is where you're going to have to play
around and really figure out how to get
those termination messages working
properly and that the model knows how to
terminate and you can customize all of
these things the system message The
Prompt Etc there the coder said
terminate and yeah it's just going off
on a complete tangent now so I'm going
to stop it but we can see right here we
have output from the mistal model and we
also have output from the code llama
model so it worked perfectly well maybe
perfectly as a stretch but in terms of
getting individual models to power
individual agents that worked perfectly
now let me try one more thing just to
get it to work a little bit well so
instead of doing a group chat I'm just
going to Simply do a user proxy and an
assistant and I'm going to have them
both powered with separate models so I'm
going to delete the assistant and then
we're going to remove all this stuff
right here and then I'm going to say
user proxy do initiate chat instead of
GPT assistant let's do coder and the
message is going to be task and then for
the task we're going to say write a
python script to Output numbers 1 to 100
so let's save I'm going to clear the
screen there and let's play okay here we
go so I am still using two different
models one mistol and one code llama and
the coder is using Code llama and the
user proxy is using mistol and there we
go it did it perfectly and to give
feedback to coder enter or type exit to
stop the conversation so here we go
let's try something different now write
a script to Output numbers one to X
where X is a random number generated by
the user proxy agent this should force
them to work together okay that did not
work like I thought it would it just
used coder and I'm just going to type
enter maybe the user proxy agent is just
going to execute that code okay so what
we're going to do is we're going to
change this human input mode to never
and let's do this again I'm going to
clear the screen let's push play ah and
of course it still has our caching so
let's get rid of that cache so in my AI
projects folder I see this little
hidden. cach folder let's go ahead and
move it to the trash and of course
there's a number of ways to do that but
that's the way I'm going to do it for
now okay so let's try this write a
python script to Output numbers 1 to 100
and then the user proxy agent should run
the script go ahead and push play there
we go absolutely perfect look at that so
we have the coder who output the script
then we have the user proxy agent who
ran the script and one to 100 and we can
see all the output happening from the
different models so this worked
perfectly so what else do you want to
see about autogen before I make my
expert video let me know in the comments
below and also I'm collecting all the
best real world use cases for autogen so
if you have one especially if you have
the code drop it in the description
below or jump in my Discord and ping me
and let me know that you have it if you
liked this video please consider giving
a like And subscribe and I'll see you in
the next one