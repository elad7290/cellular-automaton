# cellular-automaton

## Rumor Spreading Simulation

### Automaton Design

Consider an automaton on a grid of size 100x100 cells. Populate the grid with individuals based on a uniform distribution parameterized by `P`, representing population density. The value of `P` will be varied during the study to observe its impact on the system's behavior.

Each individual has a level of skepticism, categorized into four levels:

- **S4:** Does not believe any rumor.
- **S3:** Basic probability of believing a rumor is 1/3.
- **S2:** Basic probability of believing a rumor is 2/3.
- **S1:** Believes every rumor.

Randomly assign each individual one of these skepticism levels. You will later manipulate the percentage of individuals at each skepticism level.

Select one individual randomly and assume they initiate spreading a rumor according to the following rules:

- When an individual spreads a rumor, it is passed to all of their neighbors.
- The recipient decides, based on their skepticism level, whether to pass the rumor to their neighbors. For instance, an individual with skepticism level `S2` has a 1/3 chance of passing the rumor to their neighbors.
- Passing of the rumor occurs immediately after receiving it. If an individual receives the same rumor from at least two different neighbors in the same generation, their skepticism level temporarily decreases. For example, if an individual with a basic skepticism level of `S3` receives the rumor from two different neighbors in the same generation, their skepticism level becomes `S2`. An individual who has spread the rumor will not do so again for the next `L` generations (another parameter to be manipulated).

### Section A: Simulation Analysis

1. Investigate how the network behaves, primarily by checking the rate of rumor spread within the population (i.e., the percentage exposed to the rumor up to a certain generation). Consider additional metrics if applicable.
2. Run multiple simulations (at least 10) for statistical reliability, varying parameters such as `P`, `L`, and the ratios between individuals of types `S1`, `S2`, `S3`, and `S4`. Aim to find a set of parameters where rumor spreading occurs at a "reasonable" rate. Reasonable implies a spread that is neither too rapid, resembling a field of weeds, nor too slow or nonexistent.

### Section B: Strategic Placement of Individuals

In Part A, the distribution (location) of individuals of types `S1`, `S2`, `S3`, `S4` within the population is random. Propose and implement a strategy for placing individuals of each type in a way that significantly alters the network's behavior. For example, design a placement that slows down the spread of rumors.
