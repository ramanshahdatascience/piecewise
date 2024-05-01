# Emit Excel formulas for piecewise linear functions

*Under construction*

This repo contains some Python tooling to simplify linear combinations of
piecewise linear functions, then finally emit them (and their first
derivatives) as Excel formulas.

The motivating application comes from my engagements with very small social
enterprise clients, virtually all of which show up with the same story. There's
a sole proprietorship or disregarded-entity LLC. It has productive, material
operations - often exhaustingly busy operations. But it's fundamentally not big
enough to put food on its owner's table.  The owner benefits from government
support, perhaps paying almost zero in income taxes and getting free
healthcare. The owner is steadily liquidating their personal wealth, often
obscured by complexities like real estate windfalls, inheritances, family help,
grants, increasing debt, or deferred maintenance.  And I get a call to apply a
couple dozen hours of my expertise to clear up the numbers.

**How much will the owner need to grow the enterprise to earn a sustainable
living, taking into account that government support will roll off?** One must
reconcile that it gets easier to make money with scale because fixed costs only
have to be paid once, but harder to make money with scale because of the loss
of the government support. Capturing these nonlinear behaviors with some
precision can be strategically critical. Sometimes, my economic modeling
reveals a plausible scale at which the owner both makes a living and stays true
to the purpose of their social enterprise.  Then the way forward is to push on
marketing to grow demand to the needed scale. Other times, there is no such
plausible scale.  For example, many social enterprises are built around
artisanal local production, or they specialize in employing workers from a
marginalized community. These operational constraints based on social-purpose
considerations could cap out before the social enterprise is financially
successful. The way forward in this case, sadly, is either to relinquish the
prosocial commitments or shut the enterprise down. That's a fraught
consideration for a social entrepreneur, and it demands clarity of mind.

Analyzing prospective business revenue and profit, including scaling of
variable costs, is often reasonably straightforward from a decent set of books,
as the math is linear. Analyzing the owner's burn rate (cost of a lifestyle
after tax) is reasonably straightforward from a variety of personal financial
data and some accounting assumptions (e.g., capitalizing personal fixed assets
like a vehicle or home). This is all routine Excel spreadsheet work.

These two things meet through government support programs that aren't linear,
hence not nearly as straightforward.

But government support programs are usually piecewise linear. In fact, many of
them can be written down as linear combinations of translations of Rectified
Linear Unit (ReLU) functions - piecewise linear, continuous functions of profit
that are constant to the left. If we can wrangle this family of functions and
emit them as Excel formulas, we can embed the web of Federal and state income
taxes, the Earned Income Tax Credit, the Premium Tax Credit, Medicaid, etc.,
within a spreadsheet analysis that will be accurate enough over a big enough
range of scaling to answer the central question.

That's the goal of this repo.
