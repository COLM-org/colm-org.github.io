COLM's deadline was March 31, 2026. Given the rise of coding agents in late 2025 and early 2026, this conference received a nontrivial number of coding agent-generated submissions.

This post details our findings of investigating these papers throughout the review process. As coding agents are moving quickly and tools are adapting, we do not intend this to be a prescription that other conferences should do exactly as we did. Rather, we describe our processes and our findings to enable others to learn from them.

No paper was desk-rejected on the basis of a detector result, and no AI detector results were shown to reviewers or ACs.

![Timeline of the AI-submission analysis process, from pre-review desk rejections in April 2026 through review, meta-reviews, and PC decisions culminating in analysis of decisions by July 2026](/static/images/blog/ai-submissions-timeline.png)

## Pre-review: Automated Analysis with GPTZero

We coordinated with GPTZero to detect the use of AI in submissions. GPTZero ran two tools: (1) AI scoring on paper text (*not* using reference information); (2) hallucinated reference detection.

### AI-scoring

**Process:** GPTZero produced scores of each paper's AI use on a scale from 0-1, producing a total ordering of all submissions by amount of AI used.

We subsequently double-checked this with Pangram. Pangram agreed that all of GPTZero's top 50 predicted AI papers were either "AI" or "mixed".

Based on these tool outputs and looking at a few hundred papers, we could tell that roughly 5% of papers used AI very heavily or were primarily AI-generated. This is a conservative estimate: a very sophisticated bespoke agent might have escaped detection. Furthermore, it is hard to draw a firm boundary here, as we see a wide range of use of AI, between polishing grammar to writing sections to writing entire papers. No punitive actions were taken on the basis of detector results alone.

The PCs then inspected around 90 of the papers determined by GPTZero to be most AI-generated.

**Actions:**

- 32 of these 90 papers (plus 14 others not in this set) were desk-rejected for violations of the LLM policy: cliques of authors submitting large numbers of papers, at least some of which did not disclose the use of LLMs in accordance with the policy. Usage of LLMs was substantiated through hallucinations in citations or other paper content, which was possible to find due to the volume of papers submitted by these authors.
- 11 papers were desk-rejected for being very poor quality or having very obvious hallucinations. (Other papers in this category were flagged by area chairs as well.)
- No paper was desk-rejected purely on the basis of a detector result.

Overall, roughly 2% of papers were desk-rejected for these criteria, not counting other desk-rejections due to formatting, anonymity, etc.

The cost-benefit tradeoff of more desk rejection was not favorable given our established processes. Due to the large gray area, substantial amounts of PC work would've been needed to confidently reject another 50-100 papers. This would only represent 3% of submissions (or less). We instead prioritized managing other parts of the review process and allowed these papers to stand for review.

### Reference detection

**Process:** Invalid references were flagged by GPTZero across all papers. The list allowed us to identify papers with completely hallucinated citations and those with large numbers of hallucinations.

The PCs inspected papers with large numbers of hallucinated references. Around 20 additional papers were desk-rejected based on hallucinated references. We saw three kinds of hallucinated references detected:

1. Completely fabricated references
2. Incorrect authors, but otherwise correct title and some correct metadata (we could tell what paper was intended to be cited here)
3. False positives: blog posts or papers from closed-access journals not easily discoverable on the web. Because of these false positives, we do not report an overall number of hallucinated references, since one cannot be accurately computed.

We desk-rejected papers that had completely fabricated references in our analysis. Papers with only a few cases of incorrect authors were allowed to stand for review.

## Review stage

Remaining papers went through review as normal, without any indication of AI usage shown to reviewers or area chairs. Reviewers and ACs in some cases flagged cases of papers that they believed to be AI-generated, or hallucinated references that they traced down themselves. However, this was pretty rare (<1% of submissions).

## Post-review: PC analysis

<figure class="inline-figure">
  <img src="/static/images/blog/ai-submissions-accept-rates.png" alt="Bar chart of acceptance rate by rank of paper by AI score: papers ranked 1-50 by AI score had a 0% acceptance rate, papers ranked 51-100 had a 10% acceptance rate, and papers ranked 101-200 had a 13% acceptance rate, all well below the overall accept rate of 29%" />
  <figcaption>Acceptance rate by rank of paper by AI score, compared to the overall accept rate of 29%.</figcaption>
</figure>

After reviewers and meta-reviewers (ACs) produced their recommendations and PCs were making final decisions, we re-examined the top AI-detected papers according to GPTZero. After a first-pass bucketing based primarily on AC recommendations, we observed the following acceptance rates in this pool (see figure).

Note that these statistics do not reflect final PC decisions, which reflected more scrutiny of edge cases, including some of these papers. Five of these papers ended up being rejected in this second phase.

## What are these papers? "Theoryslop" and "slopterpretability"

Many AI-generated papers were low-quality and peer review weeded them out effectively:

- Mostly text: position papers or proposals of frameworks/taxonomies
- Underdeveloped experimental papers: often incremental ideas, insufficient evaluation and comparison to related work, with baselines "inspired" by other papers but not rigorously evaluated against those prior methods.

Two types of papers seemed more likely to get through peer review.

**Theoryslop:**

1. Proposes a relationship like a scaling law
2. Proves a theorem or two about this relationship
3. Validates this relationship experimentally, e.g., by fitting coefficients of the scaling law

Because this paper's contribution is primarily conceptual/theoretical, there's less of a need to have a very strong empirical core like baseline comparisons. And because COLM is not a CS/ML theory venue, the theory won't be strongly evaluated on axes like taste or of interest to the CS/ML theory communities. Finally, because agents are pretty good at math, they can crank out a lot of theory, much of which is probably correct.

A few theoryslop papers were found to contain fatal errors by very hardworking reviewers. However, this is not a scalable solution. Without a uniformly exceptional review pool, such papers will not always be checked closely enough to find errors.

**Slopterpretability:**

1. Carves off a narrow question: e.g., what is the mechanism behind refusal in multi-turn jailbreaks? (not a real submitted paper)
2. Performs interpretability analysis using off-the-shelf tools, like circuit discovery or SAEs
3. Reports the results and draws conclusions, sometimes with exaggeration

Note: see this excellent post [An Analysis of AI-Generated Content at the Mechanistic Interpretability Workshop](https://www.lesswrong.com/posts/r7FBQ8XDs6qBYc4K4/an-analysis-of-ai-generated-content-at-the-mechanistic) for a description of these papers at the mechanistic interpretability workshop at ICML.

Theoryslop and slopterpretability papers can get high scores because: (1) Their main flaw is the quality and impact of the research question, which junior reviewers may find it hard to assess. (2) They are very technical, which both "pure" human reviewers and those leaning on LLMs may favor. (Note: we also conducted analysis of AI in reviewing as well but do not discuss here.)

## The best of the AI papers

Some papers ranked highly on AI detector scores and were recommended for acceptance even after careful consideration.

1. A "false positive": the paper does not look obviously AI-generated. This could either be a true miss on the detector, or AI was used to prepare the paper, but in a human-assisted way. That is, perhaps an initial draft was cleaned up with an AI in a way that triggers the detector, but the paper's "bones" are human despite the lexical style being AI.
2. A "true positive": the paper is AI-written, but the underlying contribution is very solid. For instance, the paper presents a useful dataset which has been made available. In this case, the presentation of the paper matters, but is less important than for something like a position paper. The usefulness of the artifact outweighs any subpar, AI-trope-ridden writing of the paper.

## Recommendations for the future

We share this process and findings for use by future COLM PCs and those of other conferences. Our takeaways are:

1. Running Pangram and GPTZero can provide a baseline measurement of AI usage in submitted papers and help identify bad actors submitting many AI-authored papers.
2. We should not take a very draconian policy on AI detection. Trying to detect the usage of AI separate from paper quality will be increasingly hard to enforce (too much gray area, AI will get better, and its use will continue to spread). If a paper has an authentic human-vouched contribution, the use of AI to write the paper is not automatically disqualifying.
3. The conference should employ a heavier desk-rejection phase. This may require a separate set of "pre-reviewers" who work in combination with detector results to reject poor-quality papers which were generated by AI.
4. Most radical: conferences may have to narrow the scope of allowed contributions. Theoryslop and slopterpretability are hard to manage in the same review process as other papers. The specialized expertise needed to review these papers presents a challenge given the volume at which these papers can be submitted.

## Disclaimers

COLM is different from ML and \*CL conferences in two big ways. First, it is much smaller. Second, it is not ranked on rankings like CORE, so papers in COLM "count" less than those in other venues for some researchers. As a result, it may be less of an attractive target for gaming. (We believe the quality of COLM papers is at least as high as those at other venues, and we don't view COLM acceptance as any less prestigious!)

---

**COLM Senior Program Chair:** Greg Durrett  
**COLM PCs:** Aviral Kumar, Yulia Tsvetkov, and Yoon Kim

*Thanks to Yoav Artzi (general chair) and Jonathan Kummerfeld for comments on an early draft of this post.*
