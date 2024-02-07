# Connor Shorten
# DSPy Explained
# https://www.youtube.com/watch?v=41EfOY0Ldkc

seeing how it's bootstrapping the
examples rewriting your signatures and
all that kind of stuff but so let's kick
it off with in my view I see two things
you're optimizing either the
instructions which is the language like
you are a ranker agent or you are a
query formulator that kind of thing as
well as the examples and so examples of
input outputs especially when you then
add say Chain of Thought and you want it
to you know input and then say rationale
and then answer being able to
automatically come up with these answers
is Super Value Val valuable to me that's
the quickest value to add of dpy is if
you know you want to add Chain of
Thought or program of thought or these
kind of things and you don't want to
have to write out the examples yourself
of why particularly that's the answer so
that kind of like automatic data
labeling that's it's like a synthetic
data framework is how I see dpy in
addition to of course as we discussed
earlier I think the programming model is
pretty cool but let's dive into it the
instruction tuning so the the idea is to
end this manual prompt tuning prompt
engineering and this ual example writing
so we had this thing like you know if
you're trying to have a ranker agent you
might try different phrasings of the
instruction your task is to rerank these
documents will perform differently then
I need your help reranking these
documents or take a deep breath and
rerank these documents and further which
prompt performs best for which language
model is different so maybe this one
performs the best for gbt 4 but this one
for Gem Ultra this one for llama 3 when
that comes out so this kind of like
ending the prompt tuning will help you
keep up with the new language models
like language models are going to keep
there'll be a new language model every
probably month or so for I would predict
the next year or a year and a half at
least so if you want to keep your LM
programs up if you want to be able to
just plug in a new language model and
then uh see which you know prompt
elicits the
behavior this automatic tuning framework
is great and then there's kind of this
funny thing I'm taking this from Jason
Lou Who I think has just done the best
job of describing this structured output
thing pantic all that awesome stuff so
like he has this example of like uh you
know please out with Json or I'll take a
life just like this kind of like I'll
pay you a million dollars to out Json
like that that kind of like prompt
gestures where you're trying to say out
Json and so DSP is about an end to this
so the idea is you start off with the
initial signature and then you optimize
the optimal signature so you start off
with that shorthand like answer short
factoid questions or maybe it's that
just context question answer shorthand
syntax and so it's going to optimize a a
more thorough description of the task so
the way that works is it's is so this is
kind of the interesting thing is there
are some prompts baked into the dpy
compiler
so it's like taking an end it's ending
the kind of pre-baked prompts in the
chains but there are some prompts in how
it you CU it's using llms to optimize
llms so you have the this prompt for how
you uh optimize the instruction so you
are an instruction Optimizer for large
language models I will give you a
signature of fields inputs and outputs
in English your task is to propose an
instruction that will lead a good
language model to perform the task don't
be afraid to be creative so that last
part don't be afraid to be creative
that's kind of exactly what we're hoping
to end with dpy and one of the
interesting directions for dpy is we'll
then talk about arays and ragus and that
whole development is use is this part
would also be a dsvi program but anyway
so so you would do that and then propose
some instructions and then this prompt
will take those instructions and sync
them up into one instruction so you have
this kind of ensembling and uh sampling
multiple outputs to then aggregate it
and produce the thing so that's how we
optimize the signature the description
of the task the next thing is examples
and examples has been the story of deep
learning the key difference though is
that in the past you know you read these
papers and it'll be like like the squad
question answering data set I can't
recall off the top of my head exactly
but these papers would be like we just
collected 200,000 examples of human
written natural language inference
entailment contradiction things like
this so the past story has been people
creating just enormous human label data
sets and now because of this you know
generative models we can just produce
training data from the models themselves
to compress and to finder smaller models
or to use as examples in the prompt so
to just kind of explain this concept and
maybe take a step back in the gbt 3
paper that came out in uh in 2020 they
were explaining this concept of few shot
learning this was like really surprising
that you could do this at the time so
zero shot means you just have the task
description there's no examples right so
you just tweak that instruction maybe
and you've gotten a really nice
instruction and you just go zero shot no
examples in the input one shot then
means you have one example and few shot
means you have a few examples so if
you're translating English to French
here are some examples and then here's
the input cheese and then
translates that so then graduating from
few shot examples where we're taking the
examples and putting them in the prompt
we then have fullscale fine-tuning where
we apply gradient descent updates to the
neural network to learn from the
examples that we have so fine tuning has
made massive strides lately with sparse
fine tuning like low rank adaptation and
there's all sorts of other methods
that's just low rank adaptation is the
most popular one but so the difference
here is that you're applying gradients
to change the parameters of the model
compared to just kind of eliciting the
behavior with these examples so it's
super interesting whether say you know
the Llama 2 13 billion parameter model
is faster and cheaper than these super
large models like gbt 4 Gemini Ultra but
then the question is whether you could
just fuse shot prompt latu 13B or say 7B
or mistol 7B you know so on or whether
you want to fine-tune those models and
so one part of one thing you'll see in
the dpy examples is fine-tuning the T
five large 700 million parameter models
so a 700 million parameter neural
network can run super fast and super
cheaply and so that's one of the most
exciting parts of this whole dpy
framework is you can bootstrap create
examples and maybe you can just prompt
you know uh you can there's even this
interesting scale where of course you
can prompt probably gbt 4 and Gemini
Ultra but you can also maybe prompt like
mistol 7B or llama 2 and you know llama
3 is coming out and I'm certain just at
the time of publishing this video there
will be a new model so this is the
interesting scale is when do you want to
fine-tune these models versus fuch shot
and that's what dpy is offering you is a
framework to just wrap all the
complexity of that and you don't
personally need to be bothered with it
so so that's kind of the idea of
examples in deep learning and how it
fits in this new llm programming world
so the first thing that dpy does is
bootstrapping few shot examples so you
know you you have a little bit of a data
set and the question now is uh which of
the examples should I be putting in the
prompt so let's say you have 10 examples
and you're only going to put three in
this example of translating from English
to French so that would be one way of
interpreting this is which of the 10
should I put in the in the input and
another ex another thing about this is
uh when you want to have the language
model write the examples so I think the
quickest value of this is thinking about
Chain of Thought where you have not only
the um the input output but now you want
to also have that uh let's things step
by step and then you have a rationale
output so say you have like you know
you're you're CH chatting with your docs
and you have an FAQ on your website this
is like the most common thing I've seen
and personally the common thing I've
used with developing with WEA is you
have an
FAQ so you have labeled question answer
Pairs and you're trying to sync up
you're trying to tune your rag system
for with that FAQ and now let's you want
to add that rationale Chain of Thought
you know you've retrieve these contexts
from your documentation and you know the
answer is the answer because of this
reason so you want to add that
intermediate example you know that exam
as you're giving it these examples of
how to have Chain of Thought reasoning
across the retrieve context from your
vector database or however you retrieved
it you you can now use dpy to bootstrap
that rationale have the llm write the
rationale and that leads us to the next
question of how do we know the quality
of synthetic examples so you're using
you know you're using the llm to produce
synthetic examples whether it's for the
case of putting it in the prompt or if
you're fine-tuning the model and how do
you know if that that was any good so
the answer to that is metrics in dpy so
one metric I think is you know a good
way to get started is exact match so if
you have short factoid questions like
what is the atomic number of oxygen and
then you have an answer eight this would
work pretty well like is it exactly
correct but now the problem with that
already is you know eight if you wrote
it out instead of writing the number
that exact match would say you that's
not a good answer so there are some ways
around this like the F1 score F1 score
would be like engr overlab if you have
slightly longer answers like um you know
if if you're uh
writing have a good example off my head
but let's say you're saying why is the
sky blue and it's I've been looking at
the dpy documentation long enough to
know this now it's like that Ray
scattering light scattering effect and
so you know if it has those three words
in it you know there's some overlap in
the keywords with what whatever the
language model did write the answer as
with that ground truth of of that Ray
life light scattering effect so there
are these metrics that you have and then
you know now when the dpy Box opens is
you might want to use llms as the metric
so ragus is a super interesting uh
Library which you know similar to Lang
chain llama index or you know even the
dsy signature optimiz Optimizer has the
prompt of the LM judge cooked into the
framework it's not like optimizing the
how it the prompt for how it judges the
metric which gets pretty meta but uh
aray is another paper from sad Falcon
katab Haria pots which is uh you know
using the llms to optimize the metric so
plugging in the llms As the metric is
another dpy program that will then
optimize this other dspi program so it's
pretty meta and that's maybe a big part
of why I like this so much so so you
know the LM metric looks like this kind
of like please output a scale a score on
a scale of 1 to five whether the answer
is grounded in the retriev context
question context answer and so that
would be a way to have the LM produce
the metric so let's connect this back
with how how do we know our synthetic
examples are high quality so now we have
teleprompters so teleprompters describe
the optimization Loop where we're
exploring different instruction writings
and different examples in the prompt
with that you know Ascent towards the
metric and so that could be blackbox
optimization where you just say uh you
know random searching or beijan
optimization or evolutionary search
towards the metric or if you're
fine-tuning you can directly optimize
for the metric so th this is like the
telepromter are like the system that
orchestrates uh proposing candidate
examples for the LM components as well
as you know new signatures and you know
seeing if that's improving the metric
okay let's kick things off by looking at
the code more than anything in this
video tutorial I hope that you'll get
some experience with writing dpy
programs and get some benefit just from
the off-the-shelf compilers from say
having Chain of Thought examples for
your llm programs and generally just
starting to learn the syntax let's dive
into an example to quickly get our hands
dirty and get some experience with the
Spy so we're going to do the full end to
end but I think to kick things off let's
look at what a dpy program looks like so
retrieval augmented generation is one of
the most popular llm Chains It's you
know kind of a simple llm chain where
you just retrieve and then generate and
the next program we'll look at has this
write the query part where you actually
do have two llm programs but I think
this is just a way to quickly get a
sense of the syntax so similar to
pytorch we have this initialize the
components we're going to be using and
then defining how they interact with the
input data as well as each other in the
forward pass through the llm program so
in this llm program of rag we first uh
take the question from the user we or
you know the question when it's plugged
into our app i s to hate that word user
but anyways so we we plug this question
into our retriever we get the passages
and then we pass the passages into the
generate answer so in dpy this is a
signature that tells us that gives the
llm you know a sense of the task it's
trying to do it has this kind of
shorthand notation of question context
to answer but you can also write out
signatures as well for when you want to
start the model off with a longer prompt
so similar to say instructor and these
super cool libraries around just like
how you organize these these prompts and
how you develop the you know how you
make the code look nice with say strict
typing and you know when you require the
output parsing all that kind of stuff so
you you also have this longer hand
notation where you can write an initial
prompt in the doc string and then you
can Define say types for the field
that's not shown in this example but you
can do that and you can also give it
some description of uh the input field
as well or you can just use this
shorthand notation where the language
model will infer what the variables are
used for based on the semantic names of
their type so you know question context
answer it can infer what what that that
it means in this context so so that's
the first thing to know is is using this
uh shorthand notation and the shorthand
notation is super powerful for I think
you know uh writing papers where you're
presenting some new language model chain
but you would also be able to pass in
these longer signatures into the
predictors like this where you're
passing in this signature in here and
then it inherits this one so uh now what
we have is the forward pass where we're
just you know calling our things anyway
so I think you get the gist this is a
rag program okay so now maybe you're a
little over underwhelmed so let's let's
get into a little bit more of a complex
uh program that has a bit more of this
interesting kind of two two llm programs
to be optimizing and that's really the
thing here is you have these llm
programs where you have multiple
components and you're optimizing the
language model to do each of the
intermediate tasks that it's responsible
for for creating some you know some
impressive Behavior as a whole system so
simplified bailing uh ba is a multihop
question answering system from kabad all
the idea of multi-hop question answering
is that idea where I give you a question
that's too complicated to just answer it
in one go so you break the question into
sub questions so you know the the
question from this data said that we're
about to look at is how many stories are
in the castle that David Gregory
inherited so first you would break that
question into uh you know what's the
castle what's the name of the castle and
then you would ask a question of how how
many stories are in that castle so this
is kind of idea of breaking up the
question this is probably one of the
most powerful things in rag I I think
this multihop question decomposition
thing is just going to take rag to the
next level is maybe the most exciting
thing out there reranking is also cool
but I think you'll really appreciate the
way that this ties the syntax with this
local memory and just how you can build
programs like this so again so we start
off by initializing the components we're
going to be using we're we're kicking it
off with so again we wrote a signature
for Generate search query so that's
where we have the short short
description of the task write a simple
search query that will help answer a
complex question then we give it a short
description of context may contain
relevant facts question and query we're
just going to let it you know figure
that out by the name of the variable so
uh so what we're doing is we are
assigning our modules so we have these
generate queries we have a list of the
modules so that might be a little bit
confusing and honestly I think that um
you know I I think we'll have to talk to
Omar about this one and maybe he can
leave a comment on this one but I think
you also could just write it like this
so you can just have it self generate
query equals DSP Chain of Thought
generate search query so maybe the the
interesting thing here is if you wanted
to have a different program for the
first search query compared to the you
know the second as we're going to be
looping through and generating queries
then you can maybe do it like a list and
again we'll we'll summon Omar for that
one maybe he can shine some light on
that but I'm pretty certain you can just
write it like this so then we have our
retrieval this could be something like
we8 and uh so then we have our uh
question answer where we're going to
answer the question based on the
information so now the super interesting
thing about this in the forward pass
We're looping through the number of hops
so say we're only going to let it break
our question into two question Max hops
equals 2 so we have this Loop where
we're going to generate the question
where we take as input the current
context what we've searched for so far
as well as the question then we're going
to retrieve these passages then we're
going to use a helper function so
already note how you can use these
helper functions and add them into your
forward passes of your llm programs and
how you can interface this syntax to
write what ever you can imagine with
these llm programs so we're going to D
duplicate it and then we're going to
keep looping so it's going to you know
say you ask it this question of how many
stories are in the castle that David
Gregory inherited it's going to come up
with the search query for the first
search query maybe that is the idea of
the list sorry to be distracting the
video with that but so it's going to
generate the first query it's going to
retrieve some context and then it's
going to use that as input when it's
saying you know hey what's the next
query I'm about to generate so then you
aggregate all these contexts and you
pass this into the generate answer and
it's going to answer the question okay
so now before wrapping up let's just go
through the entire notebook to bring all
the concepts together so I've already
set my open AI key and deleted it but
first you would need to have your en
open AI key whether you're getting it
from the environment variable or however
you want to do it all right so we import
dpy uh then we're connecting to gbt 313B5
turbo uh Colbert is a retrieval model
that does this super interesting late
interaction thing with the token with
the qu document vectors and query
vectors but anyway so here's a hosted um
Colbert of Wikipedia abstract
and so we're configuring dpy by setting
the language model and this cobbert
retrieval model so you could also plug
in your we8 URL and um you can see a a
description of how to do that in the
weeva uh wva RM in the ds. I'll link
that in the video as well okay so
anyways all right so we're going to be
using the hotot QA data set Hotpot QA is
used to Benchmark Benchmark uh multihop
question answering so in a second we'll
see an example of this but um in the
data set so we're going to be using 20
training examples and 50 examples for
validation with our metric so that's
like just the huge thing that's
different about deep learning that
compared to what it used to be is we
have dsy this new pytorch like framework
you know from Stanford and it has 20
examples is all we need to optimize it
so this is just like a huge paradigm
shift in deep learning and so marching
along I had to cut the video and
re-record because I was surprised at the
first example so uh the first example is
the question is at my window was
released by which American singer
songwriter and I'm not sure that's a
multihop question I'm pretty sure that
that that that's the author of the song
so let's see maybe another question uh
which American actor was Candice ke
guest start with okay now that's a good
one because to do that first you have to
ask uh what movies has uh Candace ke
been in and then within those movies you
would have to say um who are who are the
American actors in each of them so that
this one's a great example of a question
that you you would need to break it up
into sub questions in order to answer it
so so this is our training data set that
we're going to be using using to again
optimize the signatures optimize the
examples or maybe fine tuna model it and
then we have the development set that
we're going to be we're never going to
touch this touch this during training
but this is how we're going to get our
metrics out okay so these are just some
things about the data sets and how you
format data sets in dpy uh so so first
we have this is the longer hand for dpy
signatures where we have the doc string
that we give it you know a description
of the task answer questions the short
fact toid answers we have the inpoint
inut input field where we could give it
a description about it but we don't have
to we're just going to use the name of
the variable and then we have the output
field in description of that uh so then
in this case we're going to be doing a
super simple dpy program where all you
do is just you know one layer dpy do
predict so another kind of interesting
thing about dpy is that you can um
inspect the intermediate output so this
is kind this is kind of related to Andre
Kathy's tweet about how you know my
eyesight's improved I'm sleeping better
is because um when you want to see
intermediate outputs of neural networks
pytorch is super great for that and
that's one of the key ways that pytorch
differentiated itself from tensor flow
and you can also do this kind of thing
with Dy if you want to you know just run
one inference with just one layer you
can do it like this so here's an example
of the uncompiled dpy what is the
nationality of the chef and restaurant
restaurator featured in Restaurant
Impossible predicted answer American so
so right away you're seeing how the you
know it the I don't know this particular
restaurant all that well but the the
story is that uh it's British and you
need to break this question up but
anyway so back into the dpy building
blocks you can do language model.
inspect history to see the most recent
thing that was put into your language
model in dpy framework so you're seeing
how it has the instruction again from
our signature answer questions with
short Factory answers you know input
field see how it's just inferring it
from the name of the variable and then
you gave it the short description of
answer and then the inference it was
just faced with okay so now let's come
back into again what I believe is the uh
key motivating factor of why I would you
know encourage people to switch to this
ASAP is if you want to add Chain of
Thought to your
prompts you just change DSP y. predict
to dp. Chain of Thought and dpy will
come up with the rationals for you to
add that prompting and Chain of Thought
that like add an explanation it's always
going to be better it's always because
you know if you want to debug it it's
always going to be nice to have that
little rationale in there and not only
just that it does improve the
performance so here's the example of now
you have thought so we again we haven't
compiled this at all it's just a again
just a forward pass and if we want we
could also again do um turbo. inspect
history n equals 1 and we can see the um
now it's adding the reasoning to The
Prompt so that's what kind of like the
built-in modules do for you is they add
this to the prompt and so now we have
this intermediate reasoning that's been
produced for us let's think step by step
and so the language model you know this
is just a forward pass again we haven't
compiled this but already we see it
switches from American to British by
just adding that um that thinking step
in there so that's already that's
something that I think is the quickest
value to to Havey had so here's a quick
example of connecting to one of the
retrievers uh you retrieve with the
question and you know here's just like
showing you uh like what the in like
what the type is of the outputs
um let's see so maybe it would help to
see it without the formatting so you see
you just get like this list of strings
the list of strings is what it's
expecting from these DSP y. retrievers
so for example you're using it with we8
it's expecting a list of strings to come
out of wbaa okay so this is just like
another example of you know querying our
Colbert uh that we're accessing again
with the URL okay so now let's uh now
let's compile a rag program so we're
going to start off by with the generate
answer signature answer questions with
short fact answers the input field the
context um has the description of it
might contain relevant facts the
question we're just going to get that
from the variable name answer often
between one and five words okay so now
we're writing our rag program so we
initialize the components we need
retrieve and then generate answer with
the Chain of Thought and then passing in
this
signature into the dpy Chain of Thought
so again dpy Chain of Thought is going
to add this part the reasoning thing to
the prompt and then and then you know
when you're doing the inference it'll
have the reasoning okay so but this time
we're going to compile it so in the
forward pass we just you know take the
question give it the question take these
passages give it you know give it to the
question answer and that's how we do it
okay so now we're in the teleprompter
the optimizer so first we Define our
metric so we're going to be using exact
match which again is you know if it's
British is the answer then it's got to
be exactly British uh and then passage
match so I think passage match is in
this case we have supervision on the
retrieval as well but let's just kind of
focus on exact match to keep things easy
so the teleprompter is going to be
bootstrap few shot examples so it's
going to be uh looking to add few shot
examples into the prompt and that's how
it's going to be optimizing so then you
have compiled rag equals teleprompt do
compile we pass in rag we have our
training set and then we just do it so
you'll see the optimizing it'll stop
once it's you know once it's got a
certain amount of performance and maybe
this is something that we could
something that I think could have a
little more documentation on exactly how
that works but anyway so now we can see
these questions so now that we've
compiled our rag we you know compiled
our program we can run inference by you
know passing in the input so similar to
you know pytorch how you would pass in a
new input to it and we get this answer
to what Castle did David Gregory inherit
and all these kind of things so again we
can do the turbo inspect history if we
want to see the uh when you know we just
asked it uh this question of um what
Castle did David Gregory inherit and we
can you know we can debug like what the
last thing that the model S saw was so
we see how now you have these um you
know these examples in the The Prompt of
you know what it means to um to firstly
what it means to answer questions with
short factoid answers and then what it
means to follow the format that we want
with the uh with the question the
rationale and then you know it has a few
examples of the things so this part
right here is again and I've said this
like a hundred times in this video but
this reasoning is what I think is the
quickest value of dpy is you you want
rag but you don't want to have to write
this reasoning part for your uh fa again
if you're chatting with your docs and
you have an fa Q data set you don't want
to have to write this reasoning probably
cuz it's just kind of tedious to do
especially if especially if you have
like all sorts of com imagine you have
eight components and you know you're
like writing the email thing you don't
want to have to write the rationals for
each step and so that I think that sells
it pretty strongly okay so if you want
to inspect the parameters the parameters
being the examples this would be how you
do that and then uh if you want to use
the evaluate so this would be evaluate
would be um it's it's going through that
data set and you have the metrics and so
you know it's just running the forward
pass of your program and giving you that
like um you know what is the exact match
and as well as passes match in this
example so uh again in this uh first
example you also have supervision on the
titles because the hot pot QA data set
in addition to the answers it comes with
annotations for the the passages that
contain the
answers okay so while that's running
maybe we can just kind of March ahead
because you know this will output the
whatever the exact match score was of
the program so I don't think it'll be
too interesting to people listening but
okay so now we're looking at multi-hop
surch so we're graduating from our rag
program which you know was pretty simple
and now we're adding now we're going to
have two LM components and from there
hopefully you can imagine how to
generalize that to however many you need
um but I guess like the interesting
thing about this is you know that idea
of you don't need to supervise
intermediate layers in deep learning and
neural networks and now you don't need
to supervise intermediate components
it's sort of interesting we'll see how
that plays out but but in this in this
particular example it's very
straightforward how the queries might be
like connected to the final answer
whereas maybe your like intermediate
steps are more abstract than that and
now we have like the llm metrics and
intermediate so there is definitely a
lot to explore but anyways so now we are
adding a new component uh oops so here's
the output of the um sorry so so just
preempting with this finish but this is
the evaluation this is the kind of thing
you can expect example answer you know
the final exact match score and you can
see this kind of visualization cool okay
so so we have all moving into multi-hop
search so write a simple search query
that will answer a complex question we
have the Bine this is multihop system
developed by kabol in 2001 and what it
does is it uh starts off with the
context it's going to Loop through the
max HS which is two it's going to
generate a query taking as input the
context so far in the question it's
going to retrieve passages for the query
then it's going to D duplicate these
contexts if they're already in the
context and then it's going to pass this
back in so so um you know say your first
question again was it was about um it
was like an actress and it was what
American actors have been in movies with
her and so it will um you know it will
first ask that question of uh what
movies has she been in it'll get those
answers and it'll add that to the
context and it will still have the
question so it will it will be in its
input see the context it has so far when
it's producing that next query to keep
answering the question so pretty
interesting system in my opinion uh and
yeah like there's there maybe I'm going
out tangent but there's been a lot of
like reranking I think this kind of
multihop query decomposition is maybe
underappreciated this is I definitely am
more interested in this after going
through the dsy stuff anyways okay so
let me make sure I ran that okay so so
that's our program our uncompiled
program is when we're just you know
running a forward pass through it and we
can inspect the history to see uh the
last input of the uh uncompiled uh
program so uncompiled we you know know
uh we don't have the examples yet so we
just have the prompt and then we have
the context and then we have this
reasoning but we don't have examples of
how to produce the reasoning and maybe
you can see that the reasoning so far is
like not it's not that thorough of
reasoning and yeah so so now we'll give
it some examples and see how that
improve so so again this is like a
supervision on the intermediate Hops and
that's something we can maybe dive into
in a later video let me know any
particular comments you have and I'll I
can look into it all right cool so
bootstrap F shot metrics we're passing
in the metric all right so now we're
compiling this and okay so now we've got
a pretty interesting thing going where
now we're going to be uh we have a
teacher
model to produce the uh to produce the
supervision for the other model uh so I
think I actually missed this detail when
I first looked at it but from looking at
it like for as well as everyone watching
it looks like what we're doing is maybe
um we have this passages per hop thing
so it looks looks like maybe we have a
teacher model that only looks at two and
then it supervises one with
three uh yeah so I'm not sure exact I I
personally still need to be running more
examples but I hope this the purpose of
this video is really just to you know
get the concept together and so so yeah
so I think hopefully hopefully maybe
like yeah concluding so so I think with
this example you you hopefully got a
sense of how to write the syntax and
then yeah like even for me I think like
I've you know not even for me but like
I've been looking at it a little bit if
this is your first time seeing it in
this video and I'm still kind of
wrapping my head around all the
different teleprompters cuz there's
definitely a lot of depth to this whole
llms optimizing llms but anyways I hope
you found this useful awesome so I hope
you enjoyed this overview of dpy going
through things like the programming
model and the compiler and looking
through the introduction example showing
basic question answering adding uh Chain
of Thought reasoning as well as Rag and
multihop questions and all these things
so let me leave leave you with some
reasons I think everyone should start
using dpy today so first of all it's a
super fun syntax as Andre carpy says
you'll you'll sleep better and your
eyesight will improve it is fun to write
these programs in dspi it's you know
it's a really nice abstraction putting
you know if you do have longer prompts
organizing them as signatures and
passing signatures into the program it
really organizes this kind of stuff so
the next big thing I think the quickest
value added and I know I've said it a
lot in this video but if you want to use
Chain of Thought
prompting you know especially with the
few shot examples in the prompt you
would have to write these rationals
yourself and so I think just the getting
around needing to write your own
rationals is a really cool quick win
that you pick up with dsy uh the next
thing is you know llms it's like
changing every week almost it's like
last thing was the mixed R of experts
and so you might be switching your rag
program from you know gbt 3.5 to that
and then say gbt 428k then comes out and
then we have Gemini Ultra and you know
probably all sorts of language models
that we don't know yet are on the
horizon say coheres command so the each
llm is sensitive to the particular
language that you use to get it to do a
task which is you know this prompt
tuning this like that's been the story
is dpy is trying to end this manual
tweaking of the prompts to make it work
for certain LMS LM so you know I can't
tell you what the best LM is going to be
in a few months from now but what I can
tell you is that if you want to be able
to just recompile your program change
the prompts to whatever the new language
model is writing your prompts into dpy
will give you the you know the framework
to quickly adapt to these new things the
last thing I think is super interesting
is olama so AMA is a library for local
LM inference built on top of llama C++
and I don't know what's I don't know I'm
not familiar with everything that's been
happening but when I first tried llama
CPP my laptop was like you know it's
like about to shut down or something and
it was really slow but you know I've
tried it last week and AMA is fast and
so it you know it's getting really fast
and it's just super interesting what
these local llms can unlock and
generally just like you know if you can
run them on CPUs and stuff it's going to
make it cheaper and this whole like
intermediate program thing it's all just
so compelling so I think this idea of
using dpy to fine-tune models down into
smaller models that are served with
things like AMA like you know imagining
putting the T5 large or I think T5 has
this encoder decoder that might slow
down the inference compared to um anyway
sorry I'm distracting myself but anyways
I think this local llm thing is really
exciting and I think dpy also gives you
the right framework to you know see if
firstly the local LMS can do the job and
and then also there's the finetuning
angle so just a super interesting thing
and so I hope these reasons kind of help
motivate starting with Dy today so thank
you so much for watching if you want to
reach out on X my Twitter handle X
handle is Cort and3 and if you want to
send me a direct message I'd be more
than happy to take a look at anything
you're building with dpy and or we8 and
you know if you want to just ask ask a
question or chat about anything I'm more
than happy to do that and also um so
it's early with the dpy Discord but if
you're interested in dpy and want to
have some chats I highly recommend
joining it it's been a lot of fun and
that'll be linked in the description
thank you so much for watching