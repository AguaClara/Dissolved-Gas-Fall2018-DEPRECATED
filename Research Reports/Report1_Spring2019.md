# Dissolved Gas, Spring 2019 Subteam
#### Saul Bernaber, Thomas Bradford, Emily Wood
#### 22 February 2018

Hola!

## Abstract
Excess dissolved air in a treatment plant’s influent water decreases the functionality of the plant's filters and sedimentation tanks. The Dissolved Gas subteam’s goal is to design a gravity-powered apparatus that extracts this excess gas from influent water prior to entry into the treatment plant, using a fluidized bed. The Fall 2018 subteam gathered literature, developed a small-scale prototype, and fabricated a small-scale prototype reactor and an accompanying system. The Spring 2019 subteam will iterate improvements based on experimental data to work towards a prototype that may be scaled up for application in an AguaClara plant.

## Table of Contents

- [Introduction](#Introduction)
- [Literature Review](#Literature-Review)
  - [Fluidized Beds and Bubble Formation](#Fluidized-Beds-&-Bubble-Nucleation)
  - [Controlling Pressure](#Controlling-Pressure)
  - [Analysis of Literature](#Analysis-of-Literature)
- [Previous Work](#Previous-Work)

## Introduction

Excess dissolved gas in influent water of AguaClara plants at Tamara, Honduras and EL PODA, Nicaragua has significantly reduced the plants' efficiencies. To clarify: “excess dissolved gas” does not entail *bubbles* being present in influent water. The influent water is *supersaturated* with gas: gas molecules are dispersed throughout the water, not congregated in bubbles.

Due to the presence of this excess gas, bubbles form in the plants' sedimentation tanks. Flocs adhere to these bubbles and rise, causing materials that should settle to float and to continue into the remainder of the plants. Bubbles also form in the plants' sand filters between sand particles, effectively clogging the filters [(Scardina, 2004)](https://vtechworks.lib.vt.edu/bitstream/handle/10919/26497/PaoloScardinaDissertation2004.pdf?sequence=1). To remedy these issues, the Dissolved Gas subteam intends to develop a reactor that removes such dissolved gas from influent water prior to entering the plant.

For the sake of efficiency, this report uses the term “supersaturated water” to denote water containing excess dissolved gas, whether air or otherwise.

The basic concept of the system design is as follows. Influent water will flow from its source at a high elevation. Once the influent water has descended and is near to the AguaClara plant, piping will direct it upwards into a reactor. Atmospheric pressure decreases as elevation increases [(Hodanbosi)](https://www.grc.nasa.gov/www/k-12/WindTunnel/Activities/fluid_pressure.html). According to Henry’s Law, gas becomes less soluble at lower pressures, making bubble formation more likely [(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html). Additional aspects of the reactor will further encourage bubble formation (i.e. nucleation) in the reactor. Subsequently, the water and the gas bubbles that form will flow upward and out of the reactor. Piping will direct this effluent downward into liquid-gas separator (e.g. a basin containing a vent) such that the gas bubbles may escape into the atmosphere. The water, no longer supersaturated, will then flow into the treatment plant. Figure 1 illustrates this general design.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Figure%201_%20GeneralUpdated.png?raw=true" height=450>
</p>

**Figure 1**: This diagram depicts (not to scale) the general design of the system to remove excess dissolved gas from influent water, as the above paragraph describes.

The subteam has focused its research on the use of a fluidized bed reactor. While technical details are more thoroughly discussed in the Literature Review section, the main attributes of such a reactor are as follows.

A fluidized bed reactor consists of an enclosed reactor containing a suspension of particles, such as sand grains, in a fluid; they are kept in suspension by a particular flow rate directed upwards (i.e. the "fluidization flow" of the sand bed) [(Department of Chemical Engineering, 2017)](http://ww2.che.ufl.edu/unit-ops-lab/experiments/FB/FB-manual.pdf). This flow is that of the influent water, entering the reactor from the bottom and flowing upwards toward an exit pipe. The suspended particles provide surfaces on which bubbles can form. The bubbles then rise from the reactor, leaving the sand behind. Figure 2 illustrates this design.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Fluidized_Bed_Reactor.jpg?raw=true" height=450>
</p>

**Figure 2**: This diagram depicts (not to scale) the general concept of a fluidized bed reactor using sand particles, as the above paragraph describes.

In a fluidized bed reactor, bubbles may immediately travel upward once they form, since their nucleation sites (sand grains) are relatively mobile. Bubbles may depart the fluid at a smaller size, carrying a high internal pressure, being likely to rupture and disperse into solution.

Despite these potential issues, the subteam believes the fluidized bed reactor may still be effective, because a large number of sand grains may provide a large surface area for bubbles. In future semesters, the subteam may consider an alternative reactor type and weigh the merit of each design.

After gathering and analyzing literature, the Fall 2018 subteam fabricated a prototype fluidized bed reactor using a transparent PVC pipe, silica sand, and flow components; the subteam assembled a basic apparatus to resemble the design proposed in Figure 1. Photographs of this apparatus are shown in Figure 4; influent water passes in through a peristaltic pump and through tubing into a vertically oriented fluidized bed reactor, and out into a small bucket. Further details on this apparatus are given in the Methods and Manual sections of the report.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype_1/Prototype1_Photograph.jpg?raw=true" height = 520>

<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype_1/FinalFinal_Prototype1_PhotoDiagram.jpg?raw=true" height = 520>

</p>

**Figure 4**: The left-hand photograph is of the first prototype apparatus; the right-hand photograph contains graphical enhancement to clarify the system's progression. Influent water (purple arrow) enters the system through the peristaltic pump (orange rectangle), flows up into the fluidized bed reactor (green rectangle), exits the reactor as effluent water (dotted purple), and pours into a small bucket (yellow rectangle) that serves as an open-faced vent.

The remainder of this report includes further explanation of concepts such as fluidized beds, considerations of pressure, and details concerning the apparatus' fabrication. The Spring 2019 subteam hopes to pursue qualitative and quantitative experiments to evaluate the reactor's feasibility as a solution. **Such experiments will include determining whether air forms bubbles when supersaturated water is input into the system; determining the quantity / percentage of dissolved gas that the apparatus removes.**

## Literature Review
**Discuss what is already known about your research area based on both external work and that of past AguaClara Teams. Connect your objectives with what is already known and explain what additional contribution you intend to make. Make sure to add APA formatted in-text citations. If you mention the author(s) in your sentence, you can simply give the year of publication.[(Logan et. al. 1987)](http://www.jstor.org/stable/pdf/25043431.pdf?acceptTC=true)**

The subteam concentrated its research on optimizing the system's fluidized bed reactor and manipulating pressure to ensure maximum dissolved gas removal. The subteam’s research can be summarized as follows: gas solubility decreases with decreasing ambient pressure. Therefore, to catalyze bubble growth in a reactor for ease of gas removal, the subteam aimed to design a reactor exerting minimal pressure on gas molecules. Such pressure can be controlled by altering the reactor’s height, by influencing bubble size, and by modifying dimensions of the tubing in the system. Pressure control, combined with providing nucleation sites in a fluidized bed reactor, helps the dissolved gas form stable bubbles that escape from the surrounding water. The subteam hypothesizes that such a reactor design can be developed to alleviate the problems that the plants at El PODA, Nicaragua and Tamara, Honduras are facing.

### Fluidized Beds & Bubble Nucleation

When a liquid or a gas is pumped through a granular solid at a certain velocity, the material behaves like a fluid. The velocity required to cause this behavior is known as the minimum fluidization velocity. The corresponding flow rate may be denoted as the minimum fluidization flow. The minimum fluidization velocity depends on numerous characteristics of the fluidized bed, including particle density, shape, size, and porosity [(Department of Chemical Engineering, 2017)](http://ww2.che.ufl.edu/unit-ops-lab/experiments/FB/FB-manual.pdf). The relationship is quantified by the equation below [(Weber-Shirk)](https://courses.cit.cornell.edu/cee4540/pdf/Filtration.pdf).

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

In the prototype reactor the subteam has fabricated, sand serves as the granular solid and water serves as the fluid. Water has a known density and kinematic viscosity, but the material properties of sand may vary. The subteam used silica sand to design the prototype reactor, as it was readily available in the AguaClara laboratory. The subteam experimentally determined the silica sand's porosity and average grain diameter, as discussed in the Methods section. The subteam found silica sand's density in a presentation by [Weber-Shirk](https://courses.cit.cornell.edu/cee4540/pdf/Filtration.pdf).

**Insert explanation of entrainment velocity**
#### Equation X: Entrainment Velocity

**Variables**

Because of the reactor’s dependence on bubble formation, the subteam also directed research toward bubble nucleation sites. The subteam found that the solid particles in the fluidized beds would provide nucleation sites for bubble formation.

Typically, small, solid particles can provide a place for bubbles to grow large enough so they rise to the top of a reactor and escape [(Boudreau et al., 2005)](https://pubs.geoscienceworld.org/gsa/geology/article/33/6/517/103815/bubble-growth-and-rise-in-soft-sediments). Boudreau found that bubbles that form in sand-like sediments are spherical, in contrast to the oblate spheroid-shaped bubbles that form in muddy sediments. His research suggests that the difference in shape is caused by the differences in responses to the stress of the materials; while mud fractures under stress, sand “acts fluidly or plastically in response to growth stresses.” This informed the subteam as to what type of materials to use in the reactor because the subteam needs the particles to have a fluid-like behavior.

Bubble formation and size in gas-solid fluidized beds is fairly predictable at low gas velocities [(Harrison and Leung, 1961)](https://www.nature.com/articles/190433a0). However, Schulz states that this is not the case for liquid-solid fluidized beds: “In most liquid-fluidized beds, … although instability is present and can be seen in the form of wavy structures this does not lead rapidly to bubble formation.” [(Schulz, 2004)](https://www.opuscula.agh.edu.pl/vol24/1/art/opuscula_math_2412.pdf). This instability could cause problems for the subteam, but there are solutions to commonly reported issues.

If bubble formation is slow or inconsistent, it may be due to the ratio between the density of the particles and the density of water. Schulz found that bubble formation was present in fluidized beds with high ratios, so the subteam may want to consider using denser particles if problems arise.

The subteam aims to remove the most gas from the influent water as possible by creating bubbles. As previously stated, bubbles can be created by providing nucleation sites on sand grains; it can also be done by decreasing gas solubility.

### Controlling Pressure

The solubility of a gas in a solution is directly proportional to its partial pressure above said solution. It is also dependent on a particular constant, determined by the composition of the gas and the solution, and the temperature of both [(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html).

Henry's Law quantifies this relationship, represented by the following equation.

#### Equation 2

$$ C=k P $$

**Variables**
$C$ = Dissolved gas’s concentration in a solvent at equilibrium
$k$ = Henry’s Law constant, which is determined experimentally for each combination of gas, solvent, and temperature. In this case, the interface may be considered as the border between the bubble and the surrounding water.
$P$ = Dissolved gas’s partial pressure at the interface of liquid and gas

Therefore, in order to decrease gas's solubility inside of the reactor, the subteam must find a way to decrease the pressure. This pressure can be minimized through control of two components.

The first of these components is the water pressure at the site of bubble formation. As the height difference between the fluidized bed and the vent changes, the water pressure changes, given by the following relation [(Hodanbosi)](https://www.grc.nasa.gov/www/k-12/WindTunnel/Activities/fluid_pressure.html).

#### Equation 3

$$\Delta P = \rho g \Delta h$$

**Variables**
$\Delta P$ = Change in pressure
$\rho$ = Density of the material
$g$ = Acceleration due to gravity
$\Delta h$ = Change in depth

Because water pressure decreases at lesser depths, building a reactor at a greater height in the water column will minimize pressure inside the reactor, and as a result, minimize gas solubility.

Another factor that influences the pressure difference between the reactor and the vent is that of *head loss*; head loss corresponds to energy lost due to friction, which in turn depends on material properties of the piping [(CodeCogs, 2012)](http://www.codecogs.com/library/engineering/fluid_mechanics/pipes/head_loss/pipe-head-loss.php). In this case, the relevant piping is the effluent pipe through which water exits the reactor and passes into the vent. Head loss is dependent on tubing parameters according to the following equation [(Brown, 2000)](https://bae.okstate.edu/faculty-sites/Darcy/DarcyWeisbach/Darcy-WeisbachEq.htm).

#### Equation 4

 $$ h_f = \frac{32\mu L V}{\rho g D^2} $$

**Variables**
$h_f$ = Head loss
$\mu$ = Absolute viscosity of water
$L$ = Length of the pipe in question
$g$ = Acceleration due to gravity
$\rho$ = Density of water
$D$ =Diameter of the pipe in question
$V$ = Velocity of water in the pipe

Building off [Equation 4](#Equation-4), the pressure difference between two ends of a pipe due to head loss is given by the following equation [(Brown, 2000)](https://bae.okstate.edu/faculty-sites/Darcy/DarcyWeisbach/Darcy-WeisbachEq.htm).

#### Equation 5

$$\Delta P = \rho g h_f$$

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

**Figure 5**: This diagram illustrates the descriptions of surface tension, pressure inside the bubble, and pressure outside the bubble for the given equation [(Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/surten2.html).

The dissolved gas subteam plans on using the principles of this formula to even further decrease the pressure inside the bubble. Because it is known that an increase in radius will result in a decrease in pressure, the subteam must find a way to increase bubble radius.

One way to increase radius may be to prevent the bubbles in the reactor from quickly escaping; if a bubble stays inside the reactor for a longer period of time, it will have a longer time to expand.

In the Analysis of Literature section, Equations 2-6 are evaluated and related to one another to form one basis for parameters of the system design.

### Analysis of Literature
Through conceptual analysis and algebraic manipulation, Equations 2-6 combine to form an estimation of a gas’ solubility in water in an apparatus as illustrated in Figure 1. The following paragraphs describe this process; all variables have been defined in the Literature Review section.

The pressure relevant to Henry's Law (i.e. the pressure of a gas above a liquid, in [Equation 2](#Equation-2)) is the pressure *within* a bubble [(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html).
$$ C = k P $$

$P$ equates to the gas's pressure within a bubble. Therefore, $P$ is relabeled as $P_b$ (i.e. pressure in a bubble).

As shown in [Equation 6](#Equation-6), the pressure within a bubble is directly related to the bubble's radius, the liquid's surface tension, and the pressure outside the bubble [(Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/surten2.html).

$$P_i = P_o + 4 \frac{T}{R}$$

$P_i$ denotes the pressure within a bubble and therefore is relabeled as $P_b$. $P_o$ denotes the pressure outside of the bubble and is relabeled $P_r$ (i.e. pressure in the liquid within the reactor).

The pressure outside of the bubble can be equated to atmospheric pressure, plus a change in pressure due to the height difference between the reactor and the vent ($\Delta P_{height}$) [(Equation 3)](#Equation-3), plus a change in pressure due to head loss in the tubing connecting the reactor and the vent ($\Delta P_{head loss}$) [(Equation 5)](#Equation-5).

$$\Delta P_{height} = \rho g \Delta h$$

$$\Delta P_{head loss} = \rho g h_f$$

The greater the difference in height, the lower the pressure within the reactor. The greater the head loss, the greater the pressure within the reactor. Thus, the pressure within the reactor may be written as follows:

####Equation 3.1

$$P_r = P_{atm} + \Delta P_{height} + \Delta P_{head loss} = P_{atm} - \rho g \Delta h + \rho g h_f$$

The second term of this equation was negated to indicate that, while $\Delta h$ increases in magnitude, the pressure in the reactor decreases.

These equations may be combined and rearranged given their relabeled variables. The following relationship emerges to relate the solubility of the gas in the reactor to a bubble's radius, the height of the reactor, the water's surface tension, the dimensions of the effluent tubing, and the constant relevant to Henry's Law:

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

[Equation 7](#Equation-7), supplemented by [Equation 1](#Equation-1) concerning fluidization velocity, informed the subteam's fabrication of the prototype apparatus. In future semesters, the equation may be used to perform optimizations once the subteam has gathered sufficient experimental data.

## Previous Work

**The following is an amalgamation of the previous Final Report's Future Work & Conclusions sections**
The Fall 2018 subteam's work comprised research, design, fabrication, and basic experimentation to begin development of a reactor to remove excess dissolved gas from influent water in AguaClara plants. Specifics can be found in the [Fall 2018 Final Report](https://github.com/AguaClara/Dissolved-Gas/blob/master/Research%20Reports/Final_Report.md).

The subteam began development of a fluidized bed reactor that would encourage bubble formation by providing bubble nucleation sites. The subteam gathered literature on concepts including fluidization, bubble nucleation, and gas solubility. After analyzing the literature, the subteam experimentally determined relevant system parameters, then designed and fabricated a prototype system. **The subteam also calculated the minimum fluidization velocity, and corresponding flow rate, for the prototype reactor. The subteam also wrote Python code to facilitate easy calculation of a fluidized bed's fluidization velocity and fluidization flow, and head loss through tubing containing laminar flow.**

After fabricating the prototype system, the subteam ran basic tests to determine its functionality. The reactor's sand bed failed to consistently fluidize while using a 100 RPM peristaltic pump, in both one-pump-head and parallel four-pump-head configurations.

The Spring 2019 subteam acquired a 600 RPM peristaltic pump to incorporate into the system, pictured in Figure 4.

Once the subteam experimentally determines the sand bed's fluidization velocity (as opposed to the fluidization velocity calculated with Equation 1), the subteam will progress with experimentation, evaluation, and iteration.

The subteam will determine qualitatively, likely with the assistance of a camera, if bubbles form inside the reactor. If this is true, the premise of using a fluidized bed to encourage bubble formation and to remove excess dissolved air from water is valid. After modifying the system as necessary to achieve qualitative success, the subteam will move on to a quantitative analysis of the prototype. The subteam will use dissolved oxygen probes to determine the difference in concentration of dissolved oxygen between the influent and effluent water. The subteam expects that the water's dissolved oxygen content is proportional to the water's dissolved air content since the major source of the dissolved oxygen is air. Therefore, the system's effectiveness in removing dissolved oxygen should be proportional to the system's effectiveness in removing dissolved air. After analysis of concentration data, the subteam will modify the system to optimize the removal of dissolved gas.

The subteam looks forward to future semesters' experimentation and iteration to analyze and improve the system, and to eventually develop a practical reactor.

## Bibliography
**Edit this bibliography such that it only contains the sources mentioned in the current form of the report**

Averill, B., & Eldredge, P. (n.d.). *Principles of General Chemistry* (Vol. 1). Creative Commons. Retrieved from https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html

Boudreau, B. P., Algar, C., Johnson, B. D., Croudace, I., Reed, A., Furukawa, Y., … Gardiner, Bruce S. (2005, June 5). *Bubble growth and rise in soft sediments.* Retrieved September 17, 2018, from https://pubs.geoscienceworld.org/gsa/geology/article/33/6/517/103815/bubble-growth-and-rise-in-soft-sediments

Bradford, Dokko, Harris (2018). Filter Constrictions, Spring 2018. Retrieved from https://raw.githubusercontent.com/AguaClara/filter-constrictions/master/Reports_Tutorials/FinalReport.md

Brown, G. (2000, June 22). *The Darcy-Weisbach Equation*. Retrieved from https://bae.okstate.edu/faculty-sites/Darcy/DarcyWeisbach/Darcy-WeisbachEq.htm

CodeCogs.(2012, February 24). Pipe Head Loss. Retrieved from http://www.codecogs.com/library/engineering/fluid_mechanics/pipes/head_loss/pipe-head-loss.php

Department of Chemical Engineering. (2017, February). *Fluidization: A Unit Operation in Chemical Engineering.* Gainesville, FL: University of Florida. Retrieved from http://ww2.che.ufl.edu/unit-ops-lab/experiments/FB/FB-manual.pdf.

Florida State University. (n.d.). Solubility. Retrieved December 3, 2018, from https://www.chem.fsu.edu/chemlab/chm1046course/solubility.html

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
