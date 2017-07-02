# Introduction

First off, thank you for taking time to consider contributing to Pricebots. Please, read over these guidelines and rules for contributing. If you have any questions about any of the topics listed below, then please shoot us a message on our <a href="http://pricebots.enterslack.com">
	<img src='https://cdn.worldvectorlogo.com/logos/slack.svg' width='90'>
</a>

Following these guidelines helps to communicate that you respect the time of the developers' managment and development of this open source project. In return, they should reciprocate your respect in addressing your issue, assessing changes, and helping you finalize your pull requests.

### What contributions is the Pricebots team looking for?

Pricebots is an open source project and we love to receive contributions from our community — you! There are many ways to contribute, from writing tutorials or blog posts, improving the documentation, submitting bug reports and feature requests, or writing code which can be incorporated into Pricebots itself.

Please, don't use the issue tracker for support questions. Check whether the #general channel on <a href="http://pricebots.enterslack.com">
	<img src='https://cdn.worldvectorlogo.com/logos/slack.svg' width='90'>
</a> can help with your issue. Stack Overflow is also worth considering.

# Ground Rules

### Responsibilities
* Ensure cross-platform compatibility for every change that's accepted.
(e.g., Windows, Ubuntu/Raspberry Linux).
* Ensure the code that goes into core meets all requirements in this
[checklist](https://gist.github.com/audreyr/4feef90445b9680475f2).
* Create issues for any major changes and enhancements that you wish to make. Discuss things transparently and get community feedback.
* Don't add any classes to the codebase unless absolutely needed. Err on the side of using functions.
* Keep feature versions as small as possible, preferably one new feature per version.
* Be welcoming to newcomers and encourage diverse new contributors from all backgrounds. See the [Community Code of Conduct](https://github.com/JordanDworaczyk/Pricebots/blob/master/CODE_OF_CONDUCT.md).



# Your First Contribution

Unsure where to begin contributing to Pricebots? You can start by looking
through issues labeled _Ready_ and by reading the _Issue Log_:
- **_Ready_ issues** - are issues that have been discussed. These issues have a
solution that needs to be implemented, and requirements that need to be met, for
the issue to be considered closed. These issues are ready to be in Progress
because their _Issue Logs_ have been completed during the _Discussion_ phase.
- _**Issue Log**_ - is a comment provided with each _Ready_ issue that explains the details of the issue, a method for implementing a solution, requirements for the issue to be considered closed, and the status of the issue.

_Issue Logs_ are maintained by project curators and are there to help contributors understand exactly what needs to be done for the issue to be closed. If you have any questions about an issue you can first consult the _Issue Log_, otherwise, feel free to comment, discuss, or ask questions while the issue is at any phase during the workflow.

Are you working on your first Pull Request and don't know where to start, then you can learn all about Github from this *free* series, [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github).  



# Getting started
We have Five phases in our workflow. Each phase of an issue has a matching label, so that you can quickly understand where each issue is at during the workflow. These phases are listed as:
1. Discussion  
2. Ready  
3. in Progress
4. Needs Review
5. Done

The **Discussion** phase is where an issue goes immediately after it has been created. Here the issue will be discussed until a project curator completes the issue's _Issue Log_.

The **Ready** phase is where issues go once the _Issue Log_ is competed. You do not start working on an issue until the issue has been moved into the _Ready_ phase.

The **in Progress** phase is where the issue goes while it is being worked on. A branch should be created for every issue that is _in Progress_. If you are to work on an issue, then you must create a new branch off of the master branch, and title the branch with nothing but the issue-number of the issue that you are working on. For example, if you were working on issue #45, then the title of your branch would be just the single three characters of `#45`.

**NOTE:** If you decide to work on an issue that is already in progress, then you will need to branch off of the branch that contains your issue number. In this case, you may name the branch whatever title that you please. :smile:

The **Needs Review** phase is where the code gets reviewed after it has been _in Progress_. Once you feel that your code closes the issue that you were working on, you may submit your code by creating a pull request.

**NOTE:**
Please, title your pull request using this syntax, ```closes #[enter issue number here]```. For example, if you were submitting code for review which closed issue #45, then you would title the pull request with ```closes #45```.

The **Done** phase is where the issue goes when it is done! Hopefully, to never be seen again. :wink:

### Issue Logs
We use an _Issue Log_ with every issue that gets submitted to Pricebots. _Issue Logs_ are created and updated regularly during the workflow by the project curator(s) so that contributors can easily understand the status of an issue. An _Issue Log_ contains four things:
- Story details
- Implementation
- Requirements
- Status

**Story Details** explains in more detail each [user story](https://en.wikipedia.org/wiki/User_story) that needs to completed. This is not criteria that must be completed for the issue to be closed, but instead more of a rational, merit, or explanation of why this issue is important and should be addressed.

**Implementation** is how we will best approach implementing the solution to this issue. The solution may change by the time the issue is closed, but an implementation method must be laid out before the issue can be moved into the Ready phase of the workflow.

**Requirements** are  what need to be met for this issue to be closed. The requirements must be listed before the issue can be moved into the _Ready phase_. And, requirements may change by the time that the issue is closed, but there must be requirements laid out before the issue can be moved into the _Ready_ phase.

**Status** is the status of the issue.

### Issue Management
We use Waffle.io to manage our issues. You can see our process [here](https://waffle.io/JordanDworaczyk/Pricebots/join). We do our best to rate the difficulty of each issue. The points with the smallest numbers are to be considered less difficult, and the points with the larger numbers are to be considered more difficult.

We also manage our issues into Milestones. Milestones each contain a pseudo-deadline and a description of the milestone to be reached. You can see our Milestones [here](https://github.com/JordanDworaczyk/Pricebots/milestones).

# How to report a bug
### Security Disclosures
If you find a security vulnerability, do NOT open an issue. Email jordan.dwo@gmail.com instead.

In order to determine whether you are dealing with a security issue, ask yourself these two questions:
* Can I access something that's not mine, or something I shouldn't have access to?
* Can I disable something for other people?

If the answer to either of those two questions are "yes", then you're probably dealing with a security issue. Note that even if you answer "no" to both questions, you may still be dealing with a security issue, so if you're unsure, just email us at jordan.dwo@gmail.com.


### Bugs
If you find a bug, then please submit an issue explaining the bug in detail.

# How to suggest a feature or enhancement
 If you find yourself wishing for a feature that doesn't exist in Pricebots, you are probably not alone. There are bound to be others out there with similar needs. Many of the features that Pricebots has today have been added because our users saw the need. Open an issue on our issues list on GitHub which describes the feature you would like to see, why you need it, and how it should work.

# Code review process
A contribution gets accepted once it has gone through all phases of the workflow. The review process takes place, by project curator(s), during the _Needs Review_ phase, and may take up to two weeks before you get a response from the core team.

Code is reviewed by the core team and needs to be signed off by Jordan Dworaczyk before it can be accepted. In order to become part of the core team, you must contribute to the Pricebots project often.

# Community
At this point, you're ready to make your changes! If you are a beginner, then feel free to ask for help; everyone is a beginner at first! :smile_cat:

Also, if you have any questions you can chat with the core team on <a href="http://pricebots.enterslack.com">
	<img src='https://cdn.worldvectorlogo.com/logos/slack.svg' width='90'>
</a>.
