Thomas Rando at ARDD2023 - Longevity Medicine Day: Stem cell aging: From basic science to lifesty...
https://www.youtube.com/watch?v=5xg4J1ZT_Q4

Exercise and stem cell aging: inflammation, myokines, and cellular rejuvenation


1. **What are the goals of the study? What is the motivation for the work (i.e., why should this work be done; what’s the benefit)? Also, list 2-3 key ideas/findings from past work that this work is based on.**
- Carlson & faulkner 1989 muscle transplatation between young and old rats... young host could accept and regenerate both young and old translplanted muslce, but old host could do neither.
- hetero parabiosis. what he did in early 2000s to see how enviornment in which tissue repairs how important it is for it to repair... when old mouse is exposed to circulatory env of young mouse , it had good regeneration. They showed this in muscle, liver (2005, 2007), in brain and cns (early 2010s), then in bone, kidney, intervertebral discs etc
- ? are there physiological intervetions that can restore youthful regeerative potential in aged tissues ?


2. **In your own words, what is the take home message of this paper? i.e., what do you hope to remember about this work?**
- exercises --> upregulation of cycline D1 --> inhibtion of TGFbeta signaling ---> rejuivantion

3. **What are the key concepts, background fields, and associated studies or reviews.**
- Cyclin D1, coded by CCND1, is a key regularotry protein that drives the cell cycle from G1 growth phase into the S DNA-replication phase.
- Cycline D1 has alot of non-canonical roles such as trascrptional co-repressor.... most prominently it supresses TGF-beta
- osteopontin blocks the beneficial effecets of exercise.... msucle can be thought of as an endecrine organ.

4. **What topics did this paper make you want to read/learn more about?** 
- learn the motivation and units of the TFBS enrichment score z score on y axis graph showing REL and Smad3 as the identified transcription factor targets...

5. **What are the key computational, statistical, and biological methods used**
- volcano plot of transcription expression. log2(old with exercise / old without exercise) on x axis. y axis is -log10(Q-value). not p-val. q value measures the minimum false discovery rate (FDR) when performing may tests at once. a q value of 0.05 means that signifcant results are expected to be false positives... done by 1. gathering all m p-values from simultaneous tests, ordering them from smallest to largets, look at distr and calcultion est fraction of tests where null is actually true.
- he knocked out Cyclin D1 --> lose repression of certain genes that Cyclin D1 is usually a transcriptional corepressor for ---> some genes are upregulated??  TFBS enrichment score z score on y axis, # genes targetd on x axis... IDK what this is about
- hallmark gene sets and normalized enrichment score that identified TGF beta signaliing as the pathway or something more related to the above bullet.
- DMSO, EdU+, Ly364947
- single cell RNA seq on white blood cells, msucle, plasma, etc... but RNAseq on msucle fibers... plot of cells on umap coordinates.
- data filtering idea: ?whcih genes change with age, and which gnees change in same direction with exercise or just respond to exercise, then give ranked order of that
- quark/quart plot?

6. **Connections to concepts/terms encountered before.**


7. **What are some specific ways in which this paper makes you think differently and/or give you ideas about your own project(s)?** 
- i should listen to more MD speakers on ardd because they give full picture and understanding of bio.
- read endocrine or cellular sigalling section in alberts.

8. **Overall rating out of 10 for value in revisting the talk and associated paper/s in greater depth later.**
- 10/10. 
- good stuff to learn for following the logic of the experiment and statistical ideas and variables. single cell is in here so could be good learning segway into that and maybe could even replicate their scRNAseq analsyis.
- Rando has great organization and presents the context well almost in a identical fashion to the layout of these krishnan questions. great slides, logic, and 