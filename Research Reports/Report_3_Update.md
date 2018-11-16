# Dissolved Gas, Fall 2018 Subteam

### Thomas Bradford, Karalyn Buhl, Isaac Singer

### 16 November, 2018

## Abstract
Excess dissolved air in a water treatment plant’s influent water decreases the functionality of the treatment plant's filters and sedimentation tanks. The Dissolved Gas subteam begins its first semester with the goal to design a gravity-powered apparatus that extracts this gas from influent water prior to entry into the treatment plant through the use of a fluidized bed. The subteam will gather literature, develop designs, fabricate a small-scale prototype, and iterate improvements based on experimental data to work towards a model that may be scaled up for application in an AguaClara plant.

## Table of Contents

- [Introduction](#Introduction)
- [Literature Review](#Literature-Review)
  - [Fluidized Beds and Bubble Formation](#Fluidized-Beds-&-Bubble-Nucleation)
  - [Controlling Pressure](#Controlling-Pressure)
  - [Analysis of Literature](#Analysis-of-Literature)
- [Methods](#Methods)
  - [Determining Reactor Parameters](#Determining-Reactor-Parameters)
  - [Fabrication Details](#Fabrication-Details)
- [Future Work](#Future-Work)
- [Bibliography](#Bibliography)
- [Manual](#Manual)
  - [Experimental Methods](#Experimental-Methods)
  - [Fabrication Details](#Fabrication-Manual)
  - [Python Code](#Python-Code)

## Introduction
Excess dissolved gas in influent water in AguaClara plants at Tamara, Honduras and EL PODA, Nicaragua has significantly reduced the plants' efficiencies. To clarify: “excess dissolved gas” does not entail *bubbles* being present in influent water. The influent water is *supersaturated* with gas: gas molecules are dispersed throughout the water, not congregated in bubbles.

Due to the presence of this excess gas, bubbles form in the plants' sedimentation tanks. These bubbles stick to flocs and rise, causing materials that should settle to float and to continue into the remainder of the plant. Bubbles also form in the plants' sand filters between sand particles, effectively clogging the filters [(Scardina, 2004)](https://vtechworks.lib.vt.edu/bitstream/handle/10919/26497/PaoloScardinaDissertation2004.pdf?sequence=1). To remedy these issues, the Dissolved Gas subteam intends to design a reactor that removes such dissolved gas from influent water prior to entering the plant.

For the sake of efficiency, the term “supersaturated water” will be used in this report to denote water containing excess dissolved gas, whether air or otherwise.

The basic concept of the system design is as follows. Influent water will flow from its source at a high elevation. Once the influent water is near to the AguaClara plant, piping will direct it upwards into a reactor. Atmospheric pressure decreases as elevation increases [(Hodanbosi)](https://www.grc.nasa.gov/www/k-12/WindTunnel/Activities/fluid_pressure.html). According to Henry’s Law, gas becomes less soluble at lower pressures, making bubble formation more likely [(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html). Aspects of the reactor will further encourage bubble formation (i.e. nucleation) in the reactor. The water, then containing gas bubbles, will flow upward and out of the reactor. Piping will direct the water downward into a basin containing a vent through which gas may exit the water. The water, no longer supersaturated, will then flow into the treatment plant. Figure 1 illustrates this general design.
<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Figure%201_%20GeneralUpdated.png?raw=true" height=450>
</p>


**Figure 1**: The above diagram depicts (not to scale) the general design of the system to remove excess dissolved gas from influent water, as the above paragraph describes.

At the start of the semester, the subteam considered two options for the design of the reactor: a fluidized bed reactor, and a vertical plate reactor. So far, the subteam has focused its research on the fluidized bed reactor. While technical details are more thoroughly discussed in the Literature Review section, the main attributes of the two options are as follows.

A fluidized bed reactor consists of an enclosed reactor containing a suspension of particles, such as sand grains, in a fluid; they are kept in suspension by a particular flow rate directed upwards [(Department of Chemical Engineering, 2017)](http://ww2.che.ufl.edu/unit-ops-lab/experiments/FB/FB-manual.pdf). This flow is that of the influent water, entering the reactor from the bottom and flowing upwards toward an exit pipe. The suspended particles provide surfaces on which bubbles can form. The bubbles then rise from the reactor, leaving the sand particles behind. Figure 2 illustrates this design.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Fluidized_Bed_Reactor.jpg?raw=true" height=450>
</p>

**Figure 2**: The above diagram depicts (not to scale) the general concept of a fluidized bed reactor using sand particles, as the above paragraph describes.

A vertical plate reactor consists of an enclosed reactor containing a series of parallel, vertically aligned, textured plates. Supersaturated water enters the bottom of the reactor and flows upward along the plates to reach the exit pipe. The texturization of the plates provides sites for bubbles to form (i.e. nucleation sites) while the water flows. In theory, after reaching a specific critical diameter, these bubbles detach from the plates and flow upwards as effluent. In the future, the subteam may investigate the mechanisms of bubble growth and detachment in the vertical plate reactor. Figure 3 illustrates this design.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Figure3_VerticalPlateReactor.png?raw=true" height=450>

</p>

**Figure 3**: The above diagram depicts (not to scale) the general concept of a vertical plate reactor, as the above paragraph describes. The plates, depicted by brown lines, extend outward from the plane of the page.

The subteam considered that the vertical plate reactor design has the potential benefit of keeping bubbles stationary while they grow and accumulate. In a fluidized bed reactor, bubbles may immediately travel upward once they form, since their nucleation sites (sand grains) are mobile. Bubbles may depart the fluid at a smaller size, carrying a high internal pressure, being likely to rupture and disperse into solution.

Despite these potential issues, the subteam believes the fluidized bed reactor may still be more effective, because a large number of sand grains may provide a greater surface area for bubbles to form than individual, vertical plates. The subteam will consider the vertical plate reactor at a later time in the semester and will weigh the merit of each design.

The subteam has recently fabricated a prototype fluidized bed reactor using a transparent PVC pipe, silica sand, and basic flow components; the subteam has assembled a basic apparatus to resemble the design proposed in Figure 1. Photographs of this apparatus are shown in Figure 4; influent water passes in through a peristaltic pump and through tubing into a vertically oriented fluidized bed reactor, and out into a small bucket. Further details on this apparatus are given in the Methods and Manual sections of the report.
<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype_1/Prototype1_Photograph.jpg?raw=true" height = 520>

<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype_1/Prototype1_PhotoDiagram.jpg?raw=true" height = 520>

</p>

**Figure 4**: The left-hand photograph is of the first prototype apparatus; the right-hand photograph contains graphical enhancement to clarify the system's progression. Influent water (purple arrow) enters the system through the peristaltic pump (orange rectangle), flows up into the fluidized bed reactor (green rectangle), exits the as effluent water (red arrow), and pours into a small bucket (yellow rectangle) that serves as an open-faced vent.

The remainder of this report will include further explanation of concepts such as fluidized beds, considerations of pressure that informed parameters of the reactor's design, and details concerning the apparatus' fabrication. The experimental process the subteam hopes to pursue to evaluate the reactor's feasibility as a solution is discussed in the Future Work section.

## Literature Review

The subteam concentrated its research on optimizing the fluidized bed reactor and manipulating pressure to ensure maximum dissolved gas removal. The subteam’s research can be summarized as follows: gas solubility decreases with decreasing ambient pressure. Therefore, to catalyze bubble growth in a reactor for ease of gas removal, the subteam aims to design a reactor exerting minimal pressure on gas molecules. Such pressure can be controlled by altering the reactor’s height, by influencing bubble size, and by modifying dimensions of the tubing in the system. Pressure control, combined with providing nucleation sites in a fluidized bed reactor, will help the dissolved gas form stable bubbles that will escape from the water. The subteam hypothesizes that this will alleviate the problems that the plants at El PODA, Nicaragua and Tamara, Honduras are facing.

### Fluidized Beds & Bubble Nucleation

When a liquid or a gas is pumped through a granular solid at a certain velocity, the granular solid behaves like a fluid. The minimum velocity required to cause this behavior is known as the minimum fluidization velocity. This value depends on numerous characteristics of the fluidized bed, including particle density, shape, size, and porosity [(Department of Chemical Engineering, 2017)](http://ww2.che.ufl.edu/unit-ops-lab/experiments/FB/FB-manual.pdf). The relationship is quantified by the equation below [(Weber-Shirk)](https://courses.cit.cornell.edu/cee4540/pdf/Filtration.pdf).

#### Equation 1

$$ V_{minfl}= \frac{\phi^3 g D^2}{36kv(1-\phi)}(\frac{\rho_s}{\rho_w}-1) $$

**Variables**
$V_{minfl}$ = Minimum approach velocity required to fluidize the sand bed
$\phi$ = Porosity (Approximately 0.4 for uniform size media) (Note: porosity and voidage are equal quantities)
$g$ = Acceleration due to gravity
$D$ = Diameter of a sand grain
$k$ = Kozeny constant (approximately equal to 5 for most filtration conditions)
$v$ = Kinematic viscosity of water
$\rho_s$ = Density of sand particles
$\rho_w$ = Density of water

In the reactor the subteam plans to use, sand will serve as the granular solid and water as the fluid. Water has a known density and kinematic viscosity, but the material properties of sand may vary. The subteam will determine these quantities in the near future.

Because of the reactor’s dependence on bubble formation, much of the subteam’s research was also directed toward bubble nucleation sites. The subteam found through research that the solid particles in the fluidized beds will provide nucleation sites for bubble formation.

Typically, small, solid particles can provide a place for bubbles to grow large enough so they rise to the top of the reactor and escape [(Boudreau et al., 2005)](https://pubs.geoscienceworld.org/gsa/geology/article/33/6/517/103815/bubble-growth-and-rise-in-soft-sediments). Boudreau found that bubbles that form in sand-like sediments are spherical, in contrast to the oblate spheroid-shaped bubbles that form in muddy sediments. His research suggests that the difference in shape is caused by the differences in responses to the stress of the materials; while mud fractures under stress, sand “acts fluidly or plastically in response to growth stresses.” This gives the subteam an idea of what type of materials to use in the reactor because the subteam needs the particles to have a fluid-like behavior.

Bubble formation and size in gas-solid fluidized beds is fairly predictable at low gas velocities [(Harrison and Leung, 1961)](https://www.nature.com/articles/190433a0). However, Schulz states that this is not the case for liquid-solid fluidized beds: “In most liquid-fluidized beds, … although instability is present and can be seen in the form of wavy structures this does not lead rapidly to bubble formation.” [(Schulz, 2004)](https://www.opuscula.agh.edu.pl/vol24/1/art/opuscula_math_2412.pdf). This instability could cause problems for the subteam, but luckily there are solutions to commonly reported issues.

If bubble formation is slow or inconsistent, it may be due to the ratio between the density of the particles and the density of water. Schulz found that bubble formation was present in fluidized beds with high ratios, so the subteam may want to consider using denser particles if problems arise.

The subteam aims to remove the most gas from the influent water as possible by creating bubbles. As previously stated, bubbles can be created by providing nucleation sites on sand grains, and it can also be done by decreasing gas solubility.

### Controlling Pressure
The solubility of a gas in a solution is directly proportional to its partial pressure above said solution. It is also dependent on a particular constant, determined by the composition of the gas and the solution, and the temperature of both.  [(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html).

A formula that illustrates this relationship is Henry's Law, given below.

#### Equation 2

$$ C=k P $$

**Variables**
$C$ = Dissolved gas’s concentration at equilibrium
$k$ = Henry’s Law constant, which is determined experimentally for each combination of gas, solvent, and temperature. In this case, the interface may be considered as the border between the bubble and the surrounding water.
$P$ = Dissolved gas’s partial pressure at the interface of liquid and gas

Therefore, in order to decrease gas's solubility inside of the reactor, the subteam must find a way to decrease the pressure. This  pressure can be minimized through control of two components.

The first of these components is the water pressure at the site of bubble formation. As the height difference between the fluidized bed and the vent changes, the water pressure changes, given by the following relation [(Hodanbosi)](https://www.grc.nasa.gov/www/k-12/WindTunnel/Activities/fluid_pressure.html).

#### Equation 3

$$\Delta P = \rho g \Delta h$$

**Variables**
$\Delta P$ = Change in pressure
$\rho$ = Density of the material
$g$ = Acceleration due to gravity
$\Delta h$ = Change in depth

Because water pressure decreases in shallower depths, building a reactor at a certain height will minimize pressure, and as a result, minimize gas solubility.

Another factor that influences the pressure difference between the reactor and the vent is that of *head loss*; head loss corresponds to energy lost due to friction, which in turn depends on material properties of the piping [(CodeCogs, 2012)](http://www.codecogs.com/library/engineering/fluid_mechanics/pipes/head_loss/pipe-head-loss.php). In this case, the relevant piping is the effluent pipe through which water exits the reactor and passes into the vent. Head loss is dependent on tubing parameters according to the following equation [(Weber-Shirk)](https://courses.cit.cornell.edu/cee4540/pdf/Flow%20Control%20and%20Measurement.pdf).

#### Equation 4

 $$ h_f = \frac{32\mu L V}{\rho g D^2} $$

**Variables**
$h_f$ = Head loss
$\mu$ = Kinematic viscosity of water
$L$ = Length of the pipe in question
$g$ = Acceleration due to gravity
$\rho$ = Density of water
$D$ =Diameter of the pipe in question
$V$ = Velocity of water in the pipe

Building off [Equation 4](#Equation-4), the pressure difference between two ends of a pipe due to head loss is given by the following equation [(Brown, 2000)](https://bae.okstate.edu/faculty-sites/Darcy/DarcyWeisbach/Darcy-WeisbachEq.htm).

#### Equation 5

$$\Delta P =  \rho  g h_f$$

**Variables**
$h_f$ = Head loss in a pipe, as given in [Equation 4](#Equation-4)
$\rho$ = Density of water
$\Delta P$ = Change in pressure across the pipe
$g$ = Acceleration due to gravity

Second, a bubble’s pressure can be expressed as a function of its diameter [(Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/surten2.html). As pressure increases, bubble size decreases. However, once the pressure exceeds 3.5 atmospheres, the bubbles will stop decreasing in size [(Han, M., 2002)](https://doi.org/10.2166/ws.2002.0148). The relationship between pressure, surface tension, and bubble radius is shown by the following equation:

#### Equation 6

$$P_i = P_o + 4 \frac{T}{R}$$

**Variables**
$P_i$ = Pressure inside the bubble
$P_o$ = Pressure outside the bubble
$T$ = Surface tension
$R$ = Bubble radius

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Bubble_Surface_Tension.jpg?raw=true" height=350>

</p>

**Figure 5**: This diagram shows the descriptions of surface tension, pressure inside the bubble, and pressure outside the bubble for the given equation [(Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/surten2.html).

The dissolved gas subteam plans on using the principles of this formula to even further decrease the pressure inside the bubble. Because it is known that an increase in radius will result in a decrease in pressure, the subteam must find a way to increase bubble radius.

One way to increase radius may be to prevent the bubbles in the reactor from quickly escaping; if bubbles stay inside the reactor for a longer period of time, it will have a longer time to expand.

In the Analysis section, Equations 2-6 are evaluated and related to one another to form one basis for parameters of the system design. In the following weeks, the subteam plans to fabricate and test the effectiveness of a fluidized bed reactor whose parameters are informed by this basis.

### Analysis of Literature
Through conceptual analysis and algebraic manipulation, Equations 2-6 combine to form an estimation of a gas’ solubility in water in an apparatus as illustrated in Figure 1. The following paragraphs walk through this process; all variables have been defined in the Literature Review section.

The pressure relevant to Henry's Law (i.e. the pressure of a gas above a liquid, in [Equation 2](#Equation-2)) is the pressure *within* a bubble [(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html).
$$ C = k P $$

$P$ equates to the gas pressure within a bubble. Therefore, $P$ is relabeled as  $P_b$ (i.e. pressure in a bubble).

As shown in [Equation 6](#Equation-6), the pressure within a bubble is directly related to the bubble's radius, the liquid's surface tension, and the pressure outside the bubble [(Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/surten2.html).

$$P_i = P_o + 4 \frac{T}{R}$$

$P_i$ denotes the pressure within a bubble, and therefore is relabeled as $P_b$. $P_o$ denotes the pressure outside of the bubble, and is relabeled $P_r$.

The pressure outside of the bubble (i.e. the pressure within the liquid) can be equated to atmospheric pressure plus a change in pressure due to the height difference between the reactor and the vent ([Equation 3](#Equation-3)), plus a change in pressure due to head loss in the tubing connecting the reactor and the vent ([Equation 5](#Equation-5)).

$$\Delta P = \rho g \Delta h$$

In [Equation 3](#Equation-3), the difference in pressure is that between atmospheric pressure (i.e. the pressure at the vent) and the pressure within the reactor itself. Therefore, if $\Delta P$ is expanded to $P_r - P_{atm}$ (i.e. pressure in the reactor minus atmospheric pressure), this equation may be rearranged into:

####Equation 3.1

$$P_r = P_{atm} - \rho g \Delta h $$

The final term of this equation was negated to indicate that, while $\Delta h$ increases in magnitude, the pressure in the reactor decreases.

Pressure difference due to head loss must also be taken into account, since it contributes to the pressure difference between the vent and the reactor.

$$\Delta P =  \rho  g h_f$$

Similarly to [Equation 3](#Equation-3), the difference in pressure can be expanded to $P_r - P_{atm}$.

These four equations may be combined and rearranged given their relabeled variables. The following relationship emerges to relate the solubility of the gas in the reactor to a bubble's radius, the height of the reactor, the water's surface tension, the dimensions of the effluent tubing, and the constant relevant to Henry's Law:

#### Equation 7

$$C = k(\frac{4T}{R} + P_{atm} - \rho g \Delta h + \rho g h_f)$$

**Variables**
$C$ = Solubility of a gas in the water
$k$ = A constant for a given substance at a given temperature; related to Henry’s Law
$T$ = Surface tension of the water at a given temperature
$R$ = Radius of a bubble in the reactor
$P_{atm}$= Atmospheric air pressure at the level of the vent
$⍴$ = Density of water
$g$ = Acceleration due to gravity
$\Delta h$ = Height difference between the vent and the reactor (this is a negative quantity)
$h_f$ = Head loss in the outlet tubing, as given in [Equation 4](#Equation-4)

[Equation 7](#Equation-7) mathematically summarizes the concepts addressed in the Literature Review section. In order to minimize gas solubility (and therefore, to maximize the amount of gas that is removed from influent water): the radii of bubbles that form must be maximized, the head loss in the exit tubing must be minimized, and the height difference between the reactor and vent must be maximized, within reason. Further considerations may arise when [Equation 4](#Equation-4) is substituted for the $h_f$ value.

While [Equation 7](#Equation-7) is powerful in its efficiency, it may only act as an approximation of the solubility of a gas in the fluidized bed reactor. Equations 2-6 assume equilibrium: that the rates of air shifting from liquid to gas phase and vice versa are equal. The system may not be in equilibrium while the reactor is in use. Therefore, [Equation 7](#Equation-7) remains only a qualitative description of the relationships between different system parameters.

In the near future, the subteam will perform exact calculations and optimizations with these parameters in mind. [Equation 7](#Equation-7), supplemented by [Equation 1](#Equation-1) concerning fluidization velocity, will be instrumental in informing the subteam's fabrication of the prototype apparatus.

## Methods

Although the subteam has not yet begun experimentation, the methods of determining the reactor parameters and fabrication details are described in this section.

### Determining Reactor Parameters

The prototype design aligns with that illustrated in Figure 6. Exact parameters can be found in the Fabrication Details section.

The prototype system’s design is as follows: a peristaltic pump will pump hot water (as hot water is supersaturated with gas) into a tube system and through the fluidized bed reactor. The reactor, a transparent PVC pipe, contains a sand bed. This will be fluidized by the influent water, which will be traveling at no slower than the sand’s fluidization velocity. Ideally, as the supersaturated water travels through the reactor, excess gas particles in the water will accumulate on the sand grains and form bubbles. Such bubbles will then depart from their sand grains and flow upward, out of the reactor, through the effluent tubing and into a bucket. This bucket will act as the open-faced vent (as in Figure 1) for the air bubbles to escape into the atmosphere.

One should note that a mesh is installed at the bottom of the reactor to prevent any sand from falling down/out of the reactor.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype_Diagram.jpg?raw=true" height=450>

</p>

**Figure 6**: The above diagram depicts (not to scale) the prototype the subteam has built to test the hypothesis regarding the use of a fluidized bed reactor to encourage bubble formation.

The prototype model was built with intentions to minimize head loss, and maximize the difference in depth between the reactor and the bucket. These parameters are illustrated in [Equation 7](#Equation-7), with the purpose of minimizing gas' solubility and therefore maximizing bubble formation within the reactor.

#### Determining Porosity of Sand
In order to fabricate a viable prototype, the Dissolved Gas subteam needed to determine the appropriate fluidization velocity to suspend the sand in the reactor.

The fluidization velocity of the sand is dependent on the sand's density, the kinematic viscosity of water, the reactor's cross sectional area, the height of the sand bed, and the porosity of the sand bed, as stated in [Equation 1](#Equation-1).

To determine porosity, the following steps were taken, adapted from the work of [Ms. Worth](https://socratic.org/questions/how-do-scientists-measure-the-porosity-of-soil).

First, the subteam acquired silica sand from the AguaClara laboratory. Then, the subteam measured the volume of the sand ($V_{sample}$) in a graduated cylinder. In a second graduated cylinder, the subteam measured an excess volume of water. Then, water from the graduated cylinder was poured over the sand  until the top of the meniscus was level with the sand bed. Next, the volume of water added to the sand ($V_{pore}$) was determined by subtracting the final volume from the initial volume of water in the graduated cylinder. The porosity of the sand bed was then calculated using the following formula:

#### Equation 8

$$\phi = \frac{V_{pore}}{V_{sample}}$$

**Variables**
$\phi$ = Porosity
$V_{pore}$ = Volume of water used to saturate sand
$V_{sample}$ = Volume of sand

This is equivalent to the formula given by [University of Florida Dept of Chemical Engineering](http://ww2.che.ufl.edu/unit-ops-lab/experiments/FB/FB-manual.pdf).

| Trial number | Measured volume of sand (mL) $(V_{sample})$ | Volume of water in cylinder (mL) |Volume of water remaining in cylinder after saturating sand (mL) | Pore Volume (mL) $(V_{pore})$| Calculated Porosity  ($\phi$) |
|:-:|:--:|:---:|:---:|:--:|:----:|
| 1 | 40 | 150 | 136 | 14 | 0.35 |
| 2 | 40 | 150 | 136 | 14 | 0.35 |
| 3 | 40 | 150 | 136 | 14 | 0.35 |
**Table 1**: This table shows the data collected by the subteam to calculate the porosity of the sand bed.

The average calculated porosity of the silica sand was 0.35, with a standard deviation of 0.0%. These statistics were calculated using StandardDeviation.py, code given in the Manual.

This has a percent difference of 0% compared to [Weber-Shirk](https://courses.cit.cornell.edu/cee4540/pdf/Filtration.pdf)'s suggested value of 0.4 (when the calculated value is rounded to one significant figure).

#### Determining Sand Grain Dimensions
Fluidization velocity of a sand bed is also dependent on sand grain diameter. Although the sand used for the subteam's reactor was already sieved, there were some minor variations that were not yet taken into account.

In order to determine the average size of the sand grains, ten random grains were measured 3 times by subteam members using a caliper. The ten sand grains were taken as a representative sample of the sand used in the reactor. The data is shown in the following table:

| Sand grain | Measurement 1 (mm)| Measurement 2 (mm) | Measurement 3 (mm)|
|:-:|:----:|:----:|:----:|
| 1 | 0.69 | 0.84 | 1.08 |
| 2 | 1.33 | 0.85 | 1.31 |
| 3 | 1.13 | 1.32 | 0.90 |
| 4 | 1.20 | 1.17 | 0.86 |
| 5 | 0.98 | 0.79 | 0.77 |
| 6 | 0.71 | 0.73 | 0.72 |
| 7 | 1.00 | 0.78 | 0.82 |
| 8 | 0.76 | 0.92 | 0.70 |
| 9 | 0.69 | 0.70 | 0.76 |
|10 | 0.91 | 0.74 | 1.10 |
**Table 2**: This table shows the sand dimensions measured by each subteam member.

The average measured diameter of the sand grains was 0.91mm, with a standard deviation of 0.21mm. This was calculated using the StandardDeviation.py code given in the Manual.

#### Determining the reactor's cross sectional area
The subteam acquired a clear PVC pipe of approximate 1 inch diameter.

After marking the pipe at approximately 50 cm in length with a permanent marker (the length was measured using measuring tape), the pipe was cut at that mark using a Sawzawll reciprocating saw. To maintain the correct orientation of the pipe, the subteam labeled the pipe with colored tape, with white tape denoting the bottom end (where the influent water will travel into the reactor) and red tape denoting the top (where the effluent water will leave the reactor).

The measured dimensions of the cut pipe are given  below. Measurements were taken using a caliper, in units of millimeters. Measurements were taken at both ends of the pipe: influent (marked with white) and effluent (red). The pipe's "inner diameter" was calculated by subtracting twice the thickness of the pipe's wall from the pipe's outer diameter.

This pipe was used as the main component of the prototype reactor.

##### Influent side
| Measurement | Thickness of Pipe Wall| Outer Diameter | Calculated Inner Diameter | Calculated Inner Cross Sectional Area (mm$^2$) |
|:-------:|:----:|:-----:|:-----:|:-----:|
|    1    | 4.35 | 33.54 | 24.84 | 484.6 |
|    2    | 4.39 | 33.36 | 24.58 | 474.5 |
|    3    | 4.40 | 33.46 | 24.66 | 477.6 |
| Average | 4.38 | 33.45 | 24.69 | 478.9 |
**Table 3**: This table shows the measured diameters of the influent side of the pipe. The table also shows the cross sectional area as well as average values.

##### Effluent side
| Measurement | Thickness of Pipe Wall | Outer Diameter | Calculated Inner Diameter | Calculated Inner Cross Sectional Area (mm$^2$) |
|:-------:|:----:|:-----:|:-----:|:-----:|
|    1    | 4.26 | 33.66 | 25.14 | 496.4 |
|    2    | 4.67 | 33.44 | 24.10 | 456.2 |
|    3    | 4.20 | 33.41 | 25.01 | 491.3 |
| Average | 4.38 | 33.5  | 24.75 | 481.3 |
**Table 4**: This table shows the average values of various dimensions of the pipe, the focus being the pipe's cross-sectional area.

The percent difference between the calculated, inner, cross-sectional area of the pipe at either end is 0.500%. The overall average cross-sectional area of the pipe is 481.1mm$^2$, with a standard deviation of 1.697mm$^2$.

### Fabrication Details

The clear PVC pipe, cut to 0.5m as described in the prior section, is labeled with the following bands of tape to denote certain properties.
1. Orange: subteam name, member names and NetIDs
2. Red: top / effluent end of the pipe
3. White: bottom / influent end of the pipe
4. Pink: prototype number

A watertight flow connector, shown in Figure 7, were attached to either side of the PVC pipe to connect the influent and effluent tubing to the reactor.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype_1/PipeConnector1.jpg?raw=true" height=250>

**Figure 7**: The above flow connector enables the reactor (pipe) to be connected to clear flex tubing.

A fine, wire mesh was cut into a circle of approximately the same cross sectional area as the pipe and was placed at the bottom of the PVC pipe to prevent any sand from falling out of the reactor.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype_1/Mesh_1.jpg?raw=true" height=250>

<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype_1/MeshInConnector1.jpg?raw=true" height=250>

</p>

**Figure 8**: The image on the left shows the mesh that is cut to the approzimate size of the pipe diameter. On the right, the image shows the mesh placed at the bottom of the reactor.

</p>

The following image shows the labeled reactor, capped at either end with the connectors shown in Figure 7.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype_1/Prototype1_Sand.jpg?raw=true" height=450>

</p>

**Figure 9**: The photograph above is of the Prototype 1 reactor labeled with team members' names and with the appropriate influent (white) and effluent (red) tape labels. The Prototype 1 reactor contains a silica sand bed (indicated with a green circle in the figure), measured with a graduated cylinder.

The subteam filled the Prototype 1 with 70 mL of silica sand, measured with a graduated cylinder. The 70 mL volume was decided so that when the sand bed fluidized, it would not expand to be larger than the reactor. Dividing that volume of sand by the reactor's cross sectional area, which had been calculated to be 4.811 cm$^2$ (shown in our reactor measurements file), resulting in the height of the unfluidized sand bed being approximately 15 cm.

The subteam mounted the reactor above a lab bench, fastening it to a vertically oriented metal arm with three metal hose clamps. The 80/20 arm was previously fabricated by the [Filter Constrictions subteam](https://raw.githubusercontent.com/AguaClara/filter-constrictions/master/Reports_Tutorials/FinalReport.md), and more information can be found in the subteam's final report. The subteam placed a bucket on the table to catch effluent water. Figure 4 shows the

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype_1/Prototype1_Photograph.jpg?raw=true" height=450>

<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype_1/Prototype1_PhotoDiagram.jpg?raw=true" height = 450>

</p>

**Figure 4**

The subteam used 3/8 inch diameter clear flex tubing to carry water from the sink to the peristaltic pump, 1/8" Masterflex tubing (06508-16) to fit in the peristaltic pump, and 3/16 inch diameter clear flex tubing for the influent and effluent tubing for the reactor. In order to prevent the effluent tubing from reaching its maximum bend radius, the tubing is taped to a nearby light fixture.

All tubes were connected to each other using push-to-connect components and barbed fittings to ensure water tightness.

## Future Work

The subteam now has a prototype system assembled (with the exact parameters outlined in the Methods Section) but has encountered some errors in the system assembly which need to be corrected before moving on. The subteam will continue to troubleshoot and fix the current system failures, and once everything is running smoothly with all the appropriate equipment, the subteam will move on to focus on experimentation, evaluation, and iteration.

Initially, the subteam experienced problems when attempting to fluidize the sand bed due to leaks at the connection points in the influent tubing. These leaks were fixed by inserting push-to-connect components and barbed fittings on each of the tubing connections.

Next, the subteam discovered that in order to have the influent water travel at no slower than the fluidization velocity in order to fluidize the sand bed, it would be necessary to acquire a 600 RPM peristaltic pump. Currently, there are no such pumps available for use. As a result, the subteam can either recreate the prototype system using a new pipe with a smaller diameter for the fluidized bed reactor, or a new peristaltic pumped can be purchased for the subteam's use. Once the subteam is able to fluidize the sand bed by one of these two options, initial testing of the functionality of the prototype will be conducted.

If the prototype functions ideally, the effluent water will no longer contain any excess dissolved gas. The subteam will test the functionality of the prototype in two ways. First, the subteam will determine qualitatively, likely with the assistance of a camera, whether bubbles form inside the reactor. If this is true, the premise of using a fluidized bed to encourage bubble formation and to remove dissolved gas from water is valid. After modifying the system as necessary to achieve qualitative success, the subteam will move on to a quantitative analysis of the prototype. The subteam will use dissolved oxygen probes to determine the difference in concentration of dissolved oxygen between the influent and effluent water. With such data, the subteam will then modify the system as necessary to optimize the amount of dissolved gas that is removed.

Although the subteam will be observing bubble formation of oxygen gas within our prototype reactor, it is expected that the percentage of dissolved oxygen removed will be proportional to the percentage of total dissolved gas removed in the actual system. The principles of Henry's Law and Pascal's Law and the equations the subteam put together to model gas solubility are universal, so it is expected that oxygen will give an accurate representation of the reactor's ability to remove any dissolved gas.

As the subteam progresses to experimentation, the subteam will be utilizing ProCoDA in order automate data collection and to control many parts of the experimental apparatus.

The subteam continues to look forward to experimentation and iteration to prove the validity and functionality of the research done throughout the semester.

## Bibliography
Averill, B., & Eldredge, P. (n.d.). *Principles of General Chemistry* (Vol. 1). Creative Commons. Retrieved from https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html

Boudreau, B. P., Algar, C., Johnson, B. D., Croudace, I., Reed, A., Furukawa, Y., … Gardiner, Bruce S. (2005, June 5). *Bubble growth and rise in soft sediments.* Retrieved September 17, 2018, from https://pubs.geoscienceworld.org/gsa/geology/article/33/6/517/103815/bubble-growth-and-rise-in-soft-sediments

Bradford, Dokko, Harris (2018). Filter Constrictions, Spring 2018. https://raw.githubusercontent.com/AguaClara/filter-constrictions/master/Reports_Tutorials/FinalReport.md

Brown, G. (2000, June 22). *The Darcy-Weisbach Equation*. Retrieved from https://bae.okstate.edu/faculty-sites/Darcy/DarcyWeisbach/Darcy-WeisbachEq.htm

CodeCogs.(2012, February 24). Pipe Head Loss. Retrieved from http://www.codecogs.com/library/engineering/fluid_mechanics/pipes/head_loss/pipe-head-loss.php

Department of Chemical Engineering. (2017, February). *Fluidization: A Unit Operation in Chemical Engineering.* Gainesville, FL: University of Florida. Retrieved from http://ww2.che.ufl.edu/unit-ops-lab/experiments/FB/FB-manual.pdf.

Han, M., Park, Y., Lee, J., & Shim, J. (2002). *Effect of pressure on bubble size in dissolved air flotation.* Water Science and Technology: Water Supply, 2(5–6), 41–46. https://doi.org/10.2166/ws.2002.0148

Harrison, D., & Leung, L. S. (1961, April 29). *Bubble Formation at an Orifice in a Fluidized Bed | Nature*. Retrieved September 20, 2018, from https://www.nature.com/articles/190433a0

Hodanbosi, C. (n.d.). *Fluids Pressure and Depth*. Retrieved from https://www.grc.nasa.gov/www/k-12/WindTunnel/Activities/fluid_pressure.html

Hyperphysics. (n.d.). *Surface Tension and Bubbles.* Retrieved from http://hyperphysics.phy-astr.gsu.edu/hbase/surten2.html

Mori, S., & Wen, C. Y. (1975). *Estimation of bubble diameter in gaseous fluidized beds.* AIChE Journal, 21(1), 109–115. https://doi.org/10.1002/aic.690210114

Scardina, P... (2004). *Effects of Dissolved Gas Supersaturation and Bubble Formation on Water Treatment Plant Performance* (Unpublished doctoral dissertation). Virginia Polytechnic Institute and State University. Blacksburg, Virginia. https://vtechworks.lib.vt.edu/bitstream/handle/10919/26497/PaoloScardinaDissertation2004.pdf?sequence=1

Schulz, P. (2004). *Instability and the formation of bubbles and the plugs in fluidized beds*, 24(1), 27. Retrieved from https://www.opuscula.agh.edu.pl/vol24/1/art/opuscula_math_2412.pdf

*Viscosity of Water – Viscosity table and viscosity chart* : Anton Paar Wiki. (2018). Retrieved October 29, 2018, from https://wiki.anton-paar.com/en/water/

Weber-Shirk, M. *Filtration Theory: On removing little particles with big particles* [PowerPoint Slides]. Retrieved from https://courses.cit.cornell.edu/cee4540/pdf/Filtration.pdf.

Weber-Shirk, M. *Flow Control and Measurement* [PowerPoint Slides]. Retrieved from https://courses.cit.cornell.edu/cee4540/pdf/Flow%20Control%20and%20Measurement.pdf.

Worth, M. (2018, January 18). How do scientists measure the porosity of soil? | Socratic. Retrieved November 5, 2018, from https://socratic.org/questions/how-do-scientists-measure-the-porosity-of-soil

## Manual
This manual lays out the details of the materials and methods used for the aforementioned experiments and fabrication.

### Experimental Methods

#### Determining the Porosity of Silica Sand
The porosity of silica sand was a necessary quantity to calculate the sand bed's fluidization velocity ([Equation 1](#Equation-1)). The following procedure was used to determine the porosity of the silica sand used in the reactor, based off the procedure outlined by [Worth, 2018](https://socratic.org/questions/how-do-scientists-measure-the-porosity-of-soil). The equation for determining porosity may be verified by dimensional analysis in comparison with the equation found in the source: [Department of Chemical Engineering, 2017](http://ww2.che.ufl.edu/unit-ops-lab/experiments/FB/FB-manual.pdf).

**Set-Up**
1. Acquire silica sand, water, and two graduated cylinders.
2. Transfer a portion of the sand to a graduated cylinder and record the sand bed’s volume. This is the “sample volume”, $V_{sample}$.
3. Pour an excess volume of water into a second graduated cylinder. Record this volume.

**Experiment**
1. Pour water from its graduated cylinder into the graduated cylinder containing sand until the meniscus’ peak is level with that of the sand bed. This equates to saturating the sand with water.
2. Record the volume of water remaining in its respective graduated cylinder. Subtract this volume from the initial volume of water present in the graduated cylinder; the difference is the volume of water used to saturate the sand. This quantity is equal to the "pore volume", $V_{pore}$.
4. Repeat the Set-Up and Experimental Steps 1-2  until three trials’ worth of data has been recorded.
5. Use [Equation 8](#Equation-8) to calculate the sand’s porosity ($\phi$).

$$\phi = \frac{V_{pore}}{V_{sample}}$$


#### Determining the Average Diameter of Silica Sand Grains
The average diameter of the silica sand grains was a necessary quantity to calculate the sand bed’s fluidization velocity ([Equation 1](#Equation-1)). The subteam used the following procedure to approximate the average diameter of the sand grains.

1. Acquire a sample of silica sand and a digital caliper.
2. Randomly select a number of sand grains, preferably greater than or equal to ten, from the sample.
3. Using the caliper, measure each sand grain’s diameter three times to account for the grains’ asymmetrical natures. Record these measurements.
4. Compute the average diameter for all sand grains in the sample.

Note: the subteam used the file StandardDeviation.py to calculate such average values; this code is detailed in the section Python Code.

#### Measuring Pipe Dimensions
The prototype fluidized bed reactor was comprised of a transparent PVC pipe containing a silica sand bed, modified with components specified in the Fabrication Manual.

**Set-Up**
The subteam cut the pipe to be a particular length prior to taking measurements.
1. Acquire: a transparent PVC pipe of approximately 1” diameter, a Sawzall reciprocating saw, colored tape in two shades, permanent markers, measuring tape, and a caliper.
2. Use a measuring tape and marker to indicate a length of 0.5 m on the PVC pipe. Cut the PVC pipe using the Sawzall such that it matches this length.
3. Wrap tape of opposing colors on opposing ends of the pipe, but *leave several inches between the edge of the pipe and the tape itself*. The tape should be several inches from the edge of the pipe. Use this tape to maintain consistent awareness of the ends of the pipe.

**Measurement**
1. Use a caliper to take the following measurements on both opposite ends of the pipe:
- Measure the thickness of the pipe’s wall in three locations. Compute the average thickness of the pipe’s wall.
- Measure the diameter of the pipe (including the wall) in three locations. These measurements are of the pipe’s “outer diameter”. Compute the average outer diameter of the pipe.
- Subtract twice the wall’s thickness from the outer diameter; the difference is the “inner diameter”. Use this quantity to calculate the cross sectional area of the pipe.
2. Compute the average cross sectional area of the pipe, using the measurements from both ends.

### Fabrication Manual

**Materials required**
1. PVC pipe of approximately 0.5m length, whose ends are labeled with opposing colors of tape, as shown in Figure 9. This is described further in the Measuring Pipe Dimensions section of the Manual.
2. A fine wire mesh
3. Approximately 70 mL of silica sand, measured with a graduated cylinder.
4. Circular clamps
5. 3/16 inch diameter clear flex tubing
6.  3/8 inch diameter clear flex tubing
7. 1/8" Masterflex tubing (06508-16)
8. Peristaltic pump
9. Barbed fittings & push-to-connect components
10. Access to a sink containing a push-to-connect nozzle
11. A plastic bucket
12. Two copies of the following pipe-tubing connector component:
<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype_1/PipeConnector1.jpg?raw=true" height=250
</p>

**Figure 7**

**Fabrication**
1. Cut the wire mesh to obtain a circular mesh whose radius is approximately that of the pipe.
2. Place the mesh at the bottom of the pipe reactor, at the side designated for influent to enter the pipe. Place this mesh into the flow component that from (11).
3. Pour the 70 mL of sand into the pipe, such that it halts on the mesh.
4. Fasten the second copy of the flow component from (11) to the effluent (top) end of the reactor.
5. Mount the pipe on the 80/20 arm using circular clamps, screwed tight around the reactor.
6. Connect 1/8" Masterflex tubing (06508-16) to the Peristaltic Pump.
7. Connect 3/8" diameter clear flex tubing from the sink to the influent end of the Peristaltic Pump.
8. Connect 3/16" diameter clear flex tubing from the effluent end of the peristaltic pump to the influent end of the reactor.
9. Cut approximately 2.4 m of 3/16" diameter clear flex tubing. Connect this to the effluent (upper) end of the reactor, and lead it down into the bucket.


### Python Code
####Determining the Sand Bed's Fluidization Flow

The subteam used the following code, copied from the file FluidizationVelocity.py found on the subteam's GitHub page, to estimate the fluidization velocity & fluidization flow of the sand bed in the prototype reactor. The code is based off of [Equation 1](#Equation-1). The code requests as input: the reactor's cross-sectional area; the kinematic viscosity of water at a particular temperature (e.g. room temperature); the sand's porosity, which the subteam experimentally determined; silica sand's density; the average diameter of the sand grains, which the subteam measured. The code outputs the velocity and flow of water required to fluidize the sand bed.

The following values were used for the subteam to calculate the fluidization flow of 2.54mL/s:

Cross-sectional area of the reactor: 481.1 mm$^2$
Porosity of the silica sand: 0.35
Density of silica sand: 2650kg/m$^3$ [(Weber-Shirk)](https://courses.cit.cornell.edu/cee4540/pdf/Filtration.pdf)
Average diameter of the silica sand grains: 0.91 mm
Kinematic viscosity of water: 0.9344 mm$^2$/s [(Anton Paar)](https://wiki.anton-paar.com/en/water/)

```python
# This code assumes the user knows the porosity of the sand used in the fluidized bed. This code makes use of aide_design, a package provided by AguaClara Cornell

# Assumptions: All input values are real numbers.

import math
import numpy as nm
import aide_design as ad
from aide_design import utility as ut
from aide_design.play import*

area_reactor = float(input("\nWhat is the cross sectional area of the fluidized bed reactor, in units of millimeters squared?\n"))*u.mm**2
porosity = float(input("What is the porosity of the sand bed?\n"))

density_sand = float(input("What is the density of the sand, in units of kilograms per cubic meter?\n"))*u.kg/(u.m**3)
density_water = 997*u.kg/(u.m**3)

diameter = float(input("What is the average diameter of the sand grains, in units of millimeters?\n")) * u.mm


g = 9.8 *u.m/(u.s**2)
kozeny = 5
viscosity = float(input("What is the kinematic viscosity of water, in units of millimeters squared per second?\n"))*u.mm**2/u.s

fluidization_velocity_FirstTerm = (porosity**3 * g * (diameter)**2)/(36*kozeny*(viscosity)*(1-porosity))

fluidization_velocity_SecondTerm = (density_sand/density_water - 1)

fluidization_velocity = fluidization_velocity_FirstTerm * fluidization_velocity_SecondTerm * (1000*u.mm)/(1*u.m)

fluidization_flow = fluidization_velocity * area_reactor * (0.001*u.mL)/(1*u.mm**3)

print("\nThe reactor's fluidization velocity is "+ str(ut.sig(fluidization_velocity,3))+".")
print("The reactor's fluidization flow is "+ str(ut.sig(fluidization_flow,3))+".")
```
####Calculating Averages and Standard Devations
The following code, copied from the file StandardDeviation.py found on the subteam's GitHub page, outputs the average value and the standard deviation of a group of input values.

```python
import math
import numpy as nm
import aide_design as ad
from aide_design import utility as ut
from aide_design.play import*

print("\n"+"Please input only real numbers; make sure the list is at least two items long! If you're done inputting your list, just type 'done'."+"\n")
values = []
item = "blank"
for n in range(100):
    item = input("What number would you like to add to the list?" +"\n")
    if item == "done":
        break
    else:
        try:
            values.append(float(item))
        except:
            print("It seems like you didn't input a number. Please try again!")

total=0
for n in range(len(values)):
    total += values[n]

average= total / len(values)

numerator = 0
for n in range(len(values)):
    numerator += (values[n]-average)**2

standard_deviation = math.sqrt(numerator / (len(values)-1))

print("The list you've entered has an average value of " + str(ut.sig(average, 4)) +", with a standard deviation of "+ str(ut.sig(standard_deviation, 4))+'.')
```
