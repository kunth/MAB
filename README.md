MAB(Multi-Armed Bandit)
===

The author had written a simple article about multi-armed bandit [here](http://kunth.github.io/bandit-algorithm/)

The author wants to collect some materials about Multi-Armed bandit here.

## From abroad 
1. [Bandit algorithm for website optimization(pdf)](http://pdf.th7.cn/down/files/1312/bandit_algorithms_for_website_optimization.pdf) 
, [And the code of this book](https://github.com/johnmyleswhite/BanditsBook)

2. [Algorithms for the multi-armed bandit problem(pdf)](http://www.cs.mcgill.ca/~vkules/bandits.pdf)

## From home
1. [通过试验学习(ppt)](http://netcomm.bjtu.edu.cn/wp-content/uploads/2013/08/%E7%AC%AC%E5%8D%81%E4%B8%89%E8%AF%BE%EF%BC%9A%E9%80%9A%E8%BF%87%E8%AF%95%E9%AA%8C%E5%AD%A6%E4%B9%A0.pptx)

******

`Bandit algorithm for website optimization `
> 1. **Arm**: For historical reasons, these options are typically referred to as **arms**, so we’ll talk about Arm 1 and Arm 2 and Arm N rather than Option 1, Option 2 or Option N.

> 2. **Reward**:a reward is something quantitative that we can keep of track of mathematically and that larger amounts of reward are better than smaller amounts

> 3. **Bandit Problem**: 
* We’re facing a complicated slot machine, called a bandit, that has a set of N arms that we can pull on.
* When pulled, any given arm will output a reward. But these rewards aren’t reliable, which is why we’re gambling: Arm 1 might give us 1 unit of reward only 1% of the time, while Arm 2 might give us 1 unit of reward only 3% of the time. Any specific pull of any specific arm is risky.
* Not only is each pull of an arm risky, we also don’t start off knowing what the reward rates are for any of the arms. We have to figure this out experimentally by actually pulling on the unknown arms.
* We only find out about the reward that was given out by the arm we actually pulled.
Whichever arm we pull, we miss out on information about the other arms that we
didn’t pull. Just like in real life, you only learn about the path you took and not the
paths you could have taken.
* Every time we experiment with an arm that isn’t the best arm, we lose reward because we could, at least in principle, have pulled on a better arm.
