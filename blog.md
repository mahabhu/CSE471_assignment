## CSE471 Assignment | Blog 
# Paths to Equilibrium in Games | NeurIPS 2024
**Authors**: Bora Yongacoglu, Gürdal Arslan, Lacra Pavel, Serdar Yüksel  

---

## Introduction  

### Multi-Agent Reinforcement Learning (MARL)  

In MARL, multiple agents interact within an environment to achieve individual or collective goals. Each agent iteratively updates its strategy based on observations and feedback. While MARL has seen significant success in cooperative and adversarial scenarios, achieving convergence to equilibrium in complex, multi-agent environments remains a challenge.  

### Normal-Form Games and Nash Equilibrium  

**Normal-form games** provide a mathematical framework for modeling strategic interactions. In such a game:  
- There are \( n \) players, each capable of selecting from a finite set of actions \( A_i \).  
- Each player \( i \) receives a reward \( R_i \) based on the joint action profile \( a = (a_1, \ldots, a_n) \).  
- A player's objective is to maximize their expected reward by choosing a strategy \( x_i \) from their strategy set \( X_i \), where \( x_i \) is a probability distribution over \( A_i \).  

#### Nash Equilibrium  

A strategy profile \( x^* = (x_1^*, x_2^*, \ldots, x_n^*) \) is a **Nash equilibrium** if no player can unilaterally improve their reward by changing their strategy:  

\[
R_i(x_i^*, x_{-i}^*) \geq R_i(x_i, x_{-i}^*) \quad \forall x_i \in X_i, \quad \forall i \in \{1, \ldots, n\},
\]  

where \( x_{-i}^* \) represents the strategies of all players except \( i \).  

Finding Nash equilibria is central to MARL but is often computationally challenging due to the coupled nature of the reward functions and the high-dimensional strategy space.  

---

## Problem Statement  

The authors investigate whether **satisficing paths**—strategy update sequences where satisfied agents (those already using their best response) do not change their strategies, and unsatisfied agents freely explore—can always lead to a Nash equilibrium in finite normal-form games.  

### Core Question  

For any finite normal-form game and any initial strategy profile, can we construct a satisficing path that guarantees convergence to Nash equilibrium?  

### Key Insight  

The paper proves that such a path always exists. Interestingly, this result leverages **suboptimal updates**—a departure from conventional reward-improving approaches—to achieve equilibrium and avoid cyclical behaviors.  

---

## Mathematical Framework  

### Game Representation  

A finite \( n \)-player normal-form game \( \Gamma \) is defined by:  
1. \( n \): Number of players.  
2. \( A = A_1 \times A_2 \times \cdots \times A_n \): Set of joint actions.  
3. \( r = (r_1, r_2, \ldots, r_n) \): Reward functions, where \( r_i: A \to \mathbb{R} \) specifies the reward for player \( i \).  

The strategy profile \( x = (x_1, x_2, \ldots, x_n) \) consists of mixed strategies \( x_i \in X_i = \Delta(A_i) \), where \( \Delta(A_i) \) is the probability simplex over \( A_i \).  

### Satisficing Paths  

A sequence of strategy profiles \( \{x^t\}_{t=1}^\infty \) is a **satisficing path** if for all players \( i \):  
- \( x_i^{t+1} = x_i^t \) if \( x_i^t \) is a best response to \( x_{-i}^t \).  
- \( x_i^{t+1} \in X_i \) (freely updated) if \( x_i^t \) is not a best response.  

---

## Proof Outline: Existence of Satisficing Paths  

The proof establishes that any finite \( n \)-player normal-form game \( \Gamma \) has a satisficing path that terminates at Nash equilibrium.  

### Step 1: Define Satisfaction and Unsatisfaction  

For any strategy profile \( x \), define:  
- \( \text{Sat}(x) = \{i \in \{1, \ldots, n\} : x_i \in BR_i(x_{-i})\} \): Satisfied players.  
- \( \text{UnSat}(x) = \{1, \ldots, n\} \setminus \text{Sat}(x) \): Unsatisfied players.  

### Step 2: Iterative Strategy Updates  

1. **Initialization**: Start with any initial strategy profile \( x^1 \).  
2. **Update Unsatisfied Players**: At each step \( t \), update the strategies of players in \( \text{UnSat}(x^t) \) to increase their satisfaction.  
3. **Stopping Condition**: The process terminates when \( \text{UnSat}(x^T) = \emptyset \), i.e., all players are satisfied.  

### Step 3: Suboptimal Updates and Convergence  

#### Key Insight: Use of Suboptimal Updates  
- At each step, allow unsatisfied players to explore suboptimal strategies.  
- This exploration increases the number of unsatisfied players, avoiding cyclical behaviors.  

#### Termination Guarantee  
- The number of unsatisfied players is strictly increasing until all players are satisfied.  
- Since the total number of players is finite (\( n \)), the process terminates in at most \( n \) steps.  

### Step 4: Nash Equilibrium at Termination  

When \( \text{UnSat}(x^T) = \emptyset \), the strategy profile \( x^T \) satisfies the Nash equilibrium condition.  

---

## Insights and Implications  

### Key Takeaways  

1. **Convergence Assurance**: Satisficing paths guarantee convergence to Nash equilibrium in finite normal-form games.  
2. **Breaking Cycles**: The use of suboptimal updates avoids cyclical behaviors common in adversarial dynamics.  
3. **Distributed Applicability**: This approach can be implemented in decentralized systems where agents independently assess their satisfaction.  

### Implications for MARL  

- **Exploration and Exploitation**: The satisficing principle balances exploration (for unsatisfied agents) and exploitation (for satisfied agents).  
- **Scalability**: Reducing updates for satisfied agents minimizes computational overhead in large systems.  

---

## Broader Applications  

### Extensions to Dynamic Games  

The framework holds promise for generalization to dynamic settings, such as:  
- **Markov Games**: State-dependent rewards and evolving strategies.  
- **Stochastic Games**: Probabilistic transitions and long-term objectives.  

---

## Conclusion  

This work redefines equilibrium-seeking dynamics in games by introducing satisficing paths. By allowing exploratory updates for unsatisfied agents and freezing satisfied agents, it guarantees convergence to Nash equilibrium in finite normal-form games.  

This theoretical breakthrough inspires new MARL algorithms that prioritize robust and decentralized learning dynamics, paving the way for advanced applications in AI, distributed systems, and strategic decision-making.  
