# Emit Excel formulas for piecewise linear functions

*Under construction*

This repo contains some tooling to simplify linear combinations of piecewise
linear functions, then finally emit them (and their first derivative) as Excel
formulas.

The motivating application comes from my engagements with very small social
enterprise clients, virtually all of which show up with the same story. There's
a fledgling sole proprietorship or disregarded-entity LLC. It has material
operations - often exhaustingly busy operations, in fact. But it's
fundamentally not big enough to put food on its owner's table.  The owner
benefits from government support - perhaps paying almost zero in income taxes
and getting free healthcare. The owner is steadily liquidating wealth, often
obscured by complexities like real estate windfalls, inheritances, family help,
grants, increasing debt, or deferred maintenance. And I get the call to apply
one or two dozen hours of data science expertise to clear up the numbers.

**How much will the owner need to grow the business to earn a sustainable
living, taking into account that taxes and health insurance premiums will wake
up?** To double the cash available to fund their lifestyle, they'll have to
more than double their revenue. But how much more than double? This question
can be of great strategic importance in assessing whether a business can
sustainably fund it's owner's survival, and if so, how that would look.
Sometimes, there is a scale that seems achievable and accords with what the
owner values about their enterprise. Sometimes the scale required would
alienate the animating purpose of the venture, and the best thing would be to
shut the business down. These are big, hard questions for a social entrepreneur
that demand precise answers.

Analyzing prospective business revenue and profit, including scaling of
variable costs, is often reasonably straightforward from a decent set of books,
as the math is linear. Analyzing the owner's burn rate (cost of a lifestyle
after tax) is reasonably straightforward from a variety of personal financial
data and some accounting assumptions (e.g. for depreciation of personal fixed
assets like a vehicle or home). This is all routine Excel spreadsheet work.

These two things meet through government tax and support programs that aren't
linear, hence not nearly as straightforward.

But government programs are usually piecewise linear: linear combinations of
translations of Rectified Linear Unit (ReLU) functions. If we can wrangle them,
we can reduce the web of Federal and state income taxes, the Earned Income Tax
Credit, subsidies for healthcare, etc, to one or a few scary Excel formulas
that will be acceptably adequate over a big enough range of business scaling to
answer the animating question.

That's the goal of this repo.
