# General Notes
- This file will be for notes not able to fit into any of the catagories. 

### Relevant Research
- **White Papers**  
https://arxiv.org/abs/2205.05748 Tiny Robot Learning: Challenges and Directions for Machine Learning in Resource-Constrained Robots'

  https://sites.google.com/berkeley.edu/cloudfolding Learning to Fold Real Garments with One Arm: 
A Case Study in Cloud-Based Robotics Research

- **Youtube Videos**  
https://youtu.be/rRFgm_QSc74?s 12 Design Tips And Tricks for Inventors and Makers

### Steady-State
- the behavior of a system or process that is unchanging in time. 
- #### Continuous time
    - the partial derivative, with respect to time, is zero
    - $\frac{\partial p}{\partial t} = 0$
- #### Discrete time
    - The first difference (subtraction) of each property is zero
    - $p_t - p_{t-1} = 0$

### Diffusion
- The net movement of anything generally from a region of higher concentration to a region of lower concentration.

### Determinism
- Taking a snapshot and applying/quantifying a value
    - The world is continuous, so only use in measurements
    - Its like taking a slice, its true but only for a *determined* point in time 

### Derivative 
- A deterministic value, quantifies a specific change to a single variable. 

### Gradient
- The generalization of the derivative to multiple variables
    - i.e. Combine/Generalize all the derivatives (like a fluid's movements) to get the gradient
        - IT IS STILL STRUCTURED, it creates a vector that points to the steepest increase

## Design Methodology
- Repeat this process for each major subsystem
    - i.e. single servo, single leg, full chasis, gait cycle etc.

### Engineering Method
- component-level validation → digital twin simulation → software integration → physical validation → refinement

### Actual Method
- test each part -> FreeCAD mockup -> code implementation -> Simulate -> iterate or real-life test -> iterate or refine

