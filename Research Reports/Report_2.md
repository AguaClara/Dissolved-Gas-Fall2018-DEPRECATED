# Dissolved Gas, Fall 2018 Subteam

### Thomas Bradford, Karalyn Buhl, Isaac Singer

### 26 October, 2018

## Abstract
Excess dissolved air in a water treatment plant’s influent water decreases functionality of the treatment plant's filters and sedimentation tanks. The Dissolved Gas subteam begins its first semester with the goal to design a gravity-powered apparatus that extracts this gas from influent water prior to entry into the treatment plant. The subteam will gather literature, develop designs, fabricate a small-scale prototype, and iterate improvements based on experimental data to work towards a model that may be scaled up for application in an AguaClara plant. **This semester, the subteam aims to fabricate a reactor that quantitatively reduces the amount of dissolved gas in influent water. In future semesters, the subteam will aim to maximize the quantity of dissolved gas that is removed, as well to minimize the complexity and cost of the reactor.**

## Introduction
Excess dissolved gas in influent water in AguaClara plants at Tamara, Honduras and EL PODA, Nicaragua has inhibited the plants' efficiencies. Excess gas causes bubbles to form in the sedimentation tank, causing flocs that should settle to rise and to continue into the remainder of the plant. In the sand filter, gas bubbles form between sand particles and effectively clog the filter [(Scardina, 2004)](https://vtechworks.lib.vt.edu/bitstream/handle/10919/26497/PaoloScardinaDissertation2004.pdf?sequence=1). To remedy this, the Dissolved Gas subteam intends to design a reactor that removes such dissolved gas from influent water prior to entering the plant, in order to preserve the efficiency of the water treatment process.

To clarify, “excess dissolved gas” does not entail *bubbles* being present in influent water. The influent water is supersaturated with gas: gas molecules are dispersed throughout the water, not congregated in bubbles. Due to the presence of this excess gas, bubbles then form in the plant's sedimentation tank and in its sand filter. For this reason, the subteam plans to remove the excess gas through the use of a reactor stationed prior to the plant.

For the sake of efficiency, the term “supersaturated water” will be used in this report to reference water containing excess dissolved gas, whether air or otherwise.

The current conception of the system design is as follows: influent water will flow from its source at a high elevation. Once the influent water is near to the AguaClara plant, piping will direct it upwards into a reactor. Atmospheric pressure decreases as elevation increases; according to Henry’s Law, gas becomes less soluble at lower pressures, making bubble formation more likely. Aspects of the reactor will further encourage bubble formation (a.k.a nucleation) in the reactor. The water, now containing gas bubbles, will flow upward out of the reactor. Piping will direct the water downward into a basin containing a vent through which gas may exit the water. The water, no longer supersaturated, will then flow into the treatment plant. Figure 1 illustrates this general design.
<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Figure%201_%20GeneralUpdated.png?raw=true" height=450>
</p>


**Figure 1**: The above diagram depicts (not to scale) the general design of the system to remove excess dissolved gas from influent water, as the above paragraph describes.

The subteam currently considers two main options for the design of the reactor itself: a fluidized bed reactor, and a vertical plate reactor. As of yet, the subteam has focused its research on the fluidized bed reactor. While technical details are more thoroughly discussed in the Literature Review section, the main attributes of the two options are as follows.

A fluidized bed reactor [(Department of Chemical Engineering, 2017)](http://ww2.che.ufl.edu/unit-ops-lab/experiments/FB/FB-manual.pdf) consists of an enclosed reactor containing a suspension of particles, such as sand grains, in a fluid; they are kept in suspension by a particular flow rate directed upwards. This flow is that of the influent supersaturated water, entering the reactor from the bottom and flowing upwards toward an exit pipe. The suspended particles provide surfaces on which bubbles can form. The bubbles then rise from the reactor, leaving the sand particles behind. Figure 2 illustrates this design.
<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Figure%202_%20Fluidized%20Bed.png?raw=true" height=450>
</p>

**Figure 2**: The above diagram depicts (not to scale) the general concept of a fluidized bed reactor using sand particles, as the above paragraph describes.

A vertical plate reactor consists of an enclosed reactor containing a series of parallel, vertically aligned, textured plates. Supersaturated water enters the bottom of the reactor and flows upward along the plates to reach the exit pipe. The texturization of the plates provides sites for bubbles to form while the water flows. In theory, after reaching a specific critical diameter, these bubbles detach from the plates and flow upwards as effluent. Figure 3 illustrates this design.
<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Figure3_VerticalPlateReactor.png?raw=true" height=450>

</p>

**Figure 3**: The above diagram depicts (not to scale) the general concept of a vertical plate reactor as the above paragraph describes. The plates, depicted by brown lines, extend outward in the plane of the page.

The subteam considers that the vertical plate reactor design has the potential benefit of keeping bubbles stationary while they grow and accumulate. In the case of a fluidized bed reactor, bubbles may immediately travel upward once they form, since their formation site is mobile. They may depart the fluid at a smaller size, carrying a high internal pressure, and being likely to rupture and disperse into solution.

**Despite these benifits, the subteam believes the fluidized bed reactor may still be more effective, because a large number of sand grains may provide a greater surface area for bubbles to form than individual, vertical plates** The subteam intends to first design and fabricate a prototype fluidized bed reactor, and to evaluate its feasibility as a solution. The subteam will consider the vertical plate reactor at a later time in the semester and will weigh the merits of both designs.

**The remainder of this report will include further explanation of concepts such as fluidized beds, and considerations of pressure that will be treated as parameters for the reactor's design. The design for the first prototype reactor that the subteam plans to fabricate will be discussed in the Future Work section.**

## Literature Review

**{This introductory paragraph can be modified after polishing the Literature Review section} The subteam concentrated its research on two subjects in particular: the effect of ambient pressure on gas solubility, and bubble nucleation sites. Understanding these topics is necessary to understanding the subteam’s potential fluidized bed reactor.**

The subteam’s research is summarized as follows: gas solubility decreases with decreasing ambient pressure. Therefore, to catalyze bubble growth for ease of gas removal, the subteam aims to design a reactor exerting minimal pressure on gas molecules. Such pressures can be controlled by altering the reactor’s height. Pressure control, combined with providing nucleation sites in a fluidized bed reactor, will help the dissolved gas form stable bubbles that will escape from the water. The subteam hypothesizes that this will solve the problems that the plants at El PODA, Nicaragua and Tamara, Honduras are facing.

### Fluidized Beds & Bubble Nuclelation
**Add fluidization velocity discussion**

**When a liquid or a gas is pumped through a granular solid at a certain velocity, the granular solid behaves like a fluid. The minimum velocity required to cause this behavior is known as the minimum fluidization velocity. This value depends on numerous characteristics of the fluidized bed, including particle density, shape, size, and porosity. [(Department of Chemical Engineering, 2017)](http://ww2.che.ufl.edu/unit-ops-lab/experiments/FB/FB-manual.pdf) The relationship is quantified by the equation below [(Weber-Shirk)](https://courses.cit.cornell.edu/cee4540/pdf/Filtration.pdf).**

$$ V_{minfl}= \frac{\phi g D^2}{36kv(1-\phi)}(\frac{\rho_s}{\rho_w}-1) $$

**Equation 1**

$V_{minfl} =$ minimum approach velocity required to fluidize the sand bed
$\phi =$ porosity (0.4 for uniform size media) (Note: porosity and voidage are equal quantities)
$g =$ acceleration due to gravity
$D^2 =$ diameter of the sand grain, squared
$k =$ Kozeny constant, approximately equal to 5 for most filtration conditions
$\rho_w =$ density of water
$\rho_s =$ density of sand particles
$v =$ kinematic viscosity

**In the reactor the subteam plans to use, the subteam will be using sand as the granular solid and water as the fluid. Water has a known  density and kinematic viscosity, but the material properties of sand can vary. The subteam will determine these quantities later on.**

**Because of the reactor’s dependence on gas solubility and bubble formation, much of the subteam’s research was also directed toward bubble nucleation sites. The subteam found through research that the solid particles in the fluidized beds will provide nucleation sites for bubble formation.**

Typically, small, solid particles can provide a place for bubbles to grow large enough so they rise to the top of the reactor and escape. [(Boudreau et al., 2005)](https://pubs.geoscienceworld.org/gsa/geology/article/33/6/517/103815/bubble-growth-and-rise-in-soft-sediments) Boudreau found that bubbles that form in sand-like sediments are spherical, in contrast to the oblate spheroid-shaped bubbles that form in muddy sediments. His research suggests that the difference in shape is caused by the differences in responses to the stress of the materials; while mud fractures under stress, sand “acts fluidly or plastically in response to growth stresses.” This gives the subteam an idea of what type of materials to use in the reactor because the subteam needs the particles to have a fluid-like behavior.

Bubble formation and size in gas-solid fluidized beds is fairly predictable at low gas velocities [(Harrison and Leung, 1961)](https://www.nature.com/articles/190433a0). However, Schultz states that this is not the case for liquid-solid fluidized beds: “In most liquid-fluidized beds, … although instability is present and can be seen in the form of wavy structures this does not lead rapidly to bubble formation.” [(Schultz, 2004)](https://www.opuscula.agh.edu.pl/vol24/1/art/opuscula_math_2412.pdf). This could cause problems for the subteam, but luckily there are solutions to commonly reported issues.

If bubble formation is slow or inconsistent, it may be due to the ratio between the density of the particles and the density of water. Schultz found that bubble formation was present in fluidized beds with high ratios, so the subteam may want to consider using more dense particles if problems arise.

**The subteam aims to remove the most gas as possible; this corresponds to increasing the number of bubbles; this corresponds to decreasing gas solubility. According to Henry's Law, this is done by manipulating pressure**

### Controlling Pressure
The solubility of a gas in a solution changes proportionally to the partial pressure above said solution [(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html).

A formula that illustrates this relationship is Henry's Law, given below.

$$ C=k P $$
<p style="text-align: center;">
**Equation 2**
</p>

$C$ is the dissolved gas’s concentration at equilibrium, $P$ is the dissolved gas’s partial pressure at the interface of liquid and gas, and $k$ is the Henry’s Law constant, which is determined experimentally for each combination of gas, solvent, and temperature. In this case, the interface may be considered as the border between the bubble and the surrounding water.

This partial pressure can be minimized through control of two components.

The first of these components is the water pressure at the site of bubble formation. As the height difference between the fluidized bed and the vent changes, the water pressure changes, given by the following relation. **Insert source**

$$\Delta P = \rho g \Delta h$$
<p style="text-align: center;">
**Equation 3**
</p>

$\Delta P$ is the change in pressure, $\rho$ is the density of the material, $g$ is acceleration due to gravity, and $\Delta h$ is the change in depth.

**Second, a bubble’s pressure can be expressed as a function of its diameter [(Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/surten2.html). As pressure increases, bubble size decreases. However, once the pressure exceeds 3.5 atmospheres, the bubbles will stop decreasing in size [(Han, M., 2002)](https://doi.org/10.2166/ws.2002.0148). The relationship between pressure, surface tension, and bubble radius is given below:**

$$P_i = P_o + 4 \frac{T}{R}$$
<p style="text-align: center;">
**Equation 4**
</p>

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Surface_Tension_Bubble.png?raw=true" height=250>

</p>

**Figure 4**: The above diagram shows the descriptions of surface tension, pressure inside the bubble, and pressure outside the bubble for the given equation [(Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/surten2.html).

**The dissolved gas subteam plans on using the principles of this formula to even further decrease the pressure inside the bubble. Because it is known that an increase in radius will result in a decrease in pressure, the subteam must find a way to increase bubble radius.**

**One way to increase radius may be to prevent the bubbles in the reactor from quickly escaping; if bubbles stay inside the reactor for a longer period of time, it will have a longer time to expand.**

Another factor that influences the pressure difference between the reactor and the vent is that of *head loss*; head loss corresponds to energy lost due to friction, whichM in turn is reliant on material properties of the piping [(CodeCogs, 2012)](http://www.codecogs.com/library/engineering/fluid_mechanics/pipes/head_loss/pipe-head-loss.php). In this case, the piping will be the effluent tubing that exits the reactor and directs the water into the vent.

 $$ h_f = \frac{32\mu L V}{\rho g D^2} $$
<p style="text-align: center;">
**Equation 5**
</p>

In the Analysis section, the significance of this quantity will be discussed.

In the following weeks, the subteam plans to test the effectiveness of a fluidized bed reactor in removing excess dissolved gas.

In the following section, the above equations are related to one another to form one basis for parameters of the system design.

## Analysis
Based upon the literature gathered and reviewed above, through analysis and algebraic manipulation, Equations 2, 3, 4, and 5 combine to form an estimation of a gas’ solubility in an apparatus as described. One should note that, because all of the equations assume a system in equilibrium, the equation that will be presented will serve only as an approximation for the solubility of a gas in the reactor; the system may not be in equilibrium when the reactor is in use.

The pressure within a bubble is directly related to the pressure outside the bubble, plus a quotient determined by the liquid’s surface tension and the bubble’s radius [(Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/surten2.html).

The subteam considers that the pressure outside of the bubble, the pressure within the liquid, may be equated to atmospheric pressure plus a change in pressure due to the height difference between the reactor and the vent, as seen in Figure 1. This equivalent to the pressure difference as observed in Pascal’s Law, Equation 3.

The subteam considers that the pressure relevant to Henry's Law, the pressure of a gas above a liquid, is the pressure within the bubble; the lower the pressure within the bubble, the lower the solubility of the gas in the surrounding water [(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html).

The pressure within the reactor is further influenced by the pressure difference due to head loss.

The equations relating these quantities (height of reactor; bubble radius; head loss; gas solubility)  may be combined to form one cohesive relationship. This equation gives the solubility of the gas in solution as a function of a bubble's radius, the height of the reactor, surface tension, dimensions of the effluent tubing, and the constant relevant to Henry's Law.

This theory may act as an approximation of the pressure within the bubbles. These equations assume equilibrium: that the rates of air shifting from liquid to gas phase and vice versa are equal. This may not be the case in the entirety of the reactor.
The following is the actualization of this concept. The meaning of all variables has been previously defined.

$$ C=k P $$
<p style="text-align: center;">
**Equation 2**
</p>

In equation 2, P approximates the gas pressure within a bubble; the subteam considers the bubble-water border as an interface between a liquid and a gas, as considered by Henry's Law. Therefore, P will be denoted as $P_b$ (i.e. pressure in a bubble).

$$\Delta P = \rho g \Delta h$$
<p style="text-align: center;">
**Equation 3**
</p>

From this equation one can extrapolate that $ \Delta P = \rho g \Delta h $, given that the liquid’s density and that acceleration due to gravity remain constant. In this equation, the difference in pressure is that between atmospheric pressure (the pressure at the open-faced vent, downstream from the reactor) and the pressure within the reactor itself. Therefore, if $\Delta P$ is expanded to $P_r - P_{atm}$ (i.e. pressure in the reactor minus atmospheric pressure), this equation may be modified into $P_r = P_{atm} + \rho g \Delta h $.

$$ h_f = \frac{32\mu L V}{\rho g D^2} $$
<p style="text-align: center;">
**Equation 5**
</p>

Pressure difference due to head loss must also be taken into account, in terms of the pressure difference between the open-faced vent and the reactor itself. Combined with the previous equation, the relationship becomes: $P_r = P_{atm} - \rho g \Delta h + \rho g h_f $. The reasoning for the negative sign prior to the second term is as follows: the reactor is higher than the vent; therefore, $\Delta h$ is technically a positive quantity. However, pressure decreases as depth decreases. The negative sign's purpose is to indicate this relationship mathematically.

$$P_i = P_o + 4 \frac{T}{R}$$
<p style="text-align: center;">
**Equation 4**
</p>

In this equation, $P_i$ denotes the pressure within a bubble, and may be relabeled as $P_b$. $P_o$ denotes the pressure outside of the bubble, which may be denoted $P_r$ given the above reasoning.

When all of these equations are combined, the following relationship appears:

$$C = k(\frac{4T}{R} + P_{atm} - \rho g \Delta h + \rho g h_f)$$
<p style="text-align: center;">
**Equation 6**
</p>

**Variables**
$C$ = solubility of a gas in a given fluid
$k$ = a constant for a given substance at a given temperature; related to Henry’s Law
$T$ = the surface tension of the liquid at a given temperature
$R$ = the radius of a bubble in the reactor
$P_{atm}$= the air pressure, most likely atmospheric, at the level of the vent
$⍴$ = the density of water
$g$ = acceleration due to gravity
$\Delta h$ = the height difference between the vent and the reactor (this is a negative quantity)
$h_f$ = the head loss in the outlet tubing, due to the outlet tubing dimensions and water’s material properties

Due to the above reasoning concerning assumption of equilibrium, the above equation is a qualitative description of the relationships between different system parameters, rather than a quantitative relationship.

This overall equation supports the subteam's theory, and directs it, toward our optimization of our system design: to minimize gas solubility in water, we must maximize the size of bubbles that form; maximize, within reason, the height between the reactor and vent; and minimize the pressure difference due to head loss. In the future, exact calculations and optimizations will be made with these parameters in mind, as well as the limiting factor of Equation 1, the velocity of water required to use a fluidized bed in the first place.

This equation, supplemented by Equations 1 and 3, will inform the subteam's fabrication of the prototype system.

## Future Work
**Insert description & Figure concerning the prototype reactor**


## Bibliography
Averill, B., & Eldredge, P. (n.d.). *Principles of General Chemistry* (Vol. 1). Creative Commons. Retrieved from https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html

Boudreau, B. P., Algar, C., Johnson, B. D., Croudace, I., Reed, A., Furukawa, Y., … Gardiner, Bruce S. (2005, June 5). *Bubble growth and rise in soft sediments.* Retrieved September 17, 2018, from https://pubs.geoscienceworld.org/gsa/geology/article/33/6/517/103815/bubble-growth-and-rise-in-soft-sediments

CodeCogs.(2012, February 24). Pipe Head Loss. Retrieved from http://www.codecogs.com/library/engineering/fluid_mechanics/pipes/head_loss/pipe-head-loss.php

Department of Chemical Engineering. (2017, February). *Fluidization: A Unit Operation in Chemical Engineering.* Gainesville, FL: University of Florida. Retrieved from http://ww2.che.ufl.edu/unit-ops-lab/experiments/FB/FB-manual.pdf.

Han, M., Park, Y., Lee, J., & Shim, J. (2002). *Effect of pressure on bubble size in dissolved air flotation.* Water Science and Technology: Water Supply, 2(5–6), 41–46. https://doi.org/10.2166/ws.2002.0148

Harrison, D., & Leung, L. S. (1961, April 29). *Bubble Formation at an Orifice in a Fluidized Bed | Nature*. Retrieved September 20, 2018, from https://www.nature.com/articles/190433a0

Hyperphysics. (n.d.). *Surface Tension and Bubbles.* Retrieved from http://hyperphysics.phy-astr.gsu.edu/hbase/surten2.html

Mori, S., & Wen, C. Y. (1975). *Estimation of bubble diameter in gaseous fluidized beds.* AIChE Journal, 21(1), 109–115. https://doi.org/10.1002/aic.690210114

Scardina, P... (2004). *Effects of Dissolved Gas Supersaturation and Bubble Formation on Water Treatment Plant Performance* (Unpublished doctoral dissertation). Virginia Polytechnic Institute and State University. Blacksburg, Virginia. https://vtechworks.lib.vt.edu/bitstream/handle/10919/26497/PaoloScardinaDissertation2004.pdf?sequence=1

Schulz, P. (2004). *Instability and the formation of bubbles and the plugs in fluidized beds*, 24(1), 27. Retrieved from https://www.opuscula.agh.edu.pl/vol24/1/art/opuscula_math_2412.pdf

Weber-Shirk, M. *Filtration Theory: On removing little particles with big particles* [PowerPoint Slides]. Retrieved from https://courses.cit.cornell.edu/cee4540/pdf/Filtration.pdf.
