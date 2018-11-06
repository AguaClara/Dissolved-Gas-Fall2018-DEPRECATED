# Reactor Measurements
## Pipe dimensions | Trial
The subteam is considering the use of a clear, colorless, PVC pipe as the body of the prototype reactor. The measured dimensions of the full-length pipe are given  below. Measurements were taken using a caliper, in units of millimeters. Measurements were taken at both ends of the pipe.

This particular pipe may not be used for the actual reactor, but the data will be kept.

#### Side 1
| Measurement | Thickness of Pipe | Outer Diameter | Calculated Inner Diameter | Calculated Inner Cross Sectional Area (mm^2) |
|:--:|:--:|:--:|:--:|:--:|
| 1 | 3.96 | 33.39 | 25.47 | 509.5 |
| 2 | 3.99 | 33.32 | 25.34 | 504.3 |
| 3 | 4.16 | 33.38 | 25.06 | 493.2 |
| Average | 4.04 | 33.36 | 25.29 | 502.3 |

#### Side 2
| Measurement | Thickness of Pipe | Outer Diameter | Calculated Inner Diameter | Calculated Inner Cross Sectional Area (mm^2) |
|:--:|:--:|:--:|:--:|:--:|
| 1 | 4.08 | 33.30 | 25.14 | 496.4 |
| 2 | 4.40 | 33.30 | 24.50 | 471.4 |
| 3 | 4.05 | 33.39 | 25.29 | 502.3 |
| Average | 4.18 | 33.33 | 24.98 | 490.1 |

The percent difference between the calculated, inner, cross-sectional area of the pipe at either end is **2.46%**. The subteam believes this is an acceptable percent difference for the pipe to be a usable component for the prototype.

The overall average cross-sectional area of the pipe is **496.2mm^2**, with a standard deviation of **13.44mm^2**.

##Sand grain dimensions
The following measurements were made using a caliper; the sand is Silica sand, and the ten sand grains are taken to be a representative sample of the sand used in the reactor.

The average measured diameter of the sand grains is 0.91mm, with a standard deviation of 0.21mm. This was calculated using the StandardDeviation.py code.

| Sand grain | Measurement 1 (mm)| Measurement 2 (mm) | Measurement 3 (mm)|
|:----------:|:-------------:|:-------------:|:-------------:|
|1           |0.69           |0.84           |1.08           |
|2           |1.33           |0.85           |1.31           |
|3           |1.13           |1.32           |0.90           |
|4           |1.20           |1.17           |0.86           |
|5           |0.98           |0.79           |0.77           |
|6           |0.71           |0.73           |0.72           |
|7           |1.00           |0.78           |0.82           |
|8           |0.76           |0.92           |0.70           |
|9           |0.69           |0.70           |0.76           |
|10          |0.91           |0.74           |1.10           |

##Porosity of the Silica sand
According to Fluidization Source 4, the density of silica sand is 2650kg/m^3. The porosity of this sand, which will serve as the fluidized agent in the reactor, will be calculated using the following equation from Fluidization Source 1. According to Fluidization Source 4, the porosity of the silica should approximately be 0.4.

$$ \epsilon=\frac{V_t-V_p}{V_t} $$
$$ \epsilon=1-\frac{m}{\rho_p A H} $$

For the sake of consistency, $\phi$ will be used to denote porosity rather than $\epsilon$.

$\rho_p =$ density of particles
$m =$ the total mass of the particles in the bed
$A =$ the cross sectional area of the tube
$H =$ the height of the bed
$\epsilon =$ the porosity of the bed (aka. the bed voidage)
$V_t =$ total volume of the bed $= AH$
$V_p =$ total volume of particles within the fluidized bed $= AH(1-\epsilon)$

### Experimental method
The following steps will be taken to determine porosity, adapted from Fabrication Source 1.

1. Acquire silica sand from the AguaClara laboratory.
2. Transfer the sand to a graduated cylinder to measure the volume of the sand, and record it exactly. This is the sample's volume. ($V_{sample}$)
3. Measure an excess amount of water into a second graduated cylinder. Record this volume.
4. Saturate the silica sand with water, pouring water into the sand bed until the top of the meniscus is level with the top of the sand bed.
5. Subtract the volume of input water from the dry sand's volume in the graduated cylinder. That shows you how much water it took to saturate the sand. The volume of the water used is equal to the Pore Volume. ($V_{pore}$)
6. Lastly, you can use the formula to find porosity ($\phi$):

$$\phi = \frac{V_{pore}}{V_{sample}}$$

This is equivalent to the formula given in Fluidization Source 1.

### Data &  Results
| Trial number | Measured volume of sand (mL) $(V_{sample})$ | Volume of water in cylinder (mL) |Volume of water remaining in cylinder after saturating sand (mL) | Pore Volume (mL) $(V_{pore})$| Calculated Porosity  ($\phi$) |
|:-:|:--:|:---:|:---:|:--:|:----:|
| 1 | 40 | 150 | 136 | 14 | 0.35 |
| 2 | 40 | 150 | 136 | 14 | 0.35 |
| 3 | 40 | 150 | 136 | 14 | 0.35 |

The average calculated porosity of the Silica sand is **0.35**, with a standard deviation of **0.0%**. These statistics were calculated using StandardDeviation.py in the subteam's Code folder.

This has a percent difference of 0% compared to Fluidization Source 4's suggested value of 0.4 (when the calculated value is rounded to one significant figure). This is very encouraging!

## Pipe dimensions | Official Prototype 1
**Specify how the pipe is cut; this information will be put into the Manual for Report 3**

The measured dimensions of the cut pipe are given  below. Measurements were taken using a caliper, in units of millimeters. Measurements were taken at both ends of the pipe.

This particular pipe will be used for the first prototype reactor.

#### Side 1
| Measurement | Thickness of Pipe | Outer Diameter | Calculated Inner Diameter | Calculated Inner Cross Sectional Area (mm^2) |
|:--:|:--:|:--:|:--:|:--:|
| 1 |  |  |  |  |
| 2 |  |  | |  |
| 3 |  |  |  |  |
| Average |  |  |  |  |

#### Side 2
| Measurement | Thickness of Pipe | Outer Diameter | Calculated Inner Diameter | Calculated Inner Cross Sectional Area (mm^2) |
|:--:|:--:|:--:|:--:|:--:|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| Average |  |  |  |  |

For clarification: the "outer diameter" includes the pipe's thickness, while the inner diameter does not.

The percent difference between the calculated, inner, cross-sectional area of the pipe at either end is **x%**. The subteam believes this is an acceptable percent difference for the pipe to be a usable component for the prototype.

The overall average cross-sectional area of the pipe is **mm^2**, with a standard deviation of **mm^2**.

## Fluidization flow | Official Prototype 1
Using the code FluidizationVelocity.py, the following fluidization flow was calculated for the Official Prototype 1 reactor:

This value will be compared with the qualitatively determined fluidization velocity for the prototype once it is constructed. 
